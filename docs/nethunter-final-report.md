# Kali NetHunter Kernel Database - Final Report
Generated October 2026. The machine-readable master is `data/nethunter_master.csv`; the readable catalog is `docs/nethunter-final-catalog.md`.

## Objective

Discover and document publicly verifiable Android kernels and kernel ports that enable or improve Kali NetHunter compatibility, including obscure and independent projects, and separate source existence from boot/feature evidence.

## Deliverables

| Mission deliverable | Result |
|---|---|
| 1. Device-by-device catalog | `docs/nethunter-final-catalog.md` and `data/nethunter_device_catalog.csv` (343 device/codename groups; 313 canonical cards on the site) |
| 2. Obscure/independent projects | `docs/nethunter-independent-kernels.md` and `docs/nethunter-hidden-ports.md`; 310 deduplicated community kernel projects plus 55 per-device search discoveries |
| 3. Feature compatibility matrix | `docs/nethunter-feature-matrix.md` and `data/nethunter_feature_matrix.csv` |
| 4. Kernels with boot evidence | `docs/nethunter-evidence-lists.md`; 0 independently verified, 19 developer-reported, 4 reported not booting |
| 5. Demonstrated monitor/injection/HID | `docs/nethunter-evidence-lists.md`; developer-reported tests listed, no independent verification |
| 6. Unverified/abandoned/broken/recoverable | `docs/nethunter-evidence-lists.md`; 186 unverified, 42 abandoned, 4 credible not-booting reports |
| 7. Source-linked log and dataset | `docs/nethunter-research-log.md`, `data/nethunter_master.csv`, `data/nethunter_master.json` |
| 8. Coverage report | `docs/nethunter-coverage-report.md` |

## Headline numbers

| Metric | Count |
|---|---:|
| Official NetHunter devices | 126 |
| Official distribution variants | 275 |
| Community kernel projects in master | 310 |
| Device-level GitHub search discoveries | 55 |
| Total kernel rows | 640 |
| Canonical device cards on the site | 313 |
| Unique source repositories on the site | 487 |
| Independent verified boot reports | 0 |
| Developer-reported boot rows | 19 |
| Compatibility claim rows (no boot test) | 19 |
| Rows reported not booting | 4 |
| Boot status not verified | 598 |
| Rows with a direct ZIP/IMG/archive file | 36 |
| Source confirmed (official registry) | 266 |
| Developer claimed (all rows) | 146 |
| Unverified candidate (all rows) | 186 |
| Abandoned (all rows) | 42 |

## Per-source status enrichment

Every row now carries evidence-scoped status fields. The website renders them as small lines under each source so a user can see the basis before flashing.

| Field | Values | Meaning |
|---|---|---|
| `boot_status` | `Developer-reported boot`, `Compatibility claim`, `Reported not booting`, `Not verified` | What the source text actually says about booting; none are independent tests. |
| `working_status` | `Working (developer-reported)`, `Working (claimed)`, `Reported not working`, `Not verified` | Mirrors the boot claim without upgrading it. |
| `boot_note` | quoted line or fallback | The exact README/release sentence, or an explicit "no report" note. |
| `rom_note` | ROM/Android/kernel text or `Not specified` | ROM compatibility stated by the source, not inferred. |
| `direct_file_count` | integer | Count of usable ZIP/IMG/archive links; stock, backup, opensource, and `vendor_boot` assets are excluded. |
| `guide_status` | `README installation guide`, `README flash notes`, `Generic guide only`, `No guide found` | Whether the source itself documents installation. |
| `release_count` / `release_source` | integer / source | GitHub releases, tags, GitLab, non-GitHub, or unavailable. |

The "Direct files only" control filters both the device list and the per-source kernel list. A device remains visible only if at least one source has a real file; inside it, only file-bearing kernels are listed. The download button then points at the first file-bearing source, not at a release page without assets.


## Evidence model

- `Verified boot` requires reliable, independent evidence on the exact variant. The dataset contains 0 such rows.
- `Developer claimed` means the project text makes a claim. Detailed test logs are labelled `Developer-reported test` but remain self-reported.
- `Source confirmed` means the official registry publishes a kernel source entry. It does not mean the kernel boots.
- 9 official registry entries publish a kernel id but no source URL; they are retained as `Unverified candidate` rather than promoted to `Source confirmed`.
- `Unverified candidate` means the project is relevant but boot/features were not established.
- `Abandoned` means no recent maintenance was found; it does not prove the kernel fails.
- `Unknown` is used wherever evidence is absent. No field was filled by assumption.

## Honest limitations

- XDA, YouTube, Google, Telegram, Reddit, and blogs were not machine-accessible. The dataset therefore cannot claim to contain every hidden thread or video-linked port.
- A later deep-search pass ran 14 broad queries with two pages each (341 unique repositories, 155 new versus the previous master). It integrated 79 curated repositories as 89 device records, including the previously missed `clarencelol/kernel_xiaomi_sm6250`. Per-codename query templates are still not exhaustive; see `docs/nethunter-deep-search-report.md`.
- No physical device was available for independent boot, monitor-mode, injection, or HID testing. All 19 "boots" entries are developer self-reports, and 4 rows explicitly report bootloops; 598 rows remain unverified.
- The official registry does not publish model numbers or per-device feature results.
- Regional variants are not assumed compatible; model numbers are mostly `Unknown`.

## Recommended use

1. Start from the exact codename in `data/nethunter_device_catalog.csv`.
2. Treat `Source confirmed` as a build lead, not a compatibility guarantee.
3. Before flashing, read the linked repository and match ROM, kernel branch, and variant.
4. Reproduce developer-reported tests and record the result; only then promote a row to verified.

## Data dictionary

The 29 requested fields are present in `data/nethunter_master.csv`. Extra fields are `manufacturer`, `record_type`, `maintenance_status`, `evidence_url`, `evidence_quote`, `feature_evidence_level`, and `boot_evidence`.

| Field | Meaning |
|---|---|
| `device_name` | Commercial device name, or `Unknown` |
| `model_number` | Exact model, or `Unknown` |
| `codename` | Device codename, or `Unknown` |
| `chipset` | SoC family when stated, else `Unknown` |
| `android_version` | Android/ROM version when stated |
| `kernel_version` | Linux kernel version when stated |
| `rom_compatibility` | Stock/custom ROM when stated |
| `nethunter_features` | Feature claims found in source text |
| `internal_wifi_support` | Internal Wi-Fi evidence |
| `external_wifi_support` | USB Wi-Fi adapter evidence |
| `monitor_mode` | Monitor-mode evidence |
| `packet_injection` | Frame/packet injection evidence |
| `hid_gadget` | HID/BadUSB evidence |
| `usb_gadget` | USB gadget/OTG evidence |
| `required_drivers` | Stated drivers, else `Unknown` |
| `required_patches` | Stated patches/config |
| `root_requirements` | Magisk/KernelSU/etc. |
| `bootloader_requirements` | Unlock requirement if stated |
| `installation_method` | fastboot/TWRP/AnyKernel3 if stated |
| `developer` | Author/maintainer |
| `repository_url` | Source link |
| `release_url` | Release link if found |
| `discussion_url` | Discussion link if found |
| `last_update` | Last repository update, or `Unknown` |
| `evidence_level` | What kind of source was inspected |
| `verification_status` | Mission status |
| `known_limitations` | Stated limitations |
| `confidence` | Low/Medium/High based on evidence depth |
| `notes` | Variant details and resolution notes |
