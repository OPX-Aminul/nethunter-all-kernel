#!/usr/bin/env python3
"""Find source-only kernels that have a NetHunter defconfig and an AnyKernel config.

Uses raw.githubusercontent.com HEAD requests, so it does not consume GitHub API quota.
Writes data/build_candidates.csv. A candidate is not a build promise: the source still
has to compile, and the output is untested unless someone boots it on the device.
"""
import concurrent.futures as cf
import csv
import json
import re
import sys
import urllib.error
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
QUEUE = ROOT / 'data/build_queue.csv'
OUT = ROOT / 'data/build_candidates.csv'
DEFCONFIGS = ('arch/arm64/configs/nethunter_defconfig', 'arch/arm/configs/nethunter_defconfig')
ANYKERNELS = ('AnyKernel3/anykernel.sh', 'anykernel.sh', 'anykernel3/anykernel.sh')
UA = {'User-Agent': 'nethunter-build-candidate-audit/1.0'}


def head(url, timeout=20):
    req = urllib.request.Request(url, method='HEAD', headers=UA)
    try:
        with urllib.request.urlopen(req, timeout=timeout) as res:
            return res.status
    except urllib.error.HTTPError as exc:
        return exc.code
    except Exception:
        return 0


def get(url, timeout=20):
    req = urllib.request.Request(url, headers=UA)
    try:
        with urllib.request.urlopen(req, timeout=timeout) as res:
            return res.read().decode('utf-8', 'replace')
    except Exception:
        return ''


def parse_anykernel(text):
    blocks = re.findall(r'^\s*(?:block|BLOCK)=([^;\n]+)', text, re.M)
    names = re.findall(r'^device\.name\d+=(\S+)', text, re.M)
    return blocks, names


def main():
    rows = list(csv.DictReader(open(QUEUE, encoding='utf-8')))
    repos = {}
    for row in rows:
        url = (row.get('repository_url') or '').strip().rstrip('/')
        match = re.match(r'https?://github\.com/([^/]+)/([^/#?]+)', url)
        if not match:
            continue
        key = (match.group(1), re.sub(r'\.git$', '', match.group(2)))
        repos.setdefault(key, []).append(row)

    def check(item):
        (owner, repo), source_rows = item
        base = f'https://raw.githubusercontent.com/{owner}/{repo}/HEAD/'
        found = [path for path in DEFCONFIGS if head(base + path) == 200]
        if not found:
            return None
        anykernel = next((path for path in ANYKERNELS if head(base + path) == 200), '')
        blocks, names = [], []
        if anykernel:
            blocks, names = parse_anykernel(get(base + anykernel))
        return {
            'owner': owner,
            'repo': repo,
            'repository_url': f'https://github.com/{owner}/{repo}',
            'defconfig': ';'.join(found),
            'anykernel': anykernel,
            'block_device': ';'.join(b for b in blocks if b.lower() != 'auto'),
            'device_names': ';'.join(names[:8]),
            'source_rows': len(source_rows),
            'codename': ';'.join(sorted({r.get('codename', '') for r in source_rows if r.get('codename')})),
            'device': ';'.join(sorted({r.get('device', '') for r in source_rows if r.get('device')})),
            'status': 'has_defconfig_and_anykernel' if anykernel else 'needs_anykernel_and_block',
        }

    found = []
    with cf.ThreadPoolExecutor(max_workers=24) as pool:
        for index, result in enumerate(pool.map(check, repos.items()), 1):
            if result:
                found.append(result)
                print(f"candidate {result['owner']}/{result['repo']} :: {result['status']}", file=sys.stderr)
            if index % 100 == 0:
                print(f'checked {index}/{len(repos)} repositories', file=sys.stderr)

    fields = list(found[0].keys()) if found else ['owner']
    with open(OUT, 'w', newline='', encoding='utf-8') as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows(sorted(found, key=lambda x: (x['status'], x['owner'], x['repo'])))
    print(f"wrote {OUT}: {len(found)} candidate repositories from {len(repos)} unique GitHub sources")


if __name__ == '__main__':
    main()
