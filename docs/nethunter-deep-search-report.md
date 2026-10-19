# Kali NetHunter Deep-Search Integration Report

Date: 2026-10-19. This pass responds to two concrete problems: an important source (`clarencelol/kernel_xiaomi_sm6250`) was missing, and several device recommendations were wrong because repositories had been mapped to the wrong codename.

The machine-readable result is `data/nethunter_master.csv`. The website payload is `site/data.json`.

## Current totals

| Metric | Value |
|---|---:|
| Kernel records | 640 |
| Official distribution variants | 275 |
| Community kernel projects | 310 |
| Per-device search discoveries | 55 |
| Distinct source repositories | 487 |
| Device/codename groups in the catalog | 343 |
| Canonical device cards on the website | 313 |
| Records with a direct binary or release asset | 37 |
| Devices with at least one direct file | 32 |
| Developer-reported boot | 5 |
| Independently verified boot | 0 |

Evidence status by row: 266 Source confirmed, 186 Unverified candidate, 146 Developer claimed, 42 Abandoned.

## What this pass added

The broad deep-search run executed 14 queries with two pages each and produced 341 unique repositories, 155 of which were not in the previous master. After filtering out scripts, chroots, patchers, builders, driver-only repositories, and generic mirrors, 79 repositories were curated and integrated as 89 device-level records.

Selected additions:

| Repository | Devices | Why it matters |
|---|---|---|
| `clarencelol/kernel_xiaomi_sm6250` | POCO M2 Pro, Redmi Note 9S, Note 9 Pro, Note 9 Pro Max, Note 10 Lite | 30 releases, 124 assets, MIUI/HyperOS/AOSP, KSU/NONKSU, Extreme Edition |
| `Naster17/NetHunter-Kernels` | Redmi Note 9 Pro | Built-in monitor mode, HID, external Wi-Fi, CAN, HackRF/Ubertooth |
| `ViP3R-KERNELs/kernel_oneplus_sm8250` | OnePlus 8T | Android 14 NetHunter kernel |
| `Neternels/android_kernel_oneplus_sm8250` | OnePlus 8 / 8 Pro | NetHunter kernel based on neutrino |
| `shandongtlb/kernel_samsung_sm8350_S21U` | Galaxy S21 Ultra (SM-G9980) | One UI NetHunter kernel |
| `shandongtlb/kernel_xiaomi_sm8350_M11` | Mi 11 | MIUI 12.0.22 NetHunter kernel |
| `matthewrackley/Moto-G-Stylus-2022_Kali-NH` | Moto G Stylus 5G (2022) / Edge 30 Fusion | Previously mis-mapped to Nexus 5 |
| `Kirito6785/KALI-NETHUNTER-KERNEL-FOR-ONLY-RM6785-` | Realme 6 / 6i / 7 (RM6785) | Previously mis-mapped to Galaxy Nexus |
| `piashmsu/nubia-nx709s-kernel` | Nubia Red Magic 7S Pro (NX709S) | GKI 5.10 build workspace |
| `Anmol6002/nethunter-kernel-smx115` | Galaxy Tab A9 LTE (SM-X115) | Two repositories from the same maintainer |
| `cmjester6421/kali_nethunter_lgg2` | 7 LG G2 variants | One source covering d800/d801/d802/d803/ls980/vs980/f320 |
| `evost/android_kernel_leeco_msm8996_lineage_kali_nethunter` | LeEco Le 2, Le Pro3 | Source-only NetHunter kernel |
| `Retardog/Nethunter_Kernel_Nord_AC2001` | OnePlus Nord N200 5G | AC2001 model hint |

The full addition list is in `data/deep_rows.csv` and `data/deep_repos.json`.

## clarencelol integration

`kernel_xiaomi_sm6250` is not a single-device release. Its release notes name the whole miatoll family, including the Redmi Note 10 Lite. It publishes 30 releases and 124 assets, with MIUI, HyperOS, and AOSP branches plus KSU and NONKSU variants.

Integrated as:

- `gram` POCO M2 Pro
- `curtana` Redmi Note 9S
- `joyeuse` Redmi Note 9 Pro
- `excalibur` Redmi Note 9 Pro Max
- `miatoll` Redmi Note 10 Lite

Direct assets are attached for all five rows. The website now recommends clarencelol for these devices instead of a zero-byte boot-image lead.

## Recommendation and mapping errors corrected

| Problem | Correction |
|---|---|
| `Naster17/NetHunter-Kernels` was listed for Redmi Note 9 (`merlinx`) | README is Redmi Note 9 Pro only; the `merlinx` row was removed |
| `KirillTank/Kernel-xiaomi_sm6150` was listed for Redmi Note 10 (`mojito`) | README supports `sweet` / `sweetin` only; the `mojito` row was removed |
| `cycoslave/kali-nethunter-kernels` was treated as a OnePlus One kernel | It is a copy of the official NetHunter devices repository; removed as a device source |
| A Galaxy S20 Ultra kernel was stored under codename `c2s` | Moved to `z3s` (c2s is Note20 Ultra) |
| OPPO A72 and Galaxy A72 were split despite the same `a72q` hint | Merged under Galaxy A72 |
| Moto G Stylus / Edge 30 Fusion rows used the placeholder name `device (milanf)` | Merged under one `milanf` card with 6 sources |
| Realme RM6785 was shown as Galaxy Nexus | Corrected to the Realme RM6785 device |
| Nubia NX709S showed a `stock-boot-backup` file as its download | Stock/backup/opensource assets are now excluded from direct downloads |
| Galaxy Tab A9 showed a stock opensource ZIP as a kernel | Same asset filter now rejects stock and opensource archives |
| Recommended source and download button could point to different kernels | Download now follows the recommended source first, then its release page |
| Redmi Note 9 Pro and Redmi Note 9 Pro (Global) were separate cards | Device-name canonicalization now merges them |
| Brand prefixes created duplicate cards | Grouping strips manufacturer prefixes while keeping a readable display name |

## Website assets

The site now exposes:

- 313 canonical device cards
- 640 kernel records
- 487 source repositories
- 32 devices with a direct file
- 27 devices with a ZIP
- 9 devices with an IMG
- 5 developer-reported boot cases

Direct downloads are still gated by an ownership check: a release asset is only shown as a device download when the repository name, device name, codename, or a known family alias matches the device.

## Remaining gaps

1. 92 deep-search candidates remain unresolved. Most are generic builders, patch sets, Termux/chroot tools, driver-only repositories, or multi-device GKI kernels without a device list. Conservative exclusion is intentional.
2. 67 of 999 checked URLs returned non-200 during the first link sweep. Most were HTTP 429 rate limits; confirmed 404 repositories were removed when they were duplicate or non-device sources, and historical dead links remain marked in notes.
3. No hardware was available. Boot, monitor mode, injection, and HID claims remain self-reported.
4. XDA, Telegram, YouTube, Reddit, and blogs are still not machine-accessible. Long-tail ports that exist only in videos or chat threads cannot be claimed as covered.
5. Multi-device GKI projects such as `nullptr-t-oss/Dragonw1nd-Kernels` and `cyberknight777/android_kernel_nethunter` need manual README/branch inspection before they can be attached to specific devices.

## Next actions

1. Manually inspect the remaining multi-device GKI and builder repositories and attach only devices that are explicitly named.
2. Retry the 429 URLs with a slower queue and remove confirmed dead repositories from the public source buttons.
3. Expand model-number matching for Samsung SM-* and Motorola XT-* repositories.
4. Add per-device release history and branch/ROM compatibility once the remaining sources are resolved.
