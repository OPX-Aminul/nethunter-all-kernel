#!/usr/bin/env bash
set -euo pipefail

: "${REPOSITORY_URL:?REPOSITORY_URL is required}"
: "${CODENAME:?CODENAME is required}"
: "${DEFCONFIG:?DEFCONFIG is required}"
: "${BLOCK_DEVICE:?BLOCK_DEVICE is required}"
ARCH="${ARCH:-arm64}"
REF="${REF:-}"
TOOLCHAIN="${TOOLCHAIN:-clang}"
OUT_ZIP="${OUT_ZIP:-nethunter-${CODENAME}-$(date -u +%Y%m%d).zip}"

work="$(mktemp -d)"
src="$work/kernel"
ak="$work/AnyKernel3"

echo "Cloning $REPOSITORY_URL"
if [ -n "$REF" ]; then
  git clone --depth 1 --branch "$REF" "$REPOSITORY_URL" "$src"
else
  git clone --depth 1 "$REPOSITORY_URL" "$src"
fi

confdir="$src/arch/$ARCH/configs"
if [ -f "$confdir/$DEFCONFIG" ]; then
  target="$DEFCONFIG"
elif [ -f "$confdir/${DEFCONFIG}_defconfig" ]; then
  target="${DEFCONFIG}_defconfig"
else
  echo "No defconfig '$DEFCONFIG' under $confdir" >&2
  exit 2
fi

echo "Building $target for $ARCH with $TOOLCHAIN"
if [ "$TOOLCHAIN" = "gcc" ]; then
  make -C "$src" O="$work/out" ARCH="$ARCH" "$target"
  make -C "$src" O="$work/out" ARCH="$ARCH" -j"$(nproc)" Image.gz
else
  make -C "$src" O="$work/out" ARCH="$ARCH" CC=clang LLVM=1 "$target"
  make -C "$src" O="$work/out" ARCH="$ARCH" CC=clang LLVM=1 -j"$(nproc)" Image.gz
fi

image=""
for candidate in "$work/out/arch/$ARCH/boot/Image.gz-dtb" "$work/out/arch/$ARCH/boot/Image.gz" "$work/out/arch/$ARCH/boot/Image" "$work/out/arch/$ARCH/boot/zImage"; do
  if [ -s "$candidate" ]; then image="$candidate"; break; fi
done
if [ -z "$image" ]; then
  echo "Build completed without a kernel image. Refusing to package." >&2
  exit 3
fi

echo "Using kernel image $image"
git clone --depth 1 https://github.com/osm0sis/AnyKernel3.git "$ak"
cp "$image" "$ak/$(basename "$image")"
# AnyKernel3 needs the exact device and block path. Refuse to guess.
sed -i "s/^device.name1=.*/device.name1=$CODENAME/" "$ak/anykernel.sh"
sed -i "s#^BLOCK=.*#BLOCK=$BLOCK_DEVICE;#" "$ak/anykernel.sh"
if ! grep -q "^device.name1=$CODENAME" "$ak/anykernel.sh"; then
  echo "Could not set AnyKernel3 device name" >&2
  exit 4
fi
if ! grep -q "^BLOCK=$BLOCK_DEVICE;" "$ak/anykernel.sh"; then
  echo "Could not set AnyKernel3 block device" >&2
  exit 5
fi

mkdir -p dist
( cd "$ak" && zip -r9 "$OLDPWD/dist/$OUT_ZIP" . -x '*.git*' 'README.md' 'LICENSE' )
unzip -l "dist/$OUT_ZIP" | grep -qE "Image|zImage" || { echo "ZIP has no kernel image" >&2; exit 6; }
sha256sum "dist/$OUT_ZIP" > "dist/$OUT_ZIP.sha256"
echo "Wrote dist/$OUT_ZIP"
