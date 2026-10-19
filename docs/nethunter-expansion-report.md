> Status: this report covers the first expansion pass (548 rows). A later deep-search pass added 89 device records and corrected several mappings. Current totals: 640 rows, 487 source repositories, 311 canonical device cards. See `docs/nethunter-deep-search-report.md`.

# NetHunter Expansion Report

Date: 2026-10-19
Scope: public GitHub repositories, releases, README evidence, device inventories, and public Telegram channel previews.

## Headline

The database grew from **461 records / 213 device groups** to **548 records / 282 raw device+codename pairs**, shown on the website as **267 canonical device cards** after merging duplicate name variants.

| Metric | Before | After |
|---|---:|---:|
| Kernel records | 461 | **548** |
| Device + codename pairs | 213 | **282** (267 canonical cards) |
| Distinct source repositories | 333 | **409** |
| Community records | 131 | **218** |
| Direct ZIP/IMG download devices | not tracked | **14** (18 verified assets) |

New this pass:

- **87 new device-kernel records**
- **76 newly resolved independent repositories**
- **69 new device + codename groups**
- **261 additional GitHub repositories screened** from an expanded 1,585-repo search pool

Row status after the merge:

| Status | Records |
|---|---:|
| Source confirmed | 266 |
| Unverified candidate | 186 |
| Developer claimed | 63 |
| Abandoned | 33 |
| **Total** | **548** |

Boot evidence remains conservative: 5 developer-reported boot claims, 0 independently verified boots.

## Requested devices

| Device | Codename | Result |
|---|---|---|
| POCO M2 Pro | `gram` | Binary `new-boot.img` (Magisk-patched NetHunter boot image) via `0x1k4rt1k/miatoll-nethunter-boot` |
| Redmi Note 9 | `merlin` / `merlinx` | Binary ZIP from `killindodo`; source from `ritikthakur22`; source from `Neternels/NetHunter-MT6768` |
| Redmi Note 9 Pro | `joyeuse` | 4 kernels: `dhiimr/NHunter_Joyeuse`, `dhiimr/nethunter_note9pro`, `Naster17/NetHunter-Kernels`, `Anonym3310/AkameKernel-joyeuse`; plus miatoll boot image |
| Redmi Note 9 Pro Max | `excalibur` | miatoll NetHunter boot image (`new-boot.img`) |
| Redmi Note 9S | `curtana` | miatoll NetHunter boot image (`new-boot.img`) |
| Xiaomi Mi 9 | `cepheus` | Already present and retained: 5 records (1 source confirmed, 2 developer claimed, 2 unverified) |

The `miatoll` boot image is explicitly a **binary distribution**, not a source-confirmed kernel. Its README says: "Magisk-patched NetHunter boot image for Xiaomi Miatoll devices", tested on Android 15, kernel 4.14.336, ARM64.

## Direct download devices

All 18 assets across 14 devices returned HTTP 200 during verification. The site sends users to the maintainer's release file; it does not host these files.

| Device | Direct asset |
|---|---|
| POCO M2 Pro / Note 9S / Note 9 Pro / Note 9 Pro Max | `new-boot.img` |
| Redmi Note 9 | `kali-nethunter-kernel-redminote9-20260813-0658.zip` |
| POCO X5 5G | `DarkHunterMoon_reborn...Inject.zip` |
| POCO F4 GT | `boot.img` |
| Pixel 3a | `semi-kernel.zip` |
| Pixel 9a | `tegu-rt2800usb-6.1.145.tar.gz` |
| Galaxy A71 | `gnus-kernel.zip` |
| OnePlus Nord N10 5G | `magisk_patched-30700_HOwgT.img` |
| Xperia 10 II | `kali-nethunter-2026.2-pdx201-los-thirteen-full-repaired.zip` |
| Pixel 3a XL | `semi-kernel.zip` (shared sargo/bonito package) |
| POCO F5 | `NetKernel-V2.zip` and modules |

Additional binary releases exist for Nord 4 (`boot.img`) and Redmi 5A (`Nethunter-Kernel-1.0.zip`); they were found and recorded, but the recommended variant on those device pages is source-first.

## Binary-only and Telegram channels

Public GitHub releases confirm several binary-first projects, including `0x1k4rt1k/miatoll-nethunter-boot`, `GPTmadeit/nethunter-pixel9a-rt2800usb`, `killindodo/merlin...`, and `ruik3z/avalon-ingres`.

Telegram channels referenced by these projects:

`nethunter_kernels`, `WildKernelsTG`, `pocohunter_kernel`, `MrRobin_Ho_Od`, `Hilledkinged`, `COD3XBUILDsDiscussion`, `PARADOX_X20`, `SamsungTweaks`, `TheWildJames`, `hammzabellouch`, `init_user0`, `a14stuffs`, `ahmed_alnassif_tg`, `echo_tester`.

Only the public `t.me/s/<channel>` preview pages were reachable. They expose channel metadata but no enumerable message/file index without joining, so Telegram-only binaries are **not counted as verified device records**. They remain leads, not evidence.

## Prior data confirmation

- All 461 earlier records were retained; no earlier record was deleted.
- 266 source-confirmed official records are unchanged.
- 5 developer-reported boot claims are unchanged.
- The 55 hidden-port discoveries remain in `nethunter-hidden-ports.md`.
- Mi 9 `cepheus` was already covered and was not duplicated.
- New records were deduplicated by repository URL; multi-device repositories fan out only to devices explicitly named in the repository name or description.

## Limits

- The public searchable GitHub universe does not contain "thousands" of distinct NetHunter kernels. The expanded search found 1,585 repositories, reduced to 282 relevant non-fork candidates, and 76 could be resolved to a specific device without guessing.
- GitHub unauthenticated rate limits constrained code and repository search.
- XDA, YouTube, Google, and Reddit were not machine-accessible. Telegram content was not enumerable.
- Feature and boot values remain evidence labels, not independent test results. No row is marked "verified" without reproduction.

## Website

Preview: **https://8080-5f9482488d23365c.monkeycode-ai.live**

The site now shows 267 canonical device cards with:

- device name and codename
- source repository count, summed GitHub forks, kernel count, and direct file count
- recommended kernel and recommendation reason
- direct **Download ZIP / IMG** when a maintainer asset exists, otherwise a releases link
- **per-build download inventory**: every ZIP/IMG/archive, its file type, channel (stable/beta), status, release page, and source link
- **installation guide** for each device: requirements, ordered flashing steps, installation method (recovery image, recovery ZIP, fastboot, Magisk-patched boot, KernelSU module, sideload, source build), customization claims, and safety warnings
- **33 README-derived installation guides** with maintainer notes; the remaining 376 repositories show clearly labeled generic file-type/source-build guidance
- clear labels distinguishing README-derived requirements/customizations from generic file-type steps
- source-code and details buttons
- mobile-first search, status filters, feature filters, "direct files only" filter, sorting by files, and load-more

Data files:

- `data/nethunter_master.csv` — 548 records
- `data/nethunter_expansion.csv` — 87 new records
- `site/data.json` — website payload
- `data/nethunter_final_summary.json` — aggregate metrics
