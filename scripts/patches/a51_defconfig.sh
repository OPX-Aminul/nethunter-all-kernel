#!/usr/bin/env bash
set -euo pipefail

# Upstream bugs: passes a path to make, and stays inside the toolchain directory.
sed -i 's#^nh_defconfig=.*#nh_defconfig="nethunter_defconfig"#' build.sh
sed -i 's#\$TOPDIR#$topdir#g' build.sh
sed -i 's#^if \[ ! -d "\$topdir/out" \]; then#cd "$topdir"\nif [ ! -d "$topdir/out" ]; then#' build.sh
grep -q '^nh_defconfig="nethunter_defconfig"' build.sh
grep -q '^cd "\$topdir"$' build.sh
