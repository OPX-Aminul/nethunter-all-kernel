# NetHunter All Kernel

An evidence-first database of Kali NetHunter Android kernels, kernel ports, and device-specific builds, packaged with a fast, mobile-friendly static website.

**Live site:** https://opx-aminul.github.io/nethunter-all-kernel/

The project collects public kernel sources, release binaries, installation notes, ROM compatibility statements, and boot reports. It deliberately separates **what a source claims** from **what has been independently verified**. No kernel in this dataset has been independently boot-tested by this project.

## Coverage

| Metric | Count |
|---|---:|
| Device cards on the website | 313 |
| Kernel records in the master dataset | 640 |
| Unique source repositories | 487 |
| Device cards with at least one direct file | 32 |
| Kernel rows with a direct ZIP/IMG/archive | 36 |
| Best-evidence recommendations | 117 |
| Developer-reported boot rows | 19 |
| Compatibility claims without a boot test | 19 |
| Rows reported not booting | 4 |
| Boot status not verified | 598 |
| Kernels with no prebuilt file (build queue) | 604 |
| Mirrored releases in this repository | 70 |
| Mirrored developer assets | 170 |
| Independently verified boot reports | 0 |

Counts are generated from `data/nethunter_master.csv` and `site/data.json`. The website is the canonical human-readable view; the CSV is the canonical machine-readable table.

## Download and release model

- If a developer already published a flashable ZIP or boot image, the site links to it.
- The `Publish kernel releases` workflow mirrors validated developer files into this repository's Releases, one release per device, kernel, and upstream tag. The current mirror contains 70 releases and 170 assets.
- If no prebuilt file exists, the kernel is marked `source build required`. It is not replaced with a generic ZIP and it is not published as if it were tested.
- Source-only kernels are listed in `data/build_queue.csv`. A real build needs the exact codename, defconfig, kernel branch, toolchain, AnyKernel3 block path, and ROM target.
- The `Build source kernel` workflow is deliberately gated: it only runs a recipe from `data/build_recipes.csv` and can publish a draft release after a successful build.

See `docs/nethunter-release-audit.md` for the per-device kernel/release counts and `docs/nethunter-kernel-build-guide.md` for the build policy.

## What the site shows

- Search by device, codename, model number, developer, ROM, or kernel version.
- Filter by evidence status, NetHunter feature, direct-file availability, and sort order.
- Per-device source and fork counts, recommended kernel, last update, and download links.
- Per-source status lines:
  - **Boot**: developer-reported, compatibility claim, reported not booting, or not verified.
  - **Working**: the same evidence scope, never upgraded to "verified".
  - **Files**: direct ZIP/IMG/archive count.
  - **Guide**: README installation guide, README flash notes, generic guide only, or no guide.
  - **Releases**: release/tag count and the release source.
  - **ROM**: ROM or Android version stated by the source.
- "Direct files only" mode filters both the device list and the kernels inside each card. The download button then points at an actual file-bearing source, not an empty release page.

## Evidence model

| Label | Meaning |
|---|---|
| `Developer-reported boot` | The source text says the kernel was flashed, booted, or tested on a real device. It is still self-reported. |
| `Compatibility claim` | The source says it works with a device, ROM, or kernel line, but provides no boot test. |
| `Reported not booting` | The source reports a bootloop, failed boot, or non-working build. |
| `Not verified` | No explicit boot statement was found in the inspected README, release text, or notes. |

Feature claims (monitor mode, packet injection, HID/BadUSB, external Wi-Fi) follow the same rule: they are recorded only when the source states them, with the evidence level kept visible.

## Repository layout

```text
.
├── data/                  Raw and curated CSV/JSON research data
│   ├── nethunter_master.csv
│   ├── nethunter_master.json
│   ├── nethunter_device_catalog.csv
│   ├── nethunter_feature_matrix.csv
│   └── ...
├── docs/                  Reports, catalogs, evidence lists, research log
├── site/                  Static website and its generated dataset
│   ├── index.html
│   ├── app.js
│   ├── styles.css
│   ├── build_data.py
│   └── data.json
├── scripts/               Audit, release mirroring, and build tooling
├── .github/workflows/     Release publication and gated source build
├── README.md
└── LICENSE
```

## Branches

- `main` contains the complete project: research data, reports, build script, and website source.
- `gh-pages` contains only the deployable contents of `site/` at the branch root. GitHub Pages serves this branch.

## Automation

| Workflow | Trigger | Purpose |
|---|---|---|
| `Publish kernel releases` | Manual | Mirror validated developer ZIP/IMG files, rebuild the site dataset, and refresh the `gh-pages` snapshot. |
| `Build source kernel` | Manual | Build one recipe from `data/build_recipes.csv`, validate the ZIP, and optionally create a draft release. |

Dry-run the mirror first:

```bash
# Show the planned releases and asset counts without uploading
python3 scripts/publish_kernel_releases.py --dry-run
```

## Run locally

```bash
# Serve the static site on port 8080
python3 -m http.server 8080 --directory site
```

Open `http://localhost:8080`.

## Rebuild the website dataset

```bash
# Regenerate site/data.json from the master CSV and guide data
python3 site/build_data.py
```

The build script expects `data/nethunter_master.csv`, `data/nethunter_guides.json`, and the README/release caches referenced by the research pipeline. The committed `data.json` is ready to serve without running the build.

## Data sources

The dataset is compiled from public sources, including the official Kali NetHunter device registry, GitHub repositories and releases, GitLab projects, project READMEs, and public device/kernel inventories. Every row keeps its source URL and the evidence text used for its status.

This is a best-effort catalog, not a guarantee of completeness. Regional models, private Telegram builds, deleted repositories, and login-gated forums may be missing.

## Before flashing

- Match the exact codename and, where possible, the model number.
- Match the ROM, Android version, kernel branch, and security patch level.
- Read the linked source and installation notes before flashing.
- Back up the current boot image and data.
- A wrong kernel can brick the device or prevent boot. You flash at your own risk.

## License

Original code, documentation, and dataset structure are released under the MIT License. See `LICENSE`.

Upstream kernels, binaries, trademarks, and quoted source text remain the property of their respective authors and are subject to their own licenses. Kali NetHunter is a project of Offensive Security. This project is not affiliated with or endorsed by Offensive Security.
