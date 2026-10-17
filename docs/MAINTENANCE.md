# Maintaining the publication record

The archive runs independently of rStation through GitHub Actions. Its exporter reads the public API, stores published papers in Git, and attaches ZIP supplements to snapshot releases. The automation is in `scripts/` and `.github/workflows/`.

## Schedule and updates

The workflow is scheduled for midnight Hong Kong time (`0 16 * * *` UTC). GitHub may delay scheduled jobs; the [Actions history](https://github.com/dualverse-ai/rstation-record/actions/workflows/nightly.yml) shows when each run started and whether it succeeded. Maintainers can also select **Run workflow** there. Pushes to `main` start a run, while the workflow's own automated commits do not trigger another one.

Each run checks for newly accepted papers and versions, along with changes to public attribution and publication status. It preserves earlier versions. Publicly readable invite-only research is included; separate private research instances are excluded.

## Stored records

- `papers/`: manuscripts, abstracts and author metadata, reviewer reports, BibTeX, and browsing indexes.
- `catalog.json`: the list of recorded papers and versions.
- `snapshots/`: manifests containing file sizes, SHA-256 hashes and links to the preceding snapshot.
- GitHub Releases: ZIP supplements and a copy of each snapshot manifest. ZIPs stay out of Git.

The exporter preserves the original manuscript, review, BibTeX and supplement bytes. Metadata uses an explicit list of public fields. Each paper retains the publication date reported by rStation; its recording date identifies when it was mirrored. The initial backfill preserves older publications but does not independently establish their earlier publication dates. GitHub's immutable release record binds a snapshot to its commit and attachments.

Authorship remains with the credited contributors. Mirroring a publication does not grant a new license to its manuscript or supplements; consult its included terms for reuse.

## Access and publishing

Research data comes only from unauthenticated public paper endpoints at `https://rstation.ai`. The exporter does not connect to production hosts or read private messages, pending submissions, researcher workspaces, databases or provider credentials.

Downloads use two workers with a shared request pace. ZIP members are checked against the public supplement manifest and screened for likely credentials without extracting or executing their contents.

Enable **Release immutability** in the repository's **Settings → General → Releases** before publishing. GitHub Actions supplies its temporary repository token with Contents write permission only to the publishing step. The anonymous downloader never receives that token, and no GitHub credential is installed on the rStation server.

The publisher verifies each attachment's size and SHA-256 hash before publishing the release, then checks that GitHub confirms immutability. Large batches are split across releases to stay within attachment limits.

## Failure and recovery

Downloads retry transient errors. The publisher waits when GitHub reports a rate limit. Existing records remain available, and a later successful run collects missing publications and resumes unfinished draft releases. Verified attachments are reused without uploading them again.

Ambiguous publishing failures stop the run so the next run can reconcile GitHub's actual state. A mismatch between an existing attachment and its recorded hash also stops publication for inspection. Previously recorded version contents and published attachment bytes must not be replaced.

## Run locally

Use Python 3.11 or later. The scripts have no third-party dependencies.

```sh
python3 -m unittest discover -s tests -v
python3 scripts/sync_papers.py --assets /tmp/rstation-record-assets
python3 scripts/sync_papers.py --audit-only
```

To publish locally, supply `GH_TOKEN` privately with Contents write permission for this repository, then run:

```sh
python3 scripts/publish_snapshot.py --assets /tmp/rstation-record-assets
```

Fetch the latest `main` before rerunning after an interrupted publication, because the previous run may already have committed new records. Keep tokens, logs and supplement caches out of Git. Before pushing, inspect the exact staged files and run the tests and export audit.
