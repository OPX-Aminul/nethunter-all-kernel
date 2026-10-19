# NetHunter Evidence Lists
This file separates what is verified, what a developer reports, what is merely claimed, and what is unresolved. It follows the mission rule that a successful boot does not prove monitor mode, packet injection, or HID.

## 1. Kernels with verified boot evidence

**None (0).** No independent boot report was available for any exact device variant in this dataset. The official registry proves that a kernel source entry exists, not that it booted.

## 2. Kernels with developer-reported boot evidence (5)

These are explicit statements in the project's own documentation. They are not independent verification.

| Device | Variant/codename | Project | Evidence excerpt |
|---|---|---|---|
| Samsung Galaxy Note 10 Plus | `d2s` | <https://github.com/pho5nix/d2s-los23-nethunter-kernel> | Phone boots into LineageOS as normal. Verify the kernel is live. |
| Samsung Galaxy Note20 Ultra (Exynos) | `c2s` | <https://github.com/MocLG/android_kernel_samsung_exynos990_nethunter> | V4.4 is the final release, and it is complete and working. Everything listed below was verified on hardware, including internal Bluetooth, which was the last feature to land. |
| Google Pixel 11 | `cubs` | <https://github.com/Gajeel420/cubs-gki-rt2800usb> | \| Boot to Android 17 \| verified \| |
| OnePlus 8T | `kebab` | <https://github.com/Mist3r-N0b0dy/NetHunter_Kernel-OP8T-crDroid12-A16> | > ## Status: SOLVED ✅ — kernel boots, monitor mode **and packet injection** work on both tested adapters |
| Nothing Phone (1) | `spacewar` | <https://github.com/thw01f/nethunter-spacewar-kernel> | It boots on **crDroid 11 (Android 15)** and preserves working WiFi, touch, and Bluetooth while enabling NetHunter's attack surface. |

## 3. Developer-reported monitor mode / packet injection / HID


### Monitor Mode

| Device | Project | Evidence excerpt |
|---|---|---|
| Google Pixel 11 (`cubs`) | <https://github.com/Gajeel420/cubs-gki-rt2800usb> | \| Boot to Android 17 \| verified \| |
| Xiaomi Redmi Note 8 Pro (`begonia`) | <https://github.com/fxritadicc/begonia-kali_nethunter-kernel> | \| **USB HID Gadget (BadUSB)** \| ÇALIŞIYOR \| `/dev/hidg0` ve `/dev/hidg1` desteği ile Rubber Ducky (BadUSB) saldırıları. \| |
| OnePlus 8T (`kebab`) | <https://github.com/Mist3r-N0b0dy/NetHunter_Kernel-OP8T-crDroid12-A16> | > ## Status: SOLVED ✅ — kernel boots, monitor mode **and packet injection** work on both tested adapters |
| Pixel 9 Pro (`caiman`) | <https://github.com/shemed-mwangome/nethunter-komodo-usbwifi> | rides a `/vendor/firmware` overlay. Developed and verified on `6.1.162-android14-11-g2ec90535fa34-ab15810641`. > For authorized security testing on hardware and networks you own. Monitor mode / injection is a > penetration-testing capability — use it lawfully. |
| Pixel 9 Pro XL (`komodo`) | <https://github.com/shemed-mwangome/nethunter-komodo-usbwifi> | rides a `/vendor/firmware` overlay. Developed and verified on `6.1.162-android14-11-g2ec90535fa34-ab15810641`. > For authorized security testing on hardware and networks you own. Monitor mode / injection is a > penetration-testing capability — use it lawfully. |
| Pixel 9a (`tegu`) | <https://github.com/GPTmadeit/nethunter-pixel9a-rt2800usb> | hields.io/badge/kernel-GKI%206.1.145-38bdf8"> <img alt="driver" src="https://img.shields.io/badge/driver-rt2800usb-a78bfa"> <img alt="status" src="https://img.shields.io/badge/monitor%20mode-verified%20%E2%9C%93-22c55e"> <img alt="license" src="https://img.shi |
| F(x)tec Pro1 X (`pro1x`) | <https://github.com/xokitten999/pro1x-nethunter-kernel> | # pro1x-nethunter-kernel A custom, NetHunter-patched Android kernel for the Fxtec Pro1X (SM6115/Bengal platform), built from source with Wi-Fi injection (confirmed working monitor mode) and USB HID/BadUSB gadget support (confirmed working). Full writeup below  |

### Packet Injection

| Device | Project | Evidence excerpt |
|---|---|---|
| Google Pixel 4a 5G (`bramble`) | <https://github.com/Hotelk52339/nethunter_kernel_google_redbull> | - **WiFi monitor mode** — native RX on internal WCN3998 (`con_mode=4`) |
| Realme X (`rmx1901`) | <https://github.com/ishashanknigam/kernel-realme-RMX1901> | \| WCN3998 packet injection (controlled Probe Requests) \| ✅ Verified \| Phase 7 independently captured all 20 controlled broadcast Probe Request transmissions over the air on channel 6; 20/20 exact frame matches \| |
| OnePlus 8T (`kebab`) | <https://github.com/Mist3r-N0b0dy/NetHunter_Kernel-OP8T-crDroid12-A16> | > ## Status: SOLVED ✅ — kernel boots, monitor mode **and packet injection** work on both tested adapters |
| Samsung Galaxy S10e (SM-G970N) (`beyond0lte`) | <https://github.com/unreliablecode/ArtisanROM-PomPomSU-NetHunter> | - USB HID, ACM, generic serial, RNDIS and mass storage. |
| POCO X5 5G (`moonstone`) | <https://github.com/edbastida/Kernel_Stone_DarkHuntermoon-Reborn> | atures ### WiFi & Injection - **wlan0 native frame injection** — qcacld-3.0 Madara273 5.4.302 series, validated 100% with `aireplay-ng --test` - mac80211 packet injection patch - wlan0 monitor mode support (QCACLD-3.0) - Monitor channel change without restrict |

### Hid Gadget

| Device | Project | Evidence excerpt |
|---|---|---|
| Xiaomi Redmi Note 8 Pro (`begonia`) | <https://github.com/fxritadicc/begonia-kali_nethunter-kernel> | \| **USB HID Gadget (BadUSB)** \| ÇALIŞIYOR \| `/dev/hidg0` ve `/dev/hidg1` desteği ile Rubber Ducky (BadUSB) saldırıları. \| |
| Nothing Phone (1) (`spacewar`) | <https://github.com/thw01f/nethunter-spacewar-kernel> | It boots on **crDroid 11 (Android 15)** and preserves working WiFi, touch, and Bluetooth while enabling NetHunter's attack surface. |
| F(x)tec Pro1 X (`pro1x`) | <https://github.com/xokitten999/pro1x-nethunter-kernel> | # pro1x-nethunter-kernel A custom, NetHunter-patched Android kernel for the Fxtec Pro1X (SM6115/Bengal platform), built from source with Wi-Fi injection (confirmed working monitor mode) and USB HID/BadUSB gadget support (confirmed working). Full writeup below  |
| Redmi Note 10 Pro (`sweet`) | <https://github.com/piwwing23/sweet-kernel-NetHunter> | ctive* & *Performance* untuk menjaga stabilitas FPS (Zero Stuttering). * **GPU Boost:** Optimalisasi Adreno 618 untuk beban grafis intensif. ### 🛡️ Security & Pentesting * **Full Monitor Mode:** Dukungan penuh untuk audit jaringan nirkabel. * **Packet Injectio |

Rows that only claim support: 26. Rows with source/config evidence only: 43. Full list: `data/nethunter_feature_claims.csv`.

## 4. Unverified candidates (186)

These projects mention NetHunter or device-specific kernel support but have not been inspected far enough to establish boot or features. Full list: `data/nethunter_unverified.csv`.

| Device | Project | Status | Why unverified |
|---|---|---|---|
| Redmi 1S (`armani`) | Unknown | Unverified candidate | Official registry entry (source link missing) |
| Xiaomi Pocophone F1 (`beryllium`) | Unknown | Unverified candidate | Official registry entry (source link missing) |
| Nokia 6.1 Plus (`drg`) | Unknown | Unverified candidate | Official registry entry (source link missing) |
| OnePlus Nord (`oneplus-nord`) | Unknown | Unverified candidate | Official registry entry (source link missing) |
| OnePlus Nord (`oneplus-nord`) | Unknown | Unverified candidate | Official registry entry (source link missing) |
| OnePlus Nord (`oneplus-nord`) | Unknown | Unverified candidate | Official registry entry (source link missing) |
| OnePlus 7 / 7 Pro / 7T / 7T Pro (`oneplus7`) | Unknown | Unverified candidate | Official registry entry (source link missing) |
| Xiaomi Redmi Note 6 Pro (`tulip`) | Unknown | Unverified candidate | Official registry entry (source link missing) |
| Xiaomi Pocophone X3 Pro (`vayu`) | Unknown | Unverified candidate | Official registry entry (source link missing) |
| OnePlus 6 / 6T (`enchilada/fajita`) | <https://github.com/johanlike/DJY-Oneplus6-or-Oneplus6T-Nethunter-Andrax-Kernel> | Unverified candidate | Repository description |
| OnePlus 6 / 6T (`enchilada/fajita`) | <https://github.com/johanlike/DJY-Nethunter-Andrax-Kernel-Source> | Unverified candidate | Repository description |
| Samsung Galaxy S20 FE 5G (Snapdragon) (`r8q`) | <https://github.com/Svirusx/Nethunter-Kernel-S20_FE_5G> | Unverified candidate | Repository description |
| OnePlus 6 / 6T (`enchilada/fajita`) | <https://github.com/acai66/Acai-Oneplus6-or-Oneplus6T-Nethunter-Kernel> | Unverified candidate | README/capability text |
| Xiaomi device (sunny) (`sunny`) | <https://github.com/Neternels/android_kernel_xiaomi_sunny> | Unverified candidate | Repository description |
| OnePlus 6 / 6T (`enchilada/fajita`) | <https://github.com/acai66/op6-op6t-nethunter-kernel> | Unverified candidate | Repository description |
| Google Pixel 3a / 3a XL (`bonito/sargo`) | <https://github.com/Duhjoker/Mad-Kali-MaxHunter-kernel-prebuilt> | Unverified candidate | README/capability text |
| Google Pixel 4a (`sunfish`) | <https://github.com/V3rB0se/Alynx-nethunter-sunfish> | Unverified candidate | README/capability text |
| LG V30+ (`h930ds`) | <https://github.com/SrDayne/lge_msm8998_h930ds> | Unverified candidate | Repository description |
| Xiaomi Redmi 4 / 4X (`santoni`) | <https://github.com/MomboteQ/hackphone_kernel_xiaomi_msm8937> | Unverified candidate | Repository description |
| Xiaomi device (sunstone/moonstone) (`sunstone/moonstone`) | <https://github.com/dare-devil-ex/kernel_xiaomi_stone> | Unverified candidate | Repository description |
| Nothing Phone (3a) / (3a) Pro (`asteroids`) | <https://github.com/Tbeard602/nothing-phone-3a-nethunter> | Unverified candidate | Repository description |
| Xiaomi Redmi 10C (`fog`) | <https://github.com/anomaly-4rc/android_kernel_xiaomi_fog-nethunter> | Unverified candidate | Repository description |
| Xiaomi Redmi 15 (`creek`) | <https://github.com/dr1408/Creek_Nethunter> | Unverified candidate | README/capability text |
| Xiaomi device (sunstone/moonstone) (`sunstone/moonstone`) | <https://github.com/Adithyancoder/Stone-kernel-Nethunter-17> | Unverified candidate | Repository metadata only |
| Xiaomi Redmi 8 / 8A / 7A (SDM439) (`olive/olivelite/olivewood/pine`) | <https://github.com/atsauban/android_kernel_xiaomi_sdm439> | Unverified candidate | Repository description |
| OnePlus Ace 6T (`ce6t`) | <https://github.com/back475/ce6t-nethunter-kernel> | Unverified candidate | README/capability text |
| Galaxy S9 / S9+ (`starlte`) | <https://gitlab.com/mildg0d/exynos9810_starlte_kernel> | Unverified candidate | Repository description |
| Realme 9 Pro 5G (`oscar`) | <https://github.com/sirt-sirt/oscar-nethunter-kernel> | Unverified candidate | README/capability text |
| Samsung Exynos 1380 devices (`s5e8835`) | <https://github.com/TheBizarreAbhishek/android_kernel_samsung_s5e8835> | Unverified candidate | Repository description |
| Samsung Galaxy J8 (2018) (`j8y18lte`) | <https://gitlab.com/Adrilaw/android_kernel_samsung_j8y18lte> | Unverified candidate | Repository description |
| Unknown (`lilium/chime`) | <https://github.com/agussaepul0-cloud/kernel-lilium-chime-nethunter-RT5370> | Unverified candidate | Repository metadata only |
| OnePlus 8T (`kebab`) | <https://github.com/alexparent062-bit/kernel> | Unverified candidate | Repository description |
| Xiaomi Mi 8 Lite (`platina`) | <https://github.com/almost-nowhere/platina-ksunext-nethunter> | Unverified candidate | README/capability text |
| Samsung Galaxy A05 (`a05`) | <https://github.com/amirtubayi-HACK/nethunter-kernel-a05> | Unverified candidate | Repository metadata only |
| OnePlus 15 (`Unknown`) | <https://github.com/Aroichan/oneplus15-nethunter-kernel> | Unverified candidate | Repository metadata only |
| Unknown (`Unknown`) | <https://github.com/arouf0/nethunter-kernel> | Unverified candidate | Repository metadata only |
| Ulefone Armor 34+ (`armor34plus`) | <https://gitlab.com/art0181/android_kernel_ulefone_armor34plus_gki> | Unverified candidate | Repository description |
| Samsung Galaxy J7 Neo (`j7velte`) | <https://github.com/asesoriaogam-collab/nethunter-kernel-j701m> | Unverified candidate | Repository metadata only |
| Unknown (`Unknown`) | <https://github.com/beronathan9-sudo/nethunter-kernel> | Unverified candidate | Repository metadata only |
| Motorola Moto G8 Power (`sofiar`) | <https://github.com/brunodzogovic/kali-nethunter-kernel-motorola-sofiar> | Unverified candidate | Repository description |
| Motorola Moto G5 Plus (`potter`) | <https://github.com/CarlosRgoku/Nethunter-Kernel-potter> | Unverified candidate | Repository metadata only |
| Google Pixel 4 / 4 XL (`coral/flame`) | <https://github.com/chenyjie/coral-nethunter-kernel> | Unverified candidate | README/capability text |
| Unknown (`Unknown`) | <https://github.com/DEADMAN610716/my-nethunter-kernel> | Unverified candidate | Repository metadata only |
| Unknown (`Unknown`) | <https://github.com/deviljin05/GKI-NETHUNTER-KERNEL> | Unverified candidate | Repository metadata only |
| Unknown (`Unknown`) | <https://github.com/deviljin05/GKI-NETHUNTER-KERNEL-WITH-DRIVER-2> | Unverified candidate | Repository metadata only |
| Unknown (`Unknown`) | <https://github.com/deviljin05/Kali-nethunter-kernel-gki-5.10> | Unverified candidate | Repository metadata only |
| Unknown (`Unknown`) | <https://github.com/deviljin05/Kali-nethunter-kernel-testing-phase-> | Unverified candidate | Repository metadata only |
| Unknown (`Unknown`) | <https://github.com/deviljin05/kali-nethunter-kernel-testing-phase-2-> | Unverified candidate | Repository metadata only |
| Xiaomi 11T Pro (`vili`) | <https://github.com/dinelo/vili-nethunter-kernel> | Unverified candidate | Repository metadata only |
| Xiaomi Redmi 9C NFC (`angelican`) | <https://gitlab.com/edmondseropyan6/nethunter_kernel_xiaomi_angelican> | Unverified candidate | Repository description |
| Xiaomi device (cas) (`cas`) | <https://github.com/fahmigk/cas-nethunter-kernel> | Unverified candidate | Repository metadata only |
| Samsung Galaxy A12 (`a12`) | <https://github.com/greenxhatzgreyty/samsung-a127f> | Unverified candidate | Repository description |
| Xiaomi Mi Max 2 (`oxygen`) | <https://github.com/grzegorzpalczynski6-boop/Build-NetHunter-kernel-for-Xiaomi-Mi-Max-2> | Unverified candidate | Repository metadata only |
| Pixel 7a (`lynx`) | <https://github.com/HeRrKrUgEr/nethunter-kernel-lynx> | Unverified candidate | README/capability text |
| Google Pixel 9 Pro Fold (`comet`) | <https://github.com/jdawg867/nethunter-kernel> | Unverified candidate | Repository description |
| Samsung Galaxy A21s (`a21s`) | <https://github.com/karamdev1/nethunter_kernel_samsung_a21s> | Unverified candidate | Repository description |
| Samsung Galaxy A23 (SM-A235F) (`a23`) | <https://github.com/karamdev1/nethunter_kernel_samsung_a235f> | Unverified candidate | Repository description |
| Xiaomi 11 Lite 5G NE (`lisa`) | <https://github.com/Kirolos124/NH-Lisa> | Unverified candidate | README/capability text |
| Samsung Galaxy A05 (`a05`) | <https://github.com/kllr98331-maker/a05-kernel-nethunter> | Unverified candidate | Repository metadata only |
| Xiaomi Redmi Note 4 / 4X (`mido`) | <https://github.com/linlinger/kernel_xiaomi_mido> | Unverified candidate | Repository description |
| Moto G Stylus 5G (2022) / Edge 30 Fusion (`milanf`) | <https://github.com/Madara273/Karui-NetHunter-Kernel-SM7325> | Unverified candidate | Repository description |
| Google Pixel 9 Pro XL (`komodo`) | <https://github.com/maniaco13/NH_kernel_pixel9proxl_komodo> | Unverified candidate | Repository description |
| Xiaomi Mi 10i 5G (`gauguinpro`) | <https://github.com/mashunterbd/Nethunter_kernel_Gauguinpro> | Unverified candidate | Repository description |
| Xiaomi POCO X2 / Redmi K30 (`phoenix`) | <https://github.com/MDXWAJID/phoenix-nethunter-kernel> | Unverified candidate | Repository metadata only |
| Xiaomi POCO X2 / Redmi K30 (`phoenix`) | <https://github.com/MDXWAJID/poco-x2-nethunter-kernel> | Unverified candidate | Repository metadata only |
| vivo iQOO Neo 9 (`neo9`) | <https://github.com/meoflii/nethunter-kernel-neo9> | Unverified candidate | Repository metadata only |
| OnePlus Ace 6T (`Unknown`) | <https://github.com/Muet-ahup/Ace6T-NetHunter-Kernel> | Unverified candidate | Repository metadata only |
| Samsung Galaxy S10+ (`beyond2lte`) | <https://github.com/muhammadfikri-dev/laksanasoft-enterprise-beyond2lte-kernel> | Unverified candidate | README/capability text |
| Samsung Galaxy A10 (`a10`) | <https://github.com/mwafik2002/Nethunter-Kernel-Exynos7885> | Unverified candidate | Repository description |
| Xiaomi POCO F6 (`peridot`) | <https://github.com/pancikula69/peridot-nethunter-kernel> | Unverified candidate | Repository description |
| Unknown (`Unknown`) | <https://github.com/portuguezhj34-spec/Nethunter-kernel> | Unverified candidate | Repository description |
| OnePlus 7 (`guacamoleb`) | <https://github.com/rahulrahuu678-ops/Kali-nethunter-kernel-for-OnePlus-7-GM1901> | Unverified candidate | Repository description |
| Xiaomi Redmi Note 10 Pro (`sweet`) | <https://gitlab.com/RiasJ1Dar/sweet-nethunter-kernel> | Unverified candidate | Repository description |
| Sony Xperia XZ2 (`xz2`) | <https://github.com/salk-cell/nethunter-kernel-xz2> | Unverified candidate | Repository metadata only |
| Xiaomi Redmi Note 7 (`lavender`) | <https://github.com/sauravsinha239/Nethunter_kernel_lavender> | Unverified candidate | Repository description |
| Unknown (`Unknown`) | <https://github.com/secretoryx/nethunter-kernel> | Unverified candidate | Repository metadata only |
| OPPO A37 (`a37`) | <https://gitlab.com/shifujowo/nethunter-kernel-a37> | Unverified candidate | Repository metadata only |
| OnePlus 9R (`lemonades`) | <https://github.com/srezvee-hue/oneplus9r-kernel-autobuild> | Unverified candidate | Repository description |
| Xiaomi Redmi Note 11 (fleur) (`fleur`) | <https://github.com/Sudarshanb789/fleur-nethunter-kernel> | Unverified candidate | Repository metadata only |
| Xiaomi Redmi 8A Dual (`olivelite`) | <https://gitlab.com/sunilkumardasdev/redmi-8a-dual-nethunter-kernel> | Unverified candidate | Repository metadata only |
| Samsung Galaxy S5 LTE Duos (`klteduos`) | <https://github.com/syfaldhbly38-ux/NetHunter-kernel-for-klteduos> | Unverified candidate | Repository description |
| Samsung Galaxy Note 8 (`greatlte`) | <https://github.com/Taha-Sheikh032/Note-8-nethunter-kernel> | Unverified candidate | Repository description |
| Xiaomi Redmi Note 8 Pro (`begonia`) | <https://github.com/tarq04125-lang/begonia-nethunter-kernel> | Unverified candidate | Repository metadata only |
| Xiaomi Redmi Note 8 Pro (`begonia`) | <https://github.com/tarq04125-lang/begonia-NetHunter-Kernel-A14> | Unverified candidate | Repository metadata only |
| Xiaomi Redmi Note 8 Pro (`begonia`) | <https://github.com/Thirushub/begonia-nethunter-kernel> | Unverified candidate | Repository description |
| Moto G Stylus 5G (2022) / Edge 30 Fusion (`milanf`) | <https://github.com/TigerClips1/kali-nethunter-milanf-kernel> | Unverified candidate | Repository metadata only |
| Galaxy A72 (`a72q`) | <https://gitlab.com/vakula2004/a72q-nethunter-kernel> | Unverified candidate | Repository metadata only |
| Google Pixel 7 (`panther`) | <https://github.com/Werq4u8/Pixel-7-panther-kernel-nethunter-cp41.260831.007> | Unverified candidate | Repository metadata only |
| Samsung Galaxy A14 (`a14`) | <https://github.com/xkzetsu2/a14-nethunter-kernel> | Unverified candidate | Repository metadata only |
| Moto G Stylus 5G (2022) / Edge 30 Fusion (`milanf`) | <https://github.com/xthecreator/milanf-nethunter-kernel> | Unverified candidate | Repository metadata only |
| Samsung Galaxy A5 (2016) (`a5xelte`) | <https://github.com/jeanphilippelaflammme/kernel-nethunter-2020.2-rc1-a5xelte-nougat> | Unverified candidate | Per-device GitHub search result |
| Google/Huawei Nexus 6P (`angler`) | <https://github.com/DKingAlpha/nougat-angler-kernel-nethunter> | Unverified candidate | Per-device GitHub search result |
| Redmi 1S (`armani`) | <https://github.com/daedroza/nethunter_kernel_xiaomi_armani> | Unverified candidate | Per-device GitHub search result |
| Xiaomi Pocophone F1 (`beryllium`) | <https://github.com/KekHunterOS/android_kernel_beryllium> | Unverified candidate | Per-device GitHub search result |
| Xiaomi Pocophone F1 (`beryllium`) | <https://github.com/Team-420/android_kernel_xiaomi_sdm845> | Unverified candidate | Per-device GitHub search result |
| Samsung Galaxy S10 (`beyond1lte`) | <https://github.com/SomewhatAwake/exynos9820-beyond1lte-ksu-nh> | Unverified candidate | Per-device GitHub search result |
| Samsung Galaxy S10+ (`beyond2lte`) | <https://github.com/SKyLiNe1980/GemsterKernel> | Unverified candidate | Per-device GitHub search result |
| Xiaomi Mi 9 cepheus (PixelOS 15) (`cepheus`) | <https://github.com/ibaoly/kernel_xiaomi_cepheus> | Unverified candidate | Per-device GitHub search result |
| Xiaomi Mi 9 cepheus (PixelOS 15) (`cepheus`) | <https://github.com/asna80/android_kernel_xiaomi_cepheus_MI9> | Unverified candidate | Per-device GitHub search result |
| Xiaomi Mi 9T (`davinci`) | <https://github.com/KoraiLabs/davinci-nethunter-21> | Unverified candidate | Per-device GitHub search result |
| Google Nexus 7 (2013) (`flo`) | <https://github.com/0E800/Nexus-7-2013-Flo-Experimental> | Unverified candidate | Per-device GitHub search result |
| Redmi Note 8 (`ginkgo`) | <https://github.com/medlam1981/ginkgo_nethunter_kernel> | Unverified candidate | Per-device GitHub search result |
| Redmi Note 8 (`ginkgo`) | <https://github.com/Neternels/NetHunter-Ginkgo> | Unverified candidate | Per-device GitHub search result |
| Redmi Note 8 (`ginkgo`) | <https://github.com/Team-420/NetHunter-ginkgo> | Unverified candidate | Per-device GitHub search result |
| Redmi Note 8 (`ginkgo`) | <https://github.com/Anonym3310/AkameKernel-ginkgo> | Unverified candidate | Per-device GitHub search result |
| Google Nexus 5 (`hammerhead`) | <https://github.com/mayankmetha/Nethunter-Hammerhead-Kernel> | Unverified candidate | Per-device GitHub search result |
| Samsung Galaxy Note 3 (`hlte`) | <https://github.com/majid10243/nethunter-hlte-build> | Unverified candidate | Per-device GitHub search result |
| Xiaomi Redmi 3 / 3 Pro (`ido`) | <https://github.com/l33tnoob/ido_kernel-kali> | Unverified candidate | Per-device GitHub search result |
| Samsung Galaxy S5 (`klte`) | <https://github.com/amahlaka/android_kernel_samsung_klte_nethunter> | Unverified candidate | Per-device GitHub search result |
| Xiaomi Mi A3 (`laurel-sprout`) | <https://github.com/CaliBerrr/NetHunter_laurel_sprout> | Unverified candidate | Per-device GitHub search result |
| LG K20 Plus (`lv517`) | <https://github.com/robnew/NetHunter_K20plus_arm64_Kernel-Source> | Unverified candidate | Per-device GitHub search result |
| Xiaomi Redmi Note 9S/Pro (`miatoll`) | <https://github.com/AyusmanNanda/Nethunter-relese-miatoll> | Unverified candidate | Per-device GitHub search result |
| Xiaomi Redmi Note 4X (`mido`) | <https://github.com/Serp3n7/Astraea-kernel-mido> | Unverified candidate | Per-device GitHub search result |
| Xiaomi Redmi Note 4X (`mido`) | <https://github.com/p3h3n9-pr0j3ct/NetHunter-mido-SL-FINAL> | Unverified candidate | Per-device GitHub search result |
| Xiaomi Redmi Note 4X (`mido`) | <https://github.com/p3h3n9-pr0j3ct/NetHunter-mido-Q-FINAL> | Unverified candidate | Per-device GitHub search result |
| Xiaomi Redmi Note 4X (`mido`) | <https://github.com/p3h3n9-pr0j3ct/NetHunter-mido-R-FINAL> | Unverified candidate | Per-device GitHub search result |
| Xiaomi MiPad 1 (`mocha`) | <https://github.com/InfidelRahul/mocha-kernels> | Unverified candidate | Per-device GitHub search result |
| Samsung Galaxy S20 FE 5G (Snapdragon) (`r8q`) | <https://github.com/IslomTI/Nethunter-S20-FE-5G-G78XX> | Unverified candidate | Per-device GitHub search result |
| Samsung Galaxy S20 FE 5G (Snapdragon) (`r8q`) | <https://github.com/hendramanudinata03/NetHunter_samsung_r8q> | Unverified candidate | Per-device GitHub search result |
| Realme C15 Mediatek (`rmx2180`) | <https://github.com/Frostleaft07/Nethunter_C15> | Unverified candidate | Per-device GitHub search result |
| Nothing Phone (1) (`spacewar`) | <https://github.com/Pri-S-Godase/Kali-NetHunter-Pro-Nothing-Phone-1-Spacewar> | Unverified candidate | Per-device GitHub search result |
| Nothing Phone (1) (`spacewar`) | <https://github.com/ExTV/android_kernel_msm-5.4_nothing_sm7325> | Unverified candidate | Per-device GitHub search result |
| Galaxy S9 / S9+ (`starlte`) | <https://github.com/JimmyF-web/https-github.com-V0lk3n-nethunter_kernel_samsung_exynos9810> | Unverified candidate | Per-device GitHub search result |
| Galaxy S9 / S9+ (`starlte`) | <https://github.com/Tkpointz/exynos9810_starlte_kernel> | Unverified candidate | Per-device GitHub search result |
| Xiaomi Pocophone X3 NFC (`surya`) | <https://github.com/dr1408/kernel_xiaomi_surya_nethunter> | Unverified candidate | Per-device GitHub search result |
| Xiaomi Pocophone X3 NFC (`surya`) | <https://github.com/zulfi0/surya_kernel_nethunter_docker> | Unverified candidate | Per-device GitHub search result |
| Xiaomi Pocophone X3 NFC (`surya`) | <https://github.com/entrysky/kernel_kali_nethunter_xiaomi_surya> | Unverified candidate | Per-device GitHub search result |
| Xiaomi Pocophone X3 Pro (`vayu`) | <https://github.com/sozibkhanshox-crypto/Vayu_nethunter_build> | Unverified candidate | Per-device GitHub search result |
| Xiaomi Pocophone X3 Pro (`vayu`) | <https://github.com/sozibkhanshox-crypto/vayu-nethunter-build> | Unverified candidate | Per-device GitHub search result |
| Xiaomi Pocophone X3 Pro (`vayu`) | <https://github.com/cyberknight777/nethunter_kernel_xiaomi_vayu> | Unverified candidate | Per-device GitHub search result |
| Xiaomi Redmi Note 5 Pro (`whyred`) | <https://github.com/Redfern89/android_kernel_xiaomi_sdm660-nethunter> | Unverified candidate | Per-device GitHub search result |
| Redmi Note 8 Pro (`begonia`) | <https://github.com/tarq04125-lang/begonia-nethunter-kernel1> | Unverified candidate | Expanded GitHub + release/README inspection |
| Redmi Note 8 Pro (`begonia`) | <https://github.com/tarq04125-lang/begonia-nethunter-kernel2> | Unverified candidate | Expanded GitHub + release/README inspection |
| POCO M2 Pro (`gram`) | <https://github.com/0x1k4rt1k/miatoll-nethunter-boot> | Unverified candidate | Expanded GitHub + release/README inspection |
| Redmi Note 9S (`curtana`) | <https://github.com/0x1k4rt1k/miatoll-nethunter-boot> | Unverified candidate | Expanded GitHub + release/README inspection |
| Redmi Note 9 Pro (`joyeuse`) | <https://github.com/0x1k4rt1k/miatoll-nethunter-boot> | Unverified candidate | Expanded GitHub + release/README inspection |
| Redmi Note 9 Pro Max (`excalibur`) | <https://github.com/0x1k4rt1k/miatoll-nethunter-boot> | Unverified candidate | Expanded GitHub + release/README inspection |
| Pixel 6 Pro (`raven`) | <https://github.com/ahksoft/Pixel6Pro-Nethunter> | Unverified candidate | Expanded GitHub + release/README inspection |
| Redmi 5 Plus (`vince`) | <https://github.com/kotkaaja/NetHunter-kernel-vince-R-by-p3h3n9-Remake> | Unverified candidate | Expanded GitHub + release/README inspection |
| Galaxy Tab S6 Lite (LTE) (`gta4xl`) | <https://github.com/mohammedddd5/nethunter-kernel-gta4xl> | Unverified candidate | Expanded GitHub + release/README inspection |
| Pocophone F1 (`beryllium`) | <https://github.com/DX4GREY/kernel_xiaomi_sdm845> | Unverified candidate | Expanded GitHub + release/README inspection |
| Mi MIX 3 (`perseus`) | <https://github.com/kamstartech/perseus-kernel-modules> | Unverified candidate | Expanded GitHub + release/README inspection |
| Moto G 5G Plus / Motorola One 5G (`nairo`) | <https://github.com/joenyr/nethunterkernel-nairo> | Unverified candidate | Expanded GitHub + release/README inspection |
| Redmi 5 (`rosy`) | <https://github.com/hellojonh9955/rosy-android14ksu-nethunter-kernel> | Unverified candidate | Expanded GitHub + release/README inspection |
| Galaxy A5 (2017) (`a5y17lte`) | <https://github.com/cycoslave/a5y17lte-kali-nethunter> | Unverified candidate | Expanded GitHub + release/README inspection |
| POCO F5 (Global) (`marble`) | <https://github.com/PARADOX-X20/kernel_xiaomi_sm8450> | Unverified candidate | Expanded GitHub + release/README inspection |
| Redmi 9 / 9 Prime (`lancelot`) | <https://github.com/deepcomon/kernel-nethunter-for-Redmi-9A> | Unverified candidate | Expanded GitHub + release/README inspection |
| Pixel 6a (`bluejay`) | <https://github.com/Ashabil/kernel-bluejay> | Unverified candidate | Expanded GitHub + release/README inspection |
| Pixel 9a (`tegu`) | <https://github.com/Flofy-Dev/Pixel_9a_nethunter_kernel> | Unverified candidate | Expanded GitHub + release/README inspection |
| Pixel 8 (`shiba`) | <https://github.com/Trijal08/dragon_device_google_shusky-kernels_5.15> | Unverified candidate | Expanded GitHub + release/README inspection |
| Pixel 8 Pro (`husky`) | <https://github.com/Trijal08/dragon_device_google_shusky-kernels_5.15> | Unverified candidate | Expanded GitHub + release/README inspection |
| Redmi Note 8T (`willow`) | <https://github.com/vaginessa/Cuh-Nethunter-Kernel-willow> | Unverified candidate | Expanded GitHub + release/README inspection |
| Redmi Note 9 Pro (`joyeuse`) | <https://github.com/dhiimr/nethunter_note9pro> | Unverified candidate | Expanded GitHub + release/README inspection |
| OnePlus Nord N10 5G (`billie`) | <https://github.com/jose-dev-tools/OnePlus-Nord-N10-Kali-NetHunter> | Unverified candidate | Expanded GitHub + release/README inspection |
| POCO F1 (`beryllium`) | <https://github.com/hmonojit/Poco-F1-Dual-Boot-Nethunter-Pro-Android-13> | Unverified candidate | Expanded GitHub + release/README inspection |
| Galaxy Note 10 Plus (Exynos) (`d2s`) | <https://github.com/Tkpointz/exynos9820-25_kernel> | Unverified candidate | Expanded GitHub + release/README inspection |
| Xperia 10 II (`pdx201`) | <https://github.com/howfan31/kali-nethunter-2026.2-pdx201-los-thirteen-full-repaired> | Unverified candidate | Expanded GitHub + release/README inspection |
| 6 / 6T (`oneplus6`) | <https://github.com/nuthan923/NetHunter-Enchilada-Oneplus6> | Unverified candidate | Expanded GitHub + release/README inspection |
| Moto G (2013) (`falcon`) | <https://github.com/theindicator/NETHUNTER-for-falcon> | Unverified candidate | Expanded GitHub + release/README inspection |
| 5 / 5T (`oneplus5`) | <https://github.com/simonpunk/nethunter-apk-and-magisk-module> | Unverified candidate | Expanded GitHub + release/README inspection |
| Mi Pad 4 (`clover`) | <https://github.com/DevKyurria/nethunter_kernel_xiaomi_clover> | Unverified candidate | Expanded GitHub + release/README inspection |
| Redmi 5 Plus (`vince`) | <https://github.com/p3h3n9-pr0j3ct/NetHunter-vince-R-FINAL> | Unverified candidate | Expanded GitHub + release/README inspection |
| Redmi 5 (`rosy`) | <https://github.com/p3h3n9-pr0j3ct/NetHunter-vince-R-FINAL> | Unverified candidate | Expanded GitHub + release/README inspection |
| Redmi Note 7 Pro (`violet`) | <https://github.com/ryzen-kernel/nethunter_kernel_xiaomi_violet> | Unverified candidate | Expanded GitHub + release/README inspection |
| Mi A1 (`tissot`) | <https://github.com/prorooter007/Nethunter_Kernel_Xiaomi_msm8953> | Unverified candidate | Expanded GitHub + release/README inspection |
| Galaxy J7 (`j7elte`) | <https://github.com/Anonymop1/j7xelte-nethunter-rom1> | Unverified candidate | Expanded GitHub + release/README inspection |
| Galaxy J7 (`j7elte`) | <https://github.com/Anonymop1/j7xelte-nethunter-rom> | Unverified candidate | Expanded GitHub + release/README inspection |
| Galaxy S20 Ultra (5G) (`z3s`) | <https://github.com/ben443/Nethunter_kernel_samsung_exynos990> | Unverified candidate | Expanded GitHub + release/README inspection |
| Galaxy S9 / S9+ (`starlte`) | <https://github.com/ouroboros420/android_kernel_samsung_exynos9810> | Unverified candidate | Expanded GitHub + release/README inspection |
| Galaxy Note 4 (Qualcomm) (`trltexx`) | <https://github.com/PhilZ-cwm6/nethunter_kernel_trlte> | Unverified candidate | Expanded GitHub + release/README inspection |
| Galaxy Note 4 (`treltexx`) | <https://github.com/PhilZ-cwm6/nethunter_kernel_trlte> | Unverified candidate | Expanded GitHub + release/README inspection |
| Pixel XL (`marlin`) | <https://github.com/Kernels-by-ravindu644/google_kernel_marlin_nethunter> | Unverified candidate | Expanded GitHub + release/README inspection |
| Mi A2 Lite (`daisy`) | <https://github.com/AzeAstro/miA2Lite_kernel> | Unverified candidate | Expanded GitHub + release/README inspection |
| Galaxy S5 Plus (`kccat6`) | <https://github.com/jcadduono/nethunter_kernel_kccat6> | Unverified candidate | Expanded GitHub + release/README inspection |
| G4 (International) (`h815`) | <https://github.com/nepheloid/nethunter_kernel_g4> | Unverified candidate | Expanded GitHub + release/README inspection |
| Redmi 9 / 9 Prime (`lancelot`) | <https://github.com/Neternels/NetHunter-MT6768> | Unverified candidate | Expanded GitHub + release/README inspection |
| Redmi Note 9 (`merlinx`) | <https://github.com/Neternels/NetHunter-MT6768> | Unverified candidate | Expanded GitHub + release/README inspection |
| Redmi Note 8 Pro (`begonia`) | <https://github.com/Anonym3310/AkameKernel-begonia> | Unverified candidate | Expanded GitHub + release/README inspection |
| Redmi Note 9 Pro (`joyeuse`) | <https://github.com/Anonym3310/AkameKernel-joyeuse> | Unverified candidate | Expanded GitHub + release/README inspection |
| Redmi 8 (`olive`) | <https://github.com/leoshanumber69/AkameKernel-NetHunter> | Unverified candidate | Expanded GitHub + release/README inspection |
| Redmi Note 6 Pro (`tulip`) | <https://github.com/satana666luciferka/KERNEL-NETHUNTER-REDMI-NOTE-6-PRO> | Unverified candidate | Expanded GitHub + release/README inspection |
| Pixel 5 (`redfin`) | <https://github.com/Fak3adm1n/Build-Nethunter-kernel-for-redfin> | Unverified candidate | Expanded GitHub + release/README inspection |
| Redmi Note 7 (`lavender`) | <https://github.com/Postcard7952/Lavender-Nethunter> | Unverified candidate | Expanded GitHub + release/README inspection |
| Galaxy A72 (`a72q`) | <https://github.com/vakula2004/kernel_a72q> | Unverified candidate | Expanded GitHub + release/README inspection |
| Redmi Note 7 (`lavender`) | <https://github.com/sauravsinha239/nethunter-lavender> | Unverified candidate | Expanded GitHub + release/README inspection |
| Pixel 4 (`flame`) | <https://github.com/cyberknight777/nethunter_kernel_google_floral> | Unverified candidate | Expanded GitHub + release/README inspection |

## 5. Abandoned / unmaintained projects

`Abandoned` means no recent maintenance was found. It does not prove the kernel is broken. All repositories below still had a source URL at research time, so they are potentially recoverable by clone/fork.

| Device | Project | Last update | Maintenance | Recoverability |
|---|---|---|---|---|
| Redmi K20 Pro (`raphael`) | <https://github.com/DOITfit/Redmi-K20Pro-Nethunter-Project> | 2026-10-05 | Archived | Source present; clone/fork possible |
| Xiaomi Redmi Note 4 / 4X (`mido`) | <https://github.com/chkndrp/device_xiaomi_mido-nethunter-kernel> | 2026-03-02 | Archived | Source present; clone/fork possible |
| ASUS ZenFone Max Pro M1 (`sdm660`) | <https://github.com/tutaf/kernel_asus_sdm660> | 2023-09-11 | Archived | Source present; clone/fork possible |
| Samsung Galaxy A21s (`a21s`) | <https://github.com/BasGame1/nethunter_kernel_a21s> | 2026-02-15 | Archived | Source present; clone/fork possible |
| Samsung Galaxy A01 (`a01`) | <https://github.com/ravindu644/kernel_samsung_a01> | 2025-12-31 | Archived | Source present; clone/fork possible |
| OnePlus 6 (`enchilada`) | <https://github.com/cdizzle97/enchilada-nethunter> | 2018-12-16 | Unmaintained | Source present; clone/fork possible |
| Samsung Galaxy A8 (a8elte) (`a8elte`) | <https://github.com/DeadSquirrel01/nethunter-kernel-a8elte> | 2019-02-24 | Unmaintained | Source present; clone/fork possible |
| Xiaomi Mi 10T Lite / Redmi Note 9 Pro 5G (`gauguin`) | <https://github.com/Dqdd/gauguin_nethunter_kernel> | 2022-09-01 | Unmaintained | Source present; clone/fork possible |
| Samsung Galaxy A10 (`a10`) | <https://github.com/fast50/NethunterKernel-Galaxy-A105xxx> | 2022-03-27 | Unmaintained | Source present; clone/fork possible |
| Google Nexus 7 (2013) (`flo`) | <https://github.com/jcadduono/nethunter_kernel_flo> | 2019-02-24 | Unmaintained | Source present; clone/fork possible |
| Xiaomi Mi Max 3 (`nitrogen`) | <https://github.com/Jemacivan/nitrogen-kernel> | 2023-11-11 | Unmaintained | Source present; clone/fork possible |
| OnePlus X (`oneplusx`) | <https://github.com/lvlrt/nethunter_kernel_oneplusx_cm> | 2016-09-20 | Unmaintained | Source present; clone/fork possible |
| Motorola Moto G6 (`evert`) | <https://github.com/mapachesantander/Unofficial-Nethunter-Kernel-Evert> | 2022-09-21 | Unmaintained | Source present; clone/fork possible |
| Unknown (`Unknown`) | <https://github.com/MechRocker/kernel-nethunter> | 2021-05-19 | Unmaintained | Source present; clone/fork possible |
| OnePlus 5 / 5T (`cheeseburger/dumpling`) | <https://github.com/prodject/OP5_Nethunter_kernel> | 2018-04-28 | Unmaintained | Source present; clone/fork possible |
| Samsung Galaxy M52 5G (`m52xq`) | <https://github.com/RebertiCS/M52-NetHunter-Kernel> | 2024-08-24 | Archived | Source present; clone/fork possible |
| Samsung Galaxy S7 (flat) (`herolte`) | <https://github.com/syzh120/nethunter-kernel> | 2021-05-12 | Unmaintained | Source present; clone/fork possible |
| Unknown (`Unknown`) | <https://github.com/zahirrayhan/Nethunter-Kernel> | 2021-04-24 | Unmaintained | Source present; clone/fork possible |
| Nokia 3.1 (`es2`) | <https://github.com/yesimxev/android_kernel_nokia_es2_sprout> | 2020-03-13 | Unmaintained | Source present; clone/fork possible |
| Google Nexus 7 (2013) (`flo`) | <https://github.com/0E800/kernel_flo_pie_nh> | 2021-08-31 | Unmaintained | Source present; clone/fork possible |
| OnePlus One (`oneplus1`) | <https://github.com/WhiteishRat/oneplus1_kernel_nethunter> | 2019-08-01 | Unmaintained | Source present; clone/fork possible |
| Google Nexus 6 (`shamu`) | <https://github.com/JLynx69/Shamu-kali> | 2021-05-24 | Unmaintained | Source present; clone/fork possible |
| Xiaomi Pocophone X3 Pro (`vayu`) | <https://github.com/lair-nula/NetHunter-PocoX3-Pro-Vayu> | 2022-05-24 | Unmaintained | Source present; clone/fork possible |
| Redmi Note 9 Pro (`joyeuse`) | <https://github.com/dhiimr/NHunter_Joyeuse> | 2023-05-25 | Unmaintained | Source present; clone/fork possible |
| Oneplus 2 (`oneplus2`) | <https://github.com/xNNism/aosp_nethunter-kernel_oneplus_msm8994> | 2019-02-24 | Unmaintained | Source present; clone/fork possible |
| HTC One M8 (`htc-m8`) | <https://github.com/darobbe/AnyKernel2-nethunter-Htc-m8> | 2017-12-12 | Unmaintained | Source present; clone/fork possible |
| Galaxy J6 (`j6lte`) | <https://github.com/L4FeeR/j6lte-nethunter-kernel> | 2022-06-19 | Unmaintained | Source present; clone/fork possible |
| Redmi 4A (`rolex`) | <https://github.com/Thiviyan/-Xiaomi-Redmi-4A-Nethunter> | 2020-08-27 | Unmaintained | Source present; clone/fork possible |
| Galaxy Note 9 (`crownlte`) | <https://github.com/Tkpointz/exynos9810_crownlte_kernel> | 2023-09-18 | Unmaintained | Source present; clone/fork possible |
| Nubia Z17 (`nx563j`) | <https://github.com/HiterretiH/nx589j_nougat_kernel_nethunter> | 2019-10-15 | Unmaintained | Source present; clone/fork possible |
| Redmi 5 Plus (`vince`) | <https://github.com/kitkat-rek777013/kernel-nethunter-vince-krypton-based> | 2019-06-28 | Unmaintained | Source present; clone/fork possible |
| Xperia SP (`huashan`) | <https://github.com/haleem254/nethuntersp> | 2016-11-17 | Unmaintained | Source present; clone/fork possible |
| Redmi Note 6 Pro (`tulip`) | <https://github.com/satana666luciferka/redmi-note-6-pro-kernel-nethunter-HELLP> | 2019-01-27 | Unmaintained | Source present; clone/fork possible |
| Nexus 7 (2012) (`grouper`) | <https://github.com/re4son/android_kernel_asus_grouper_3.0> | 2023-06-09 | Abandoned | Source present; clone/fork possible |
| Realme 6 / 6i / 7 (RM6785) (`rm6785`) | <https://github.com/kirito6785/kali-nethunter-kernel-for-only-rm6785-> | 2023-04-20 | Abandoned | Source present; clone/fork possible |
| Galaxy J8 (2018) (`j8y18lte`) | <https://github.com/abhishektor55/android_nethunter_kernel_samsung_j8y18lte> | 2023-01-03 | Abandoned | Source present; clone/fork possible |
| Moto Z (`griffin`) | <https://github.com/abdullahgok/tubichu-z-kernel> | 2018-08-23 | Abandoned | Source present; clone/fork possible |
| Redmi 5 Plus (`vince`) | <https://github.com/rek777013/kali_nethunter_kernel_vince> | 2018-07-24 | Abandoned | Source present; clone/fork possible |
| Galaxy A13 4G (`a137f`) | <https://github.com/ravindu644/android_kernel_nethunter_sm-a137f> | 2025-12-31 | Active | Source present; clone/fork possible |
| LeEco Le 2 (`s2`) | <https://github.com/evost/android_kernel_leeco_msm8996_lineage_kali_nethunter> | 2020-03-27 | Abandoned | Source present; clone/fork possible |
| LeEco Le Pro3 (`zl1`) | <https://github.com/evost/android_kernel_leeco_msm8996_lineage_kali_nethunter> | 2020-03-27 | Abandoned | Source present; clone/fork possible |
| Galaxy Tab S3 LTE (`gts3llte`) | <https://github.com/pinnace/sm-t825> | 2018-02-08 | Abandoned | Source present; clone/fork possible |

## 6. Broken or incompatible

**None (0) with credible, specific evidence.** This is not a claim that every project works; it means no inspected source documented a reproducible failure on an exact variant. Absence of evidence is not evidence of compatibility.

## 7. Potentially recoverable

All abandoned projects with a reachable repository are listed above. A fork should be rebuilt against the matching kernel branch and validated on the exact model/region before being called compatible.
