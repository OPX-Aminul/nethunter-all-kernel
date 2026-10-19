# Mobile Device Kernels - Public Source Documentation

Compiled: October 2026. Sources: official APIs, official project repositories, and public
device databases. This document is a reproducible index of publicly documented mobile
device/kernel support - not a claim that every kernel in existence is listed.

## 1. What this covers

| Source | Devices | Kernel records | What it documents |
|---|---:|---:|---|
| Kali NetHunter | 126 | 191 kernels / 275 variant rows | Device + kernel ID + Android/Linux version + ROM + author + source repo |
| postmarketOS | 555 | 352 kernel packages | Device + kernel package + kernel version + category/status |
| LineageOS | 631 | 77 official kernel repos | Official device roster + shared kernel repositories |
| Ubuntu Touch | 111 | not published per device | Community port + port progress |
| /e/OS | 199 | not published per device | Device + Android base version + official/community build |
| GitHub (independent repos) | 59 repos | - | Publicly indexed independent mobile kernel projects |

Unified dataset: `data/mobile_devices_kernels_unified.csv` (1,771 rows, 1,297 distinct
codenames across sources).

Important caveat on matching: postmarketOS prefixes codenames with the vendor
(`samsung-klte`), while LineageOS/NetHunter use the bare codename (`klte`). The zero
overlap reported between postmarketOS and the Android sources is a naming artifact, not
proof that the devices are different.

## 2. Files and what each contains

| File | Content |
|---|---|
| `docs/nethunter-kernels.md` | Full NetHunter device/kernel table (275 variant rows) |
| `docs/nethunter-only-kernels.md` | NetHunter-only filtered summary and search coverage |
| `docs/nethunter-independent-kernels.md` | 139 standalone community NetHunter kernel projects |
| `docs/nethunter-forks-and-tooling.md` | NetHunter forks, builders, and mirrors |
| `docs/postmarketos-devices.md` | All 555 pmaports devices with kernel package/version |
| `docs/lineageos-devices.md` | All 631 official LineageOS devices |
| `docs/lineageos-kernel-repos.md` | 77 official `android_kernel_*` repositories |
| `docs/ubuntu-touch-devices.md` | 111 Ubuntu Touch ports and progress |
| `docs/eos-devices.md` | 199 /e/OS devices with version and build type |
| `docs/github-mobile-kernel-repos.md` | 59 independent GitHub kernel repositories |
| `data/*.csv` | Machine-readable versions of every table |
| `data/summary.json` | Row counts |

## 3. How "stock ROM" vs "custom ROM" was determined

- NetHunter `devices.yml` descriptions explicitly name the ROM. Descriptions containing
  Stock, TouchWiz, One UI, MIUI, OxygenOS/OOS, Realme UI/RUI, ColorOS, EMUI, or
  "stock" are classified as **stock-based**; LineageOS, CyanogenMod, AOSP, crDroid,
  and similar are **custom**.
- postmarketOS, LineageOS, Ubuntu Touch, and /e/OS are **custom** distributions by definition.
- This is a label from the upstream description, not a verification that the ROM image
  was built by the vendor.

Across the unified dataset: 840 custom-ROM rows, 666 custom-Linux rows, 199 degoogled
Android rows, and 66 stock-based-ROM rows.

## 4. Kernel feature and package support

### 4.1 What is actually published

| Source | Kernel version | Feature flags | Package/injection support |
|---|---|---|---|
| Kali NetHunter | Yes (Linux version per kernel) | Not in `devices.yml`; features come from kernel config/patches | HID and WiFi injection patches are published in the build repo |
| postmarketOS | Yes, from `linux-*` APKBUILD | Not in deviceinfo; features depend on kernel config | Kernel package + firmware packages listed in `depends` |
| LineageOS | Not in device wiki | Not published per device | Shared kernel repos; configs live in each repo |
| Ubuntu Touch | Not in device list | Not published per device | Port page only |
| /e/OS | Not published | Not published | Build channel only |

Therefore a per-device "supports packet injection / HID / SDR" column cannot be
truthfully filled from these sources alone. Anyone claiming a complete per-device
feature matrix without reading each kernel config is guessing.

### 4.2 NetHunter kernel features that are documented upstream

The official NetHunter kernel build repository publishes these patch families:

| Capability | Upstream evidence | Scope |
|---|---|---|
| USB HID / BadUSB gadget | `patches/hid/hid_gadget-4.4.patch`, `patches/hid/hid_gadget-4.14.patch` | Kernels 4.4 and 4.14; newer kernels may include upstream gadget support |
| WiFi monitor mode / packet injection | `patches/wifi/wifi-injection-4.14.patch` | Kernel 4.14 patch; depends on the wireless driver |
| External USB WiFi adapters | Documented in NetHunter wireless-card guide | Adapter/chipset dependent, not kernel-only |
| SDR (RTL-SDR etc.) | NetHunter kernel config guides (SDR section) | USB host mode + driver config |
| CAN / SocketCAN | NetHunter kernel config guide (CAN section) | Kernel config dependent |
| NFS | NetHunter kernel config guide (NFS section) | Kernel config dependent |
| Bluetooth / USB arsenal | NetHunter app + kernel USB/Bluetooth config | Device dependent |

Practical verification for any specific device:

```bash
# On a rooted/running device
zcat /proc/config.gz | grep -E 'CONFIG_USB_CONFIGFS_F_HID|CONFIG_MAC80211|CONFIG_CFG80211|CONFIG_CAN|CONFIG_NFS_FS'

# From a kernel image or boot.img
extract-ikconfig boot.img | grep -E 'CONFIG_USB_CONFIGFS_F_HID|CONFIG_MAC80211|CONFIG_CFG80211'
```

If `/proc/config.gz` is absent, the config was not enabled or was stripped.

## 5. Independent and "unknown" developers

The user's concern is valid: many working device kernels never appear in a general web
search because they live in personal GitHub/GitLab forks, Telegram groups, or XDA threads.
This index captures the public, machine-readable part:

- NetHunter `devices.yml` records the kernel author and clone URL per kernel.
- postmarketOS records the kernel package and its source in Git.
- LineageOS publishes 77 official shared kernel repos; unofficial forks are not in the
  official roster.
- The GitHub search sample (`github-mobile-kernel-repos.md`) surfaces independent repos
  such as NetHunter kernel forks by individual developers.

Not captured, by design or technical limit:

- Private repositories, deleted repos, and invite-only groups.
- XDA/Telegram/Discord content: not machine-readable, and bulk scraping violates those
  platforms' terms. Individual threads can be linked or read manually.
- Personal identity data. Only publicly published author/maintainer strings are included.

## 6. Reproducing and extending

Commands used to build the dataset:

```bash
# postmarketOS: sparse clone of device metadata only
git clone --depth 1 --filter=blob:none --sparse https://gitlab.com/postmarketOS/pmaports.git
cd pmaports && git sparse-checkout set device

# NetHunter: official device/kernel registry
curl -L https://gitlab.com/kalilinux/nethunter/build-scripts/kali-nethunter-kernels/-/raw/main/devices.yml

# LineageOS: official device wiki and GitHub org repositories
curl -L https://wiki.lineageos.org/devices/
curl -H "Accept: application/vnd.github+json" \
  "https://api.github.com/orgs/LineageOS/repos?per_page=100&page=1&type=public"

# Ubuntu Touch and /e/OS device tables
curl -L https://devices.ubuntu-touch.io/
curl -L https://doc.e.foundation/devices
```

To add a new source, map it to the unified schema:
`source, codename, device, kernel, kernel_version, rom, rom_type, status, author, source_url, notes`.

## 7. NetHunter-only filtered index

A dedicated NetHunter-only pass is in `docs/nethunter-only-kernels.md`:

- 126 official devices, 191 kernel IDs, 275 variants, 80 published authors.
- 139 unique standalone community kernel projects, including 103 with zero stars.
- 93 forks of the official kernel registry, kept separate from unique work.
- 63 builder/tooling projects and 5 re-uploads.

Full listings: `docs/nethunter-independent-kernels.md` and
`docs/nethunter-forks-and-tooling.md`. Machine-readable data:
`data/nethunter_independent_kernels.csv`, `data/nethunter_registry_clean.csv`,
`data/nethunter_all.csv`.

## 8. Limitations and safety

- Coverage is bounded by what each project publishes. There is no global registry of
  every mobile kernel, and many devices have multiple kernels (stock, custom, mainline).
- Kernel availability does not imply bootability. Verify the exact device variant,
  bootloader, Android base, and kernel branch before flashing.
- A kernel entry can be source-only; a prebuilt image may not exist.
- Flashing can brick a device or void warranties. This document is informational only.
- GitHub stars are a popularity snapshot, not a security or quality signal.
