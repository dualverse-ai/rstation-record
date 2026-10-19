#!/usr/bin/env python3
"""Commit audited records and publish verified, immutable Release attachments."""
from __future__ import annotations
import argparse
import json
import os
from pathlib import Path
import re
import subprocess
import time
import urllib.error
import urllib.parse
import urllib.request
from sync_papers import (REPOSITORY, PublicClient, audit, digest, file_record, json_bytes,
                         load_json, scan_secret, validate_supplement)


class NoGitHubRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        raise ValueError('Authenticated GitHub redirects are not followed')


class GitHub:
    def __init__(self, token):
        if not token:
            raise ValueError('GitHub token missing')
        self.token = token
        self.last_mutation = 0.0
        self.opener = urllib.request.build_opener(urllib.request.ProxyHandler({}), NoGitHubRedirect())

    def call(self, path, method='GET', data=None, raw=False, missing=False):
        origin = 'https://uploads.github.com' if raw else 'https://api.github.com'
        # Every authenticated URL is constructed from a fixed repository and fixed API origin.
        url = origin + '/repos/' + REPOSITORY + path
        headers = {'Authorization': 'Bearer ' + self.token, 'Accept': 'application/vnd.github+json',
                   'User-Agent': 'rStation-Public-Record', 'X-GitHub-Api-Version': '2022-11-28'}
        if data is not None:
            headers['Content-Type'] = ('application/json' if path.endswith('.json') else 'application/zip') if raw else 'application/json'
        payload = data if raw else (json_bytes(data) if data is not None else None)
        for attempt in range(8):
            if method != 'GET':
                time.sleep(max(0, 1.05 - (time.monotonic() - self.last_mutation)))
                self.last_mutation = time.monotonic()
            try:
                with self.opener.open(urllib.request.Request(url, data=payload, headers=headers, method=method), timeout=120) as response:
                    body = response.read()
                    return json.loads(body) if body else None
            except urllib.error.HTTPError as exc:
                if exc.code == 404 and missing:
                    return None
                # A rate-limit rejection is safe to retry; ambiguous mutation failures
                # are reconciled from existing records/assets on the next workflow run.
                message = exc.read(8192).decode('utf-8', errors='replace').lower()
                limited = exc.code == 429 or (exc.code == 403 and (
                    exc.headers.get('x-ratelimit-remaining') == '0' or
                    'rate limit' in message or 'abuse detection' in message))
                if limited and attempt < 7:
                    delay = min(3600, 60 * 2 ** attempt)
                    retry = exc.headers.get('Retry-After', '')
                    reset = exc.headers.get('x-ratelimit-reset', '')
                    if retry.isdigit():
                        delay = max(delay, int(retry))
                    if exc.headers.get('x-ratelimit-remaining') == '0' and reset.isdigit():
                        delay = max(delay, float(reset) - time.time() + 1)
                    print(f'GitHub rate limit: waiting {delay:.0f} seconds before retrying.', flush=True)
                    time.sleep(delay)
                    continue
                if method != 'GET' or exc.code not in (500, 502, 503, 504) or attempt == 7:
                    raise RuntimeError(f'GitHub {method} failed: HTTP {exc.code} (response withheld)') from None
                time.sleep(2 ** (attempt + 1))
        raise RuntimeError('GitHub retry exhausted')

    def releases(self):
        result = {}
        page = 1
        while True:
            rows = self.call(f'/releases?per_page=100&page={page}')
            for row in rows:
                result[row['tag_name']] = row
            if len(rows) < 100:
                return result
            page += 1

    def assets(self, release_id):
        result = {}
        page = 1
        while True:
            rows = self.call(f'/releases/{release_id}/assets?per_page=100&page={page}')
            for row in rows:
                result[row['name']] = row
            if len(rows) < 100:
                return result
            page += 1


def git(root, *args):
    return subprocess.check_output(['git', '-C', str(root), *args], text=True).strip()


def changes(root):
    tracked = git(root, 'diff', '--name-only', 'HEAD', '--', 'papers', 'catalog.json', 'snapshots').splitlines()
    untracked = git(root, 'ls-files', '--others', '--exclude-standard', '--', 'papers', 'catalog.json', 'snapshots').splitlines()
    names = sorted(set(tracked + untracked))
    for name in names:
        path = root / name
        if not path.is_file() or path.is_symlink() or path.suffix not in ('.md', '.json', '.bib'):
            raise ValueError('Invalid exported path')
    return names


def commit_records(api, root):
    paths = changes(root)
    parent = api.call('/git/ref/heads/main')['object']['sha']
    if git(root, 'rev-parse', 'HEAD') != parent:
        raise ValueError('Remote main changed; fetch it and rerun before publishing')
    if not paths:
        return parent
    tree_sha = api.call('/git/commits/' + parent)['tree']['sha']
    batch, size = [], 0
    for name in paths:
        # read_text() performs universal-newline conversion, corrupting exact
        # manuscript bytes when a published source uses CRLF or bare CR.
        content = (root / name).read_bytes().decode('utf-8')
        entry = {'path': name, 'mode': '100644', 'type': 'blob', 'content': content}
        size += len(json_bytes(entry))
        batch.append(entry)
        if size >= 1024 * 1024:
            tree_sha = api.call('/git/trees', 'POST', {'base_tree': tree_sha, 'tree': batch})['sha']
            batch, size = [], 0
    if batch:
        tree_sha = api.call('/git/trees', 'POST', {'base_tree': tree_sha, 'tree': batch})['sha']
    commit = api.call('/git/commits', 'POST', {'message': 'Record publicly available rStation publications', 'tree': tree_sha, 'parents': [parent]})
    api.call('/git/refs/heads/main', 'PATCH', {'sha': commit['sha'], 'force': False})
    print('Recorded publication files in commit ' + commit['sha'], flush=True)
    return commit['sha']


def existing_asset_matches(existing, name, expected):
    if name not in existing:
        return False
    item = existing[name]
    if item.get('size') != expected['bytes'] or item.get('digest') != 'sha256:' + expected['sha256']:
        raise ValueError('Existing attachment does not match snapshot; operator review required')
    return True


def ensure_asset(api, release, existing, name, body, expected):
    if digest(body) != expected['sha256'] or len(body) != expected['bytes']:
        raise ValueError('Local attachment hash mismatch')
    if existing_asset_matches(existing, name, expected):
        return
    item = api.call(f'/releases/{release["id"]}/assets?name={urllib.parse.quote(name)}', 'POST', body, raw=True)
    if item.get('state') != 'uploaded' or item.get('size') != len(body) or item.get('digest') != 'sha256:' + digest(body):
        raise ValueError('Uploaded attachment verification failed')
    existing[name] = item


def publish(api, root, asset_dir, client):
    audit(root)
    # Repository immutability is enabled once by its owner. The workflow token
    # needs Contents write only; it cannot read or change administrative settings.
    sha = commit_records(api, root)
    releases = api.releases()
    for path in sorted((root / 'snapshots').glob('*.json')):
        manifest = load_json(path)
        tag = manifest['snapshot']
        if not re.fullmatch(r'snapshot-\d{8}T\d{12}Z(?:-\d{3,})?', tag):
            raise ValueError('Invalid snapshot tag')
        release = releases.get(tag)
        if release and not release['draft'] and release.get('immutable'):
            continue
        assets = [v['supplement'] for v in manifest['new_versions'] if v.get('supplement')]
        if len(assets) >= 1000:
            raise ValueError('Snapshot exceeds release attachment count; split the batch before publishing')
        if not release:
            release = api.call('/releases', 'POST', {'tag_name': tag, 'target_commitish': sha, 'name': 'Publication record · ' + manifest['observed_at'],
                'body': f'Public papers mirrored from https://rstation.ai.\n\n{len(manifest["new_versions"])} newly recorded accepted versions; {manifest["papers_recorded_total"]} papers and {manifest["versions_recorded_total"]} versions preserved in total.\n\nPublication dates are reported by rStation. This release records the time of this independent snapshot, including any historical backfill.\n\n[Snapshot manifest](https://github.com/{REPOSITORY}/blob/{sha}/snapshots/{tag}.json) · [Browse papers](https://github.com/{REPOSITORY}/tree/{sha}/papers)\n\nSupplements are preserved as received and have not been executed by this archive.',
                'draft': True, 'prerelease': False})
        existing = api.assets(release['id'])
        if not release['draft']:
            # Recover a publication made before the owner enabled immutability.
            # Verify the complete existing release before changing its draft state;
            # its tag and all attachment bytes stay unchanged.
            records = {item['name']: item for item in assets}
            records[path.name] = file_record(root, path)
            if set(existing) != set(records):
                raise ValueError('Published mutable snapshot has unexpected or missing attachments')
            for name, expected_record in records.items():
                existing_asset_matches(existing, name, expected_record)
            print('Republishing the identical verified snapshot to enable immutability: ' + tag, flush=True)
            release = api.call(f'/releases/{release["id"]}', 'PATCH', {'draft': True})
        for index, item in enumerate(assets, 1):
            if not re.fullmatch(r'[a-z0-9_]+_v[1-9][0-9]*_[a-f0-9]{16}\.zip', item['name']):
                raise ValueError('Unsafe supplement attachment name')
            if not re.fullmatch(r'[a-f0-9]{64}', item['sha256']):
                raise ValueError('Invalid supplement fingerprint')
            if existing_asset_matches(existing, item['name'], item):
                continue
            file = asset_dir / item['name']
            if file.is_symlink() or not file.resolve().is_relative_to(asset_dir.resolve()):
                raise ValueError('Supplement escaped the asset directory')
            if not file.exists():
                body = client.get(item['source_url'])
                asset_dir.mkdir(parents=True, exist_ok=True)
                file.write_bytes(body)
            body = file.read_bytes()
            validate_supplement(body, item['manifest'], item['name'])
            ensure_asset(api, release, existing, item['name'], body, item)
            if index % 25 == 0 or index == len(assets):
                print(f'{tag}: verified {index}/{len(assets)} supplement uploads.', flush=True)
        body = path.read_bytes()
        ensure_asset(api, release, existing, path.name, body, file_record(root, path))
        expected = {a['name'] for a in assets} | {path.name}
        if set(existing) != expected:
            raise ValueError('Unexpected attachment in draft release')
        published = api.call(f'/releases/{release["id"]}', 'PATCH', {'draft': False, 'make_latest': 'true'})
        if not published.get('immutable'):
            check = api.call('/releases/' + str(release['id']))
            if not check.get('immutable'):
                raise ValueError('GitHub did not confirm release immutability')
        print('Published verified snapshot: ' + published['html_url'], flush=True)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=Path('.'))
    parser.add_argument('--assets', type=Path, default=Path('/tmp/rstation-record-assets'))
    args = parser.parse_args()
    publish(GitHub(os.environ.get('GH_TOKEN', '')), args.root.resolve(), args.assets.resolve(), PublicClient())


if __name__ == '__main__':
    main()
