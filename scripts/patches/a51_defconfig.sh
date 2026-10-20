#!/usr/bin/env bash
set -euo pipefail

# The upstream build.sh passes a path to `make` instead of a defconfig target.
sed -i 's#^nh_defconfig=.*#nh_defconfig="nethunter_defconfig"#' build.sh
grep -q '^nh_defconfig="nethunter_defconfig"' build.sh
