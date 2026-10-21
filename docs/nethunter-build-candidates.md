# NetHunter kernel build-candidate audit

This audit checks which source-only kernel records can be built with a real NetHunter
configuration instead of a guessed one. It does not claim that a candidate compiles or
boots.

## Result

| Item | Count |
|---|---:|
| Source-only kernel rows in `data/build_queue.csv` | 604 |
| Unique source URLs in the queue | 468 |
| Unique GitHub source repositories scanned | 450 |
| Repositories containing `arch/arm64/configs/nethunter_defconfig` or `arch/arm/configs/nethunter_defconfig` | 60 |
| Build-queue rows inside those 60 repositories | 83 |
| Build-queue rows still without any NetHunter defconfig | 521 |
| Repositories also containing an AnyKernel3 script | 6 (7 rows) |
| Repositories with a defconfig but no AnyKernel3 script | 54 |
| GitHub repositories with no NetHunter defconfig | 390 |

The scan uses `raw.githubusercontent.com` HEAD requests against the default branch, so it
does not consume GitHub API search quota. A repository outside GitHub was not scanned.

## Repositories with a defconfig and an AnyKernel script

| Device | Codename | Repository | Candidate ZIP configuration |
|---|---|---|---|
| Redmi Note 8 | `ginkgo` | `ikteach/ginkgo_nethunter_kernel` | `nethunter_defconfig`, block `/dev/block/bootdevice/by-name/boot`, repo `build.sh` |
| Redmi Note 8 | `ginkgo` | `medlam1981/ginkgo_ai_kernel` | `nethunter_defconfig`, block `/dev/block/bootdevice/by-name/boot`, repo `build.sh` |
| Redmi Note 8T | `willow` | `vaginessa/Cuh-Nethunter-Kernel-willow` | `nethunter_defconfig`, block `/dev/block/bootdevice/by-name/boot`, repo `build.sh` |
| Galaxy A51 | `a51` | `leonidas20145/lancer-kernel-galaxy-a51-kernel` | `nethunter_defconfig`, block `/dev/block/platform/13520000.ufs/by-name/boot`, repo `build.sh` |
| Mi A3 | `laurel-sprout` | `yesimxev/android_kernel_laurel_sprout` | `nethunter_defconfig`, block `/dev/block/bootdevice/by-name/boot`, repo `build.sh` |
| Mi 9 | `cepheus` | `asna80/android_kernel_xiaomi_cepheus_MI9` | `nethunter_defconfig`, AnyKernel block is `auto`, repo `build.sh` |

The Mi 9 repository uses `block=auto`; it is not a fixed block path, so packaging it needs a
manual review before it can be treated as a candidate.

## Verified-only build status

| Device | Repository | Status |
|---|---|---|
| Redmi Note 8 / 8T (`ginkgo`) | `ikteach/ginkgo_nethunter_kernel` | **Built**, ZIP validated, not boot-tested |
| Redmi Note 8 / 8T (`ginkgo`) | `medlam1981/ginkgo_ai_kernel` | **Failed**: qcacld build hit `/bin/sh: Argument list too long` |
| Galaxy A51 (`a51`) | `leonidas20145/lancer-kernel-galaxy-a51-kernel` | **Failed**: upstream Kconfig references a missing `rtl8188eus` source directory |
| Redmi Note 8T (`willow`) | `vaginessa/Cuh-Nethunter-Kernel-willow` | Blocked: script expects a local `tc/prelude-clang` that the repo does not contain |
| Mi A3 (`laurel-sprout`) | `yesimxev/android_kernel_laurel_sprout` | Blocked: script hardcodes `/mnt/QuickBoi/LineageOS/22` |
| Mi 9 (`cepheus`) | `asna80/android_kernel_xiaomi_cepheus_MI9` | Blocked: `block=auto` and hardcoded `/mnt/data` toolchain |

A blocked repository is not published with a guessed block path or a guessed toolchain. A failed build is not published at all. Attempt records are in `data/build_attempts.csv`.

## Why 604 ZIPs cannot be published as "perfect"

- 54 of the 60 NetHunter-defconfig repositories have no AnyKernel3 script. Their block
  device and device-name list must be recovered from the device, a working boot image, or
  the developer's instructions.
- 390 GitHub repositories have no `nethunter_defconfig`. Building them with a vendor
  defconfig is possible, but it is not the same kernel configuration the developer used.
- A successful compile only proves that an image was produced. It does not prove that the
  image boots, that Wi-Fi or HID works, or that the ZIP is safe for a specific ROM.
- No physical device is attached to this project, so every build remains
  **project-built, not boot-tested**.

## Publication rule

A build is published only when the recipe has an exact repository, ref, defconfig, and
block device. The first published builds are marked as project builds and are not mixed
with developer-published files. A draft release is preferred until a user confirms boot on
the matching device and ROM.

## Reproduce

```bash
python3 scripts/discover_build_candidates.py
```

The output is `data/build_candidates.csv`. Add validated rows to
`data/build_recipes.csv` and run the `Build source kernel` workflow.


## Completed project builds

| Device | Codename | Source commit | ZIP | Status |
|---|---|---|---|---|
| Redmi Note 8 / 8T | `ginkgo` / `willow` | `6b899fb` | `nethunter-ginkgo-20261020.zip` | Built and ZIP-validated; not boot-tested |

The build record, SHA-256, workflow run, defconfig, and block path are in
`data/project_builds.csv`. The first artifact is a draft release until a matching device
confirms boot.
