# Kali NetHunter Research Log - Final Pass
Date: October 2026. This log records what was actually searched, what failed, and what remains. It does not claim coverage that was not performed.

## Discovery layers

1. Official registry: `devices.yml` from `kalilinux/nethunter/build-scripts/kali-nethunter-kernels`.
2. Broad repository search across GitHub, GitLab, and Codeberg.
3. Per-codename GitHub queries for all official codenames (in progress/completed as recorded below).
4. Public ROM/OS device inventories (LineageOS, postmarketOS, Ubuntu Touch, /e/OS) to build the search frame.
5. README/capability inspection for community projects to separate boot/feature reports from metadata.

## Broad queries used

| Platform | Query | Reported total | Fetched | Notes |
|---|---|---:|---:|---|
| GitHub | nethunter in:name,description,readme | 4026 | 200 | 2 pages, star-sorted; discovery |
| GitHub | nethunter kernel | 470 | 100 | updated-sorted |
| GitHub | nethunter kernel | 470 | 100 | star-ascending to surface zero-star repos |
| GitHub | kali nethunter | 675 | 100 | star-sorted |
| GitHub | nethunter topic:android | 60 | 60 | topic filter |
| GitHub | nethunter kernel archived:true | 10 | 10 | archived/abandoned projects |
| GitHub | packet injection android kernel | 3 | 3 | feature-first query |
| GitHub | monitor mode android kernel | 9 | 9 | feature-first query |
| GitHub | HID gadget android kernel | 4 | 4 | feature-first query |
| GitLab | nethunter | - | 500 | 5 pages of 100 projects |
| Codeberg | nethunter / kali nethunter / android kernel | 0 | 0 | API returned ok:true with empty data |
| XDA via DuckDuckGo HTML | site:xda-developers.com nethunter kernel | - | 0 | bot challenge / no results |
| XDA via Bing | site:xda-developers.com nethunter kernel | - | 0 | query ignored, unrelated results |
| YouTube | kali nethunter kernel | - | 0 | not accessed; API key/login required |
| Google | kali nethunter kernel | - | 0 | not accessed; automated access blocked |
| Telegram/Reddit/blogs | nethunter kernel | - | 0 | not accessed in Batch 1 |

## Deep-search pass (October 2026)

- 14 broad queries, 2 pages each, 341 unique repositories, 155 not in the previous master.
- 79 curated repositories integrated as 89 device records; 92 records in the master now carry `Deep search` evidence.
- Added `clarencelol/kernel_xiaomi_sm6250` with 30 releases and 124 assets, covering POCO M2 Pro, Redmi Note 9S, Note 9 Pro, Note 9 Pro Max, and Note 10 Lite.
- Removed false mappings: Naster17 (Note 9 Pro only, not Note 9), KirillTank (sweet/sweetin only, not mojito), and the generic cycoslave mirror.
- Corrected S20 Ultra from `c2s` to `z3s`, merged OPPO/Galaxy A72, merged all `milanf` rows, and normalised brand prefixes and parenthetical qualifiers.
- Deep-search evidence is separate from README evidence. A repository name is not treated as boot proof.

## Per-device GitHub queries

- Device queries executed: 126 of 126.
- Last codename recorded: `zerolte`.
- Repository results returned: 710.
- Only one query template per codename was executed. The other 14 templates are generated but marked `not executed` in `data/nethunter_perdevice_queries.csv`.

## What was inaccessible, and why

| Platform | Attempt | Result |
|---|---|---|
| XDA Developers | DuckDuckGo HTML, Bing site search | Bot challenge / query ignored; no usable thread data |
| YouTube | Direct search and video pages | Not accessed; API key/login required, and video descriptions are not reliably indexable |
| Google | Automated web search | Blocked for automated access |
| Codeberg | Gitea API, three queries | `ok:true` with empty data; no NetHunter kernels found |
| Telegram / Reddit / blogs | Not attempted programmatically | Access rules and anti-bot controls; not searched |
| OEM support sites | Not attempted | Model/variant data is region- and login-gated |

## Dead links and unresolved sources

- A first link sweep checked 999 URLs. 67 returned non-200: most were HTTP 429 rate limits, while confirmed 404 repositories were removed when they were duplicate or non-device sources. Dead historical links remain marked in notes rather than presented as working downloads.
- Some README fetches returned only the stock Linux kernel README. Those were rejected as evidence rather than treated as NetHunter documentation.
- 92 deep-search candidates remain unresolved; most are builders, patch sets, chroot/Termux tools, driver-only repositories, or multi-device GKI kernels without an explicit device list.
- Many official entries have `model_number=Unknown`; the registry does not publish model numbers.

## Unresolved compatibility questions

- Which regional variants share a kernel? The dataset records the exact codename when available but cannot infer regional compatibility.
- Which developer-reported features survive a clean rebuild? Most claims were not reproduced.
- Which abandoned kernels still boot on current firmware? No boot report exists for them.
- Which hidden XDA/Telegram ports exist? Those sources were not accessible, so they remain outside the dataset.

## Files produced

- `data/nethunter_master.csv`
- `data/nethunter_master.json`
- `data/nethunter_final_summary.json`
- `data/nethunter_device_catalog.csv`
- `data/nethunter_feature_matrix.csv`
- `data/nethunter_feature_claims.csv`
- `data/nethunter_boot_evidence.csv`
- `data/nethunter_unverified.csv`
- `data/nethunter_abandoned_recoverable.csv`
- `data/deep_search.jsonl`
- `data/deep_repos.json`
- `data/deep_rows.csv`
- `data/nethunter_perdevice_queries.csv`
- `data/nethunter_search_candidates.csv`
