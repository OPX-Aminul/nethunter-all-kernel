#!/usr/bin/env python3
"""Audit per-device kernel and release availability from the site dataset."""
import csv, json, re
from collections import Counter, defaultdict
from datetime import date
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parent.parent
DATA = json.load(open(ROOT / 'site/data.json', encoding='utf-8'))
MIRROR = {}
try:
    MIRROR = json.load(open(ROOT / 'site/mirrored_releases.json', encoding='utf-8'))
except Exception:
    MIRROR = {}
OUT_DATA = ROOT / 'data'
OUT_DOC = ROOT / 'docs/nethunter-release-audit.md'


def upstream_tag(url):
    m = re.search(r'/releases/download/([^/]+)/', url or '')
    return unquote(m.group(1)) if m else ''


def kernel_rows():
    for dev in DATA['devices']:
        for v in dev['variants']:
            assets = [a for a in (v.get('assets') or [])
                      if a.get('kind') in ('zip', 'img', 'archive') and a.get('url')]
            tags = sorted({upstream_tag(a['url']) for a in assets if upstream_tag(a['url'])})
            yield dev, v, assets, tags


def audit_doc(dev_rows, kernel_list, totals):
    lines = [
        '# NetHunter Kernel Release Audit',
        f'Generated {date.today().isoformat()} from `site/data.json`.',
        '',
        '## Headline',
        '',
        '| Metric | Count |',
        '|---|---:|',
        f"| Device cards | {totals['devices']} |",
        f"| Kernel records | {totals['kernels']} |",
        f"| Kernels with a direct ZIP/IMG/archive | {totals['prebuilt']} |",
        f"| Kernels with no prebuilt file | {totals['source_only']} |",
        f"| Device cards with at least one prebuilt kernel | {totals['devices_prebuilt']} |",
        f"| Device cards with no prebuilt kernel | {totals['devices_source_only']} |",
        f"| Releases reported by sources | {totals['release_total']} |",
        f"| Upstream release groups found in asset URLs | {totals['asset_tags']} |",
        f"| Mirrored releases in this repository | {totals['mirror_releases']} |",
        f"| Mirrored assets in this repository | {totals['mirror_assets']} |",
        f"| Mirror failures / skipped assets | {totals['mirror_failures']} |",
        '',
        'A release count is what the source publishes. A direct file is an actual ZIP, IMG, or archive link that can be downloaded. The two are not the same: many repositories have releases with no kernel asset.',
        '',
        '## Kernels and releases by device',
        '',
        '| Device | Codename | Kernels | Prebuilt | Source-only | Releases |',
        '|---|---|---:|---:|---:|---:|',
    ]
    for r in sorted(dev_rows, key=lambda x: (-x['kernel_count'], x['device'])):
        lines.append(f"| {r['device']} | `{r['codename']}` | {r['kernel_count']} | {r['prebuilt_kernels']} | {r['source_only_kernels']} | {r['release_total']} |")
    lines += [
        '',
        'The full machine-readable tables are `data/device_availability.csv` and `data/kernel_availability.csv`.',
        '',
        '## Device cards with prebuilt files',
        '',
        '| Device | Codename | Prebuilt kernels | Direct files | Upstream release tags |',
        '|---|---|---:|---:|---:|',
    ]
    for r in sorted([x for x in dev_rows if x['prebuilt_kernels']], key=lambda x: (-x['direct_files'], x['device'])):
        lines.append(f"| {r['device']} | `{r['codename']}` | {r['prebuilt_kernels']} | {r['direct_files']} | {r['asset_tags']} |")
    nofile = [r for r in dev_rows if not r['prebuilt_kernels']]
    lines += [
        '',
        '## Source-only devices',
        '',
        f'{len(nofile)} of {len(dev_rows)} device cards currently have no prebuilt kernel file. These need a real device build: a matching defconfig, a working toolchain and kernel branch, and a product/vendor setup. They must not be replaced with a generic AnyKernel3 ZIP that contains no kernel.',
        '',
        'Examples:',
        '',
    ]
    for r in sorted(nofile, key=lambda x: (-x['kernel_count'], x['device']))[:15]:
        lines.append(f"- {r['device']} (`{r['codename']}`): {r['kernel_count']} kernel record(s), 0 prebuilt files")
    lines += [
        '',
        '## Build and publication policy',
        '',
        '1. Prebuilt developer ZIP/IMG assets are mirrored only after download validation and source attribution.',
        '2. A source-only row is marked `build_required`. It is never published as a flashable ZIP unless a kernel image was actually produced from its source.',
        '3. A build must match the exact codename and defconfig. Cross-device or cross-ROM ZIPs are rejected.',
        '4. Every release body must include the upstream source, the exact kernel/ROM target, boot evidence scope, and the original release link.',
        '5. Files that fail ZIP/IMG validation or exceed the upload limit are skipped and reported.',
        '',
        '## Evidence caveat',
        '',
        'No kernel in this dataset has been independently boot-tested by this project. The website labels developer claims separately from verified results. Publishing a ZIP does not make it safe for every ROM or regional model.',
    ]
    OUT_DOC.write_text('\n'.join(lines) + '\n', encoding='utf-8')


def main():
    dev_rows = []
    kernel_list = []
    asset_count = 0
    tag_set = set()
    for dev, v, assets, tags in kernel_rows():
        tag_set.update(tags)
        asset_count += len(assets)
        kernel_list.append({
            'device': dev['device'],
            'codename': dev['codename'],
            'manufacturer': dev.get('manufacturer', 'Unknown'),
            'developer': v.get('developer', 'Unknown'),
            'kernel': v.get('kernel', 'Unknown'),
            'repository_url': v.get('repo', ''),
            'release_url': v.get('releaseUrl', ''),
            'release_count': v.get('releaseCount') if v.get('releaseCount') is not None else '',
            'release_source': v.get('releaseSource', ''),
            'direct_file_count': v.get('directFileCount', 0),
            'prebuilt': 'yes' if v.get('hasFile') else 'no',
            'asset_kinds': ','.join(sorted({a['kind'] for a in assets})),
            'upstream_tags': ';'.join(tags),
            'build_required': 'no' if v.get('hasFile') else 'yes',
            'boot_status': v.get('bootStatus', ''),
            'working_status': v.get('workingStatus', ''),
            'rom_note': v.get('romNote', ''),
            'android': v.get('android', 'Unknown'),
            'recovery': v.get('recovery', 'Unknown'),
            'root': v.get('root', 'Unknown'),
            'bootloader': v.get('bootloader', 'Unknown'),
            'guide_status': v.get('guideStatus', ''),
            'source_url': v.get('sourceUrl', ''),
            'record_type': v.get('recordType', 'Unknown'),
            'build_reason': 'No developer ZIP/IMG; source-only row' if not v.get('hasFile') else '',
        })
    for dev in DATA['devices']:
        variants = dev['variants']
        prebuilt = sum(1 for v in variants if v.get('hasFile'))
        dev_rows.append({
            'device': dev['device'],
            'codename': dev['codename'],
            'manufacturer': dev.get('manufacturer', 'Unknown'),
            'kernel_count': len(variants),
            'prebuilt_kernels': prebuilt,
            'source_only_kernels': len(variants) - prebuilt,
            'direct_files': sum(int(v.get('directFileCount') or 0) for v in variants),
            'release_total': sum(int(v.get('releaseCount') or 0) for v in variants if v.get('releaseCount') is not None),
            'kernels_with_releases': sum(1 for v in variants if (v.get('releaseCount') or 0) > 0),
            'asset_tags': len({upstream_tag(a['url']) for v in variants for a in (v.get('assets') or []) if a.get('url') and upstream_tag(a['url'])}),
            'last_update': dev.get('lastUpdate', 'Unknown'),
            'recommended': (dev.get('recommended') or {}).get('developer', 'Unknown'),
        })
    OUT_DATA.mkdir(exist_ok=True)
    with open(OUT_DATA / 'kernel_availability.csv', 'w', newline='', encoding='utf-8') as f:
        w = csv.DictWriter(f, fieldnames=list(kernel_list[0].keys()))
        w.writeheader(); w.writerows(kernel_list)
    with open(OUT_DATA / 'device_availability.csv', 'w', newline='', encoding='utf-8') as f:
        w = csv.DictWriter(f, fieldnames=list(dev_rows[0].keys()))
        w.writeheader(); w.writerows(dev_rows)
    queue = [k for k in kernel_list if k['build_required'] == 'yes']
    queue.sort(key=lambda k: (k['record_type'] != 'official_distribution_variant', k['device'], k['developer']))
    with open(OUT_DATA / 'build_queue.csv', 'w', newline='', encoding='utf-8') as f:
        fields = ['device', 'codename', 'manufacturer', 'developer', 'kernel', 'repository_url', 'release_url',
                  'record_type', 'boot_status', 'rom_note', 'android', 'recovery', 'build_reason']
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        for k in queue:
            w.writerow({key: k.get(key, '') for key in fields})
    totals = {
        'devices': len(dev_rows),
        'kernels': len(kernel_list),
        'prebuilt': sum(1 for k in kernel_list if k['prebuilt'] == 'yes'),
        'source_only': sum(1 for k in kernel_list if k['build_required'] == 'yes'),
        'devices_prebuilt': sum(1 for d in dev_rows if d['prebuilt_kernels']),
        'devices_source_only': sum(1 for d in dev_rows if not d['prebuilt_kernels']),
        'release_total': sum(d['release_total'] for d in dev_rows),
        'asset_tags': len(tag_set),
        'mirror_releases': len(MIRROR.get('releases', [])),
        'mirror_assets': sum(len(r.get('asset_map') or {}) for r in MIRROR.get('releases', [])),
        'mirror_failures': len(MIRROR.get('failures', [])),
    }
    audit_doc(dev_rows, kernel_list, totals)
    print('wrote data/device_availability.csv rows', len(dev_rows))
    print('wrote data/kernel_availability.csv rows', len(kernel_list))
    print('wrote data/build_queue.csv rows', sum(1 for k in kernel_list if k['build_required'] == 'yes'))
    print('wrote docs/nethunter-release-audit.md')
    print(totals)
    print('assets', asset_count, 'unique tags', len(tag_set))


if __name__ == '__main__':
    main()
