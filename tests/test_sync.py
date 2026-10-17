import copy
from datetime import datetime, timezone, timedelta
import io
import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch
import zipfile
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
import sync_papers as s
import publish_snapshot as p


def bundle(files=None):
    files = files or {'code.py': b'print("research")\n'}
    buffer = io.BytesIO()
    with zipfile.ZipFile(buffer, 'w') as z:
        for name, body in files.items():z.writestr(name, body)
    return buffer.getvalue(), [{'path': k, 'bytes': len(v), 'sha256': s.digest(v)} for k, v in files.items()]


class Fixture:
    def __init__(self):
        self.zip, self.manifest = bundle()
        self.latest = 2
        self.fail = False
        self.calls = []
        self.paper = {'paper_id': 'math_test_1', 'number': 1, 'problem_name': 'math_test', 'title': 'A result',
                      'author': 'scholar', 'coauthors': [], 'standing': 'accepted', 'version': 2}

    def pages(self, path):
        if '/versions' in path:return iter([{'version': v} for v in range(1, self.latest+1)])
        return iter([{**self.paper, 'version': self.latest}])

    def data(self, path):
        v = int(path.rsplit('/', 1)[1])
        self.calls.append(path)
        return {**self.paper, 'version': v, 'abstract': 'A published abstract.', 'tags': ['math'],
                'submitted_at': '2020-01-01T00:00:00Z', 'published_at': '2020-01-02T00:00:00Z',
                'change_summary': '', 'statement_version': 1, 'downloads': {'supplement': 'present'},
                'supplement_manifest': self.manifest, 'PRIVATE_FIELD': 'must not be exported'}

    def get(self, path):
        self.calls.append(path)
        if self.fail:raise RuntimeError('failure')
        if path.endswith('/supplement'):return self.zip
        if path.endswith('/bibtex'):return b'@misc{test}\n'
        if path.endswith('/review/download'):return b'# Accept\nSound proof.\n'
        return b'# Theorem\nExact original text.\n'


class ExportTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name) / 'repo'
        self.assets = Path(self.temp.name) / 'assets'
        self.client = Fixture()
        self.now = datetime(2026, 10, 17, tzinfo=timezone.utc)

    def tearDown(self):self.temp.cleanup()

    def sync(self):return s.sync(self.root, self.assets, self.client, now=self.now)

    def test_backfill_preserves_all_versions_and_exact_bytes(self):
        m = self.sync()
        self.assertEqual(m['versions_recorded_total'], 2)
        self.assertEqual(len(list(self.assets.glob('*.zip'))), 2)
        self.assertFalse(list(self.root.rglob('*.zip')))
        folder = self.root / 'papers/math_test/1/v1'
        self.assertEqual((folder/'paper.md').read_bytes(), b'# Theorem\nExact original text.\n')
        metadata = json.loads((folder/'metadata.json').read_text())
        self.assertEqual(metadata['published_at'], '2020-01-02T00:00:00Z')
        self.assertNotEqual(metadata['first_recorded_at'], metadata['published_at'])
        self.assertNotIn('PRIVATE_FIELD', metadata)
        self.assertNotIn('must not be exported', str(metadata))
        s.audit(self.root)

    def test_large_backfill_splits_into_chained_release_batches(self):
        self.client.latest = 901
        def export(client, root, assets, paper, version, tag, observed):
            return {'paper_id': paper['paper_id'], 'version': version,
                    'files': [], 'supplement': None, 'snapshot': tag}
        with patch.object(s, 'export_version', side_effect=export), patch('builtins.print'):
            self.sync()
        manifests = sorted((self.root / 'snapshots').glob('*.json'))
        self.assertEqual(len(manifests), 2)
        first, second = [s.load_json(path) for path in manifests]
        self.assertEqual(len(first['new_versions']), 900)
        self.assertEqual(len(second['new_versions']), 1)
        self.assertEqual(second['previous_snapshot'], s.file_record(self.root, manifests[0]))
        self.assertTrue(first['snapshot'].endswith('-001'))
        self.assertTrue(second['snapshot'].endswith('-002'))
        s.audit(self.root)

    def test_repeat_is_noop_and_revision_only_downloads_new_version(self):
        self.sync()
        first = (self.root/'papers/math_test/1/v1/metadata.json').read_bytes()
        self.client.calls.clear()
        self.now += timedelta(days=1)
        self.assertIsNone(self.sync())
        self.assertEqual(self.client.calls, [])
        self.client.latest = 3
        m = self.sync()
        self.assertEqual([v['version'] for v in m['new_versions']], [3])
        self.assertEqual(first, (self.root/'papers/math_test/1/v1/metadata.json').read_bytes())
        s.audit(self.root)

    def test_status_change_is_recorded_without_rewriting_old_version(self):
        self.sync()
        self.now += timedelta(days=1)
        self.client.paper['standing'] = 'withdrawn'
        m = self.sync()
        self.assertEqual(m['new_versions'], [])
        self.assertEqual(s.load_json(self.root/'catalog.json')['math_test_1']['standing'], 'withdrawn')
        s.audit(self.root)

    def test_failure_does_not_advance_catalog_or_snapshot(self):
        self.client.fail = True
        with self.assertRaises(RuntimeError):self.sync()
        self.assertFalse((self.root/'catalog.json').exists())
        self.assertFalse((self.root/'snapshots').exists())
        self.client.fail = False
        self.sync()
        s.audit(self.root)

    def test_tampering_is_detected(self):
        self.sync()
        (self.root/'papers/math_test/1/v1/paper.md').write_text('modified')
        with self.assertRaisesRegex(ValueError, 'changed'):s.audit(self.root)

    def test_invalid_identity_cannot_write_outside_repo(self):
        self.client.paper['problem_name'] = '../../private'
        with self.assertRaises(ValueError):self.sync()

    def test_coauthor_allowlist(self):
        self.assertEqual(s.coauthors([{'handle':'alice','status':'confirmed','api_key':'private'}]),
                         [{'handle':'alice','status':'confirmed'}])

    def test_pagination_follows_next_and_detects_loop(self):
        c = s.PublicClient(interval=0)
        with patch.object(c, 'data', side_effect=[{'items':[1], 'has_more':True, 'next':'/api/v1/papers?cursor=x'}, {'items':[2], 'has_more':False, 'next':None}]):
            self.assertEqual(list(c.pages('/api/v1/papers')), [1,2])
        with patch.object(c, 'data', return_value={'items':[], 'has_more':True, 'next':'/api/v1/papers'}):
            with self.assertRaisesRegex(ValueError, 'loop'):list(c.pages('/api/v1/papers'))

    def test_public_url_rejects_private_and_foreign_destinations(self):
        for url in ['https://evil.test/api/v1/papers', 'http://rstation.ai/api/v1/papers', '/api/v1/submissions',
                    '/api/v1/agents/me', '/api/v1/papers/../../mail', '/api/v1/papers/%2e%2e/mail',
                    'https://rstation.ai@evil.test/api/v1/papers', '/api/v1/papers?token=secret']:
            with self.subTest(url=url), self.assertRaises(ValueError):s.public_url(url)
        self.assertEqual(s.public_url('/api/v1/papers?limit=100'), 'https://rstation.ai/api/v1/papers?limit=100')

    def test_public_requests_never_attach_ambient_credentials(self):
        class Response:
            def __enter__(self):return self
            def __exit__(self,*a):pass
            def read(self,n):return b'ok'
        c = s.PublicClient(interval=0)
        with patch.dict('os.environ', {'GH_TOKEN':'not-for-rstation','RSTATION_API_KEY':'private'}), patch.object(c.opener,'open',return_value=Response()) as op:
            self.assertEqual(c.get('/api/v1/papers'), b'ok')
            req=op.call_args.args[0]
            self.assertFalse(req.has_header('Authorization'))
            self.assertFalse(req.has_header('Cookie'))

    def test_zip_exact_manifest_and_secret_screen(self):
        data, manifest = bundle()
        s.validate_supplement(data, manifest, 'test')
        manifest[0]['sha256'] = '0'*64
        with self.assertRaises(ValueError):s.validate_supplement(data, manifest, 'test')
        key = ('gh'+'p_'+'a'*36).encode()
        data, manifest = bundle({'secret.txt': key})
        with self.assertRaisesRegex(ValueError,'credential'):s.validate_supplement(data,manifest,'test')

    def test_zip_path_traversal_is_rejected_without_extracting(self):
        data, manifest = bundle({'../outside':b'bad'})
        with self.assertRaises(ValueError):s.validate_supplement(data,manifest,'test')


class PublisherTests(unittest.TestCase):
    def test_rate_limited_mutation_waits_and_retries(self):
        from urllib.error import HTTPError
        class Response:
            def __enter__(self):return self
            def __exit__(self,*args):pass
            def read(self):return b'{}'
        api = p.GitHub('fixture-token')
        error = HTTPError('https://api.github.com', 403, 'Forbidden',
                          {'Retry-After': '120'}, io.BytesIO(b'{"message":"secondary rate limit"}'))
        with patch.object(api.opener, 'open', side_effect=[error, Response()]) as send, patch.object(p.time, 'sleep') as sleep:
            api.call('/releases', 'POST', {'draft': True})
            self.assertEqual(send.call_count, 2)
            self.assertIn(unittest.mock.call(120), sleep.call_args_list)

    def test_permission_or_ambiguous_mutation_failure_is_not_replayed(self):
        from urllib.error import HTTPError
        for status in (403, 500):
            api = p.GitHub('fixture-token')
            error = HTTPError('https://api.github.com', status, 'Error', {}, io.BytesIO(b'{"message":"unavailable"}'))
            with patch.object(api.opener, 'open', side_effect=error) as send, patch.object(p.time, 'sleep'):
                with self.assertRaises(RuntimeError):api.call('/releases', 'POST', {'draft': True})
                self.assertEqual(send.call_count, 1)

    def test_upload_content_type_matches_asset(self):
        class Response:
            def __enter__(self):return self
            def __exit__(self,*args):pass
            def read(self):return b'{}'
        api = p.GitHub('fixture-token')
        for name, expected in [('snapshot.json', 'application/json'), ('paper.zip', 'application/zip')]:
            with patch.object(api.opener, 'open', return_value=Response()) as send, patch.object(p.time, 'sleep'):
                api.call('/releases/1/assets?name=' + name, 'POST', b'content', raw=True)
                request = send.call_args.args[0]
                self.assertEqual(request.get_header('Content-type'), expected)
                self.assertTrue(request.full_url.startswith('https://uploads.github.com/repos/dualverse-ai/rstation-record/'))

    def test_existing_verified_asset_is_not_uploaded_again(self):
        body=b'zip';expected={'bytes':3,'sha256':s.digest(body)}
        existing={'a.zip':{'size':3,'digest':'sha256:'+s.digest(body)}}
        class API:
            def call(self,*a,**k):raise AssertionError('duplicate upload')
        p.ensure_asset(API(),{'id':1},existing,'a.zip',body,expected)

    def test_mismatched_existing_asset_is_never_overwritten(self):
        body=b'zip';expected={'bytes':3,'sha256':s.digest(body)}
        with self.assertRaisesRegex(ValueError,'does not match'):
            p.ensure_asset(None,{'id':1},{'a.zip':{'size':3,'digest':'sha256:bad'}},'a.zip',body,expected)

    def test_upload_receipt_hash_checked(self):
        body=b'zip';expected={'bytes':3,'sha256':s.digest(body)}
        class API:
            def call(self,*a,**k):return {'state':'uploaded','size':3,'digest':'sha256:'+s.digest(body)}
        existing={}
        p.ensure_asset(API(),{'id':1},existing,'a.zip',body,expected)
        self.assertIn('a.zip',existing)

    def test_workflow_credentials_only_on_publish_and_no_h1(self):
        text=(Path(__file__).resolve().parents[1]/'.github/workflows/nightly.yml').read_text()
        self.assertIn('persist-credentials: false',text)
        self.assertNotIn('ssh ',text)
        self.assertNotIn('secrets.',text)
        self.assertEqual(text.count('GH_TOKEN:'),1)
        self.assertIn('cron: \'0 16 * * *\'',text)



class RecoveryTests(unittest.TestCase):
    def test_missing_old_version_refetched_and_hash_mismatch_stops(self):
        with tempfile.TemporaryDirectory() as d:
            root=Path(d)/'repo';assets=Path(d)/'assets';f=Fixture()
            s.sync(root,assets,f,now=datetime(2026,10,17,tzinfo=timezone.utc))
            (root/'papers/math_test/1/v1/paper.md').unlink()
            s.sync(root,assets,f,now=datetime(2026,10,18,tzinfo=timezone.utc))
            # Recovery must never silently alter previously recorded metadata.
            with self.assertRaises(ValueError):s.audit(root)

    def test_disappeared_public_paper_is_preserved(self):
        with tempfile.TemporaryDirectory() as d:
            root=Path(d)/'repo';assets=Path(d)/'assets';f=Fixture()
            s.sync(root,assets,f,now=datetime(2026,10,17,tzinfo=timezone.utc))
            with patch.object(f,'pages',return_value=iter([])):
                self.assertIsNone(s.sync(root,assets,f,now=datetime(2026,10,18,tzinfo=timezone.utc)))
            self.assertTrue((root/'papers/math_test/1/v1/paper.md').exists())
            s.audit(root)

    def test_release_retry_uses_existing_assets_then_publishes(self):
        with tempfile.TemporaryDirectory() as d:
            root=Path(d)/'repo';assets=Path(d)/'assets';f=Fixture()
            m=s.sync(root,assets,f,now=datetime(2026,10,17,tzinfo=timezone.utc))
            tag=m['snapshot'];existing={a['supplement']['name']:{'size':a['supplement']['bytes'],'digest':'sha256:'+a['supplement']['sha256']} for a in m['new_versions']}
            class API:
                def releases(self):return {tag:{'id':1,'draft':True}}
                def assets(self,rid):return existing.copy()
                def call(self,path,method='GET',data=None,raw=False,**kwargs):
                    if raw:
                        self.uploads+=1
                        return {'state':'uploaded','size':len(data),'digest':'sha256:'+s.digest(data)}
                    if method=='PATCH':return {'immutable':True,'html_url':'https://github.com/example'}
                    raise AssertionError(path)
                uploads=0
            api=API()
            with patch.object(p,'commit_records',return_value='commit'):
                p.publish(api,root,assets,f)
            self.assertEqual(api.uploads,1)  # Only the missing manifest is uploaded.

    def test_published_immutable_release_is_not_changed(self):
        with tempfile.TemporaryDirectory() as d:
            root=Path(d)/'repo';assets=Path(d)/'assets';f=Fixture()
            m=s.sync(root,assets,f,now=datetime(2026,10,17,tzinfo=timezone.utc))
            class API:
                def releases(self):return {m['snapshot']:{'id':1,'draft':False,'immutable':True}}
                def call(self,*a,**k):raise AssertionError('Published release must not change')
            with patch.object(p,'commit_records',return_value='commit'):
                p.publish(API(),root,assets,f)


if __name__ == "__main__":
    unittest.main()
