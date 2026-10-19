#!/usr/bin/env python3
"""Mirror validated developer kernel files into this repository's GitHub Releases.

One release is created per device + kernel + upstream release tag. Source-only
kernels are never packaged here; they remain in the build queue.
"""
import argparse
import hashlib
import json
import os
import re
import tempfile
from collections import defaultdict
from datetime import date, datetime, timezone
from pathlib import Path
from urllib.parse import quote, unquote

import requests

ROOT = Path(__file__).resolve().parent.parent
API = 'https://api.github.com'
MAX_ASSET = 2_000_000_000
NON_KERNEL = re.compile(r'(full[-_ ]?(?:nethunter|installer)|installer|rootfs|helpers?[-_ ]?source|source[-_ ]?zip)', re.I)


def slug(value, limit=48):
    value = unquote(str(value or '')).strip().lower()
    value = re.sub(r'[^a-z0-9]+', '-', value).strip('-')
    return (value[:limit].strip('-') or 'kernel')


def up_tag(url):
    m = re.search(r'/releases/download/([^/]+)/', url or '')
    return unquote(m.group(1)) if m else ''


def release_tag(dev, v, tag):
    repo = (v.get('repo') or '').rstrip('/').split('/')[-1].replace('.git', '')
    base = f"nh-{slug(dev['codename'], 32)}-{slug(repo, 36)}-{slug(tag, 36)}"
    base = re.sub(r'-+', '-', base).strip('-')
    if len(base) > 110:
        digest = hashlib.sha1(base.encode()).hexdigest()[:8]
        base = base[:100].rstrip('-') + '-' + digest
    return base


def release_title(dev, v, tag):
    return f"{dev['device']} ({dev['codename']}) - {v.get('kernel') or 'kernel'} - {tag}"[:250]


def body(dev, v, tag):
    lines = [
        f"## {dev['device']} (`{dev['codename']}`)",
        '',
        f"- Kernel: **{v.get('kernel') or 'Unknown'}**",
        f"- Developer: **{v.get('developer') or 'Unknown'}**",
        f"- Upstream release/tag: `{tag}`",
        f"- Boot status: **{v.get('bootStatus') or 'Not verified'}**",
        f"- Working status: **{v.get('workingStatus') or 'Not verified'}**",
        f"- ROM compatibility (as stated): {v.get('romNote') or 'Not specified'}",
        f"- Android version (as stated): {v.get('android') or 'Unknown'}",
        f"- Flash method (as stated): {v.get('installation') or 'Unknown'}",
        f"- Recovery: {v.get('recovery') or 'Unknown'}",
        f"- Root requirement: {v.get('root') or 'Unknown'}",
        f"- Bootloader requirement: {v.get('bootloader') or 'Unknown'}",
    ]
    if v.get('bootNote'):
        lines += ['', f"> {v['bootNote'][:600]}"]
    lines += [
        '',
        '### Files',
        '',
        'These files were built and published by the upstream developer. They are mirrored here for availability, not rebuilt by this project.',
        '',
        f"- Source: {v.get('sourceUrl') or 'see upstream release'}",
        f"- Upstream release: {v.get('releaseUrl') or 'see source'}",
        '',
        '### Safety',
        '',
        'No independent boot test was performed by NetHunter All Kernel. Match the exact device, codename, ROM, Android version, and kernel branch before flashing. Back up the original boot partition. Flashing the wrong image can brick the device.',
        '',
        'Upstream kernel source and binaries remain subject to their authors\' licenses. This release only mirrors the files and preserves the source link.',
    ]
    return '\n'.join(lines)


def collect(devices, codename='', limit=0):
    groups = []
    seen = set()
    for dev in devices:
        if codename and dev['codename'].lower() != codename.lower():
            continue
        for v in dev['variants']:
            if not v.get('hasFile'):
                continue
            by_tag = defaultdict(list)
            for a in v.get('assets') or []:
                if a.get('kind') not in ('zip', 'img', 'archive') or not a.get('url'):
                    continue
                if NON_KERNEL.search(a.get('name') or a['url']):
                    continue
                by_tag[up_tag(a['url']) or 'manual'].append(a)
            for tag, assets in by_tag.items():
                key = (dev['codename'], v.get('repo'), v.get('developer'), v.get('kernel'), tag)
                if key in seen:
                    continue
                seen.add(key)
                groups.append({'device': dev, 'variant': v, 'upstream_tag': tag,
                               'tag': release_tag(dev, v, tag), 'assets': assets})
    groups.sort(key=lambda g: (g['device']['device'], g['tag']))
    return groups[:limit] if limit else groups


def validate(path, kind, size):
    if size <= 0:
        return False, 'empty file'
    if size > MAX_ASSET:
        return False, 'above GitHub 2GB asset limit'
    if kind == 'zip':
        with open(path, 'rb') as f:
            magic = f.read(4)
        if magic[:2] != b'PK':
            return False, 'not a ZIP archive'
    if kind == 'img' and size < 1_000_000:
        return False, 'image smaller than 1 MB'
    return True, ''


def safe_name(name, used, codename):
    name = re.sub(r'[^A-Za-z0-9._+-]+', '-', unquote(name or 'kernel.bin')).strip('-')
    name = name[:140] or 'kernel.bin'
    if name in used:
        name = f"{codename}-{name}"[:160]
    if name in used:
        digest = hashlib.sha1(name.encode()).hexdigest()[:6]
        stem, dot, ext = name.rpartition('.')
        name = f"{stem}-{digest}.{ext}" if dot else f"{name}-{digest}"
    used.add(name)
    return name


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--data', default=str(ROOT / 'site/data.json'))
    ap.add_argument('--out', default=str(ROOT / 'site/mirrored_releases.json'))
    ap.add_argument('--repo', default=os.environ.get('GITHUB_REPOSITORY', 'OPX-Aminul/nethunter-all-kernel'))
    ap.add_argument('--token', default=os.environ.get('GITHUB_TOKEN', ''))
    ap.add_argument('--codename', default='')
    ap.add_argument('--limit', type=int, default=0)
    ap.add_argument('--max-assets', type=int, default=0)
    ap.add_argument('--dry-run', action='store_true')
    args = ap.parse_args()

    data = json.load(open(args.data, encoding='utf-8'))
    groups = collect(data['devices'], args.codename, args.limit)
    print(f"planned releases: {len(groups)}")
    print(f"planned assets: {sum(len(g['assets']) for g in groups)}")
    if args.dry_run:
        for g in groups[:30]:
            print(f"  {g['tag']} :: {len(g['assets'])} file(s) :: {g['device']['device']}")
        return

    if not args.token:
        raise SystemExit('GITHUB_TOKEN is required for a real run')

    session = requests.Session()
    session.headers.update({
        'Authorization': f'Bearer {args.token}',
        'Accept': 'application/vnd.github+json',
        'X-GitHub-Api-Version': '2022-11-28',
    })
    downloader = requests.Session()
    downloader.headers.update({'User-Agent': 'nethunter-all-kernel/1.0'})

    previous = {}
    if Path(args.out).exists():
        try:
            for rel in json.load(open(args.out, encoding='utf-8')).get('releases', []):
                previous[rel.get('tag')] = rel.get('asset_map') or {}
        except Exception:
            previous = {}

    releases = []
    failures = []
    uploaded = 0
    for idx, g in enumerate(groups, 1):
        dev, v, tag = g['device'], g['variant'], g['upstream_tag']
        print(f"[{idx}/{len(groups)}] {g['tag']}")
        rel = session.get(f"{API}/repos/{args.repo}/releases/tags/{quote(g['tag'], safe='')}", timeout=60)
        if rel.status_code == 200:
            release = rel.json()
            print(f"  reuse release {release['id']}")
        elif rel.status_code == 404:
            payload = {
                'tag_name': g['tag'],
                'target_commitish': 'main',
                'name': release_title(dev, v, tag),
                'body': body(dev, v, tag),
                'draft': False,
                'prerelease': False,
                'make_latest': 'false',
            }
            created = session.post(f"{API}/repos/{args.repo}/releases", json=payload, timeout=90)
            if created.status_code not in (200, 201):
                failures.append({'tag': g['tag'], 'error': f"create {created.status_code}: {created.text[:200]}"})
                print('  create failed', created.status_code, created.text[:160])
                continue
            release = created.json()
            print(f"  created release {release['id']}")
        else:
            failures.append({'tag': g['tag'], 'error': f"lookup {rel.status_code}: {rel.text[:200]}"})
            print('  lookup failed', rel.status_code)
            continue

        have = {a['name'] for a in release.get('assets', [])}
        used = set(have)
        asset_map = dict(previous.get(g['tag'], {}))
        for a in g['assets']:
            if args.max_assets and uploaded >= args.max_assets:
                break
            name = safe_name(a.get('name') or a['url'].split('/')[-1], used, dev['codename'])
            if name in have:
                print(f"  skip existing {name}")
                continue
            try:
                with downloader.get(a['url'], stream=True, timeout=180, allow_redirects=True) as r:
                    r.raise_for_status()
                    size = int(r.headers.get('Content-Length') or 0)
                    with tempfile.NamedTemporaryFile(delete=False) as tmp:
                        path = tmp.name
                        digest = hashlib.sha256()
                        for chunk in r.iter_content(1024 * 1024):
                            if chunk:
                                tmp.write(chunk)
                                digest.update(chunk)
                    size = os.path.getsize(path)
                    ok, reason = validate(path, a.get('kind'), size)
                    if not ok:
                        failures.append({'tag': g['tag'], 'asset': name, 'error': reason})
                        print(f"  reject {name}: {reason}")
                        os.unlink(path)
                        continue
                    with open(path, 'rb') as fh:
                        up = session.post(
                            f"https://uploads.github.com/repos/{args.repo}/releases/{release['id']}/assets?name={quote(name, safe='')}",
                            data=fh,
                            headers={'Content-Type': 'application/octet-stream', 'Content-Length': str(size)},
                            timeout=900,
                        )
                    if up.status_code not in (200, 201):
                        failures.append({'tag': g['tag'], 'asset': name, 'error': f"upload {up.status_code}: {up.text[:200]}"})
                        print(f"  upload failed {name}: {up.status_code}")
                        os.unlink(path)
                        continue
                    info = up.json()
                    asset_map[a['url']] = info['browser_download_url']
                    uploaded += 1
                    print(f"  uploaded {name} ({size/1048576:.1f} MB)")
                    os.unlink(path)
            except Exception as exc:
                failures.append({'tag': g['tag'], 'asset': name, 'error': str(exc)[:300]})
                print(f"  error {name}: {exc}")
                try:
                    os.unlink(path)
                except Exception:
                    pass
        releases.append({
            'tag': g['tag'], 'url': release['html_url'],
            'codename': dev['codename'], 'device': dev['device'],
            'developer': v.get('developer'), 'kernel': v.get('kernel'),
            'upstream_tag': tag, 'asset_map': asset_map,
            'assets': [{'source_url': src, 'url': mirror} for src, mirror in asset_map.items()],
        })

    out = {
        'generated': datetime.now(timezone.utc).isoformat(timespec='seconds'),
        'repo': args.repo,
        'releases': releases,
        'failures': failures,
        'uploaded_assets': uploaded,
    }
    Path(args.out).write_text(json.dumps(out, indent=2) + '\n', encoding='utf-8')
    print(f"wrote {args.out}: {len(releases)} releases, {uploaded} uploaded, {len(failures)} failures")


if __name__ == '__main__':
    main()
