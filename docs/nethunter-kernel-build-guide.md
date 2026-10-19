# Kernel Build and Release Guide

This project separates three things that are often mixed together:

1. A source repository exists.
2. A developer published a flashable ZIP or boot image.
3. A build was actually produced and tested for an exact device/ROM.

The website keeps those states separate. A source link is not a download, and a generic AnyKernel3 ZIP is not a kernel.

## Current coverage

- 640 kernel records.
- 36 records have a direct developer ZIP/IMG/archive.
- 604 records are source-only or release-only with no kernel file.
- 32 device cards have at least one prebuilt file.
- 281 device cards have no prebuilt file.

The full per-device table is in `data/device_availability.csv` and `docs/nethunter-release-audit.md`. The source-only queue is `data/build_queue.csv`.

## Publishing already-built developer files

`scripts/publish_kernel_releases.py` groups assets by device, kernel, and upstream release tag. It:

- skips full NetHunter installers, rootfs images, and source archives;
- downloads each asset;
- rejects files above GitHub's 2 GB limit, empty files, and invalid ZIPs;
- creates one release per device + kernel + upstream tag;
- uploads the original file names and records a source-to-mirror URL map;
- writes `site/mirrored_releases.json`, which the website uses for download buttons.

Dry run:

```bash
python3 scripts/publish_kernel_releases.py --dry-run
```

One codename:

```bash
python3 scripts/publish_kernel_releases.py --codename gram --token "$GITHUB_TOKEN"
```

The GitHub Actions workflow `Publish kernel releases` runs the same script and then rebuilds `site/data.json` and the `gh-pages` snapshot. It supports `dry_run`, `codename`, `limit`, and `max_assets` inputs.

## Building a missing kernel

The project does not auto-build all 604 source-only records. A safe build needs:

- the exact device codename and model;
- the matching kernel source branch or commit;
- a working defconfig for that branch;
- the correct toolchain for the kernel age;
- the correct AnyKernel3 block device and partition layout;
- the target ROM, Android version, and vendor security patch;
- a recovery/fastboot procedure for that exact device.

Without those, a build can bootloop the phone or write to the wrong partition. GitHub Actions cannot guess them from a repository name.

### Official Kali builder

Kali publishes the NetHunter kernel builder:

```bash
# Inside the kernel source tree
git clone https://gitlab.com/kalilinux/nethunter/build-scripts/kali-nethunter-kernel.git

# Review config and local.config before building
cd kali-nethunter-kernel
./build.sh
```

Official docs: https://www.kali.org/docs/nethunter/building-nethunter/

The builder expects a `nethunter_defconfig`, Kali's patches, and the matching Android toolchain. It is designed for an operator who can verify the device tree and ROM, not for unattended mass builds.

### Gated GitHub Actions builder

`Build source kernel` reads one row from `data/build_recipes.csv`:

```csv
recipe_id,device,codename,repository_url,ref,defconfig,arch,block_device,toolchain,notes
```

Required fields:

- `repository_url`: kernel source.
- `codename`: exact device codename.
- `defconfig`: file name under `arch/<arch>/configs`, with or without `_defconfig`.
- `arch`: usually `arm64`.
- `block_device`: AnyKernel3 `BLOCK=` value, for example `/dev/block/bootdevice/by-name/boot`.
- `toolchain`: `clang` or `gcc`.

The workflow:

1. Loads the recipe; it fails if the ID is missing.
2. Clones the source and the defconfig.
3. Builds `Image.gz`.
4. Refuses to package if no kernel image was produced.
5. Clones AnyKernel3, sets the device name and block path, and validates the ZIP.
6. Uploads the ZIP as a workflow artifact.
7. Optionally creates a **draft** release for manual review.

It never publishes a public release automatically.

### Adding a recipe safely

1. Build manually on a test device or with a maintainer who has the device.
2. Record the exact source commit, defconfig, toolchain, block device, ROM, and Android version.
3. Add one row to `data/build_recipes.csv`.
4. Run the workflow with `publish_draft=true`.
5. Flash the draft on the exact device/ROM.
6. Only then promote the draft to a public release and add it to the site map.

## Release naming

Mirrored releases use:

```text
nh-<codename>-<source-repo>-<upstream-tag>
```

Example:

```text
nh-gram-kernel-xiaomi-sm6250-v4-14-343
```

Source builds use:

```text
build-<codename>-<YYYYMMDDHHMM>
```

## Licensing and attribution

Kernel source is generally GPL, but release archives can contain vendor blobs, firmware, or other files with separate terms. Every mirrored release keeps the upstream source and release links. Do not remove attribution when reusing a file.

## Safety

- No kernel in this dataset has been independently boot-tested by this project.
- A successful compile does not prove the kernel boots.
- A booting kernel on one ROM does not prove it works on another.
- Back up the boot partition before flashing.
