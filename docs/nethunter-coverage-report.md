# NetHunter Research Coverage Report
Generated for 640 database rows: 275 official variants, 310 community projects, 55 per-device search discoveries.

## What was actually investigated

| Source | Method | Result |
|---|---|---|
| Kali NetHunter registry | `devices.yml` from the official build-scripts repository | 275 variants, 126 devices, 80 authors |
| GitHub | REST repository search, broad queries plus per-codename queries | 154 retained broad-search projects; additional metadata-only candidates in `nethunter_search_candidates.csv` |
| GitLab | REST project search, 5 pages | 131 projects retained from 500 results |
| Codeberg | Gitea API, 3 queries | 0 results; API returned empty data |
| XDA Developers | DuckDuckGo HTML and Bing site search | Not searched: bot challenge / unusable results |
| YouTube | None | Not accessed: API key/login required |
| Google | None | Not accessed: automated access blocked |
| Telegram, Reddit, blogs | None | Not accessed in this pass |
| LineageOS wiki | Public device list | 631 devices, 77 kernel repositories |
| postmarketOS pmaports | Sparse clone, deviceinfo/APKBUILD | 555 devices, 352 kernel packages |
| Ubuntu Touch | Public device list | 111 ports |
| /e/OS | Public device list | 199 devices |

## Manufacturer coverage in the final catalog

| Manufacturer | Devices/codenames | Official variants | Community projects |
|---|---:|---:|---:|
| Samsung | 88 | 80 | 74 |
| OnePlus | 33 | 46 | 34 |
| Xiaomi | 97 | 38 | 106 |
| Google | 37 | 38 | 27 |
| Unknown | 10 | 13 | 17 |
| Motorola | 16 | 11 | 15 |
| LG | 16 | 10 | 12 |
| Nokia | 3 | 8 | 0 |
| Sony | 11 | 7 | 6 |
| Huawei | 3 | 7 | 0 |
| Realme | 9 | 5 | 5 |
| Nothing | 2 | 3 | 3 |
| HTC | 4 | 3 | 1 |
| LeEco | 2 | 1 | 2 |
| ASUS | 2 | 1 | 1 |
| Lenovo | 2 | 1 | 1 |
| OPPO | 2 | 1 | 1 |
| Ulefone | 1 | 1 | 1 |
| ZTE | 1 | 1 | 0 |
| Nubia | 2 | 0 | 2 |
| Honor | 1 | 0 | 1 |
| vivo | 1 | 0 | 1 |

## Coverage boundaries

- The per-device query plan covers all 126 official codenames, but not all 15 query templates were executed. One GitHub query per codename was run; the rest remain in `data/nethunter_perdevice_queries.csv` marked `not executed`.
- XDA, YouTube, Google, Telegram, Reddit, and blogs were not machine-accessible. Any claim that they were exhaustively searched would be false.
- Model numbers and regional variants are mostly `Unknown`; the official registry and repository text rarely provide exact model numbers. Do not assume regional variants share compatibility.
- Feature verification is limited to what repository authors wrote. No device was available for independent testing.
- The Android device inventory contains 1,771 rows and 1,295 unique codenames from public ROM/OS device lists. It is a search frame, not proof of NetHunter support.

## Remaining work

1. Execute the remaining 14 query templates per codename on a search platform that permits it.
2. Inspect XDA threads manually where Cloudflare/bot checks block automation.
3. Resolve model numbers and regional variants for the 17 unresolved community projects and the many official entries marked `Unknown`.
4. Reproduce developer-reported boot/feature claims on hardware before promoting any row above `Developer claimed`.
