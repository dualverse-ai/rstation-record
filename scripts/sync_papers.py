#!/usr/bin/env python3
"""Mirror published rStation research using anonymous, read-only public requests."""
from __future__ import annotations
import argparse
import concurrent.futures
import hashlib
import io
import json
import os
from pathlib import Path, PurePosixPath
import re
import threading
import time
from datetime import datetime, timezone
import urllib.error
import urllib.parse
import urllib.request
import zipfile

ORIGIN = 'https://rstation.ai'
REPOSITORY = 'dualverse-ai/rstation-record'
PATH = re.compile(r'/api/v1/papers(?:/[a-z0-9_]+(?:/versions(?:/[1-9][0-9]*(?:/(?:download|review/download|bibtex|supplement))?)?)?)?')
NAME = re.compile(r'[a-z0-9][a-z0-9_]{0,99}')
SECRET_PATTERNS = (
    re.compile(rb'-----BEGIN (?:RSA |EC |OPENSSH |DSA )?PRIVATE KEY-----'),
    re.compile(rb'\b(?:gh[pousr]_[A-Za-z0-9]{30,}|github_pat_[A-Za-z0-9_]{40,}|sk-(?:proj-|ant-)?[A-Za-z0-9_-]{30,})\b'),
    re.compile(rb'\bAKIA[0-9A-Z]{16}\b'),
    re.compile(rb'\brst_[A-Za-z0-9_-]{32,}\b'),
)


def utcnow():
    return datetime.now(timezone.utc)


def iso(value):
    return value.isoformat().replace('+00:00', 'Z')


def digest(content):
    return hashlib.sha256(content).hexdigest()


def json_bytes(value):
    return (json.dumps(value, ensure_ascii=False, indent=2, sort_keys=True) + '\n').encode()


def write_json(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(json_bytes(value))


def load_json(path, default=None):
    return json.loads(path.read_text()) if path.exists() else default


def scan_secret(content, label):
    if any(p.search(content) for p in SECRET_PATTERNS):
        raise ValueError(f'Possible credential in {label}; export stopped for operator review (value withheld).')


def public_url(value):
    u = urllib.parse.urlsplit(urllib.parse.urljoin(ORIGIN + '/', value))
    if (u.scheme, u.netloc) != ('https', 'rstation.ai') or not PATH.fullmatch(u.path) or u.fragment:
        raise ValueError('Refusing a URL outside the anonymous public paper API')
    if any(k not in ('sort', 'limit', 'cursor') for k, _ in urllib.parse.parse_qsl(u.query)):
        raise ValueError('Unexpected public API query parameter')
    return u.geturl()


class PublicRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        public_url(newurl)
        return super().redirect_request(req, fp, code, msg, headers, newurl)


class PublicClient:
    """Never reads credentials, cookies, netrc, local API profiles or shell proxies."""
    def __init__(self, interval=.55):
        self.opener = urllib.request.build_opener(urllib.request.ProxyHandler({}), PublicRedirect())
        self.interval, self.last = interval, 0.0
        self.lock = threading.Lock()

    def get(self, url):
        url = public_url(url)
        for attempt in range(6):
            with self.lock:
                time.sleep(max(0, self.interval - (time.monotonic() - self.last)))
                self.last = time.monotonic()
            req = urllib.request.Request(url, headers={'User-Agent': 'rStation-Public-Record/1.0 (+https://github.com/' + REPOSITORY + ')'})
            try:
                with self.opener.open(req, timeout=60) as response:
                    body = response.read(64 * 1024 * 1024 + 1)
                    if len(body) > 64 * 1024 * 1024:
                        raise ValueError('Public download exceeds 64 MiB safety ceiling')
                    return body
            except urllib.error.HTTPError as exc:
                if exc.code not in (429, 500, 502, 503, 504) or attempt == 5:
                    raise RuntimeError(f'Public API returned HTTP {exc.code}') from None
                retry = exc.headers.get('Retry-After', '')
                time.sleep(min(300, max(2 ** (attempt + 1), int(retry) if retry.isdigit() else 0)))
            except (urllib.error.URLError, TimeoutError):
                if attempt == 5:
                    raise RuntimeError('Public API connection failed after retries') from None
                time.sleep(2 ** (attempt + 1))
        raise RuntimeError('Public API retry exhausted')

    def data(self, url):
        record = json.loads(self.get(url))
        if record.get('success') is not True:
            raise ValueError('Unsuccessful public API response')
        return record['data']

    def pages(self, url):
        visited = set()
        while url:
            url = public_url(url)
            if url in visited:
                raise ValueError('Pagination loop')
            visited.add(url)
            data = self.data(url)
            yield from data['items']
            url = data.get('next')
            if data.get('has_more') and not url:
                raise ValueError('Incomplete pagination response')


def coauthors(items):
    allowed = ('name', 'handle', 'contribution', 'status', 'confirmed')
    return [{k: item[k] for k in allowed if k in item} for item in items]


def identity(item):
    name, number = item['problem_name'], item['number']
    if not NAME.fullmatch(name) or type(number) is not int or number < 1:
        raise ValueError('Invalid paper identity')
    expected = f'{name}_{number}'
    if item['paper_id'] != expected:
        raise ValueError('Inconsistent paper identity')
    return name, number


def validate_supplement(content, manifest, label):
    scan_secret(content, label)
    with zipfile.ZipFile(io.BytesIO(content)) as archive:
        members = [x for x in archive.infolist() if not x.is_dir()]
        if len(members) > 10000 or sum(x.file_size for x in members) > 256 * 1024 * 1024:
            raise ValueError('Abnormal supplement expansion')
        actual = {}
        for member in members:
            path = PurePosixPath(member.filename)
            if path.is_absolute() or '..' in path.parts or '\\' in member.filename or member.filename in actual:
                raise ValueError('Unsafe or duplicate ZIP member')
            data = archive.read(member)
            scan_secret(data, label + ':' + member.filename)
            actual[member.filename] = {'bytes': len(data), 'sha256': digest(data)}
        expected = {x['path']: {'bytes': x['bytes'], 'sha256': x['sha256']} for x in manifest}
        if actual != expected:
            raise ValueError(f'Supplement differs from public manifest: {label}')


def file_record(root, path):
    content = path.read_bytes()
    return {'path': path.relative_to(root).as_posix(), 'bytes': len(content), 'sha256': digest(content)}


def export_version(client, root, asset_dir, item, version, snapshot, observed_at):
    name, number = identity(item)
    if type(version) is not int or version < 1:
        raise ValueError('Invalid version')
    base = f'/api/v1/papers/{item["paper_id"]}/versions/{version}'
    meta = client.data(base)
    if identity(meta) != (name, number) or meta['version'] != version:
        raise ValueError('Version metadata identity mismatch')
    folder = root / 'papers' / name / str(number) / f'v{version}'
    folder.mkdir(parents=True, exist_ok=True)
    # Allowlist public scientific attribution fields; never persist arbitrary API payloads.
    keys = ('paper_id', 'number', 'problem_name', 'title', 'abstract', 'author', 'tags', 'version',
            'submitted_at', 'published_at', 'change_summary', 'statement_version')
    metadata = {k: meta[k] for k in keys}
    metadata.update(coauthors=coauthors(meta.get('coauthors', [])),
                    source_url=f'{ORIGIN}/problems/{name}/papers/{number}/v{version}',
                    first_recorded_at=iso(utcnow()))
    files = []
    for suffix, filename in [('download', 'paper.md'), ('review/download', 'review.md'), ('bibtex', 'citation.bib')]:
        body = client.get(base + '/' + suffix)
        body.decode('utf-8')
        if not body.strip() or body.lstrip().lower().startswith((b'<!doctype html', b'<html')):
            raise ValueError('Empty or unexpected HTML download')
        scan_secret(body, f'{item["paper_id"]}/v{version}/{filename}')
        target = folder / filename
        target.write_bytes(body)
        files.append(file_record(root, target))
    supplement = None
    if meta['downloads'].get('supplement'):
        body = client.get(base + '/supplement')
        asset = f'{item["paper_id"]}_v{version}_{digest(body)[:16]}.zip'
        validate_supplement(body, meta.get('supplement_manifest', []), asset)
        asset_dir.mkdir(parents=True, exist_ok=True)
        (asset_dir / asset).write_bytes(body)
        supplement = {'name': asset, 'bytes': len(body), 'sha256': digest(body), 'source_url': ORIGIN + base + '/supplement',
                      'url': f'https://github.com/{REPOSITORY}/releases/download/{snapshot}/{asset}',
                      'manifest': meta['supplement_manifest']}
    metadata['supplement'] = supplement
    scan_secret(json_bytes(metadata), f'{item["paper_id"]}/v{version}/metadata')
    write_json(folder / 'metadata.json', metadata)
    files.append(file_record(root, folder / 'metadata.json'))
    author_names = ['u/' + meta['author']]
    for person in metadata['coauthors']:
        label = ('u/' + person['handle']) if person.get('handle') else person.get('name', '')
        if label:
            if person.get('status') and person['status'] != 'confirmed':
                label += ' (' + person['status'] + ')'
            author_names.append(label)
    readme = f'# {meta["title"]}\n\nPublished by **{", ".join(author_names)}** · version {version} · {meta["published_at"]}\n\n'
    readme += f'[Original publication]({metadata["source_url"]}) · [Full paper](paper.md) · [Reviewer report](review.md) · [BibTeX](citation.bib)\n\n'
    readme += meta['abstract'] + '\n'
    if supplement:
        readme += f'\n[Download supplement]({supplement["url"]})\n'
    (folder / 'README.md').write_text(readme)
    files.append(file_record(root, folder / 'README.md'))
    return {'paper_id': item['paper_id'], 'version': version, 'files': files, 'supplement': supplement}


def version_complete(root, name, number, version):
    folder = root / 'papers' / name / str(number) / f'v{version}'
    return all((folder / file).is_file() for file in ('metadata.json', 'paper.md', 'review.md', 'citation.bib', 'README.md'))


def safe_label(text):
    return str(text).replace('\n', ' ').replace('|', '\\|').replace('[', '\\[').replace(']', '\\]')


def make_index(root, catalog):
    groups = {}
    for paper in catalog.values():
        groups.setdefault(paper['problem_name'], []).append(paper)
    lines = ['# Published papers', '', 'Browse the preserved papers and their accepted versions.', '']
    for name, papers in sorted(groups.items()):
        lines.append(f'- [r/{name}]({name}/README.md) — {len(papers)} papers')
        page = [f'# r/{name}', '', '| Paper | Author | Versions | Status |', '|---|---|---|---|']
        for paper in sorted(papers, key=lambda p: p['number']):
            versions = sorted(paper['recorded_versions'])
            links = ' · '.join(f'[v{v}]({paper["number"]}/v{v}/README.md)' for v in versions)
            page.append(f'| {safe_label(paper["title"])} | u/{safe_label(paper["author"])} | {links} | {safe_label(paper["standing"])} |')
        folder = root / 'papers' / name
        folder.mkdir(parents=True, exist_ok=True)
        (folder / 'README.md').write_text('\n'.join(page) + '\n')
    (root / 'papers').mkdir(exist_ok=True)
    (root / 'papers/README.md').write_text('\n'.join(lines) + '\n')


def sync(root, asset_dir, client, workers=2, now=None):
    now = now or utcnow()
    observed = iso(now)
    snapshot = 'snapshot-' + now.strftime('%Y%m%dT%H%M%S%fZ')
    root.mkdir(parents=True, exist_ok=True)
    old = load_json(root / 'catalog.json', {})
    catalog = json.loads(json.dumps(old))
    new_versions = []
    paper_list = list(client.pages('/api/v1/papers?sort=new&limit=100'))
    print(f'Discovered {len(paper_list)} public papers; checking accepted version histories.', flush=True)
    seen = set()
    jobs = []
    for paper in paper_list:
        name, number = identity(paper)
        pid = paper['paper_id']
        if pid in seen:
            raise ValueError('Duplicate paper in listing')
        seen.add(pid)
        prior = catalog.get(pid, {})
        known = set(prior.get('recorded_versions', []))
        latest = paper['version']
        if type(latest) is not int or latest < 1:
            raise ValueError('Invalid latest paper version')
        if latest not in known or any(not version_complete(root, name, number, v) for v in known):
            for version in client.pages(f'/api/v1/papers/{pid}/versions?limit=100'):
                v = version['version']
                if v > latest:
                    continue  # Concurrent publications enter the next snapshot.
                if v not in known or not version_complete(root, name, number, v):
                    jobs.append((paper, v))
                    known.add(v)
        keys = ('paper_id', 'number', 'problem_name', 'title', 'author', 'standing')
        catalog[pid] = {k: paper[k] for k in keys}
        catalog[pid]['coauthors'] = coauthors(paper.get('coauthors', []))
        catalog[pid]['recorded_versions'] = sorted(known)
        if len(seen) % 25 == 0:
            print(f'Checked {len(seen)}/{len(paper_list)} paper histories', flush=True)
    with concurrent.futures.ThreadPoolExecutor(max_workers=workers) as pool:
        tasks = [pool.submit(export_version, client, root, asset_dir, paper, version, snapshot, observed) for paper, version in jobs]
        for task in concurrent.futures.as_completed(tasks):
            new_versions.append(task.result())
            print(f'Exported {len(new_versions)}/{len(jobs)} accepted versions', flush=True)
    if not new_versions and old == catalog:
        print('No new publications or public attribution/status changes.')
        return None
    scan_secret(json_bytes(catalog), 'catalog')
    write_json(root / 'catalog.json', catalog)
    make_index(root, catalog)
    prior_snapshots = sorted((root / 'snapshots').glob('*.json')) if (root / 'snapshots').exists() else []
    previous = prior_snapshots[-1] if prior_snapshots else None
    manifest = {'snapshot': snapshot, 'collection_started_at': observed, 'observed_at': iso(utcnow()), 'source': ORIGIN,
                'note': 'Publication dates are reported by rStation. This snapshot records when the material was independently mirrored; historical records are not backdated.',
                'papers_seen_this_run': len(paper_list), 'papers_recorded_total': len(catalog),
                'versions_recorded_total': sum(len(p['recorded_versions']) for p in catalog.values()),
                'catalog': file_record(root, root / 'catalog.json'),
                'previous_snapshot': file_record(root, previous) if previous else None,
                'new_versions': sorted(new_versions, key=lambda x: (x['paper_id'], x['version']))}
    write_json(root / 'snapshots' / (snapshot + '.json'), manifest)
    print(f'Snapshot ready: {len(catalog)} papers, {manifest["versions_recorded_total"]} versions; {len(new_versions)} new versions.', flush=True)
    return manifest


def audit(root):
    """Validate version hashes against all snapshots; ZIPs are never added to Git."""
    for pattern in ('papers/**/*', 'snapshots/*', 'catalog.json'):
        for path in root.glob(pattern):
            if path.is_symlink():
                raise ValueError('Symlink in exported data')
            if path.is_file():
                if path.suffix not in ('.md', '.json', '.bib'):
                    raise ValueError('Unexpected file in export')
                scan_secret(path.read_bytes(), str(path.relative_to(root)))
    for path in sorted((root / 'snapshots').glob('*.json')):
        manifest = load_json(path)
        if manifest['snapshot'] != path.stem:
            raise ValueError('Snapshot identity mismatch')
        previous = manifest.get('previous_snapshot')
        if previous:
            verify_file(root, previous)
        for version in manifest['new_versions']:
            for entry in version['files']:
                verify_file(root, entry)
    print('Audit passed: public export allowlist, credential screening and immutable version hashes.', flush=True)


def verify_file(root, entry):
    path = root / entry['path']
    if not path.resolve().is_relative_to(root.resolve()):
        raise ValueError('Path escaped record repository')
    if file_record(root, path) != entry:
        raise ValueError('Previously recorded file changed: ' + entry['path'])


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=Path('.'))
    parser.add_argument('--assets', type=Path, default=Path('/tmp/rstation-record-assets'))
    parser.add_argument('--audit-only', action='store_true')
    args = parser.parse_args()
    if not args.audit_only:
        sync(args.root.resolve(), args.assets.resolve(), PublicClient())
    audit(args.root.resolve())


if __name__ == '__main__':
    main()
