import csv, json, re, os
from urllib.parse import unquote
from collections import defaultdict, Counter
from datetime import date

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
BASE = os.path.join(ROOT, 'data')
OUT = os.path.join(HERE, 'data.json')

def norm(url):
    u = (url or '').strip().rstrip('/')
    if not u or u.lower() == 'unknown':
        return ''
    u = u.replace('.git', '')
    return u.lower()

def is_http(u):
    return bool(re.match(r'^https?://', (u or '').strip(), re.I))

stats = {}

for r in csv.DictReader(open(f'{BASE}/nethunter_independent_kernels.csv', encoding='utf-8')):
    k = norm(r.get('url'))
    if not k:
        continue
    try:
        stars = int(r.get('stars') or 0)
    except ValueError:
        stars = 0
    try:
        forks = int(r.get('forks') or 0)
    except ValueError:
        forks = 0
    stats[k] = {
        'stars': stars,
        'forks': forks,
        'relation': r.get('relation') or '',
        'fork_of': r.get('fork_of') or '',
        'is_fork': (r.get('is_fork') or '').lower() in ('yes', 'true', '1'),
    }

# Add metadata captured by the per-device GitHub search.
jsonl = f'{BASE}/perdevice_github_results.jsonl'
if os.path.exists(jsonl):
    for line in open(jsonl, encoding='utf-8'):
        try:
            d = json.loads(line)
        except Exception:
            continue
        for it in (d.get('response') or {}).get('items', []) or []:
            k = norm(it.get('html_url'))
            if not k:
                continue
            old = stats.get(k, {})
            stats[k] = {
                'stars': it.get('stargazers_count', old.get('stars', 0)) or 0,
                'forks': it.get('forks_count', old.get('forks', 0)) or 0,
                'relation': old.get('relation', ''),
                'fork_of': old.get('fork_of', ''),
                'is_fork': bool(it.get('fork', old.get('is_fork', False))),
            }

rows = list(csv.DictReader(open(f'{BASE}/nethunter_master.csv', encoding='utf-8')))

GUIDES = {}
try:
    GUIDES = json.load(open(f'{BASE}/nethunter_guides.json', encoding='utf-8'))
except Exception:
    GUIDES = {}

expanded = f'{BASE}/expanded_candidates.json'
if os.path.exists(expanded):
    for it in json.load(open(expanded, encoding='utf-8')):
        k = norm(it.get('html_url'))
        if not k:
            continue
        old = stats.get(k, {})
        stats[k] = {
            'stars': it.get('stargazers_count', old.get('stars', 0)) or 0,
            'forks': it.get('forks_count', old.get('forks', 0)) or 0,
            'relation': old.get('relation', ''),
            'fork_of': old.get('fork_of', ''),
            'is_fork': bool(it.get('fork', old.get('is_fork', False))),
        }

def kernel_label(r):
    m = re.search(r'kernel id:\s*([^;]+)', r.get('notes', ''), re.I)
    if m:
        return m.group(1).strip()
    repo = r.get('repository_url', '').rstrip('/')
    if is_http(repo):
        tail = repo.split('/')[-1]
        return tail.replace('_', ' ').replace('-', ' ')
    return 'Official kernel'

def release_url(r):
    rel = (r.get('release_url') or '').strip()
    repo = (r.get('repository_url') or '').strip().rstrip('/')
    if is_http(rel):
        if '/releases/download/' in rel and is_http(repo):
            return repo.rstrip('/').replace('.git', '') + '/releases'
        return rel
    if is_http(repo):
        if 'github.com' in repo:
            return repo.rstrip('/').replace('.git', '') + '/releases'
        if 'gitlab.com' in repo:
            return repo + '/-/releases'
    return ''

def _alnum(x):
    return re.sub(r'[^a-z0-9]+', '', (x or '').lower())

FAMILY_ALIASES = {
    'gram': ('miatoll', 'sm6250'),
    'curtana': ('miatoll', 'sm6250'),
    'joyeuse': ('miatoll', 'sm6250'),
    'excalibur': ('miatoll', 'sm6250'),
    'merlinx': ('merlin',),
}

def file_url(u):
    u = (u or '').strip()
    if not is_http(u):
        return False
    if '/releases/download/' in u or '/-/releases/' in u:
        return True
    return bool(re.search(r'\.(zip|img|tar|tar\.gz|tgz|xz|gz)$', u.split('?')[0], re.I))

def best_asset(r):
    raw = ';'.join([r.get('binary_assets') or '', r.get('binary_url') or '', r.get('release_url') or ''])
    items = [x.strip() for x in raw.split(';') if file_url(x)]
    if not items:
        return ''
    def rank(u):
        full = u.lower()
        n = full.split('/')[-1]
        if re.search(r'(sha|sum|firmware|wireless|8812|rt2800|module|toolchain|part_|dtbo|stock|backup|vendor_boot|recovery|twrp|opensource|source)', n) or re.search(r'/(stock|backup|firmware|opensource)[^/]*/', full):
            return (0, 0, n)
        score = 0
        if re.search(r'(kernel|nethunter|(^|[-_])nh([-_]|$)|boot|anykernel|ak3)', n):
            score += 3
        if n.endswith('.img'):
            score += 2
        elif n.endswith('.zip'):
            score += 1
        return (1, score, n)
    best = sorted(items, key=rank, reverse=True)[0]
    return best if rank(best)[0] else ''

def binary_url(r):
    raw = best_asset(r)
    if not is_http(raw):
        return ''
    repo_name = (r.get('repository_url') or '').rstrip('/').split('/')[-1]
    repo = _alnum(repo_name)
    cod = (r.get('codename') or '').lower()
    dev = (r.get('device_name') or '').lower()
    if cod and cod != 'unknown' and _alnum(cod) in repo:
        return raw
    if dev:
        pat = r'(?<![a-z0-9])' + re.escape(dev) + r'(?![\s-]*(?:pro|max|gt|plus|ultra|lite|se|5g)\b)(?![a-z0-9])'
        txt = (repo_name + ' ' + (r.get('notes') or '') + ' ' + (r.get('release_url') or '')).lower()
        if re.search(pat, txt):
            return raw
    for alias in FAMILY_ALIASES.get(cod, ()):
        if alias in repo:
            return raw
    return ''

def asset_kind(name):
    n = (name or '').lower()
    if re.search(r'(sha|sum|\.txt$)', n):
        return 'checksum'
    if re.search(r'(firmware|wireless|8812|rt2800)', n):
        return 'firmware'
    if re.search(r'(modules|toolchain)', n):
        return 'modules'
    if re.search(r'(recovery|twrp)', n):
        return 'recovery'
    if n.endswith('.img'):
        return 'img'
    if n.endswith('.zip'):
        return 'zip'
    if re.search(r'\.(tar|tar\.gz|tgz|xz)$', n):
        return 'archive'
    if re.search(r'(dtbo|super|vbmeta)', n):
        return 'other-image'
    return 'file'

KIND_LABEL = {
    'zip': 'Flashable ZIP',
    'img': 'Boot image',
    'archive': 'Source/archive',
    'firmware': 'Firmware/driver',
    'modules': 'Modules',
    'recovery': 'Recovery image',
    'checksum': 'Checksum',
    'other-image': 'Other image',
    'file': 'File',
}

MIRROR_ASSETS = {}
_mirror_path = os.path.join(os.path.dirname(OUT), 'mirrored_releases.json')
if os.path.exists(_mirror_path):
    try:
        for _rel in json.load(open(_mirror_path, encoding='utf-8')).get('releases', []):
            for _orig, _new in (_rel.get('asset_map') or {}).items():
                MIRROR_ASSETS[_orig] = _new
    except Exception:
        MIRROR_ASSETS = {}

def assets_for(r):
    raw = ';'.join([r.get('binary_assets') or '', r.get('binary_url') or '', r.get('release_url') or ''])
    urls = []
    for x in raw.split(';'):
        x = x.strip()
        if not file_url(x) or x in urls:
            continue
        low = x.lower()
        name = low.split('/')[-1]
        if re.search(r'(stock|backup|opensource|vendor_boot)', name) or re.search(r'/(stock|backup|opensource)[^/]*/', low):
            continue
        urls.append(x)
    out = []
    for u in urls[:100]:
        name = unquote(u.split('/')[-1])
        kind = asset_kind(name)
        out.append({'url': u, 'mirroredUrl': MIRROR_ASSETS.get(u, ''), 'name': name, 'kind': kind, 'label': KIND_LABEL.get(kind, 'File')})
    return out

def guide_for(r):
    u = norm(r.get('repository_url'))
    g = GUIDES.get(u)
    if not g:
        return {
            'method': ['Build from source'] if source_url(r) else ['Unknown'],
            'steps': [
                'Open the maintainer repository or release page.',
                'Follow the installation instructions for your exact ROM and Android version.',
                'Back up the original boot partition before flashing anything.',
                'No extracted installation guide is available for this record.',
            ],
            'requirements': ['Exact device/ROM match', 'Unlocked bootloader where required', 'Backup of original boot.img'],
            'customizations': [],
            'warnings': ['No independent verification. Verify instructions in the maintainer README before flashing.'],
            'source': 'Fallback guide (no README extracted)',
            'channel': 'Unknown',
        }
    return g

def source_url(r):
    repo = (r.get('repository_url') or '').strip()
    return repo if is_http(repo) else ''

def score_variant(v):
    status = v.get('verification_status') or ''
    score = {'Developer claimed': 60, 'Source confirmed': 40, 'Unverified candidate': 15, 'Abandoned': 0}.get(status, 5)
    boot = v.get('boot_evidence') or ''
    if boot == 'Developer-reported boot':
        score += 30
    feat_score = 0
    for key, rank in FEATURE_RANK.items():
        feat_score += rank.get(v.get(key, 'Unknown'), 0)
    score += feat_score
    upd = v.get('last_update') or ''
    m = re.match(r'(20\d\d)', upd)
    if m:
        y = int(m.group(1))
        score += {2026: 12, 2025: 9, 2024: 5, 2023: 1, 2022: -2, 2021: -4}.get(y, -6)
    st = stats.get(norm(v.get('repository_url')), {})
    score += min(int(st.get('forks', 0)), 200) / 20
    score += min(int(st.get('stars', 0)), 500) / 100
    if release_url(v):
        score += 4
    if binary_url(v):
        score += 8
    return score

FEATURES = [
    ('monitor_mode', 'Monitor mode'),
    ('packet_injection', 'Packet injection'),
    ('hid_gadget', 'HID / BadUSB'),
    ('external_wifi_support', 'External Wi-Fi'),
    ('internal_wifi_support', 'Internal Wi-Fi'),
    ('usb_gadget', 'USB gadget'),
]
FEATURE_RANK = {
    'monitor_mode': {'Unknown': 0, 'Source/config evidence': 1, 'Claimed by developer': 2, 'Developer-reported test': 3},
    'packet_injection': {'Unknown': 0, 'Source/config evidence': 1, 'Claimed by developer': 2, 'Developer-reported test': 3},
    'hid_gadget': {'Unknown': 0, 'Source/config evidence': 1, 'Claimed by developer': 2, 'Developer-reported test': 3},
    'external_wifi_support': {'Unknown': 0, 'Source/config evidence': 1, 'Claimed by developer': 2, 'Developer-reported test': 3},
    'internal_wifi_support': {'Unknown': 0, 'Source/config evidence': 1, 'Claimed by developer': 2, 'Developer-reported test': 3},
    'usb_gadget': {'Unknown': 0, 'Source/config evidence': 1, 'Claimed by developer': 2, 'Developer-reported test': 3},
}

def clean_device(name, manufacturer, codename):
    n = (name or 'Unknown').strip()
    BRANDS = ['Samsung','Xiaomi','Google','Motorola','LG','Sony','ASUS','HTC','Nokia','Huawei','Honor','ZTE','Lenovo','Amazon','Murena']
    for b in BRANDS:
        n = re.sub(r'^' + re.escape(b) + r'\s+', '', n, flags=re.I)
    def _paren(m):
        inner = m.group(1)
        if re.search(r'(global|international|exynos|snapdragon|wifi|wi-fi|lte|5g|4g|flat|dual|single|plus)', inner, re.I):
            return ''
        if re.search(r'(pixelos|lineage|crdroid|android|aosp|rom|miui|hyperos|one ?ui|oxygenos|port)', inner, re.I):
            return ''
        return m.group(0)
    n = re.sub(r'\s*\(([^)]*)\)\s*$', _paren, n).strip()
    if codename and codename != 'Unknown':
        n = re.sub(r'\s+' + re.escape(codename) + r'$', '', n, flags=re.I).strip()
    return re.sub(r'\s+', ' ', n) or 'Unknown'

def group_name(n):
    return re.sub(r'\s*\([^)]*\)', '', n or '').strip().lower()

groups = defaultdict(list)
display = {}
for r in rows:
    codename = (r.get('codename') or 'Unknown').lower()
    name = clean_device(r.get('device_name'), r.get('manufacturer'), codename)
    key = (group_name(name), codename)
    display.setdefault(key, name)
    groups[key].append(r)

def best_feature(variants, key):
    best = 'Unknown'
    for v in variants:
        val = v.get(key, 'Unknown') or 'Unknown'
        if FEATURE_RANK[key].get(val, 0) > FEATURE_RANK[key].get(best, 0):
            best = val
    return best

def group_status(variants):
    vals = [v.get('verification_status', '') for v in variants]
    if 'Developer claimed' in vals:
        return 'Developer claimed'
    if 'Source confirmed' in vals:
        return 'Source confirmed'
    if 'Unverified candidate' in vals:
        return 'Unverified candidate'
    return 'Abandoned'

def recovery_for(v, guide):
    text = ' '.join([
        (v.get('installation_method') or ''),
        ' '.join((guide or {}).get('method') or []),
        (v.get('notes') or ''),
    ]).lower()
    labels = []
    if 'twrp' in text: labels.append('TWRP')
    if 'orangefox' in text or ('orange' in text and 'fox' in text): labels.append('OrangeFox')
    if 'fastboot' in text: labels.append('Fastboot')
    if 'odin' in text: labels.append('Odin')
    if 'anykernel' in text: labels.append('AnyKernel3')
    if 'magisk' in text: labels.append('Magisk')
    if not labels and 'recovery' in text: labels.append('Custom recovery')
    return ', '.join(dict.fromkeys(labels)) or 'Unknown'

def recommendation_reason(v):
    bits = []
    if v.get('boot_evidence') == 'Developer-reported boot':
        bits.append('developer-reported boot')
    tested = [label for key, label in FEATURES if v.get(key) == 'Developer-reported test']
    claimed = [label for key, label in FEATURES if v.get(key) == 'Claimed by developer']
    src = [label for key, label in FEATURES if v.get(key) == 'Source/config evidence']
    if tested:
        bits.append('tested ' + ', '.join(tested[:3]))
    elif claimed:
        bits.append('claims ' + ', '.join(claimed[:3]))
    elif src:
        bits.append('config/driver evidence')
    if not bits and v.get('verification_status') == 'Source confirmed':
        bits.append('official source; features untested')
    if not bits:
        bits.append('best available source in this group')
    upd = v.get('last_update') or ''
    if re.match(r'202[5-6]-', upd):
        bits.append('recent update')
    return '; '.join(bits)

devices = []
for (device_key, codename), variants in groups.items():
    device = display[(device_key, codename)]
    variants = sorted(variants, key=lambda v: (-score_variant(v), v.get('device_name', '')))
    best = variants[0]
    best_repo = best.get('repository_url') if is_http(best.get('repository_url')) else ''
    best_stats = stats.get(norm(best_repo), {}) if best_repo else {}
    distinct_repos = []
    seen = set()
    for v in variants:
        repo = source_url(v)
        if repo and norm(repo) not in seen:
            seen.add(norm(repo)); distinct_repos.append(repo)
    source_count = len(distinct_repos)
    fork_total = 0
    star_total = 0
    fork_repos = 0
    for repo in distinct_repos:
        st = stats.get(norm(repo), {})
        fork_total += int(st.get('forks', 0) or 0)
        star_total += int(st.get('stars', 0) or 0)
        if st:
            fork_repos += 1
    features = {}
    for key, label in FEATURES:
        val = best_feature(variants, key)
        if val != 'Unknown':
            features[key] = {'label': label, 'level': val}
    last_dates = [v.get('last_update', '') for v in variants if re.match(r'20\d\d-\d\d-\d\d', v.get('last_update', ''))]
    last_update = max(last_dates) if last_dates else 'Unknown'
    status = group_status(variants)
    rec_release = release_url(best)
    rec_binary = binary_url(best)
    rec_source = source_url(best)
    manufacturer = best.get('manufacturer') or 'Unknown'
    all_binaries = []
    all_zips = []
    all_imgs = []
    binary_best = None
    prepared = []
    for v in variants:
        assets = assets_for(v)
        guide = guide_for(v)
        prepared.append((v, assets, guide))
        for a in assets:
            if a['kind'] == 'checksum':
                continue
            if a['url'] not in all_binaries:
                all_binaries.append(a['url'])
            if a['kind'] == 'zip' and a['url'] not in all_zips:
                all_zips.append(a['url'])
            if a['kind'] == 'img' and a['url'] not in all_imgs:
                all_imgs.append(a['url'])
        b = binary_url(v)
        if b and (binary_best is None or score_variant(v) > score_variant(binary_best)):
            binary_best = v
    first_asset = ''
    for v, assets, guide in prepared:
        for a in assets:
            if a['kind'] in ('zip', 'img'):
                first_asset = a['url']; break
        if first_asset: break
    download_url = rec_binary or rec_release or (binary_url(binary_best) if binary_best else '') or first_asset
    best_guide = guide_for(best)
    install_methods = []
    for v, assets, guide in prepared:
        for m in guide.get('method', []):
            if m not in install_methods:
                install_methods.append(m)
    build_count = sum(1 for v, assets, guide in prepared if any(a['kind'] in ('zip','img','archive') for a in assets))
    direct_files = sum(int(v.get('direct_file_count') or 0) for v in variants)
    direct_file_kernels = sum(1 for v, assets, guide in prepared if int(v.get('direct_file_count') or 0) > 0)
    guide_kernels = sum(1 for v, assets, guide in prepared if (guide.get('source') or '') == 'README' or 'flash' in (v.get('guide_status') or '').lower())
    boot_reported = sum(1 for v in variants if (v.get('boot_status') or '') == 'Developer-reported boot')
    not_booting = sum(1 for v in variants if (v.get('boot_status') or '') == 'Reported not booting')
    devices.append({
        'id': re.sub(r'[^a-z0-9]+', '-', (device + '-' + codename).lower()).strip('-'),
        'device': device,
        'codename': codename,
        'manufacturer': manufacturer,
        'status': status,
        'score': round(score_variant(best), 2),
        'sourceCount': source_count,
        'forkCount': fork_total,
        'starCount': star_total,
        'forkRepos': fork_repos,
        'kernelCount': len(variants),
        'lastUpdate': last_update,
        'recommended': {
            'kernel': kernel_label(best),
            'repo': best_repo,
            'developer': best.get('developer') or 'Unknown',
            'status': best.get('verification_status') or status,
            'boot': best.get('boot_evidence') or 'Not independently verified',
            'lastUpdate': best.get('last_update') or 'Unknown',
            'reason': recommendation_reason(best),
            'sourceUrl': rec_source,
            'releaseUrl': rec_release,
            'binaryUrl': rec_binary,
            'downloadUrl': download_url,
            'downloadLabel': 'Download ZIP / IMG' if (rec_binary or binary_best) else ('Release / ZIP' if best.get('release_url') and is_http(best.get('release_url')) else 'Releases'),
            'binary': bool(rec_binary),
            'distribution': best.get('distribution_type') or 'Unknown',
            'stars': int(best_stats.get('stars', 0) or 0),
            'forks': int(best_stats.get('forks', 0) or 0),
            'assets': assets_for(best),
            'guide': best_guide,
            'channel': best_guide.get('channel') or 'Unknown',
            'bootStatus': best.get('boot_status') or 'Not verified',
            'bootNote': best.get('boot_note') or '',
            'workingStatus': best.get('working_status') or 'Not verified',
            'romNote': best.get('rom_note') or 'Not specified',
            'recovery': recovery_for(best, best_guide),
            'installation': best.get('installation_method') or 'Unknown',
            'root': best.get('root_requirements') or 'Unknown',
            'bootloader': best.get('bootloader_requirements') or 'Unknown',
            'releaseCount': int(best.get('release_count') or 0) if str(best.get('release_count') or '').isdigit() else None,
            'releaseSource': best.get('release_source') or 'Unknown',
            'guideStatus': best.get('guide_status') or 'Unknown',
            'directFileCount': int(best.get('direct_file_count') or 0),
            'hasFile': int(best.get('direct_file_count') or 0) > 0,
            'hasGuide': (best_guide.get('source') or '') == 'README' or 'flash' in (best.get('guide_status') or '').lower(),
        },
        'features': features,
        'guide': best_guide,
        'installMethods': install_methods,
        'downloadCount': len(all_binaries),
        'zipCount': len(all_zips),
        'imgCount': len(all_imgs),
        'buildCount': build_count,
        'directFileCount': direct_files,
        'directFileKernels': direct_file_kernels,
        'sourceOnlyKernels': len(variants) - direct_file_kernels,
        'releaseTotal': sum(int(v.get('release_count') or 0) for v in variants if str(v.get('release_count') or '').isdigit()),
        'kernelsWithReleases': sum(1 for v in variants if str(v.get('release_count') or '').isdigit() and int(v.get('release_count') or 0) > 0),
        'guideKernels': guide_kernels,
        'bootReported': boot_reported,
        'notBooting': not_booting,
        'sourceUrl': rec_source,
        'releaseUrl': rec_release,
        'binaryUrl': rec_binary,
        'binaryCount': len(all_binaries),
        'downloadUrl': download_url or 'https://www.kali.org/get-kali/#kali-mobile',
        'variants': [{
            'kernel': kernel_label(v),
            'repo': source_url(v),
            'releaseUrl': release_url(v),
            'binaryUrl': binary_url(v),
            'downloadUrl': binary_url(v) or release_url(v),
            'assets': assets,
            'guide': guide,
            'channel': guide.get('channel') or 'Unknown',
            'zipCount': sum(1 for a in assets if a['kind'] == 'zip'),
            'imgCount': sum(1 for a in assets if a['kind'] == 'img'),
            'sourceUrl': source_url(v),
            'distribution': v.get('distribution_type') or 'Unknown',
            'sourceAvailable': v.get('source_available') or 'Unknown',
            'status': v.get('verification_status') or 'Unknown',
            'recordType': v.get('record_type') or 'Unknown',
            'boot': v.get('boot_evidence') or 'Unknown',
            'bootStatus': v.get('boot_status') or 'Not verified',
            'bootNote': v.get('boot_note') or '',
            'workingStatus': v.get('working_status') or 'Not verified',
            'romNote': v.get('rom_note') or 'Not specified',
            'recovery': recovery_for(v, guide),
            'installation': v.get('installation_method') or 'Unknown',
            'root': v.get('root_requirements') or 'Unknown',
            'bootloader': v.get('bootloader_requirements') or 'Unknown',
            'releaseCount': int(v.get('release_count') or 0) if str(v.get('release_count') or '').isdigit() else None,
            'releaseSource': v.get('release_source') or 'Unknown',
            'guideStatus': v.get('guide_status') or 'Unknown',
            'directFileCount': int(v.get('direct_file_count') or 0),
            'hasFile': int(v.get('direct_file_count') or 0) > 0,
            'hasGuide': (guide.get('source') or '') == 'README' or 'flash' in (v.get('guide_status') or '').lower(),
            'developer': v.get('developer') or 'Unknown',
            'lastUpdate': v.get('last_update') or 'Unknown',
            'rom': v.get('rom_compatibility') or 'Unknown',
            'android': v.get('android_version') or 'Unknown',
            'kernelVersion': v.get('kernel_version') or 'Unknown',
            'features': {k: v.get(k, 'Unknown') for k, _ in FEATURES if v.get(k, 'Unknown') != 'Unknown'},
            'evidenceQuote': v.get('evidence_quote') or '',
            'limitations': v.get('known_limitations') or '',
            'notes': v.get('notes') or '',
            'recordType': v.get('record_type') or '',
        } for v, assets, guide in prepared],
    })

devices.sort(key=lambda d: (-d['score'], d['device'].lower(), d['codename'].lower()))

status_counts = Counter(d['status'] for d in devices)
feature_counts = Counter()
for d in devices:
    for key in d['features']:
        feature_counts[key] += 1

payload = {
    'generated': date.today().isoformat(),
    'stats': {
        'devices': len(devices),
        'kernels': len(rows),
        'sources': len({norm(r.get('repository_url')) for r in rows if is_http(r.get('repository_url'))}),
        'recommended': sum(1 for d in devices if d['recommended']['status'] == 'Developer claimed'),
        'binaryDevices': sum(1 for d in devices if d.get('binaryCount', 0) > 0),
        'zipDevices': sum(1 for d in devices if d.get('zipCount', 0) > 0),
        'imgDevices': sum(1 for d in devices if d.get('imgCount', 0) > 0),
        'directFileDevices': sum(1 for d in devices if d.get('directFileKernels', 0) > 0),
    'releaseTotal': sum(d.get('releaseTotal', 0) for d in devices),
    'prebuiltKernels': sum(d.get('directFileKernels', 0) for d in devices),
    'sourceOnlyKernels': sum(d.get('sourceOnlyKernels', 0) for d in devices),
        'bootReportedDevices': sum(1 for d in devices if d.get('bootReported', 0) > 0),
        'notBootingDevices': sum(1 for d in devices if d.get('notBooting', 0) > 0),
        'status': dict(status_counts),
        'features': dict(feature_counts),
    },
    'devices': devices,
}
json.dump(payload, open(OUT, 'w', encoding='utf-8'), ensure_ascii=False, separators=(',', ':'))
print('wrote', OUT, 'devices', len(devices), 'bytes', os.path.getsize(OUT))
print('status', dict(status_counts))
print('top', [(d['device'], d['codename'], d['recommended']['status'], d['score']) for d in devices[:5]])
