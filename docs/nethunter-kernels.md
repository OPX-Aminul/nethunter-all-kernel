# Kali NetHunter Supported Kernels and Devices

Source: `devices.yml` in the official Kali NetHunter kernels repository:
https://gitlab.com/kalilinux/nethunter/build-scripts/kali-nethunter-kernels/-/blob/main/devices.yml

- Devices: 126
- Kernel entries: 191

| # | Device codename | Model | Kernel ID | Android | Linux | Description | Author | Kernel source |
|---|---|---|---|---|---|---|---|---|
| 1 | `a37` | OPPO A37 (2016) | `a37-los` | ten | 3.10 | LineageOS 17.1 | diamant3 | `git clone https://github.com/diamant3/kernel_oppo_A37f.git -b lineage-17.1` |
| 2 | `a5ulte` | Samsung Galaxy A5 (2015) | `a5ulte-cm` | marshmallow | 3.10 | CyanogenMod 13 | DeadSquirrel01 | `git clone https://github.com/DeadSquirrel01/nethunter-kernel-a5ulte.git -b cm-13.0` |
| 3 | `a5ulte` | Samsung Galaxy A5 (2015) | `a5ulte-tw` | marshmallow | 3.10 | TouchWiz 6.0 | DeadSquirrel01 | `git clone https://github.com/DeadSquirrel01/nethunter-kernel-a5ulte.git -b touchwiz-6.0` |
| 4 | `a5xelte` | Samsung Galaxy A5 (2016) | `a5xelte-tw` | nougat | 3.10 | TouchWiz Grace | Re4son | `git clone https://github.com/Re4son/android_kernel_samsung-a5xelte -b nethunter-7.0` |
| 5 | `a7xelte` | Samsung Galaxy A7 (2016) | `a7xelte-los` | eleven | 3.10 | LineageOS 18.1 | yesimxev | `git clone https://github.com/yesimxev/android_kernel_samsung_universal7580 -b lineage-18.1` |
| 6 | `ailsa-ii` | ZTE Axon 7 | `ailsa-ii` | marshmallow | 3.18 | Android 6 | jcadduono | `git clone https://github.com/jcadduono/android_kernel_zte_msm8996.git -B nethunter-6.0` |
| 7 | `alioth` | Xiaomi Pocophone F3 | `alioth-los-ksu` | fourteen | 4.19 | Android 14 | Hani K. | `git clone https://github.com/Hani-K/Bifr0st.git -b 14.0-alioth` |
| 8 | `angler` | Google/Huawei Nexus 6P | `angler` | marshmallow | 3.10 | Android 6 | Binkybear | `git clone https://github.com/binkybear/AK-Angler.git` |
| 9 | `angler` | Google/Huawei Nexus 6P | `angler` | nougat | 3.10 | Android 7.1 | jcadduono | `git clone https://github.com/jcadduono/android_kernel_huawei_angler -b nethunter-7.1_2` |
| 10 | `angler` | Google/Huawei Nexus 6P | `angler` | oreo | 3.10 | Android 8.1 | Re4son & yesimxev | `git clone https://github.com/Re4son/android_kernel_huawei_angler -b nethunter-8.1` |
| 11 | `angler` | Google/Huawei Nexus 6P | `angler-los` | ten | 3.10 | LineageOS 17.1 & Pixel Experience 10 | Re4son & yesimxev | `git clone https://github.com/Re4son/android_kernel_huawei_angler_pixel -b nethunter-10.0` |
| 12 | `spes_matrixx` | Redmi Note 11 spes | `spes_matrixx` | fifteen | 4.19.325 | AOSPA | Madara273 | `git clone https://github.com/Madara273/Redmi-Note-11-Kernel -b main` |
| 13 | `ginkgo` | Redmi Note 8 | `ginkgoa13` | thirteen | 4.14 | ArrowOS 13 | ikteach | `git clone https://github.com/ikteach/ginkgo_kernel.git -b main` |
| 14 | `ginkgo` | Redmi Note 8 | `ginkgoa16` | sixteen | 4.14 | LineageOS 23.2 | ikteach | `git clone https://github.com/ikteach/ginkgo_nethunter_kernel.git -b main` |
| 15 | `armani` | Redmi 1S | `armani` | kitkat | 3.04 | Redmi 1S for stock Android | firstblooder | `` |
| 16 | `armor34plus` | Ulefone Armor 34+ | `armor34plus-stock` | sixteen | 6.1 | Stock Android 16 (MT6878 / Dimensity 7300) | art0181 | `git clone https://gitlab.com/art0181/android_kernel_ulefone_armor34plus_gki.git -b nethunter-6.1` |
| 17 | `beryllium` | Xiaomi Pocophone F1 | `beryllium` | eleven | 4.9 | Xiaomi Pocophone F1 for stock Android | Hilledkinged & yesimxev | `` |
| 18 | `beryllium` | Xiaomi Pocophone F1 | `beryllium-los` | fourteen | 4.9 | LineageOS 21 | Strix Vyxlor | `git clone https://github.com/Strix-Vyxlor/android_kernel_xiaomi_sdm845` |
| 19 | `beyond0lte` | Samsung Galaxy S10e | `beyond0lte-los` | sixteen | 4.14 | LineageOS 23.2 | yesimxev and v0lk3n | `git clone --recurse-submodules https://github.com/v0lk3n/nethunter_kernel_samsung_exynos9820.git -b nethunter-lineage-23.2` |
| 20 | `beyond1lte` | Samsung Galaxy S10 | `beyond1lte-los` | fourteen | 4.14 | LineageOS 21 | v0lk3n | `git clone --recurse-submodules https://github.com/v0lk3n/nethunter_kernel_samsung_exynos9820.git -b nethunter-lineage-21` |
| 21 | `beyond1lte` | Samsung Galaxy S10 | `beyond1lte-los` | fifteen | 4.14 | LineageOS 22.2 | v0lk3n | `git clone --recurse-submodules https://github.com/v0lk3n/nethunter_kernel_samsung_exynos9820.git -b nethunter-lineage-22.2` |
| 22 | `beyond1lte` | Samsung Galaxy S10 | `beyond1lte-los` | sixteen | 4.14 | LineageOS 23.2 | v0lk3n | `git clone --recurse-submodules https://github.com/v0lk3n/nethunter_kernel_samsung_exynos9820.git -b nethunter-lineage-23.2` |
| 23 | `beyond2lte` | Samsung Galaxy S10+ | `beyond2lte-los` | sixteen | 4.14 | LineageOS 23.2 | yesimxev and v0lk3n | `git clone --recurse-submodules https://github.com/v0lk3n/nethunter_kernel_samsung_exynos9820.git -b nethunter-lineage-23.2` |
| 24 | `beyondx` | Samsung Galaxy S10 5G | `beyondx-los` | sixteen | 4.14 | LineageOS 23.2 | yesimxev and v0lk3n | `git clone --recurse-submodules https://github.com/v0lk3n/nethunter_kernel_samsung_exynos9820.git -b nethunter-lineage-23.2` |
| 25 | `blueline` | Google Pixel 3 | `blueline` | twelve | 4.9 | Android 12 | Alynx | `git clone https://github.com/v3rb0se/alynx-nethunter/` |
| 26 | `blueline` | Google Pixel 3 | `blueline` | thirteen | 4.9 | Android 13 | Alynx | `git clone https://github.com/v3rb0se/alynx-nethunter/` |
| 27 | `bramble` | Google Pixel 4a 5G | `bramble` | twelve | 4.9 | Android 12L | Alynx | `git clone https://github.com/V3rB0se/redbull` |
| 28 | `bluejay-los` | Google Pixel 6a | `bluejay-los` | sixteen | 6.1 | LineageOS 23.2 (Android 16) | RishiRats | `git clone https://github.com/RishiRats/bluejay-kali_nethunter` |
| 29 | `bullhead` | Google Nexus 5X | `bullhead` | marshmallow | 3.04 | Android 6 | Binkybear | `git clone https://github.com/binkybear/kernel_msm.git -b android-msm-bullhead-3.10-marshmallow` |
| 30 | `bullhead` | Google Nexus 5X | `bullhead` | nougat | 3.04 | Android 7.1 | Binkybear | `git clone https://github.com/binkybear/kernel_msm.git` |
| 31 | `bullhead` | Google Nexus 5X | `bullhead` | oreo | 3.04 | Android 8.1 | Re4son | `git clone https://github.com/Re4son/android_kernel_lge_bullhead -b nethunter-8.1` |
| 32 | `c2s` | Samsung Galaxy Note20 Ultra (Exynos) | `c2s-oui-ksu` | thirteen | 4.19 | One UI 5.1 | Luka Gejak | `git clone https://github.com/MocLG/android_kernel_samsung_exynos990_nethunter -b nethunter-c2s-oui-ksu-v4.4` |
| 33 | `cancro` | Xiaomi Mi 3 / Mi 4 | `cancro-cm` | marshmallow | 3.04 | CyanogenMod 13 | Binkybear | `git clone https://github.com/binkybear/android_kernel_xiaomi_cancro.git -b cm-13.0` |
| 34 | `cedric` | Motorola Moto G5 | `cedric-los` | nougat | 3.18 | LineageOS 14.1 | rajeshdubey293 | `git clone https://github.com/rajeshdubey293/android_kernel_motorola_msm8937 -b cm-14.1` |
| 35 | `cedric` | Motorola Moto G5 | `cedric-los` | oreo | 3.18 | LineageOS 15.1 | rajeshdubey293 | `git clone https://github.com/rajeshdubey293/al-ice_cedric.git -b working` |
| 36 | `cepheus` | Xiaomi Mi 9 cepheus (PixelOS 15) | `cepheus-pos` | fifteen | 4.14.353-openela | PixelOS 15 | k0d14k | `git clone https://github.com/k0d14k/kernel_xiaomi_cepheus -b fifteen` |
| 37 | `crosshatch` | Google Pixel 3 XL | `crosshatch` | twelve | 4.9 | Android 12 | Alynx | `git clone https://github.com/v3rb0se/alynx-nethunter/` |
| 38 | `crosshatch` | Google Pixel 3 XL | `crosshatch` | thirteen | 4.9 | Android 13 | Alynx | `git clone https://github.com/v3rb0se/alynx-nethunter/` |
| 39 | `davinci` | Xiaomi Mi 9T | `davinci-miui` | ten | 4.14 | MIUI Global 11 | Re4son | `git clone https://github.com/Re4son/android_kernel_xiaomi_davinci_hasty -b nethunter-10.0` |
| 40 | `dogo` | Sony Xperia ZR | `dogo-cm` | marshmallow | 3.04 | CyanogenMod 13 | Daedroza | `git clone https://github.com/daedroza/nethunter_kernel_apq8064.git -b master` |
| 41 | `dragon` | Google Pixel C | `dragon` | nougat | 3.18 | Android 7.1 | jcadduono | `git clone https://github.com/jcadduono/android_kernel_google_chromeos.git -b nethunter-7.1` |
| 42 | `drg` | Nokia 6.1 Plus | `drg-los` | eleven | 4.4 | LineageOS 18.1 | yesimxev | `git clone https://github.com/yesimxev/android_kernel_nokia_sdm660 -b lineage-18.1` |
| 43 | `drg` | Nokia 6.1 Plus | `drg-los` | thirteen | 4.4 | LineageOS 20 | yesimxev | `git clone https://github.com/yesimxev/android_kernel_nokia_sdm660 -b lineage-20` |
| 44 | `drg` | Nokia 6.1 Plus | `drg-los` | fourteen | 4.4 | LineageOS 21 | yesimxev | `` |
| 45 | `es2` | Nokia 3.1 | `es2` | pie | 3.18 | Android 9.0 | yesimxev | `git clone https://github.com/yesimxev/android_kernel_nokia_es2.git -b Pie-v3.180` |
| 46 | `eva` | Huawei P9 | `eva-emui` | oreo | 4.04 | EMUI | vvvbbbcz | `git clone https://gitlab.com/vvvbbbcz/android_kernel_huawei_hi3650.git -b upstream` |
| 47 | `eva` | Huawei P9 | `eva-los` | pie | 4.04 | LineageOS 16.0 | vvvbbbcz | `git clone https://gitlab.com/vvvbbbcz/android_kernel_huawei_hi3650.git -b upstream` |
| 48 | `eva` | Huawei P9 | `eva-ultra` | oreo | 4.04 | EMUI8/LineageOS16 | apk0mix5900 | `git clone https://github.com/apk0mix5900/android_kernel_huawei_hi3650` |
| 49 | `flo` | Google Nexus 7 (2013) | `flo` | kitkat | 3.04 | Android 4.4 | Binkybear | `git clone https://github.com/binkybear/kernel_msm.git -b android-msm-flo-3.4-kitkat-mr2` |
| 50 | `flo` | Google Nexus 7 (2013) | `flo` | lollipop | 3.04 | Android 5 | Binkybear | `git clone https://github.com/binkybear/flo.git -b ElementalX-4.00` |
| 51 | `flo` | Google Nexus 7 (2013) | `flo` | marshmallow | 3.04 | Android 6 | Binkybear | `git clone https://github.com/binkybear/flo.git -b ElementalX-5.00` |
| 52 | `flo` | Google Nexus 7 (2013) | `flo-cm` | marshmallow | 3.04 | CyanogenMod | jcadduono | `git clone https://github.com/jcadduono/nethunter_kernel_flo.git -b cm-13.0` |
| 53 | `flounder` | Google Nexus 9 | `flounder` | lollipop | 3.10 | Android 5 | Binkybear | `git clone https://github.com/binkybear/flounder.git -b android-tegra-flounder-3.10-lollipop-release` |
| 54 | `flounder` | Google Nexus 9 | `flounder` | marshmallow | 3.10 | Android 6 | Binkybear | `git clone https://github.com/binkybear/flounder.git -b android-tegra-flounder-3.10-marshmallow-release` |
| 55 | `flounder` | Google Nexus 9 | `flounder` | nougat | 3.10 | Android 7.1 | SecurityAddicted | `git clone https://github.com/SecurityAddicted/ElementalX-N9-Nethunter.git` |
| 56 | `gemini4g` | Planet Computers Gemini PDA | `gemini4g-p1` | nougat | 3.18 | Android 7.1 Boot Partition 1 | Re4son | `git clone https://github.com/Re4son/gemini-kali-linux-kernel-3.18 -b nethunter` |
| 57 | `gemini4g` | Planet Computers Gemini PDA | `gemini4g-p1` | oreo | 3.18 | Android 8.1 Boot Partition 1 | Re4son | `git clone https://github.com/Re4son/gemini-kali-linux-kernel-3.18 -b nethunter-8.1` |
| 58 | `gemini4g` | Planet Computers Gemini PDA | `gemini4g-p2` | nougat | 3.18 | Android 7.1 Boot Partition 2 | Re4son | `git clone https://github.com/Re4son/gemini-kali-linux-kernel-3.18 -b nethunter` |
| 59 | `gemini4g` | Planet Computers Gemini PDA | `gemini4g-p2` | oreo | 3.18 | Android 8.1 Boot Partition 2 | Re4son | `git clone https://github.com/Re4son/gemini-kali-linux-kernel-3.18 -b nethunter-8.1` |
| 60 | `gemini4g` | Planet Computers Gemini PDA | `gemini4g-p3` | nougat | 3.18 | Android 7.1 Boot Partition 3 | Re4son | `git clone https://github.com/Re4son/gemini-kali-linux-kernel-3.18 -b nethunter` |
| 61 | `gemini4g` | Planet Computers Gemini PDA | `gemini4g-p3` | oreo | 3.18 | Android 8.1 Boot Partition 3 | Re4son | `git clone https://github.com/Re4son/gemini-kali-linux-kernel-3.18 -b nethunter-8.1` |
| 62 | `gracelte` | Samsung Galaxy Note 7 | `gracelte` | marshmallow | 3.18 | Grace UI | jcadduono | `git clone https://github.com/jcadduono/android_kernel_samsung_universal8890.git -b nethunter-6.0` |
| 63 | `gracelte` | Samsung Galaxy Note 7 | `graceltekor` | marshmallow | 3.18 | Grace UI | jcadduono | `git clone https://github.com/jcadduono/android_kernel_samsung_universal8890/commits -b nethunter-6.0` |
| 64 | `grouper` | Google Nexus 7 (2012) | `grouper` | kitkat | 3.01 | Android 4.4 | Binkybear | `git clone https://github.com/binkybear/android_kernel_asus_grouper.git -b android-tegra3-grouper-3.1-lollipop-release_tegra-l4t-r16-16.5 nexus7_2012-5` |
| 65 | `gts4llte` | Samsung Galaxy Tab S4 LTE | `gts4llte` | oreo | 4.04 | Android 8.1 | Re4son | `git clone https://github.com/Re4son/gts4lwifi -b 8.1-nethunter` |
| 66 | `gts4lwifi` | Samsung Galaxy Tab S4 WiFi | `gts4lwifi` | oreo | 4.04 | Android 8.1 | Re4son | `git clone https://github.com/Re4son/gts4lwifi -b 8.1-nethunter` |
| 67 | `h830` | LG G5 (T-Mobile) | `h830` | nougat | 3.18 | Android 7.1 (T-Online) | jcadduono | `git clone https://github.com/jcadduono/android_kernel_lge_msm8996.git -b nethunter-7.0` |
| 68 | `h850` | LG G5 (International) | `h850` | nougat | 3.18 | Android 7.1 (T-Online) | jcadduono | `git clone https://github.com/jcadduono/android_kernel_lge_msm8996.git -b nethunter-7.0` |
| 69 | `h918` | LG V20 (T-Mobile) | `h918` | nougat | 3.18 | Android 7.0 | jcadduono | `git clone https://github.com/jcadduono/android_kernel_lge_msm8996.git -b nethunter-7.0` |
| 70 | `h990` | LG V20 (International) | `h990` | nougat | 3.18 | Android 7.1 with dirtysanta patch | Re4son | `git clone https://github.com/Re4son/android_kernel_lge_msm8996 -b nethunter-7.0` |
| 71 | `h990` | LG V20 (International) | `h990` | oreo | 3.18 | Android 8 | Re4son | `git clone https://github.com/Re4son/android_kernel_lg_h990 -b nethunter-8.0` |
| 72 | `h990` | LG V20 (International) | `h990-los` | eleven | 3.18 | LineageOS 18.1 | yesimxev | `git clone https://github.com/yesimxev/android_kernel_lge_msm8996 -b nethunter-gamma-pie` |
| 73 | `h990` | LG V20 (International) | `h990-los` | twelve | 4.04 | LineageOS 19.1 | yesimxev | `git clone https://github.com/yesimxev/android_kernel_lge_msm8996 -b lineage-19.1` |
| 74 | `h990` | LG V20 (International) | `h990-los` | fourteen | 4.04 | LineageOS 21 | yesimxev | `git clone https://github.com/yesimxev/android_kernel_lge_msm8996 -b lineage-21` |
| 75 | `hammerhead` | Google Nexus 5 | `hammerhead` | kitkat | 3.04 | Android 4.4 | Binkybear | `git clone https://github.com/binkybear/furnace_kernel_lge_hammerhead.git -b android-4.4` |
| 76 | `hammerhead` | Google Nexus 5 | `hammerhead` | lollipop | 3.04 | Android 5 | Binkybear | `git clone https://github.com/binkybear/kernel_msm.git -b android-msm-hammerhead-3.4-lollipop-release` |
| 77 | `hammerhead` | Google Nexus 5 | `hammerhead` | marshmallow | 3.04 | Android 6 | Re4son | `git clone https://github.com/Re4son/android_kernel_lge_hammerhead -b nethunter-7.1` |
| 78 | `hammerhead` | Google Nexus 5 | `hammerhead-los` | nougat | 3.04 | LineageOS 14.1 | Re4son | `git clone https://github.com/Re4son/android_kernel_lge_hammerhead -b nethunter-7.1` |
| 79 | `hammerhead` | Google Nexus 5 | `hammerhead-caf-los` | nougat | 3.04 | CAF LineageOS 14.1 | chrisk44 | `git clone https://github.com/chrisk44/android_kernel_lge_hammerhead.git -b cm-14.1-caf` |
| 80 | `hero2lte` | Samsung Galaxy S7 Edge | `hero2lte-tw` | marshmallow | 3.18 | TouchWiz 6.0 | jcadduono | `git clone https://github.com/jcadduono/android_kernel_samsung_universal8890 -b nethunter-6.0` |
| 81 | `hero2lte` | Samsung Galaxy S7 Edge | `hero2lte-tw` | oreo | 3.18 | TouchWiz Grace | Svirusx | `git clone https://github.com/Svirusx/NetHunter-s7-kernel-StockOreo.git -b nethunter-8.0` |
| 82 | `hero2lte` | Samsung Galaxy S7 Edge | `hero2lte-los` | nougat | 3.18 | LineageOS 14.1 | Svirusx | `git clone https://github.com/Svirusx/NetHunter-s7-kernel-LineageOS14.1.git -b cm-14.1` |
| 83 | `hero2lte` | Samsung Galaxy S7 Edge | `hero2lte-los` | pie | 3.18 | LineageOS 16.0 | Svirusx | `git clone https://github.com/Svirusx/Nethunter-s7-kernel-LineageOS16.0.git -b lineage-16.0` |
| 84 | `hero2lte` | Samsung Galaxy S7 Edge | `hero2lte-oui` | pie | 3.18 | One UI 1.0 | Svirusx | `git clone https://github.com/Svirusx/Nethunter-s7-kernel-WirusMOD-AiO.git -b aio-mkv8` |
| 85 | `hero2lte` | Samsung Galaxy S7 Edge | `hero2lte-kor-tw` | marshmallow | 3.18 | TouchWiz 6.0 | jcadduono | `git clone https://github.com/jcadduono/android_kernel_samsung_universal8890 -b nethunter-6.0` |
| 86 | `herolte` | Samsung Galaxy S7 | `herolte-tw` | marshmallow | 3.18 | TouchWiz 6.0 | jcadduono | `git clone https://github.com/jcadduono/android_kernel_samsung_universal8890 -b nethunter-6.0` |
| 87 | `herolte` | Samsung Galaxy S7 | `herolte-tw` | oreo | 3.18 | TouchWiz Grace | Svirusx | `git clone https://github.com/Svirusx/NetHunter-s7-kernel-StockOreo.git -b nethunter-8.0` |
| 88 | `herolte` | Samsung Galaxy S7 | `herolte-los` | nougat | 3.18 | LineageOS 14.1 | Svirusx | `git clone https://github.com/Svirusx/NetHunter-s7-kernel-LineageOS14.1.git -b cm-14.1` |
| 89 | `herolte` | Samsung Galaxy S7 | `herolte-los` | pie | 3.18 | LineageOS 16.0 | Svirusx | `git clone https://github.com/Svirusx/Nethunter-s7-kernel-LineageOS16.0.git -b lineage-16.0` |
| 90 | `herolte` | Samsung Galaxy S7 | `herolte-oui` | pie | 3.18 | One UI 1.0 | Svirusx | `git clone https://github.com/Svirusx/Nethunter-s7-kernel-WirusMOD-AiO.git -b aio-mkv8` |
| 91 | `herolte` | Samsung Galaxy S7 | `herolte-kor-tw` | marshmallow | 3.18 | TouchWiz 6.0 | jcadduono | `git clone https://github.com/jcadduono/android_kernel_samsung_universal8890 -b nethunter-6.0` |
| 92 | `hlte` | Samsung Galaxy Note 3 | `hlte-can-cm` | lollipop | 3.04 | CyanogenMod 12 (Canada, Mexico, and T-Mobile) | jcadduono | `git clone https://github.com/jcadduono/idleKernel-note3.git -b ik-nethunter-L` |
| 93 | `hlte` | Samsung Galaxy Note 3 | `hlte-can-cm` | marshmallow | 3.04 | CyanogenMod 13 (Canada, Mexico, and T-Mobile) | jcadduono | `git clone https://github.com/jcadduono/idleKernel-note3.git -b ik-nethunter-M` |
| 94 | `hlte` | Samsung Galaxy Note 3 | `hlte-can-tw` | lollipop | 3.04 | TouchWiz 5.0 (Canada, Mexico, and T-Mobile) | jcadduono | `git clone https://github.com/jcadduono/idleKernel-note3.git -b ik-nethunter-touchwiz` |
| 95 | `hlte` | Samsung Galaxy Note 3 | `hlte-dcm-tw` | lollipop | 3.04 | TouchWiz 5.0 (Japanese NTT Docomo) | jcadduono | `git clone https://github.com/jcadduono/idleKernel-note3.git -b ik-nethunter-touchwiz` |
| 96 | `hlte` | Samsung Galaxy Note 3 | `hlte-eur-cm` | lollipop | 3.04 | CyanogenMod 12 (International / European) | jcadduono | `git clone https://github.com/jcadduono/idleKernel-note3.git -b ik-nethunter-L` |
| 97 | `hlte` | Samsung Galaxy Note 3 | `hlte-eur-cm` | marshmallow | 3.04 | CyanogenMod 13 (International / European) | jcadduono | `git clone https://github.com/jcadduono/idleKernel-note3.git -b ik-nethunter-M` |
| 98 | `hlte` | Samsung Galaxy Note 3 | `hlte-eur-tw` | lollipop | 3.04 | TouchWiz 5.0 (International / European) | jcadduono | `git clone https://github.com/jcadduono/idleKernel-note3.git -b ik-nethunter-touchwiz` |
| 99 | `hlte` | Samsung Galaxy Note 3 | `hlte-eur-los` | nougat | 3.04 | LineageOS 14.1 (International / European) | 4E656F | `git clone https://github.com/0x4E0x650x6F/android_kernel_samsung_msm8974.git -b cm-14.1` |
| 100 | `hlte` | Samsung Galaxy Note 3 | `hlte-kdi-tw` | lollipop | 3.04 | TouchWiz 5.0 (Japanese NTT Docomo) | jcadduono | `git clone https://github.com/jcadduono/idleKernel-note3.git -b ik-nethunter-touchwiz` |
| 101 | `hlte` | Samsung Galaxy Note 3 | `hlte-kor-cm` | lollipop | 3.04 | CyanogenMod 12 (Korean) | jcadduono | `git clone https://github.com/jcadduono/idleKernel-note3.git -b ik-nethunter-L` |
| 102 | `hlte` | Samsung Galaxy Note 3 | `hlte-kor-cm` | marshmallow | 3.04 | CyanogenMod 13 (Korean) | jcadduono | `git clone https://github.com/jcadduono/idleKernel-note3.git -b ik-nethunter-M` |
| 103 | `hlte` | Samsung Galaxy Note 3 | `hlte-kor-tw` | lollipop | 3.04 | TouchWiz 5.0 (Korean) | jcadduono | `git clone https://github.com/jcadduono/idleKernel-note3.git -b ik-nethunter-touchwiz` |
| 104 | `hlte` | Samsung Galaxy Note 3 | `hlte-spr-cm` | lollipop | 3.04 | CyanogenMod 12 (Sprint) | jcadduono | `git clone https://github.com/jcadduono/idleKernel-note3.git -b ik-nethunter-L` |
| 105 | `hlte` | Samsung Galaxy Note 3 | `hlte-spr-cm` | marshmallow | 3.04 | CyanogenMod 13 (Sprint) | jcadduono | `git clone https://github.com/jcadduono/idleKernel-note3.git -b ik-nethunter-M` |
| 106 | `hlte` | Samsung Galaxy Note 3 | `hlte-spr-tw` | lollipop | 3.04 | TouchWiz 5.0 (Sprint) | jcadduono | `git clone https://github.com/jcadduono/idleKernel-note3.git -b ik-nethunter-touchwiz` |
| 107 | `hlte` | Samsung Galaxy Note 3 | `hlte-vzw-tw` | lollipop | 3.04 | TouchWiz 5.0 (Verizon) | jcadduono | `git clone https://github.com/jcadduono/idleKernel-note3.git -b ik-nethunter-touchwiz` |
| 108 | `honami` | Sony Xperia Z1 | `honami-los` | marshmallow | 3.04 | LineageOS 13.1 | Re4son | `git clone https://github.com/Re4son/android_kernel_Hanomi.git -b master` |
| 109 | `honami` | Sony Xperia Z1 | `honami-los` | pie | 3.04 | LineageOS 16 | Re4son | `git clone https://github.com/Re4son/android_kernel_Hanomi.git -b master` |
| 110 | `htc-pmewl` | HTC 10 | `htc-pmewl` | marshmallow | 3.18 | HTC 10 Sense 8.0 | S1CAR1US | `git clone https://github.com/S1CAR1US/nethunter_kernel_htc_pmewl.git` |
| 111 | `ido` | Xiaomi Redmi 3 / 3 Pro | `ido-los` | nougat | 3.10 | LineageOS 14.1 | ariafan | `git clone https://github.com/ariafan/ido_kernel-kali.git -b kali-new` |
| 112 | `j53g` | Samsung Galaxy J5 3G (2015) | `j53g-los` | nougat | 3.10 | LineageOS 14.1 | djkido316 | `git clone https://github.com/djkido316/nethunter-kernel_j5` |
| 113 | `j5lte` | Samsung Galaxy J5 LTE (2015) | `j5lte-los` | nougat | 3.10 | LineageOS 14.1 | djkido316 | `git clone https://github.com/djkido316/nethunter-kernel_j5` |
| 114 | `j5nlte` | Samsung Galaxy J5 NFC LTE (2015) | `j5nlte-los` | nougat | 3.10 | LineageOS 14.1 | djkido316 | `git clone https://github.com/djkido316/nethunter-kernel_j5` |
| 115 | `j7y17lte` | Samsung Galaxy J7 Pro | `j7y17lte-oui` | pie | 3.18 | One UI | S133PY | `git clone https://github.com/Thiviyan/KRAKEN_7870_Nethunter -b nethunter` |
| 116 | `jalebi` | Yu Yunique | `jalebi-los` | nougat | 3.10 | LineageOS 14.1 | Satyabrat Sahoo | `git clone https://github.com/thelazyindian/kernel_8916.git -b cm-14.1-nethunter` |
| 117 | `jasmine-sprout` | Xiaomi Mi A2 | `jasmine-sprout-los` | fifteen | 4.19 | LineageOS 22.1 | mr00k3 | `git clone https://github.com/mr00k3/jasmine_sprout_nethunter -b nethunter-los-22.1` |
| 118 | `jflte` | Samsung Galaxy S4 | `jfltexx-cm` | marshmallow | 3.04 | CyanogenMod 13 | semsevens | `git clone https://github.com/semsevens/nethunter_kernel_jfltexx.git -b cm-13.0` |
| 119 | `jflte` | Samsung Galaxy S4 | `jfltexx-cm` | nougat | 3.04 | CyanogenMod 14.1 | fasheng | `git clone https://github.com/fasheng/nethunter_kernel_jfltexx.git -b cm-14.1` |
| 120 | `jiayus3a` | Jiayu S3 Advanced | `jiayus3a` | marshmallow | 3.10 | Android 6 | DKingCN | `git clone https://github.com/DKingCN/android_kernel_jiayu_s3_h560.git -b nethunter-6.0` |
| 121 | `kiwi` | Huawei Honor 5x | `kiwi-cm` | marshmallow | 3.10 | CyanogenMod 13 | DeadSquirrel01 | `git clone https://github.com/DeadSquirrel01/android_kernel_huawei_kiwi.git -b cm-13.0` |
| 122 | `klte` | Samsung Galaxy S5 | `klte-los` | nougat | 3.04 | LineageOS 14.1 (GSM) | jcadduono | `git clone https://github.com/jcadduono/android_kernel_samsung_msm8974.git -b cm-14.1` |
| 123 | `klte` | Samsung Galaxy S5 | `klte-tw` | lollipop | 3.04 | TouchWiz 5.1 (GSM) | jcadduono | `git clone https://github.com/jcadduono/nethunter_kernel_klte.git -b touchwiz-5.1` |
| 124 | `klte` | Samsung Galaxy S5 | `klte-tw` | marshmallow | 3.04 | TouchWiz 6.0 (GSM) | jcadduono | `git clone https://github.com/jcadduono/nethunter_kernel_klte.git -b touchwiz-6.0` |
| 125 | `klte` | Samsung Galaxy S5 | `klte-chn-los` | nougat | 3.04 | LineageOS 14.1 (China) | jcadduono | `git clone https://github.com/jcadduono/android_kernel_samsung_msm8974.git -b cm-14.1` |
| 126 | `klte` | Samsung Galaxy S5 | `klte-chnduo-los` | nougat | 3.04 | LineageOS 14.1 (China Duos) | jcadduono | `git clone https://github.com/jcadduono/android_kernel_samsung_msm8974.git -b cm-14.1` |
| 127 | `klte` | Samsung Galaxy S5 | `klte-duos-los` | nougat | 3.04 | LineageOS 14.1 (LTE Duos) | jcadduono | `git clone https://github.com/jcadduono/android_kernel_samsung_msm8974.git -b cm-14.1` |
| 128 | `klte` | Samsung Galaxy S5 | `klte-duos-tw` | lollipop | 3.04 | TouchWiz 5.1 (LTE Duos) | jcadduono | `git clone https://github.com/jcadduono/nethunter_kernel_klte.git -b touchwiz-5.1` |
| 129 | `klte` | Samsung Galaxy S5 | `klte-kdi-los` | nougat | 3.04 | LineageOS 14.1 (Japan) | jcadduono | `git clone https://github.com/jcadduono/android_kernel_samsung_msm8974.git -b cm-14.1` |
| 130 | `klte` | Samsung Galaxy S5 | `klte-kdi-tw` | lollipop | 3.04 | TouchWiz 5.1 (Japan) | jcadduono | `git clone https://github.com/jcadduono/nethunter_kernel_klte.git -b touchwiz-5.1` |
| 131 | `klte` | Samsung Galaxy S5 | `klte-kor-los` | nougat | 3.04 | LineageOS 14.1 (Korea) | jcadduono | `git clone https://github.com/jcadduono/android_kernel_samsung_msm8974.git -b cm-14.1` |
| 132 | `klte` | Samsung Galaxy S5 | `klte-skt-tw` | lollipop | 3.04 | TouchWiz 5.1 (Korea) | jcadduono | `git clone https://github.com/jcadduono/nethunter_kernel_klte.git -b touchwiz-5.1` |
| 133 | `klte` | Samsung Galaxy S5 | `klte-skt-tw` | marshmallow | 3.04 | TouchWiz 6.0 (Korea) | jcadduono | `git clone https://github.com/jcadduono/nethunter_kernel_klte.git -b touchwiz-6.0` |
| 134 | `klte` | Samsung Galaxy S5 | `klte-spr-los` | nougat | 3.04 | LineageOS 14.1 (US Sprint, UK Vodafone, and Oceanic) | jcadduono | `git clone https://github.com/jcadduono/android_kernel_samsung_msm8974.git -b cm-14.1` |
| 135 | `klte` | Samsung Galaxy S5 | `klte-spr-tw` | lollipop | 3.04 | TouchWiz 5.1 (US Sprint, UK Vodafone, and Oceanic) | jcadduono | `git clone https://github.com/jcadduono/nethunter_kernel_klte.git -b touchwiz-5.1` |
| 136 | `klte` | Samsung Galaxy S5 | `klte-usc-tw` | lollipop | 3.04 | TouchWiz 5.1 (US Cellular) | jcadduono | `git clone https://github.com/jcadduono/nethunter_kernel_klte.git -b touchwiz-5.1` |
| 137 | `klte` | Samsung Galaxy S5 | `klte-vzw-tw` | lollipop | 3.04 | TouchWiz 5.1 (US Verizon) | jcadduono | `git clone https://github.com/jcadduono/nethunter_kernel_klte.git -b touchwiz-5.1` |
| 138 | `kminilte` | Samsung Galaxy S5 Mini | `kminilte-los` | nougat | 3.04 | LineageOS 14.1 | yesimxev | `git clone https://github.com/yesimxev/android_kernel_samsung_kminilte.git -b N` |
| 139 | `kminilte` | Samsung Galaxy S5 Mini | `kminilte-los` | oreo | 3.04 | LineageOS 15.0 | yesimxev | `git clone https://github.com/yesimxev/android_kernel_samsung_kminilte.git -b O` |
| 140 | `kminilte` | Samsung Galaxy S5 Mini | `kminilte-los` | pie | 3.04 | LineageOS 16.0 | yesimxev | `git clone https://github.com/yesimxev/android_kernel_samsung_kminilte.git -b P` |
| 141 | `laurel-sprout` | Xiaomi Mi A3 | `laurel-sprout-los` | eleven | 4.14 | LineageOS 18.1 | yesimxev | `git clone https://github.com/yesimxev/android_kernel_xiaomi_laurel_sprout -b lineage-18.1` |
| 142 | `laurel-sprout` | Xiaomi Mi A3 | `laurel-sprout-los` | twelve | 4.14 | LineageOS 19.1 | yesimxev | `git clone https://github.com/yesimxev/android_kernel_xiaomi_laurel_sprout -b lineage-18.1` |
| 143 | `laurel-sprout` | Xiaomi Mi A3 | `laurel-sprout-los` | thirteen | 4.14 | LineageOS 20 | yesimxev | `git clone https://github.com/yesimxev/android_kernel_xiaomi_laurel_sprout -b lineage-18.1` |
| 144 | `laurel-sprout` | Xiaomi Mi A3 | `laurel-sprout-los` | fourteen | 4.14 | LineageOS 21 | yesimxev | `git clone https://github.com/yesimxev/android_kernel_laurel_sprout -b lineage-18.1` |
| 145 | `laurel-sprout` | Xiaomi Mi A3 | `laurel-sprout-los` | fifteen | 4.14 | LineageOS 22 | yesimxev | `git clone https://github.com/yesimxev/android_kernel_laurel_sprout -b lineage-18.1` |
| 146 | `laurel-sprout` | Xiaomi Mi A3 | `laurel-sprout-los` | sixteen | 4.14 | LineageOS 23.2 | yesimxev | `git clone https://github.com/yesimxev/android_kernel_xiaomi_sm6125 -b lineage-23.2` |
| 147 | `lv517` | LG K20 Plus | `lv517-los` | nougat | 3.18 | LineageOS 14.1 | robnew | `git clone https://github.com/robnew/NetHunter_K20plus_arm64_Kernel.git` |
| 148 | `mako` | Google Nexus 4 | `mako` | kitkat | 3.04 | Android 4 | Binkybear | `git clone https://github.com/binkybear/kernel_msm.git -b android-msm-mako-3.4-kitkat-mr2` |
| 149 | `mako` | Google Nexus 4 | `mako` | lollipop | 3.04 | Android 5 | Binkybear | `git clone https://github.com/binkybear/kernel_msm.git -b android-msm-mako-3.4-lollipop-release` |
| 150 | `mako` | Google Nexus 4 | `mako-cm` | marshmallow | 3.04 | CyanogenMod 13 | jcadduono | `git clone https://github.com/jcadduono/nethunter_kernel_mako.git -b cm-13.0` |
| 151 | `manning` | Lenovo K8 Note | `manning` | nougat | 3.18 | Android 7.1 | Byom Dwivedi | `git clone https://github.com/MotorolaMobilityLLC/kernel-mtk.git -b nougat-7.1.1-release-manning` |
| 152 | `manta` | Google Nexus 10 | `manta` | lollipop | 3.04 | Android 5 | jmmmbnnn | `git clone https://github.com/jmmmbnnn/kernel_samsung_manta.git -b thunderkat` |
| 153 | `markw` | Xiaomi Redmi 4 Prime | `markw-los` | oreo | 3.18 | LineageOS 15.1 | fasheng | `git clone https://github.com/fasheng/nethunter_kernel_msm8953_markw -b Nosgoth` |
| 154 | `markw` | Xiaomi Redmi 4 Prime | `markw-los` | pie | 3.18 | LineageOS 16 | fasheng | `git clone https://github.com/fasheng/nethunter_kernel_msm8953_markw -b Nosgoth` |
| 155 | `milanf` | Motorola Moto G Stylus 5G (2022) | `milanf-los` | sixteen | 5.4.302 | LineageOS 23.2 (Android 16) | TigerClips1 | `git clone https://github.com/TigerClips1/kali-nethunter-milanf-kernel -b nethunter` |
| 156 | `mocha` | Xiaomi MiPad 1 | `mocha-cm` | kitkat | 3.10 | CyanogenMod 11 | RahulTheVirus! | `git clone https://github.com/RahulTheVirus/mocha-kernels.git -b nethunter-cm11` |
| 157 | `mocha` | Xiaomi MiPad 1 | `mocha-cm` | lollipop | 3.10 | CyanogenMod 12.1 | RahulTheVirus! | `git clone https://github.com/RahulTheVirus/mocha-kernels.git -b nethunter-cm12.1` |
| 158 | `nx563j` | Nubia Z17 | `nx563j-los` | fifteen | 4.04 | LineageOS 22.2 | luckylca | `git clone https://github.com/luckylca/android_kernel_nubia_msm8998_nethunter -b nethunter-22.2` |
| 159 | `on7xlte` | Samsung Galaxy J7 Prime | `on7xlte-oui` | pie | 3.18 | One UI | S133PY | `git clone https://github.com/Thiviyan/KRAKEN_7870_Nethunter -b nethunter` |
| 160 | `onem7gpe` | HTC One M7 | `onem7gpe` | lollipop | 3.04 | Google Play Edition 5.1 | Lavanoid | `git clone https://github.com/lavanoid/android_kernel_htc_m7gpe -b android-5.1` |
| 161 | `onem8gpe` | HTC One M8 | `onem8gpe` | marshmallow | 3.04 | Google Play Edition 6 | Lavanoid | `git clone https://github.com/lavanoid/android_kernel_htc_m8gpe -b android-6.0` |
| 162 | `oneplus-nord` | OnePlus Nord | `oneplus-nord-oos` | eleven | 4.19 | OxygenOS 11 | kimocoder | `` |
| 163 | `oneplus-nord` | OnePlus Nord | `oneplus-nord-oos` | twelve | 4.19 | OxygenOS 12 | kimocoder | `` |
| 164 | `oneplus-nord` | OnePlus Nord | `oneplus-nord-oos` | sixteen | 4.19 | OxygenOS 16 | kimocoder | `` |
| 165 | `oneplus1` | OnePlus One | `oneplus1-cm` | lollipop | 3.04 | CyanogenMod 12.1 | Binkybear | `git clone https://github.com/binkybear/AK-OnePone.git -b cm-12.1` |
| 166 | `oneplus1` | OnePlus One | `oneplus1-cm` | marshmallow | 3.04 | CyanogenMod 13 | Binkybear | `git clone https://github.com/binkybear/AK-OnePone.git -b cm-13.0` |
| 167 | `oneplus1` | OnePlus One | `oneplus1-cm` | nougat | 3.04 | CyanogenMod 14.1 | yesimxev | `git clone https://github.com/yesimxev/android_kernel_oneplus_msm8974.git -b cm-14.1 oneplus14` |
| 168 | `oneplus1` | OnePlus One | `oneplus1-los` | oreo | 3.04 | LineageOS 15.1 | yesimxev | `git clone https://github.com/yesimxev/android_kernel_oppo_msm8974.git -b lineage-15.1 oneplus15` |
| 169 | `oneplus1` | OnePlus One | `oneplus1-los` | pie | 3.04 | LineageOS 16 | yesimxev | `git clone https://github.com/yesimxev/android_kernel_oppo_msm8974.git -b lineage-16.0 oneplus16` |
| 170 | `oneplus1` | OnePlus One | `oneplus1-los` | ten | 3.04 | LineageOS 17.1 | yesimxev | `git clone https://github.com/yesimxev/android_kernel_oppo_msm8974.git -b lineage-17.1 oneplus17.1` |
| 171 | `oneplus1` | OnePlus One | `oneplus1-los` | eleven | 3.04 | LineageOS 18.1 | yesimxev | `git clone https://github.com/yesimxev/android_kernel_oppo_msm8974.git -b lineage-18.1 oneplus18.1` |
| 172 | `oneplus2` | OnePlus 2 | `oneplus2-oos` | lollipop | 3.10 | OxygenOS 2 | Binkybear | `git clone https://github.com/binkybear/android_kernel_oneplus_msm8994.git -b boeffla_oos3` |
| 173 | `oneplus2` | OnePlus 2 | `oneplus2-oos` | marshmallow | 3.10 | OxygenOS 3 | Binkybear | `git clone https://github.com/binkybear/android_kernel_oneplus_msm8994.git -b 6.0.1-oos` |
| 174 | `oneplus2` | OnePlus 2 | `oneplus2-cm` | lollipop | 3.10 | CyanogenMod 12.1 | Binkybear | `git clone https://github.com/binkybear/android_kernel_oneplus_msm8994.git -b cm-12.1` |
| 175 | `oneplus2` | OnePlus 2 | `oneplus2-cm` | marshmallow | 3.10 | CyanogenMod 13.0 | Binkybear | `git clone https://github.com/binkybear/android_kernel_oneplus_msm8994.git -b cm-13.0` |
| 176 | `oneplus2` | OnePlus 2 | `oneplus2-los` | nougat | 3.10 | LineageOS 14.1 | Re4son | `git clone https://github.com/Re4son/android_kernel_oneplus_msm8994.git -b cm-14.1` |
| 177 | `oneplus2` | OnePlus 2 | `oneplus2-los` | oreo | 3.10 | LineageOS 15.1 | Re4son | `git clone https://github.com/Re4son/android_kernel_oneplus_msm8994.git -b cm-15.1` |
| 178 | `oneplus2` | OnePlus 2 | `oneplus2-los` | pie | 3.10 | LineageOS 16.0 | Re4son | `git clone https://github.com/Re4son/android_kernel_oneplus_msm8994.git -b cm-16.0` |
| 179 | `oneplus3` | OnePlus 3 / 3T | `oneplus3-3t-oos` | pie | 3.18 | OxygenOS 9.0 | Re4son | `git clone https://github.com/re4son/android_kernel_oneplus_msm8996.git -b nethunter-9.0` |
| 180 | `oneplus3` | OnePlus 3 / 3T | `oneplus3-3t-los` | ten | 3.18 | LineageOS 17.1 | Re4son | `git clone https://github.com/re4son/android_kerLoukious/nethunter_kernel_oneplus_sdm845nel_oneplus_msm8996_lineageos.git -b nethunter-17.1` |
| 181 | `oneplus3` | OnePlus 3 / 3T | `oneplus3-oos` | nougat | 3.18 | OxygenOS 4 | zanezam | `git clone https://github.com/zanezam/boeffla-kernel-oos-oneplus3.git -b t_boeffla_cm14_nethunter-V1_aa64u541` |
| 182 | `oneplus3` | OnePlus 3 / 3T | `oneplus3-v2-oos` | marshmallow | 3.18 | OxygenOS 3 | Binkybear | `git clone https://github.com/binkybear/android_kernel_oneplus_msm8996.git -b ElementalX` |
| 183 | `oneplus3` | OnePlus 3 / 3T | `oneplus3-v2-oos` | nougat | 3.18 | OxygenOS | jcadduono | `git clone https://github.com/jcadduono/android_kernel_oneplus_msm8996.git -b nethunter-7.0` |
| 184 | `oneplus3` | OnePlus 3 / 3T | `oneplus3-los` | nougat | 3.18 | LineageOS | zanezam | `git clone https://github.com/zanezam/boeffla-kernel-cm-oneplus3.git -b t_boeffla_cm14_nethunter-V1_aa64u541` |
| 185 | `oneplus3` | OnePlus 3 / 3T | `oneplus3t-los` | nougat | 3.18 | LineageOS 14 | zanezam | `git clone https://github.com/zanezam/boeffla-kernel-cm-oneplus3.git -b t_boeffla_cm14_nethunter-V1_aa64u541` |
| 186 | `oneplus3` | OnePlus 3 / 3T | `oneplus3t-los` | oreo | 3.18 | LineageOS 15.1 | flypatriot | `git clone https://github.com/flypatriot/boeffla-kernel-los-nethunter-oneplus3T.git -b t_boeffla_lineage15_nethunter` |
| 187 | `oneplus3` | OnePlus 3 / 3T | `oneplus3t-oos` | nougat | 3.18 | OxygenOS 4 | zanezam | `git clone https://github.com/zanezam/boeffla-kernel-oos-oneplus3.git -b t_boeffla_cm14_nethunter-V1_aa64u541` |
| 188 | `oneplus5` | OnePlus 5 / 5T | `oneplus5-oos` | nougat | 4.04 | OxygenOS 4 | Binkybear | `git clone https://github.com/nethunteros/android_kernel_oneplus_msm8998 -b boeffla_oos4 oneplus5` |
| 189 | `oneplus5` | OnePlus 5 / 5T | `oneplus5-cm` | nougat | 4.04 | CyanogenMod 14 | Binkybear | `git clone https://github.com/nethunteros/android_kernel_oneplus_msm8998 -b boeffla_cm14 oneplus5` |
| 190 | `oneplus5` | OnePlus 5 / 5T | `oneplus5-los` | fifteen | 4.04 | LineageOS 22.2 | seppzer0 | `git clone -b v0.6.4 https://github.com/seppzer0/zero-kernel` |
| 191 | `oneplus5` | OnePlus 5 / 5T | `oneplus5-los-ksu` | fifteen | 4.04 | LineageOS 22.2 | seppzer0 | `git clone -b v0.6.4 https://github.com/seppzer0/zero-kernel` |
| 192 | `oneplus6` | OnePlus 6 / 6T | `oneplus6-oos` | ten | 4.09 | OxygenOS 10 | kimocoder | `git clone https://github.com/kimocoder/DJY-Nethunter-Andrax-Kernel-Source -b nethunter-10.0` |
| 193 | `oneplus6` | OnePlus 6 / 6T | `oneplus6-oos` | eleven | 4.09 | OxygenOS 11 | kimocoder | `git clone https://github.com/kimocoder/android_kernel_oneplus6 -b nethunter` |
| 194 | `oneplus6` | OnePlus 6 / 6T | `oneplus6-los` | twelve | 4.09 | LineageOS 19.1 | kimocoder | `git clone https://github.com/kimocoder/android_kernel_oneplus6 -b nethunter` |
| 195 | `oneplus6` | OnePlus 6 / 6T | `oneplus6-los` | fifteen | 4.09 | LineageOS 22.2 | kimocoder & Loukious | `git clone https://github.com/Loukious/nethunter_kernel_oneplus_sdm845 -b nethunter-22.2` |
| 196 | `oneplus7` | OnePlus 7 / 7 Pro / 7T / 7T Pro | `oneplus7-oos` | pie | 4.14 | OxygenOS 9 | Re4son | `git clone https://github.com/Re4son/android_kernel_oneplus_sm8150 -b nethunter-9.0` |
| 197 | `oneplus7` | OnePlus 7 / 7 Pro / 7T / 7T Pro | `oneplus7-oos` | ten | 4.14 | OxygenOS 10 | Re4son & yesimxev | `git clone https://github.com/Re4son/android_kernel_oneplus_sm8150_draco -b nethunter-10.0` |
| 198 | `oneplus7` | OnePlus 7 / 7 Pro / 7T / 7T Pro | `oneplus7-oos` | eleven | 4.14 | OxygenOS 11 | kimocoder | `git clone https://github.com/kimocoder/nethunter_kernel_oneplus7 -b nethunter-11.0` |
| 199 | `oneplus7` | OnePlus 7 / 7 Pro / 7T / 7T Pro | `oneplus7-v2-oos` | eleven | 4.14 | OxygenOS 11 | cyberknight777 | `` |
| 200 | `oneplus7` | OnePlus 7 / 7 Pro / 7T / 7T Pro | `oneplus7-los-23.2` | sixteen | 4.14 | LineageOS 23.2 | v0lk3n | `git clone --recurse-submodules https://github.com/V0lk3n/nethunter_kernel_oneplus_sm8150.git -b nethunter-lineage-23.2` |
| 201 | `oneplus8` | OnePlus 8 / 8T / 8 Pro | `oneplus8-oos` | eleven | 4.19 | OxygenOS 11 / Custom A11 | flyP@TR!0T | `git clone https://github.com/flypatriot/neutrino_kernel_oneplus_sm8250.git -b neutrino-nethunter` |
| 202 | `oneplus8` | OnePlus 8 / 8T / 8 Pro | `oneplus8-oos` | twelve | 4.19 | OxygenOS 12 / Custom A12 | flyP@TR!0T | `git clone https://github.com/flypatriot/crdroid_12_kernel.git -b 12.0-nethunter` |
| 203 | `lemonade` | OnePlus-9/pro | `lemonade-los` | sixteen | 5.4.302 | LineageOS | varakumar01 | `git clone https://github.com/varakumar01/Levion_kernel_OP9 -b nethunterv2` |
| 204 | `lemonadep` | OnePlus-9Pro | `lemonadep_matrixx` | fifteen | 5.4.302 | Lineage | Madara273 | `git clone https://github.com/Madara273/Sakura_Kernel_OP9Pro -b staging_sakura` |
| 205 | `oneplusx` | OnePlus X | `oneplusx-cm` | marshmallow | 3.04 | CyanogenMod 13 | jcadduono | `git clone https://github.com/jcadduono/nethunter_kernel_onyx.git -b cm-13.0` |
| 206 | `osprey` | Motorola Moto G 2015 | `osprey-los` | nougat | 3.10 | LineageOS 14.1 | rajeshdubey293 | `git clone https://github.com/rajeshdubey293/kernel_osprey-cm-14.1 -b cm-14.1` |
| 207 | `osprey` | Motorola Moto G 2015 | `osprey-los` | oreo | 3.10 | LineageOS 15.1 | rajeshdubey293 | `git clone https://github.com/rajeshdubey293/kernel_osprey-oreo -b oreo-mr1` |
| 208 | `payton` | Motorola Moto X4 | `payton-los` | ten | 4.4 | LineageOS 17.1 | ciropom | `git clone https://github.com/ciropom/android_nethunter_kernel_motorola_msm8998.git -b lineage-17.1` |
| 209 | `payton` | Motorola Moto X4 | `payton-los` | thirteen | 4.4 | LineageOS 20 | yesimxev | `git clone https://github.com/yesimxev/android_kernel_motorola_msm8998 -b lineage-20` |
| 210 | `payton` | Motorola Moto X4 | `payton-los` | fifteen | 4.4 | LineageOS 22.2 | yesimxev | `git clone https://github.com/yesimxev/android_kernel_motorola_msm8998 -b lineage-22.2` |
| 211 | `pdx201` | Sony Xperia 10 II | `pdx201-los` | thirteen | 4.14 | LineageOS 20 | Mashopy | `git clone https://github.com/lineageos-on-pdx201/android_kernel_sony_sm6125 -b lineage-20` |
| 212 | `pdx235` | Sony Xperia 10 V | `pdx235-los` | sixteen | 5.4 | LineageOS 23.2 | Tom60chat | `git clone https://github.com/Tom60chat/android_kernel_sony_sm6375 -b lineage-23.2` |
| 213 | `pl2` | Nokia 6.1 | `pl2-los` | ten | 4.4 | LineageOS 21 | yesimxev | `git clone https://github.com/yesimxev/android_kernel_nokia_sdm660 -b lineage-17` |
| 214 | `pl2` | Nokia 6.1 | `pl2-los` | eleven | 4.4 | LineageOS 18.1 | yesimxev | `git clone https://github.com/yesimxev/android_kernel_nokia_sdm660 -b lineage-18.1` |
| 215 | `pl2` | Nokia 6.1 | `pl2-los` | thirteen | 4.4 | LineageOS 20 | yesimxev | `git clone https://github.com/yesimxev/android_kernel_nokia_sdm660 -b lineage-20` |
| 216 | `pl2` | Nokia 6.1 | `pl2-los` | fourteen | 4.4 | LineageOS 21 | yesimxev | `git clone https://github.com/yesimxev/android_kernel_nokia_sdm660 -b lineage-21` |
| 217 | `potter` | Motorola Moto G5 Plus | `potter-los` | nougat | 3.18 | LineageOS 14.1 | chankruze | `git clone https://github.com/chankruze/potter_kali_kernel -b cm-14.1` |
| 218 | `potter` | Motorola Moto G5 Plus | `potter-los` | pie | 3.18 | LineageOS 16 | rajeshdubey293 | `git clone https://github.com/rajeshdubey293/Optimus_Drunk_Potter.git -b 9.0` |
| 219 | `pyxis` | Xiaomi Mi 9 Lite / CC9 | `pyxis-los` | fourteen | 4.9 | LineageOS 21 | yesimxev | `git clone https://github.com/yesimxev/android_kernel_xiaomi_sdm710 -b lineage-21` |
| 220 | `pyxis` | Xiaomi Mi 9 Lite / CC9 | `pyxis-los` | fifteen | 4.9 | LineageOS 22.2 | yesimxev | `git clone https://github.com/yesimxev/android_kernel_xiaomi_sdm710 -b lineage-22.2` |
| 221 | `r8q` | Samsung Galaxy S20 FE 5G (Snapdragon) | `r8q-oui` | ten | 4.19 | One UI 2.5 | Svirusx | `git clone https://github.com/Svirusx/Nethunter-Kernel-S20_FE_5G.git -b nethunter-10.0` |
| 222 | `r8q` | Samsung Galaxy S20 FE 5G (Snapdragon) | `r8q-oui` | eleven | 4.19 | One UI 3.0 | Svirusx | `git clone https://github.com/Svirusx/Nethunter-Kernel-S20_FE_5G.git -b nethunter-11.0` |
| 223 | `r8q` | Samsung Galaxy S20 FE 5G (Snapdragon) | `r8q-oui` | twelve | 4.19 | One UI 4.0 | Svirusx | `git clone https://github.com/Svirusx/Nethunter-Kernel-S20_FE_5G.git -b nethunter-12.0` |
| 224 | `r8q` | Samsung Galaxy S20 FE 5G (Snapdragon) | `r8q-oui` | thirteen | 4.19 | One UI 5.0 | Svirusx | `git clone https://github.com/Svirusx/Nethunter-Kernel-S20_FE_5G.git -b nethunter-13.0` |
| 225 | `r8q` | Samsung Galaxy S20 FE 5G (Snapdragon) | `r8q-los` | sixteen | 4.19 | LineageOS 23.0 | Svirusx | `git clone https://github.com/Svirusx/Nethunter_LineageOS_Samsung_S20FE5G_sm8250.git -b Nethunter-16-lineage-23.0` |
| 226 | `riva` | Xiaomi Redmi 5A | `riva-los` | fourteen | 4.9 | crDroid Android 14 | ShorterKing | `git clone https://github.com/ShorterKing/Nethunter-Kernel-Redmi5A-Riva` |
| 227 | `rmx1911` | Realme 5 / 5i / 5s | `rmx1911-cos` | twelve | 4.14 | Corvus vS4.1-Eclipse | Mikhail Simon | `git clone https://github.com/mikhailsimon/nethunter-r5x` |
| 228 | `rmx1971` | Realme 5 Pro | `rmx1971` | twelve | 4.9 | Android 12 | Alynx | `git clone https://github.com/V3rB0se/Alynx-RMX1971` |
| 229 | `rmx1971-rui2` | Realme 5 Pro | `rmx1971-rui2` | sixteen | 4.9 | Android 16 (RUI2) | halfclub | `git clone https://github.com/halfclub58/rmx1971_kernel.git -b rmx1971-nethunter` |
| 230 | `rmx2180` | Realme C15 Mediatek | `rmx2180-los-ksun` | ten | 4.9 | LineageOS 17.1 | Frostleaft07 | `git clone https://github.com/Frostleaft07/android_kernel_realme_mt6765 -b Nethunter` |
| 231 | `rmx3031` | Realme X7 Max 5G | `rmx3031` | thirteen | 4.19 | Android 13 and firmware F.13 and EX01 | dek0der | `git clone https://github.com/dek0der/kernel_realme_RMX3031` |
| 232 | `s2` | LeEco Le 2 | `s2-cm` | nougat | 3.10 | CyanogenMod 14.1 | Rishabh Rao | `git clone https://github.com/nethunter-s2/android_kernel_leeco_s2.git -b cm-14.1` |
| 233 | `sailfish` | Google Pixel | `sailfish` | fifteen | 4.4 | LineageOS 22.2 | willuhmjs | `git clone git@github.com:willuhmjs/android_kernel_google_marlin -b lineage-22.2` |
| 234 | `sakura` | Xiaomi Redmi 6 Pro | `sakura-los` | ten | 4.09 | LineageOS | dek0der | `git clone https://github.com/dek0der/nethunter_kernel_redmi_6_pro_sakura` |
| 235 | `sakura` | Xiaomi Redmi 6 Pro | `sakura-los` | eleven | 4.09 | LineageOS | dek0der | `git clone https://github.com/dek0der/nethunter_kernel_redmi_6_pro_sakura` |
| 236 | `santoni` | Xiaomi Redmi 4/4X | `santoni-miui` | nougat | 3.18 | MIUI 9.0 | santoni | `git clone https://github.com/DroidKali/santoni_kernel_nethunter.git` |
| 237 | `santoni` | Xiaomi Redmi 4/4X | `santoni-vos` | thirteen | 4.9.227 | VoltageOS 2.x (A13) | MomboteQ | `git clone https://github.com/MomboteQ/hackphone_kernel_xiaomi_msm8937 -b 13` |
| 238 | `mido` | Xiaomi Redmi Note 4X | `mido-pe11` | eleven | 4.9 | Pixel Experience | linlinger | `git clone https://github.com/linlinger/kernel_xiaomi_mido.git -b nethunter-pe` |
| 239 | `mido` | Xiaomi Redmi Note 4X | `mido-los` | fourteen | 4.9 | LineageOS kernel with NetHunter features enabled | Serp3n7 | `git clone https://github.com/Serp3n7/kernel_xiaomi_mido.git` |
| 240 | `shamu` | Google Nexus 6 | `shamu` | lollipop | 3.04 | Android 5 | Binkybear | `git clone https://github.com/binkybear/kernel_msm.git -b android-msm-shamu-3.10-lollipop-release` |
| 241 | `shamu` | Google Nexus 6 | `shamu` | marshmallow | 3.04 | Android 6 | Binkybear | `git clone https://github.com/binkybear/kernel_msm.git -b android-msm-shamu-3.10-marshmallow-release` |
| 242 | `shamu` | Google Nexus 6 | `shamu` | nougat | 3.04 | Android 7.1 | Binkybear | `git clone https://github.com/binkybear/kernel_msm.git -b android-msm-shamu-3.10-n` |
| 243 | `shamu` | Google Nexus 6 | `shamu-los` | nougat | 3.04 | LineageOS 14.1 | discipuloosho | `git clone https://github.com/discipuloosho/android_kernel_moto_shamu.git -b nethunter_cm-14.1` |
| 244 | `shamu` | Google Nexus 6 | `shamu-los` | pie | 3.04 | LineageOS 16.0 | Re4son | `git clone https://github.com/Re4son/android_kernel_moto_shamu.git -b nethunter-16.0` |
| 245 | `shieldtablet` | nVidea Shield Tablet | `shieldtablet` | marshmallow | 3.10 | Android 6.0 | jcadduono | `git clone https://github.com/jcadduono/android_kernel_nvidia_shield.git -b nethunter-6.0` |
| 246 | `shieldtablet` | nVidea Shield Tablet | `shieldtablet` | nougat | 3.10 | Android 7.1 | SecurityAddicted | `git clone https://github.com/SecurityAddicted/android_kernel_nvidia_shieldtablet nethunter` |
| 247 | `spacewar` | Nothing Phone (1) | `spacewar` | twelve | 5.4 | AOSP/AOSPA Android 12 | kimocoder | `git clone https://github.com/kimocoder/android_kernel_nothing_sm7325 -b nethunter-stable` |
| 248 | `spacewar` | Nothing Phone (1) | `spacewar` | thirteen | 5.4 | AOSP/AOSPA Android 13 | kimocoder | `git clone https://github.com/kimocoder/android_kernel_nothing_sm7325 -b nethunter-stable` |
| 249 | `spacewar` | Nothing Phone (1) | `spacewar` | fourteen | 5.4 | AOSP/AOSPA Android 14 | kimocoder | `git clone https://github.com/kimocoder/android_kernel_nothing_sm7325 -b nethunter-stable` |
| 250 | `starlte` | Samsung Galaxy S9 | `starlte-los` | thirteen | 4.9 | LineageOS 20 | v0lk3n | `git clone --recurse-submodules https://github.com/v0lk3n/nethunter_kernel_samsung_exynos9810.git -b nethunter-lineage-20` |
| 251 | `star2lte` | Samsung Galaxy S9+ | `star2lte-los` | thirteen | 4.9 | LineageOS 20 | mylezgoose | `git clone https://github.com/mylesgoose/android_kernel_samsung_exynos9810.git -b lineage-20` |
| 252 | `sunfish` | Google Pixel 4a | `sunfish` | twelve | 4.9 | Android 12L | Alynx | `git clone https://github.com/V3rB0se/Alynx-nethunter-sunfish` |
| 253 | `surya` | Xiaomi Pocophone X3 NFC | `surya-los` | thirteen | 4.9 | LineageOS 20 | r0ttenbeef | `git clone https://github.com/r0ttenbeef/android_kernel_xiaomi_surya -b lineage-20` |
| 254 | `suzuran` | Sony Xperia Z5 Compact | `suzuran-los` | nougat | 3.10 | LineageOS 14.1 | Re4son | `git clone https://github.com/Re4son/android_kernel_sony_msm8994 android-14.1` |
| 255 | `ticwatchpro` | TicWatch Pro / Pro 4G/LTE / Pro 2020 | `ticwatchpro` | wearos | 3.18 | Wear OS 2.29 | yesimxev | `git clone https://github.com/yesimxev/msm-catfish-9.0-wear-os` |
| 256 | `ticwatchpro3` | TicWatch Pro 3 GPS/LTE / Pro 3 Ultra GPS/LTE | `ticwatchpro3` | wearos | 4.09 | OneOS (Wear OS 2.44) | yesimxev | `git clone https://github.com/yesimxev/mobvoi-ticwatch-kernel -b nethunter` |
| 257 | `tulip` | Xiaomi Redmi Note 6 Pro | `tulip` | eleven | 4.4 | Android 11 | TheKidBaby | `` |
| 258 | `us996` | LG V20 | `us996` | nougat | 3.18 | Android 7.0 | jcadduono | `git clone https://github.com/jcadduono/android_kernel_lge_msm8996 -b android-7.0` |
| 259 | `vayu` | Xiaomi Pocophone X3 Pro | `vayu` | eleven | 4.14 | Xiaomi Pocophone X3 Pro for stock Android | cyberknight777 | `` |
| 260 | `victara` | Motorola Moto X2 (2014) | `victara-cm` | nougat | 3.04 | CyanogenMod 14.1 | DSR! | `git clone https://github.com/xchwarze/nethunter-motorola-x2-kernel -b cm-14.1` |
| 261 | `vienna` | Huawei P9 Plus | `vienna` | marshmallow | 4.04 | MIUI 8 | 5h4d0wb0y | `git clone https://github.com/5h4d0wb0y/android_kernel_huawei_vienna.git -b 6.x` |
| 262 | `vienna` | Huawei P9 Plus | `vienna` | nougat | 4.04 | MIUI 9 | 5h4d0wb0y | `git clone https://github.com/5h4d0wb0y/android_kernel_huawei_vienna.git -b 7.x` |
| 263 | `vienna` | Huawei P9 Plus | `vienna` | oreo | 4.04 | MIUI 10 | 5h4d0wb0y | `git clone https://github.com/5h4d0wb0y/android_kernel_huawei_vienna.git` |
| 264 | `yuga` | Sony Xperia Z | `yuga-cm` | marshmallow | 3.04 | CyanogenMod 13 | Daedroza | `git clone https://github.com/daedroza/nethunter_kernel_apq8064.git -b master` |
| 265 | `z00e` | Asus Zenfone 2 Laser (720p) | `z00e-los` | marshmallow | 3.10 | LineageOS 13.0 | adrenogamer | `git clone https://github.com/adrenogamer/android_kernel_asus_msm8916 -b cm-13.0` |
| 266 | `zeroflte` | Samsung Galaxy S6 | `zeroflte-los` | nougat | 3.10 | LineageOS 14.1 | XXH3X | `git clone https://github.com/XXH3X/Exynos7420_Nethunter -b cm-14.1` |
| 267 | `zeroflte` | Samsung Galaxy S6 | `zeroflte-tw` | nougat | 3.10 | Android 7.0 | XXH3X | `git clone https://github.com/XXH3X/Ultimate-Kali` |
| 268 | `zerolte` | Samsung Galaxy S6 Edge | `zerolte-los` | nougat | 3.10 | LineageOS 14.1 | XXH3X | `git clone https://github.com/XXH3X/Exynos7420_Nethunter -b cm-14.1` |
| 269 | `zerolte` | Samsung Galaxy S6 Edge | `zerolte-tw` | nougat | 3.10 | Android 7.0 | XXH3X | `git clone https://github.com/XXH3X/Ultimate-Kali` |
| 270 | `salami` | OnePlus 11 5G | `salami-oos` | fifteen | 5.15 | OxygenOS 15 | nullptr-t-oss | `wget https://github.com/nullptr-t-oss/EmberHeart_OnePlus11/releases/download/v1.5.12-r12/EmberHeart_boot.img` |
| 271 | `salami` | OnePlus 11 5G | `salami-oos` | sixteen | 5.15 | OxygenOS 16 | nullptr-t-oss | `wget https://github.com/nullptr-t-oss/EmberHeart_OnePlus11/releases/download/v2.0.0-r2/EmberHeart_boot.img` |
| 272 | `miatoll` | Xiaomi Redmi Note 9S/Pro | `miatoll-crdroid-15.0` | fifteen | 4.14 | crDroid 15.0 | jolucas245 | `git clone https://github.com/crdroidandroid/android_kernel_xiaomi_sm6250.git -b 15.0` |
| 273 | `surya-16` | Xiaomi Poco X3 NFC (PixelOS) | `surya-16` | sixteen | 4.14 | PixelOS Android 16 QPR2 | dr1408 | `git clone https://github.com/dr1408/kernel_xiaomi_surya_16 -b main` |
| 274 | `stone-crdroid12` | POCO X5 5G / Redmi Note 12 5G (crDroid 12) | `stone-crdroid12` | sixteen | 5.4.302 | crDroid12 Android 16 | harifhaqim(mikhailsimon) | `git clone https://github.com/harifhaqim/crdroid_nethunter_stone -b 16.0` |
| 275 | `whyred` | Xiaomi Redmi Note 5 Pro | `whyred-los` | eleven | 4.4 | LineageOS 18.1 | notatallnic189 | `git clone https://github.com/notatallnic189/whyred-nethunter-kernel -b main` |

Note: a device may appear multiple times when it has several kernel variants (for example LineageOS, TouchWiz, MIUI, or different Android/Linux versions).
