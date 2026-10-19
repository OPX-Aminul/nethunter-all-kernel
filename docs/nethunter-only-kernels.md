# Kali NetHunter Kernel Index (Filtered)

Compiled October 2026. Scope: only Kali NetHunter kernels and ports. This file is the summary; the full listings are in the linked files.

## What was searched

| Source | Scanned | Retained | Method |
|---|---:|---:|---|
| Official NetHunter registry | - | 126 devices / 191 kernels / 275 variants | `devices.yml` from the official kernels repo |
| GitHub | 474 unique repos | 154 | REST search API, 6 queries (`nethunter`, `nethunter kernel`, `kali nethunter`, `topic:android`), pages and star-sorted results |
| GitLab | 500 unique projects | 131 | REST projects API, query `nethunter`, 5 pages of 100 |
| XDA / YouTube / Google | not machine-readable | 0 | Search pages returned bot challenges or require API keys; not scraped |

Filtering removed apps, Termux/chroot setups, Magisk modules, OS distros, tutorials/templates, store data, load-test projects, and repos with no kernel signal.

## Key numbers

| Metric | Count |
|---|---:|
| Official NetHunter devices | 126 |
| Official kernel IDs | 191 |
| Official device/kernel variants | 275 |
| Published kernel authors in official registry | 80 |
| Unique standalone community kernel projects | 144 |
| Standalone projects with 0 stars | 104 |
| Forks of the official NetHunter kernel registry | 93 (incl. builders) |
| Builders/tooling projects | 64 |
| GitHub-hosted official kernel sources | 262 of 275 variants |

Zero stars means low visibility, not low quality. 104 working or attempted ports by individual developers are listed separately.

## Files

- `docs/nethunter-independent-kernels.md` - all 144 standalone community projects, plus the 104 zero-star projects
- `docs/nethunter-forks-and-tooling.md` - official-registry forks, builders, mirrors
- `docs/nethunter-kernels.md` - full official device/kernel registry (275 variants)
- `data/nethunter_independent_kernels.csv` - all 285 retained GitHub/GitLab records
- `data/nethunter_registry_clean.csv` - cleaned official registry
- `data/nethunter_all.csv` - official + independent combined

Batch 1 mission deliverables:

- `docs/nethunter-database-batch1.md` - 27-field database with conservative evidence statuses
- `docs/nethunter-research-log.md` - queries, inaccessible sources, batch plan
- `docs/nethunter-coverage-report.md` - what is and is not covered
- `data/nethunter_database_batch1.csv` - machine-readable 560-row database
- `data/android_device_inventory.csv` - 1,771-row device inventory across sources

## Standalone kernel projects (top of the list)

Sorted by stars. Full list in `docs/nethunter-independent-kernels.md`.

| Repository | Platform | Stars | Updated | Device hint | Description |
| --- | --- | ---: | --- | --- | --- |
| [johanlike/DJY-Oneplus6-or-Oneplus6T-Nethunter-Andrax-Kernel](https://github.com/johanlike/DJY-Oneplus6-or-Oneplus6T-Nethunter-Andrax-Kernel) | GitHub | 192 | 2026-08-23 | oneplus6 | DJY Nethunter And Andrax Kernel Oneplus6-Oneplus6T |
| [ahmed-alnassif/GKID-Kernels](https://github.com/ahmed-alnassif/GKID-Kernels) | GitHub | 88 | 2026-10-19 |  | Blazing-fast GKI kernels with KernelSU / ReSukiSU + SUSFS, Baseband Guard, 300Hz, BBRv3, MGLRU & battery/performance optimizations. Works on all matching GKI devices. |
| [shandongtlb/MI9-Nethunter-Project](https://github.com/shandongtlb/MI9-Nethunter-Project) | GitHub | 72 | 2026-10-16 |  | Xiaomi Mi9 Kali Nethunter kernel for MIUI12-Android 10 |
| [johanlike/DJY-Nethunter-Andrax-Kernel-Source](https://github.com/johanlike/DJY-Nethunter-Andrax-Kernel-Source) | GitHub | 66 | 2026-10-11 | oneplus6 | This is the DJY nethunter kernel source code for Oneplus6 and 6T |
| [Svirusx/Nethunter-Kernel-S20_FE_5G](https://github.com/Svirusx/Nethunter-Kernel-S20_FE_5G) | GitHub | 65 | 2026-10-18 | r8q | Nethunter Kernel for Samsung Galaxy S20 FE 5G - r8q -G781X (Snapdragon) \| Hardened_Kernel based on https://github.com/anthraxx/linux-hardened/commits/4.19 |
| [acai66/Acai-Oneplus6-or-Oneplus6T-Nethunter-Kernel](https://github.com/acai66/Acai-Oneplus6-or-Oneplus6T-Nethunter-Kernel) | GitHub | 40 | 2026-04-12 | oneplus6 | Nethunter kernel for Oneplus 6 and Oneplus 6T |
| [DOITfit/Redmi-K20Pro-Nethunter-Project](https://github.com/DOITfit/Redmi-K20Pro-Nethunter-Project) | GitHub | 37 | 2026-10-05 |  | Redmi-K20-Pro kali nethunter kernel for MIUI_Q |
| [Neternels/android_kernel_xiaomi_sunny](https://github.com/Neternels/android_kernel_xiaomi_sunny) | GitHub | 36 | 2026-09-08 |  | CAFest nethunter kernel based on LA.UM.9.1.r1-11900-SMXXX0.0 with latest upstream-f2fs-stable-linux-4.14.y merged, bb and perf focused. \| Force push warning |
| [acai66/op6-op6t-nethunter-kernel](https://github.com/acai66/op6-op6t-nethunter-kernel) | GitHub | 23 | 2026-04-10 |  | KALI NetHunter kernel for OnePlus 6 and OnePlus 6T |
| [Duhjoker/Mad-Kali-MaxHunter-kernel-prebuilt](https://github.com/Duhjoker/Mad-Kali-MaxHunter-kernel-prebuilt) | GitHub | 19 | 2026-05-23 |  | repository to hold prebuilt kali nethunter kernel |
| [TsingPeng03/Mi8-Nethunter-Project](https://github.com/TsingPeng03/Mi8-Nethunter-Project) | GitHub | 16 | 2026-01-15 |  | Xiaomi Mi8 Kali Nethunter kernel for Android 10 |
| [V3rB0se/Alynx-nethunter-sunfish](https://github.com/V3rB0se/Alynx-nethunter-sunfish) | GitHub | 15 | 2026-08-06 | sunfish | Alynx Nethunter kernel for sunfish pixel 4a |
| [pho5nix/d2s-los23-nethunter-kernel](https://github.com/pho5nix/d2s-los23-nethunter-kernel) | GitHub | 8 | 2026-09-06 |  | Kali Nethunter on Android 16 (LineageOS 23) for Samsung Galaxy Note 10 Plus (d2s / SM-N975F) |
| [WhimsyGiga/Samsung-S20-ultra-exynos-nethunter-kernel](https://github.com/WhimsyGiga/Samsung-S20-ultra-exynos-nethunter-kernel) | GitHub | 8 | 2026-04-12 |  | Custom nethunter kernel for Samsung S20 Ultra Exynos Android 13 |
| [karamdev1/nethunter_kernel_samsung_mt6768](https://github.com/karamdev1/nethunter_kernel_samsung_mt6768) | GitHub | 7 | 2026-10-06 |  | Kali Nethunter Kernel for SM-A325, SM-A225, SM-E225F and SM-M225FV |

## Zero-star single-developer projects (sample)

| Repository | Platform | Updated | Device hint | Description |
| --- | --- | --- | --- | --- |
| [Adrilaw/android_kernel_samsung_j8y18lte](https://gitlab.com/Adrilaw/android_kernel_samsung_j8y18lte) | GitLab | 2025-05-05 |  | Kernel for Samsung J8y18lte running stock android 10 and lineageos 17.1, 18.0, 18.1 and 19.0 version. Also works with Crdroid 6.x , 7.x and 8.x versions. I made custom fo... |
| [agussaepul0-cloud/kernel-lilium-chime-nethunter-RT5370](https://github.com/agussaepul0-cloud/kernel-lilium-chime-nethunter-RT5370) | GitHub | 2026-10-18 |  |  |
| [alexparent062-bit/kernel](https://github.com/alexparent062-bit/kernel) | GitHub | 2026-07-31 |  | kernel for oneplus 8t nethunter with wifi |
| [almost-nowhere/platina-ksunext-nethunter](https://github.com/almost-nowhere/platina-ksunext-nethunter) | GitHub | 2026-10-12 |  | Mi 8 Lite (platina) KernelSU Next + NetHunter kernel and Simplified Chinese NetHunter app |
| [amirtubayi-HACK/nethunter-kernel-a05](https://github.com/amirtubayi-HACK/nethunter-kernel-a05) | GitHub | 2025-11-03 |  |  |
| [Aroichan/oneplus15-nethunter-kernel](https://github.com/Aroichan/oneplus15-nethunter-kernel) | GitHub | 2026-07-13 |  |  |
| [arouf0/nethunter-kernel](https://github.com/arouf0/nethunter-kernel) | GitHub | 2025-06-28 |  |  |
| [art0181/android_kernel_ulefone_armor34plus_gki](https://gitlab.com/art0181/android_kernel_ulefone_armor34plus_gki) | GitLab | 2026-10-10 | armor34plus | NetHunter GKI 6.1 Kernel for Ulefone Armor 34+ (MT6878 / Dimensity 7300) with rtl8812au & BadUSB HID |
| [artnigman-art/begonia-nethunter-kernel](https://github.com/artnigman-art/begonia-nethunter-kernel) | GitHub | 2026-10-01 |  |  |
| [asesoriaogam-collab/nethunter-kernel-j701m](https://github.com/asesoriaogam-collab/nethunter-kernel-j701m) | GitHub | 2026-10-16 |  |  |
| [beronathan9-sudo/nethunter-kernel](https://github.com/beronathan9-sudo/nethunter-kernel) | GitHub | 2026-07-24 |  |  |
| [bhindasinghcommunications123-sketch/begonia-nethunter-kernel](https://github.com/bhindasinghcommunications123-sketch/begonia-nethunter-kernel) | GitHub | 2026-10-03 |  |  |
| [brunodzogovic/kali-nethunter-kernel-motorola-sofiar](https://github.com/brunodzogovic/kali-nethunter-kernel-motorola-sofiar) | GitHub | 2026-09-14 |  | Kali NetHunter kernel for Motorola Sofiar models |
| [CarlosRgoku/Nethunter-Kernel-potter](https://github.com/CarlosRgoku/Nethunter-Kernel-potter) | GitHub | 2024-09-21 | potter |  |
| [cdizzle97/enchilada-nethunter](https://github.com/cdizzle97/enchilada-nethunter) | GitHub | 2018-12-16 |  | nethunter kernel for enchilada |

## XDA, YouTube and general search

Direct scraping of XDA threads, YouTube results, Google or Bing was not performed: XDA/YouTube need an API key or login, and search pages returned bot challenges. Use these manual searches:

- XDA: https://xdaforums.com/search/?q=NetHunter%20kernel
- YouTube: https://www.youtube.com/results?search_query=kali+nethunter+kernel
- Google: https://www.google.com/search?q=%22kali+nethunter%22+kernel+github
- GitHub: https://github.com/search?q=nethunter+kernel&type=repositories
- GitLab: https://gitlab.com/search?search=nethunter+kernel

## Verification and safety

- Repository presence does not prove a booting kernel. Check the device codename, Android base, kernel branch, and whether a prebuilt image exists.
- `fork` and `mirror` records are kept in the CSV but excluded from the unique-project count.
- Stars and timestamps are a snapshot taken during this build.
- Flashing an unsigned or unverified kernel can brick a device. Test only on hardware you can recover.
