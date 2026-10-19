# Kali NetHunter Kernel Catalog - Device by Device
Generated from `data/nethunter_master.csv` (640 rows). Evidence status is shown for every community project; official registry rows are distribution entries, not boot verification.
## Headline counts
| Metric | Count |
|---|---:|
| Official NetHunter devices (unique codenames) | 126 |
| Official distribution variants | 275 |
| Community kernel projects (deduplicated) | 310 |
| Community projects matched to a device/codename | 232 |
| Device-level search discoveries (metadata only) | 55 |
| Independently verified boot reports | 0 |
| Developer-reported boot reports | 5 |

Manufacturers are ordered alphabetically. `Unknown` groups projects whose repository text does not identify a device.

## ASUS
Devices/codenames: 2. Official variants: 1. Community projects: 1.
### ASUS ZenFone Max Pro M1 (`sdm660`)
No official NetHunter registry variant.

**Community projects**

| Project | Status | Boot evidence | Features claimed/tested | Source |
|---|---|---|---|---|
| tutaf | Abandoned | No explicit boot evidence | Unknown | <https://github.com/tutaf/kernel_asus_sdm660> |

### Asus Zenfone 2 Laser (720p) (`z00e`)
**Official NetHunter registry variants**

| ROM | Android | Kernel | Author | Source |
|---|---|---|---|---|
| LineageOS 13.0 | marshmallow | 3.10 | adrenogamer | <https://github.com/adrenogamer/android_kernel_asus_msm8916> |


## Google
Devices/codenames: 37. Official variants: 38. Community projects: 27.
### Google Nexus 10 (`manta`)
**Official NetHunter registry variants**

| ROM | Android | Kernel | Author | Source |
|---|---|---|---|---|
| Android 5 | lollipop | 3.04 | jmmmbnnn | <https://github.com/jmmmbnnn/kernel_samsung_manta.git> |

### Google Nexus 4 (`mako`)
**Official NetHunter registry variants**

| ROM | Android | Kernel | Author | Source |
|---|---|---|---|---|
| Android 4 | kitkat | 3.04 | Binkybear | <https://github.com/binkybear/kernel_msm.git> |
| Android 5 | lollipop | 3.04 | Binkybear | <https://github.com/binkybear/kernel_msm.git> |
| CyanogenMod 13 | marshmallow | 3.04 | jcadduono | <https://github.com/jcadduono/nethunter_kernel_mako.git> |

### Google Nexus 5 (`hammerhead`)
**Official NetHunter registry variants**

| ROM | Android | Kernel | Author | Source |
|---|---|---|---|---|
| Android 4.4 | kitkat | 3.04 | Binkybear | <https://github.com/binkybear/furnace_kernel_lge_hammerhead.git> |
| Android 5 | lollipop | 3.04 | Binkybear | <https://github.com/binkybear/kernel_msm.git> |
| Android 6 | marshmallow | 3.04 | Re4son | <https://github.com/Re4son/android_kernel_lge_hammerhead> |
| LineageOS 14.1 | nougat | 3.04 | Re4son | <https://github.com/Re4son/android_kernel_lge_hammerhead> |
| CAF LineageOS 14.1 | nougat | 3.04 | chrisk44 | <https://github.com/chrisk44/android_kernel_lge_hammerhead.git> |

Search discoveries (metadata only, not inspected): 1. See `data/nethunter_search_candidates.csv`.

### Google Nexus 5X (`bullhead`)
**Official NetHunter registry variants**

| ROM | Android | Kernel | Author | Source |
|---|---|---|---|---|
| Android 6 | marshmallow | 3.04 | Binkybear | <https://github.com/binkybear/kernel_msm.git> |
| Android 7.1 | nougat | 3.04 | Binkybear | <https://github.com/binkybear/kernel_msm.git> |
| Android 8.1 | oreo | 3.04 | Re4son | <https://github.com/Re4son/android_kernel_lge_bullhead> |

**Community projects**

| Project | Status | Boot evidence | Features claimed/tested | Source |
|---|---|---|---|---|
| LordNikk0n | Developer claimed | No explicit boot evidence | external wifi support, monitor mode | <https://github.com/LordNikk0n/KaliNetHunter-bullhead-kernel> |

### Google Nexus 6 (`shamu`)
**Official NetHunter registry variants**

| ROM | Android | Kernel | Author | Source |
|---|---|---|---|---|
| Android 5 | lollipop | 3.04 | Binkybear | <https://github.com/binkybear/kernel_msm.git> |
| Android 6 | marshmallow | 3.04 | Binkybear | <https://github.com/binkybear/kernel_msm.git> |
| Android 7.1 | nougat | 3.04 | Binkybear | <https://github.com/binkybear/kernel_msm.git> |
| LineageOS 14.1 | nougat | 3.04 | discipuloosho | <https://github.com/discipuloosho/android_kernel_moto_shamu.git> |
| LineageOS 16.0 | pie | 3.04 | Re4son | <https://github.com/Re4son/android_kernel_moto_shamu.git> |

Search discoveries (metadata only, not inspected): 1. See `data/nethunter_search_candidates.csv`.

### Google Nexus 7 (2012) (`grouper`)
**Official NetHunter registry variants**

| ROM | Android | Kernel | Author | Source |
|---|---|---|---|---|
| Android 4.4 | kitkat | 3.01 | Binkybear | <https://github.com/binkybear/android_kernel_asus_grouper.git> |

### Google Nexus 7 (2013) (`flo`)
**Official NetHunter registry variants**

| ROM | Android | Kernel | Author | Source |
|---|---|---|---|---|
| Android 4.4 | kitkat | 3.04 | Binkybear | <https://github.com/binkybear/kernel_msm.git> |
| Android 5 | lollipop | 3.04 | Binkybear | <https://github.com/binkybear/flo.git> |
| Android 6 | marshmallow | 3.04 | Binkybear | <https://github.com/binkybear/flo.git> |
| CyanogenMod | marshmallow | 3.04 | jcadduono | <https://github.com/jcadduono/nethunter_kernel_flo.git> |

**Community projects**

| Project | Status | Boot evidence | Features claimed/tested | Source |
|---|---|---|---|---|
| jcadduono | Abandoned | No explicit boot evidence | Unknown | <https://github.com/jcadduono/nethunter_kernel_flo> |

Search discoveries (metadata only, not inspected): 2. See `data/nethunter_search_candidates.csv`.

### Google Nexus 9 (`flounder`)
**Official NetHunter registry variants**

| ROM | Android | Kernel | Author | Source |
|---|---|---|---|---|
| Android 5 | lollipop | 3.10 | Binkybear | <https://github.com/binkybear/flounder.git> |
| Android 6 | marshmallow | 3.10 | Binkybear | <https://github.com/binkybear/flounder.git> |
| Android 7.1 | nougat | 3.10 | SecurityAddicted | <https://github.com/SecurityAddicted/ElementalX-N9-Nethunter.git> |

### Google Pixel (`sailfish`)
**Official NetHunter registry variants**

| ROM | Android | Kernel | Author | Source |
|---|---|---|---|---|
| LineageOS 22.2 | fifteen | 4.4 | willuhmjs | <https://github.com/willuhmjs/android_kernel_google_marlin> |

### Google Pixel 11 (`cubs`)
No official NetHunter registry variant.

**Community projects**

| Project | Status | Boot evidence | Features claimed/tested | Source |
|---|---|---|---|---|
| Gajeel420 | Developer claimed | Developer-reported boot | internal wifi support, external wifi support, monitor mode | <https://github.com/Gajeel420/cubs-gki-rt2800usb> |

### Google Pixel 3 (`blueline`)
**Official NetHunter registry variants**

| ROM | Android | Kernel | Author | Source |
|---|---|---|---|---|
| Android 12 | twelve | 4.9 | Alynx | <https://github.com/v3rb0se/alynx-nethunter/> |
| Android 13 | thirteen | 4.9 | Alynx | <https://github.com/v3rb0se/alynx-nethunter/> |

### Google Pixel 3 XL (`crosshatch`)
**Official NetHunter registry variants**

| ROM | Android | Kernel | Author | Source |
|---|---|---|---|---|
| Android 12 | twelve | 4.9 | Alynx | <https://github.com/v3rb0se/alynx-nethunter/> |
| Android 13 | thirteen | 4.9 | Alynx | <https://github.com/v3rb0se/alynx-nethunter/> |

### Google Pixel 3a / 3a XL (`bonito/sargo`)
No official NetHunter registry variant.

**Community projects**

| Project | Status | Boot evidence | Features claimed/tested | Source |
|---|---|---|---|---|
| Duhjoker | Unverified candidate | No explicit boot evidence | monitor mode, packet injection | <https://github.com/Duhjoker/Mad-Kali-MaxHunter-kernel-prebuilt> |

### Google Pixel 4 / 4 XL (`coral/flame`)
No official NetHunter registry variant.

**Community projects**

| Project | Status | Boot evidence | Features claimed/tested | Source |
|---|---|---|---|---|
| chenyjie | Unverified candidate | No explicit boot evidence | internal wifi support, hid gadget, usb gadget | <https://github.com/chenyjie/coral-nethunter-kernel> |

### Google Pixel 4a (`sunfish`)
**Official NetHunter registry variants**

| ROM | Android | Kernel | Author | Source |
|---|---|---|---|---|
| Android 12L | twelve | 4.9 | Alynx | <https://github.com/V3rB0se/Alynx-nethunter-sunfish> |

**Community projects**

| Project | Status | Boot evidence | Features claimed/tested | Source |
|---|---|---|---|---|
| V3rB0se | Unverified candidate | No explicit boot evidence | packet injection, usb gadget | <https://github.com/V3rB0se/Alynx-nethunter-sunfish> |
| MrBadger183 | Developer claimed | No explicit boot evidence | external wifi support, packet injection, hid gadget, usb gadget | <https://github.com/MrBadger183/android_kernel_google_msm-4.14> |

### Google Pixel 4a 5G (`bramble`)
**Official NetHunter registry variants**

| ROM | Android | Kernel | Author | Source |
|---|---|---|---|---|
| Android 12L | twelve | 4.9 | Alynx | <https://github.com/V3rB0se/redbull> |

**Community projects**

| Project | Status | Boot evidence | Features claimed/tested | Source |
|---|---|---|---|---|
| Hotelk52339 | Developer claimed | No explicit boot evidence | internal wifi support, monitor mode, packet injection | <https://github.com/Hotelk52339/nethunter_kernel_google_redbull> |

### Google Pixel 6a (`bluejay-los`)
**Official NetHunter registry variants**

| ROM | Android | Kernel | Author | Source |
|---|---|---|---|---|
| LineageOS 23.2 (Android 16) | sixteen | 6.1 | RishiRats | <https://github.com/RishiRats/bluejay-kali_nethunter> |

### Google Pixel 7 (`panther`)
No official NetHunter registry variant.

**Community projects**

| Project | Status | Boot evidence | Features claimed/tested | Source |
|---|---|---|---|---|
| Werq4u8 | Unverified candidate | No explicit boot evidence | Unknown | <https://github.com/Werq4u8/Pixel-7-panther-kernel-nethunter-cp41.260831.007> |

### Google Pixel 9 Pro Fold (`comet`)
No official NetHunter registry variant.

**Community projects**

| Project | Status | Boot evidence | Features claimed/tested | Source |
|---|---|---|---|---|
| jdawg867 | Unverified candidate | No explicit boot evidence | Unknown | <https://github.com/jdawg867/nethunter-kernel> |

### Google Pixel 9 Pro XL (`komodo`)
No official NetHunter registry variant.

**Community projects**

| Project | Status | Boot evidence | Features claimed/tested | Source |
|---|---|---|---|---|
| maniaco13 | Unverified candidate | No explicit boot evidence | Unknown | <https://github.com/maniaco13/NH_kernel_pixel9proxl_komodo> |

### Google Pixel C (`dragon`)
**Official NetHunter registry variants**

| ROM | Android | Kernel | Author | Source |
|---|---|---|---|---|
| Android 7.1 | nougat | 3.18 | jcadduono | <https://github.com/jcadduono/android_kernel_google_chromeos.git> |

### Google/Huawei Nexus 6P (`angler`)
**Official NetHunter registry variants**

| ROM | Android | Kernel | Author | Source |
|---|---|---|---|---|
| Android 6 | marshmallow | 3.10 | Binkybear | <https://github.com/binkybear/AK-Angler.git> |
| Android 7.1 | nougat | 3.10 | jcadduono | <https://github.com/jcadduono/android_kernel_huawei_angler> |
| Android 8.1 | oreo | 3.10 | Re4son & yesimxev | <https://github.com/Re4son/android_kernel_huawei_angler> |
| LineageOS 17.1 & Pixel Experience 10 | ten | 3.10 | Re4son & yesimxev | <https://github.com/Re4son/android_kernel_huawei_angler_pixel> |

Search discoveries (metadata only, not inspected): 2. See `data/nethunter_search_candidates.csv`.

### Nexus 5 (`hammerhead`)
No official NetHunter registry variant.

**Community projects**

| Project | Status | Boot evidence | Features claimed/tested | Source |
|---|---|---|---|---|
| Qaran1 | Developer claimed | Unknown | monitor mode, packet injection | <https://github.com/qaran1/nexus5-kali-nethunter> |

### Nexus 7 (2012) (`grouper`)
No official NetHunter registry variant.

**Community projects**

| Project | Status | Boot evidence | Features claimed/tested | Source |
|---|---|---|---|---|
| Re4son | Abandoned | Unknown | Unknown | <https://github.com/re4son/android_kernel_asus_grouper_3.0> |

### Pixel 3a (`sargo`)
No official NetHunter registry variant.

**Community projects**

| Project | Status | Boot evidence | Features claimed/tested | Source |
|---|---|---|---|---|
| Nougat-User | Developer claimed | No explicit boot evidence | monitor mode, packet injection, hid gadget | <https://github.com/Nougat-User/sargo_nethunter> |

### Pixel 3a XL (`bonito`)
No official NetHunter registry variant.

**Community projects**

| Project | Status | Boot evidence | Features claimed/tested | Source |
|---|---|---|---|---|
| Nougat-User | Developer claimed | No explicit boot evidence | monitor mode, packet injection, hid gadget | <https://github.com/Nougat-User/sargo_nethunter> |

### Pixel 4 (`flame`)
No official NetHunter registry variant.

**Community projects**

| Project | Status | Boot evidence | Features claimed/tested | Source |
|---|---|---|---|---|
| cyberknight777 | Unverified candidate | No explicit boot evidence | Unknown | <https://github.com/cyberknight777/nethunter_kernel_google_floral> |

### Pixel 5 (`redfin`)
No official NetHunter registry variant.

**Community projects**

| Project | Status | Boot evidence | Features claimed/tested | Source |
|---|---|---|---|---|
| Fak3adm1n | Unverified candidate | No explicit boot evidence | Unknown | <https://github.com/Fak3adm1n/Build-Nethunter-kernel-for-redfin> |

### Pixel 6 Pro (`raven`)
No official NetHunter registry variant.

**Community projects**

| Project | Status | Boot evidence | Features claimed/tested | Source |
|---|---|---|---|---|
| ahksoft | Unverified candidate | No explicit boot evidence | Unknown | <https://github.com/ahksoft/Pixel6Pro-Nethunter> |

### Pixel 6a (`bluejay`)
No official NetHunter registry variant.

**Community projects**

| Project | Status | Boot evidence | Features claimed/tested | Source |
|---|---|---|---|---|
| Ashabil | Unverified candidate | No explicit boot evidence | Unknown | <https://github.com/Ashabil/kernel-bluejay> |

### Pixel 7a (`lynx`)
No official NetHunter registry variant.

**Community projects**

| Project | Status | Boot evidence | Features claimed/tested | Source |
|---|---|---|---|---|
| HeRrKrUgEr | Unverified candidate | No explicit boot evidence | hid gadget | <https://github.com/HeRrKrUgEr/nethunter-kernel-lynx> |

### Pixel 8 (`shiba`)
No official NetHunter registry variant.

**Community projects**

| Project | Status | Boot evidence | Features claimed/tested | Source |
|---|---|---|---|---|
| Trijal08 | Unverified candidate | No explicit boot evidence | Unknown | <https://github.com/Trijal08/dragon_device_google_shusky-kernels_5.15> |

### Pixel 8 Pro (`husky`)
No official NetHunter registry variant.

**Community projects**

| Project | Status | Boot evidence | Features claimed/tested | Source |
|---|---|---|---|---|
| Trijal08 | Unverified candidate | No explicit boot evidence | Unknown | <https://github.com/Trijal08/dragon_device_google_shusky-kernels_5.15> |

### Pixel 9 Pro (`caiman`)
No official NetHunter registry variant.

**Community projects**

| Project | Status | Boot evidence | Features claimed/tested | Source |
|---|---|---|---|---|
| shemed-mwangome | Developer claimed | No explicit boot evidence | monitor mode, hid gadget | <https://github.com/shemed-mwangome/nethunter-komodo-usbwifi> |

### Pixel 9 Pro XL (`komodo`)
No official NetHunter registry variant.

**Community projects**

| Project | Status | Boot evidence | Features claimed/tested | Source |
|---|---|---|---|---|
| shemed-mwangome | Developer claimed | No explicit boot evidence | monitor mode, hid gadget | <https://github.com/shemed-mwangome/nethunter-komodo-usbwifi> |

### Pixel 9a (`tegu`)
No official NetHunter registry variant.

**Community projects**

| Project | Status | Boot evidence | Features claimed/tested | Source |
|---|---|---|---|---|
| GPTmadeit | Developer claimed | No explicit boot evidence | internal wifi support, monitor mode, packet injection | <https://github.com/GPTmadeit/nethunter-pixel9a-rt2800usb> |
| Flofy-Dev | Unverified candidate | No explicit boot evidence | Unknown | <https://github.com/Flofy-Dev/Pixel_9a_nethunter_kernel> |

### Pixel XL (`marlin`)
No official NetHunter registry variant.

**Community projects**

| Project | Status | Boot evidence | Features claimed/tested | Source |
|---|---|---|---|---|
| Kernels-by-ravindu644 | Unverified candidate | No explicit boot evidence | Unknown | <https://github.com/Kernels-by-ravindu644/google_kernel_marlin_nethunter> |


## HTC
Devices/codenames: 4. Official variants: 3. Community projects: 1.
### HTC 10 (`htc-pmewl`)
**Official NetHunter registry variants**

| ROM | Android | Kernel | Author | Source |
|---|---|---|---|---|
| HTC 10 Sense 8.0 | marshmallow | 3.18 | S1CAR1US | <https://github.com/S1CAR1US/nethunter_kernel_htc_pmewl.git> |

### HTC One M7 (`onem7gpe`)
**Official NetHunter registry variants**

| ROM | Android | Kernel | Author | Source |
|---|---|---|---|---|
| Google Play Edition 5.1 | lollipop | 3.04 | Lavanoid | <https://github.com/lavanoid/android_kernel_htc_m7gpe> |

### HTC One M8 (`htc-m8`)
No official NetHunter registry variant.

**Community projects**

| Project | Status | Boot evidence | Features claimed/tested | Source |
|---|---|---|---|---|
| darobbe | Abandoned | No explicit boot evidence | Unknown | <https://github.com/darobbe/AnyKernel2-nethunter-Htc-m8> |

### HTC One M8 (`onem8gpe`)
**Official NetHunter registry variants**

| ROM | Android | Kernel | Author | Source |
|---|---|---|---|---|
| Google Play Edition 6 | marshmallow | 3.04 | Lavanoid | <https://github.com/lavanoid/android_kernel_htc_m8gpe> |


## Honor
Devices/codenames: 1. Official variants: 0. Community projects: 1.
### Honor 9 Lite (`hi6250`)
No official NetHunter registry variant.

**Community projects**

| Project | Status | Boot evidence | Features claimed/tested | Source |
|---|---|---|---|---|
| mr-anjaneyam | Developer claimed | No explicit boot evidence | monitor mode, packet injection, hid gadget, usb gadget | <https://github.com/mr-anjaneyam/nethunter-kernel-honor-9-lite> |


## Huawei
Devices/codenames: 3. Official variants: 7. Community projects: 0.
### Huawei Honor 5x (`kiwi`)
**Official NetHunter registry variants**

| ROM | Android | Kernel | Author | Source |
|---|---|---|---|---|
| CyanogenMod 13 | marshmallow | 3.10 | DeadSquirrel01 | <https://github.com/DeadSquirrel01/android_kernel_huawei_kiwi.git> |

### Huawei P9 (`eva`)
**Official NetHunter registry variants**

| ROM | Android | Kernel | Author | Source |
|---|---|---|---|---|
| EMUI | oreo | 4.04 | vvvbbbcz | <https://gitlab.com/vvvbbbcz/android_kernel_huawei_hi3650.git> |
| LineageOS 16.0 | pie | 4.04 | vvvbbbcz | <https://gitlab.com/vvvbbbcz/android_kernel_huawei_hi3650.git> |
| EMUI8/LineageOS16 | oreo | 4.04 | apk0mix5900 | <https://github.com/apk0mix5900/android_kernel_huawei_hi3650> |

### Huawei P9 Plus (`vienna`)
**Official NetHunter registry variants**

| ROM | Android | Kernel | Author | Source |
|---|---|---|---|---|
| MIUI 8 | marshmallow | 4.04 | 5h4d0wb0y | <https://github.com/5h4d0wb0y/android_kernel_huawei_vienna.git> |
| MIUI 9 | nougat | 4.04 | 5h4d0wb0y | <https://github.com/5h4d0wb0y/android_kernel_huawei_vienna.git> |
| MIUI 10 | oreo | 4.04 | 5h4d0wb0y | <https://github.com/5h4d0wb0y/android_kernel_huawei_vienna.git> |


## LG
Devices/codenames: 16. Official variants: 10. Community projects: 12.
### G4 (International) (`h815`)
No official NetHunter registry variant.

**Community projects**

| Project | Status | Boot evidence | Features claimed/tested | Source |
|---|---|---|---|---|
| nepheloid | Unverified candidate | No explicit boot evidence | Unknown | <https://github.com/nepheloid/nethunter_kernel_g4> |

### LG G2 (AT&T) (`d800`)
No official NetHunter registry variant.

**Community projects**

| Project | Status | Boot evidence | Features claimed/tested | Source |
|---|---|---|---|---|
| cmjester6421 | Developer claimed | Unknown | Unknown | <https://github.com/cmjester6421/kali_nethunter_lgg2> |

### LG G2 (Canada) (`d803`)
No official NetHunter registry variant.

**Community projects**

| Project | Status | Boot evidence | Features claimed/tested | Source |
|---|---|---|---|---|
| cmjester6421 | Developer claimed | Unknown | Unknown | <https://github.com/cmjester6421/kali_nethunter_lgg2> |

### LG G2 (International) (`d802`)
No official NetHunter registry variant.

**Community projects**

| Project | Status | Boot evidence | Features claimed/tested | Source |
|---|---|---|---|---|
| cmjester6421 | Developer claimed | Unknown | Unknown | <https://github.com/cmjester6421/kali_nethunter_lgg2> |

### LG G2 (Korea) (`f320`)
No official NetHunter registry variant.

**Community projects**

| Project | Status | Boot evidence | Features claimed/tested | Source |
|---|---|---|---|---|
| cmjester6421 | Developer claimed | Unknown | Unknown | <https://github.com/cmjester6421/kali_nethunter_lgg2> |

### LG G2 (Sprint) (`ls980`)
No official NetHunter registry variant.

**Community projects**

| Project | Status | Boot evidence | Features claimed/tested | Source |
|---|---|---|---|---|
| cmjester6421 | Developer claimed | Unknown | Unknown | <https://github.com/cmjester6421/kali_nethunter_lgg2> |

### LG G2 (T-Mobile) (`d801`)
No official NetHunter registry variant.

**Community projects**

| Project | Status | Boot evidence | Features claimed/tested | Source |
|---|---|---|---|---|
| cmjester6421 | Developer claimed | Unknown | Unknown | <https://github.com/cmjester6421/kali_nethunter_lgg2> |

### LG G2 (Verizon) (`vs980`)
No official NetHunter registry variant.

**Community projects**

| Project | Status | Boot evidence | Features claimed/tested | Source |
|---|---|---|---|---|
| cmjester6421 | Developer claimed | Unknown | Unknown | <https://github.com/cmjester6421/kali_nethunter_lgg2> |

### LG G5 (International) (`h850`)
**Official NetHunter registry variants**

| ROM | Android | Kernel | Author | Source |
|---|---|---|---|---|
| Android 7.1 (T-Online) | nougat | 3.18 | jcadduono | <https://github.com/jcadduono/android_kernel_lge_msm8996.git> |

### LG G5 (T-Mobile) (`h830`)
**Official NetHunter registry variants**

| ROM | Android | Kernel | Author | Source |
|---|---|---|---|---|
| Android 7.1 (T-Online) | nougat | 3.18 | jcadduono | <https://github.com/jcadduono/android_kernel_lge_msm8996.git> |

### LG K10 (`m216`)
No official NetHunter registry variant.

**Community projects**

| Project | Status | Boot evidence | Features claimed/tested | Source |
|---|---|---|---|---|
| AbdoTCH | Developer claimed | Unknown | external wifi support, monitor mode, packet injection, hid gadget | <https://github.com/abdotch/nethunter-kernel-for-lg-k10-m216-> |

### LG K20 Plus (`lv517`)
**Official NetHunter registry variants**

| ROM | Android | Kernel | Author | Source |
|---|---|---|---|---|
| LineageOS 14.1 | nougat | 3.18 | robnew | <https://github.com/robnew/NetHunter_K20plus_arm64_Kernel.git> |

**Community projects**

| Project | Status | Boot evidence | Features claimed/tested | Source |
|---|---|---|---|---|
| robnew | Developer claimed | Unknown | packet injection, hid gadget | <https://github.com/robnew/nethunter_k20plus_kernel> |
| Keskebeu | Developer claimed | Unknown | Unknown | <https://github.com/keskebeu/lgk20plus_pentest_hack> |

Search discoveries (metadata only, not inspected): 1. See `data/nethunter_search_candidates.csv`.

### LG V20 (`us996`)
**Official NetHunter registry variants**

| ROM | Android | Kernel | Author | Source |
|---|---|---|---|---|
| Android 7.0 | nougat | 3.18 | jcadduono | <https://github.com/jcadduono/android_kernel_lge_msm8996> |

### LG V20 (International) (`h990`)
**Official NetHunter registry variants**

| ROM | Android | Kernel | Author | Source |
|---|---|---|---|---|
| Android 7.1 with dirtysanta patch | nougat | 3.18 | Re4son | <https://github.com/Re4son/android_kernel_lge_msm8996> |
| Android 8 | oreo | 3.18 | Re4son | <https://github.com/Re4son/android_kernel_lg_h990> |
| LineageOS 18.1 | eleven | 3.18 | yesimxev | <https://github.com/yesimxev/android_kernel_lge_msm8996> |
| LineageOS 19.1 | twelve | 4.04 | yesimxev | <https://github.com/yesimxev/android_kernel_lge_msm8996> |
| LineageOS 21 | fourteen | 4.04 | yesimxev | <https://github.com/yesimxev/android_kernel_lge_msm8996> |

### LG V20 (T-Mobile) (`h918`)
**Official NetHunter registry variants**

| ROM | Android | Kernel | Author | Source |
|---|---|---|---|---|
| Android 7.0 | nougat | 3.18 | jcadduono | <https://github.com/jcadduono/android_kernel_lge_msm8996.git> |

### LG V30+ (`h930ds`)
No official NetHunter registry variant.

**Community projects**

| Project | Status | Boot evidence | Features claimed/tested | Source |
|---|---|---|---|---|
| SrDayne | Unverified candidate | No explicit boot evidence | Unknown | <https://github.com/SrDayne/lge_msm8998_h930ds> |


## LeEco
Devices/codenames: 2. Official variants: 1. Community projects: 2.
### LeEco Le 2 (`s2`)
**Official NetHunter registry variants**

| ROM | Android | Kernel | Author | Source |
|---|---|---|---|---|
| CyanogenMod 14.1 | nougat | 3.10 | Rishabh Rao | <https://github.com/nethunter-s2/android_kernel_leeco_s2.git> |

**Community projects**

| Project | Status | Boot evidence | Features claimed/tested | Source |
|---|---|---|---|---|
| evost | Abandoned | Unknown | Unknown | <https://github.com/evost/android_kernel_leeco_msm8996_lineage_kali_nethunter> |

### LeEco Le Pro3 (`zl1`)
No official NetHunter registry variant.

**Community projects**

| Project | Status | Boot evidence | Features claimed/tested | Source |
|---|---|---|---|---|
| evost | Abandoned | Unknown | Unknown | <https://github.com/evost/android_kernel_leeco_msm8996_lineage_kali_nethunter> |


## Lenovo
Devices/codenames: 2. Official variants: 1. Community projects: 1.
### Lenovo K8 Note (`manning`)
**Official NetHunter registry variants**

| ROM | Android | Kernel | Author | Source |
|---|---|---|---|---|
| Android 7.1 | nougat | 3.18 | Byom Dwivedi | <https://github.com/MotorolaMobilityLLC/kernel-mtk.git> |

### Lenovo Tab4 10 (`tbx304`)
No official NetHunter registry variant.

**Community projects**

| Project | Status | Boot evidence | Features claimed/tested | Source |
|---|---|---|---|---|
| Neternels | Developer claimed | Unknown | Unknown | <https://github.com/neternels/android_kernel_lenovo_tbx304-neternels> |


## Motorola
Devices/codenames: 16. Official variants: 11. Community projects: 15.
### Moto G (2013) (`falcon`)
No official NetHunter registry variant.

**Community projects**

| Project | Status | Boot evidence | Features claimed/tested | Source |
|---|---|---|---|---|
| theindicator | Unverified candidate | No explicit boot evidence | Unknown | <https://github.com/theindicator/NETHUNTER-for-falcon> |

### Moto G 5G Plus / Motorola One 5G (`nairo`)
No official NetHunter registry variant.

**Community projects**

| Project | Status | Boot evidence | Features claimed/tested | Source |
|---|---|---|---|---|
| joenyr | Unverified candidate | No explicit boot evidence | Unknown | <https://github.com/joenyr/nethunterkernel-nairo> |

### Moto G Stylus 5G (2022) / Edge 30 Fusion (`milanf`)
**Official NetHunter registry variants**

| ROM | Android | Kernel | Author | Source |
|---|---|---|---|---|
| LineageOS 23.2 (Android 16) | sixteen | 5.4.302 | TigerClips1 | <https://github.com/TigerClips1/kali-nethunter-milanf-kernel> |

**Community projects**

| Project | Status | Boot evidence | Features claimed/tested | Source |
|---|---|---|---|---|
| Madara273 | Unverified candidate | No explicit boot evidence | Unknown | <https://github.com/Madara273/Karui-NetHunter-Kernel-SM7325> |
| TigerClips1 | Unverified candidate | No explicit boot evidence | Unknown | <https://github.com/TigerClips1/kali-nethunter-milanf-kernel> |
| xthecreator | Unverified candidate | No explicit boot evidence | Unknown | <https://github.com/xthecreator/milanf-nethunter-kernel> |
| matthewrackley | Developer claimed | Unknown | Unknown | <https://github.com/matthewrackley/moto-g-stylus-2022_kali-nh> |

Search discoveries (metadata only, not inspected): 1. See `data/nethunter_search_candidates.csv`.

### Moto G8 (`rav`)
No official NetHunter registry variant.

**Community projects**

| Project | Status | Boot evidence | Features claimed/tested | Source |
|---|---|---|---|---|
| Hir43th | Developer claimed | Unknown | hid gadget | <https://github.com/hir43th/oficial-kernel-kali-nethunter-para-moto-g8-rav-sofiar> |

### Moto G8 Plus (`doha`)
No official NetHunter registry variant.

**Community projects**

| Project | Status | Boot evidence | Features claimed/tested | Source |
|---|---|---|---|---|
| harshmukhija699-hash | Developer claimed | Unknown | external wifi support, monitor mode, packet injection, hid gadget | <https://github.com/harshmukhija699-hash/android_kernel_motorola_doha_nethunter> |

### Moto G8 Power (`sofiar`)
No official NetHunter registry variant.

**Community projects**

| Project | Status | Boot evidence | Features claimed/tested | Source |
|---|---|---|---|---|
| Hir43th | Developer claimed | Unknown | hid gadget | <https://github.com/hir43th/oficial-kernel-kali-nethunter-para-moto-g8-rav-sofiar> |

### Moto G82 5G (`rhodep`)
No official NetHunter registry variant.

**Community projects**

| Project | Status | Boot evidence | Features claimed/tested | Source |
|---|---|---|---|---|
| d4rks1d33 | Developer claimed | Unknown | hid gadget | <https://github.com/d4rks1d33/moto-g82-kali-nethunter-custom-kernel> |

### Moto One Action (`troika`)
No official NetHunter registry variant.

**Community projects**

| Project | Status | Boot evidence | Features claimed/tested | Source |
|---|---|---|---|---|
| secpromise-netizen | Developer claimed | Unknown | Unknown | <https://github.com/secpromise-netizen/android_kernel_nethunter_troika> |

### Moto Z (`griffin`)
No official NetHunter registry variant.

**Community projects**

| Project | Status | Boot evidence | Features claimed/tested | Source |
|---|---|---|---|---|
| AbdullahGok | Abandoned | Unknown | Unknown | <https://github.com/abdullahgok/tubichu-z-kernel> |

### Motorola Moto G 2015 (`osprey`)
**Official NetHunter registry variants**

| ROM | Android | Kernel | Author | Source |
|---|---|---|---|---|
| LineageOS 14.1 | nougat | 3.10 | rajeshdubey293 | <https://github.com/rajeshdubey293/kernel_osprey-cm-14.1> |
| LineageOS 15.1 | oreo | 3.10 | rajeshdubey293 | <https://github.com/rajeshdubey293/kernel_osprey-oreo> |

### Motorola Moto G5 (`cedric`)
**Official NetHunter registry variants**

| ROM | Android | Kernel | Author | Source |
|---|---|---|---|---|
| LineageOS 14.1 | nougat | 3.18 | rajeshdubey293 | <https://github.com/rajeshdubey293/android_kernel_motorola_msm8937> |
| LineageOS 15.1 | oreo | 3.18 | rajeshdubey293 | <https://github.com/rajeshdubey293/al-ice_cedric.git> |

### Motorola Moto G5 Plus (`potter`)
**Official NetHunter registry variants**

| ROM | Android | Kernel | Author | Source |
|---|---|---|---|---|
| LineageOS 14.1 | nougat | 3.18 | chankruze | <https://github.com/chankruze/potter_kali_kernel> |
| LineageOS 16 | pie | 3.18 | rajeshdubey293 | <https://github.com/rajeshdubey293/Optimus_Drunk_Potter.git> |

**Community projects**

| Project | Status | Boot evidence | Features claimed/tested | Source |
|---|---|---|---|---|
| CarlosRgoku | Unverified candidate | No explicit boot evidence | Unknown | <https://github.com/CarlosRgoku/Nethunter-Kernel-potter> |

### Motorola Moto G6 (`evert`)
No official NetHunter registry variant.

**Community projects**

| Project | Status | Boot evidence | Features claimed/tested | Source |
|---|---|---|---|---|
| mapachesantander | Abandoned | No explicit boot evidence | Unknown | <https://github.com/mapachesantander/Unofficial-Nethunter-Kernel-Evert> |

### Motorola Moto G8 Power (`sofiar`)
No official NetHunter registry variant.

**Community projects**

| Project | Status | Boot evidence | Features claimed/tested | Source |
|---|---|---|---|---|
| brunodzogovic | Unverified candidate | No explicit boot evidence | Unknown | <https://github.com/brunodzogovic/kali-nethunter-kernel-motorola-sofiar> |

### Motorola Moto X2 (2014) (`victara`)
**Official NetHunter registry variants**

| ROM | Android | Kernel | Author | Source |
|---|---|---|---|---|
| CyanogenMod 14.1 | nougat | 3.04 | DSR! | <https://github.com/xchwarze/nethunter-motorola-x2-kernel> |

### Motorola Moto X4 (`payton`)
**Official NetHunter registry variants**

| ROM | Android | Kernel | Author | Source |
|---|---|---|---|---|
| LineageOS 17.1 | ten | 4.4 | ciropom | <https://github.com/ciropom/android_nethunter_kernel_motorola_msm8998.git> |
| LineageOS 20 | thirteen | 4.4 | yesimxev | <https://github.com/yesimxev/android_kernel_motorola_msm8998> |
| LineageOS 22.2 | fifteen | 4.4 | yesimxev | <https://github.com/yesimxev/android_kernel_motorola_msm8998> |


## Nokia
Devices/codenames: 3. Official variants: 8. Community projects: 0.
### Nokia 3.1 (`es2`)
**Official NetHunter registry variants**

| ROM | Android | Kernel | Author | Source |
|---|---|---|---|---|
| Android 9.0 | pie | 3.18 | yesimxev | <https://github.com/yesimxev/android_kernel_nokia_es2.git> |

Search discoveries (metadata only, not inspected): 1. See `data/nethunter_search_candidates.csv`.

### Nokia 6.1 (`pl2`)
**Official NetHunter registry variants**

| ROM | Android | Kernel | Author | Source |
|---|---|---|---|---|
| LineageOS 21 | ten | 4.4 | yesimxev | <https://github.com/yesimxev/android_kernel_nokia_sdm660> |
| LineageOS 18.1 | eleven | 4.4 | yesimxev | <https://github.com/yesimxev/android_kernel_nokia_sdm660> |
| LineageOS 20 | thirteen | 4.4 | yesimxev | <https://github.com/yesimxev/android_kernel_nokia_sdm660> |
| LineageOS 21 | fourteen | 4.4 | yesimxev | <https://github.com/yesimxev/android_kernel_nokia_sdm660> |

### Nokia 6.1 Plus (`drg`)
**Official NetHunter registry variants**

| ROM | Android | Kernel | Author | Source |
|---|---|---|---|---|
| LineageOS 18.1 | eleven | 4.4 | yesimxev | <https://github.com/yesimxev/android_kernel_nokia_sdm660> |
| LineageOS 20 | thirteen | 4.4 | yesimxev | <https://github.com/yesimxev/android_kernel_nokia_sdm660> |
| LineageOS 21 | fourteen | 4.4 | yesimxev | Unknown |


## Nothing
Devices/codenames: 2. Official variants: 3. Community projects: 3.
### Nothing Phone (1) (`spacewar`)
**Official NetHunter registry variants**

| ROM | Android | Kernel | Author | Source |
|---|---|---|---|---|
| AOSP/AOSPA Android 12 | twelve | 5.4 | kimocoder | <https://github.com/kimocoder/android_kernel_nothing_sm7325> |
| AOSP/AOSPA Android 13 | thirteen | 5.4 | kimocoder | <https://github.com/kimocoder/android_kernel_nothing_sm7325> |
| AOSP/AOSPA Android 14 | fourteen | 5.4 | kimocoder | <https://github.com/kimocoder/android_kernel_nothing_sm7325> |

**Community projects**

| Project | Status | Boot evidence | Features claimed/tested | Source |
|---|---|---|---|---|
| ilyamen | Developer claimed | No explicit boot evidence | internal wifi support, monitor mode, packet injection, hid gadget, usb gadget | <https://github.com/ilyamen/nothing-phone-1-nethunter-kernel> |
| thw01f | Developer claimed | Developer-reported boot | internal wifi support, external wifi support, monitor mode, packet injection, hid gadget, usb gadget | <https://github.com/thw01f/nethunter-spacewar-kernel> |

Search discoveries (metadata only, not inspected): 2. See `data/nethunter_search_candidates.csv`.

### Nothing Phone (3a) / (3a) Pro (`asteroids`)
No official NetHunter registry variant.

**Community projects**

| Project | Status | Boot evidence | Features claimed/tested | Source |
|---|---|---|---|---|
| Tbeard602 | Unverified candidate | No explicit boot evidence | Unknown | <https://github.com/Tbeard602/nothing-phone-3a-nethunter> |


## Nubia
Devices/codenames: 2. Official variants: 0. Community projects: 2.
### Nubia Red Magic 7S Pro (`nx709s`)
No official NetHunter registry variant.

**Community projects**

| Project | Status | Boot evidence | Features claimed/tested | Source |
|---|---|---|---|---|
| piashmsu | Developer claimed | Unknown | external wifi support, hid gadget | <https://github.com/piashmsu/nubia-nx709s-kernel> |

### Red Magic 6S Pro (`nx669s`)
No official NetHunter registry variant.

**Community projects**

| Project | Status | Boot evidence | Features claimed/tested | Source |
|---|---|---|---|---|
| piashmsubd | Developer claimed | Unknown | external wifi support, monitor mode, hid gadget, usb gadget | <https://github.com/piashmsubd/android_kernel_nubia_nx669s_nethunter> |


## OPPO
Devices/codenames: 2. Official variants: 1. Community projects: 1.
### OPPO A37 (`a37`)
No official NetHunter registry variant.

**Community projects**

| Project | Status | Boot evidence | Features claimed/tested | Source |
|---|---|---|---|---|
| shifujowo | Unverified candidate | No explicit boot evidence | Unknown | <https://gitlab.com/shifujowo/nethunter-kernel-a37> |

### OPPO A37 (2016) (`a37`)
**Official NetHunter registry variants**

| ROM | Android | Kernel | Author | Source |
|---|---|---|---|---|
| LineageOS 17.1 | ten | 3.10 | diamant3 | <https://github.com/diamant3/kernel_oppo_A37f.git> |


## OnePlus
Devices/codenames: 33. Official variants: 46. Community projects: 34.
### 5 / 5T (`oneplus5`)
No official NetHunter registry variant.

**Community projects**

| Project | Status | Boot evidence | Features claimed/tested | Source |
|---|---|---|---|---|
| simonpunk | Unverified candidate | No explicit boot evidence | Unknown | <https://github.com/simonpunk/nethunter-apk-and-magisk-module> |

### 6 / 6T (`oneplus6`)
No official NetHunter registry variant.

**Community projects**

| Project | Status | Boot evidence | Features claimed/tested | Source |
|---|---|---|---|---|
| nuthan923 | Unverified candidate | No explicit boot evidence | Unknown | <https://github.com/nuthan923/NetHunter-Enchilada-Oneplus6> |

### Nord 4 (`avalon`)
No official NetHunter registry variant.

**Community projects**

| Project | Status | Boot evidence | Features claimed/tested | Source |
|---|---|---|---|---|
| ruik3z | Developer claimed | No explicit boot evidence | external wifi support, usb gadget | <https://github.com/ruik3z/avalon-firmware> |

### OnePlus 11 5G (`salami`)
**Official NetHunter registry variants**

| ROM | Android | Kernel | Author | Source |
|---|---|---|---|---|
| OxygenOS 15 | fifteen | 5.15 | nullptr-t-oss | <https://github.com/nullptr-t-oss/EmberHeart_OnePlus11/releases/download/v1.5.12-r12/EmberHeart_boot.img> |
| OxygenOS 16 | sixteen | 5.15 | nullptr-t-oss | <https://github.com/nullptr-t-oss/EmberHeart_OnePlus11/releases/download/v2.0.0-r2/EmberHeart_boot.img> |

### OnePlus 11R (`oneplus-11r`)
No official NetHunter registry variant.

**Community projects**

| Project | Status | Boot evidence | Features claimed/tested | Source |
|---|---|---|---|---|
| docdry0001 | Developer claimed | Unknown | Unknown | <https://github.com/docdry0001/android_kernel_oneplus_11r> |

### OnePlus 15 (`Unknown`)
No official NetHunter registry variant.

**Community projects**

| Project | Status | Boot evidence | Features claimed/tested | Source |
|---|---|---|---|---|
| Aroichan | Unverified candidate | No explicit boot evidence | Unknown | <https://github.com/Aroichan/oneplus15-nethunter-kernel> |

### OnePlus 2 (`oneplus2`)
**Official NetHunter registry variants**

| ROM | Android | Kernel | Author | Source |
|---|---|---|---|---|
| OxygenOS 2 | lollipop | 3.10 | Binkybear | <https://github.com/binkybear/android_kernel_oneplus_msm8994.git> |
| OxygenOS 3 | marshmallow | 3.10 | Binkybear | <https://github.com/binkybear/android_kernel_oneplus_msm8994.git> |
| CyanogenMod 12.1 | lollipop | 3.10 | Binkybear | <https://github.com/binkybear/android_kernel_oneplus_msm8994.git> |
| CyanogenMod 13.0 | marshmallow | 3.10 | Binkybear | <https://github.com/binkybear/android_kernel_oneplus_msm8994.git> |
| LineageOS 14.1 | nougat | 3.10 | Re4son | <https://github.com/Re4son/android_kernel_oneplus_msm8994.git> |
| LineageOS 15.1 | oreo | 3.10 | Re4son | <https://github.com/Re4son/android_kernel_oneplus_msm8994.git> |
| LineageOS 16.0 | pie | 3.10 | Re4son | <https://github.com/Re4son/android_kernel_oneplus_msm8994.git> |

### OnePlus 3 / 3T (`oneplus3`)
**Official NetHunter registry variants**

| ROM | Android | Kernel | Author | Source |
|---|---|---|---|---|
| OxygenOS 9.0 | pie | 3.18 | Re4son | <https://github.com/re4son/android_kernel_oneplus_msm8996.git> |
| LineageOS 17.1 | ten | 3.18 | Re4son | <https://github.com/re4son/android_kerLoukious/nethunter_kernel_oneplus_sdm845nel_oneplus_msm8996_lineageos.git> |
| OxygenOS 4 | nougat | 3.18 | zanezam | <https://github.com/zanezam/boeffla-kernel-oos-oneplus3.git> |
| OxygenOS 3 | marshmallow | 3.18 | Binkybear | <https://github.com/binkybear/android_kernel_oneplus_msm8996.git> |
| OxygenOS | nougat | 3.18 | jcadduono | <https://github.com/jcadduono/android_kernel_oneplus_msm8996.git> |
| LineageOS | nougat | 3.18 | zanezam | <https://github.com/zanezam/boeffla-kernel-cm-oneplus3.git> |
| LineageOS 14 | nougat | 3.18 | zanezam | <https://github.com/zanezam/boeffla-kernel-cm-oneplus3.git> |
| LineageOS 15.1 | oreo | 3.18 | flypatriot | <https://github.com/flypatriot/boeffla-kernel-los-nethunter-oneplus3T.git> |
| OxygenOS 4 | nougat | 3.18 | zanezam | <https://github.com/zanezam/boeffla-kernel-oos-oneplus3.git> |

### OnePlus 5 / 5T (`cheeseburger/dumpling`)
No official NetHunter registry variant.

**Community projects**

| Project | Status | Boot evidence | Features claimed/tested | Source |
|---|---|---|---|---|
| prodject | Abandoned | No explicit boot evidence | Unknown | <https://github.com/prodject/OP5_Nethunter_kernel> |

### OnePlus 5 / 5T (`oneplus5`)
**Official NetHunter registry variants**

| ROM | Android | Kernel | Author | Source |
|---|---|---|---|---|
| OxygenOS 4 | nougat | 4.04 | Binkybear | <https://github.com/nethunteros/android_kernel_oneplus_msm8998> |
| CyanogenMod 14 | nougat | 4.04 | Binkybear | <https://github.com/nethunteros/android_kernel_oneplus_msm8998> |
| LineageOS 22.2 | fifteen | 4.04 | seppzer0 | <https://github.com/seppzer0/zero-kernel> |
| LineageOS 22.2 | fifteen | 4.04 | seppzer0 | <https://github.com/seppzer0/zero-kernel> |

Search discoveries (metadata only, not inspected): 1. See `data/nethunter_search_candidates.csv`.

### OnePlus 6 (`enchilada`)
No official NetHunter registry variant.

**Community projects**

| Project | Status | Boot evidence | Features claimed/tested | Source |
|---|---|---|---|---|
| cdizzle97 | Abandoned | No explicit boot evidence | Unknown | <https://github.com/cdizzle97/enchilada-nethunter> |
| sm0k3y13 | Developer claimed | Unknown | Unknown | <https://github.com/sm0k3y13/oneplus-6-nethunter-kernel> |

### OnePlus 6 / 6T (`enchilada/fajita`)
No official NetHunter registry variant.

**Community projects**

| Project | Status | Boot evidence | Features claimed/tested | Source |
|---|---|---|---|---|
| johanlike | Unverified candidate | No explicit boot evidence | Unknown | <https://github.com/johanlike/DJY-Oneplus6-or-Oneplus6T-Nethunter-Andrax-Kernel> |
| johanlike | Unverified candidate | No explicit boot evidence | Unknown | <https://github.com/johanlike/DJY-Nethunter-Andrax-Kernel-Source> |
| acai66 | Unverified candidate | No explicit boot evidence | packet injection | <https://github.com/acai66/Acai-Oneplus6-or-Oneplus6T-Nethunter-Kernel> |
| acai66 | Unverified candidate | No explicit boot evidence | Unknown | <https://github.com/acai66/op6-op6t-nethunter-kernel> |

### OnePlus 6 / 6T (`oneplus6`)
**Official NetHunter registry variants**

| ROM | Android | Kernel | Author | Source |
|---|---|---|---|---|
| OxygenOS 10 | ten | 4.09 | kimocoder | <https://github.com/kimocoder/DJY-Nethunter-Andrax-Kernel-Source> |
| OxygenOS 11 | eleven | 4.09 | kimocoder | <https://github.com/kimocoder/android_kernel_oneplus6> |
| LineageOS 19.1 | twelve | 4.09 | kimocoder | <https://github.com/kimocoder/android_kernel_oneplus6> |
| LineageOS 22.2 | fifteen | 4.09 | kimocoder & Loukious | <https://github.com/Loukious/nethunter_kernel_oneplus_sdm845> |

### OnePlus 6T (`fajita`)
No official NetHunter registry variant.

**Community projects**

| Project | Status | Boot evidence | Features claimed/tested | Source |
|---|---|---|---|---|
| autisoid | Developer claimed | Unknown | Unknown | <https://github.com/autisoid/oneplus_fajita_qualcomm_sdm845_qcacld_injection> |
| hahawhoha187-a11y | Developer claimed | Unknown | Unknown | <https://github.com/hahawhoha187-a11y/nethunter6t> |

### OnePlus 7 (`guacamoleb`)
No official NetHunter registry variant.

**Community projects**

| Project | Status | Boot evidence | Features claimed/tested | Source |
|---|---|---|---|---|
| rahulrahuu678-ops | Unverified candidate | No explicit boot evidence | Unknown | <https://github.com/rahulrahuu678-ops/Kali-nethunter-kernel-for-OnePlus-7-GM1901> |

### OnePlus 7 / 7 Pro / 7T / 7T Pro (`oneplus7`)
**Official NetHunter registry variants**

| ROM | Android | Kernel | Author | Source |
|---|---|---|---|---|
| OxygenOS 9 | pie | 4.14 | Re4son | <https://github.com/Re4son/android_kernel_oneplus_sm8150> |
| OxygenOS 10 | ten | 4.14 | Re4son & yesimxev | <https://github.com/Re4son/android_kernel_oneplus_sm8150_draco> |
| OxygenOS 11 | eleven | 4.14 | kimocoder | <https://github.com/kimocoder/nethunter_kernel_oneplus7> |
| OxygenOS 11 | eleven | 4.14 | cyberknight777 | Unknown |
| LineageOS 23.2 | sixteen | 4.14 | v0lk3n | <https://github.com/V0lk3n/nethunter_kernel_oneplus_sm8150.git> |

### OnePlus 7T Pro (`hotdog`)
No official NetHunter registry variant.

**Community projects**

| Project | Status | Boot evidence | Features claimed/tested | Source |
|---|---|---|---|---|
| jaisummagithub | Developer claimed | Unknown | monitor mode, packet injection, hid gadget | <https://github.com/jaisummagithub/oneplus-7t-pro-lineageos-nethunter> |

### OnePlus 8 (`instantnoodle`)
No official NetHunter registry variant.

**Community projects**

| Project | Status | Boot evidence | Features claimed/tested | Source |
|---|---|---|---|---|
| Neternels | Developer claimed | Unknown | Unknown | <https://github.com/neternels/android_kernel_oneplus_sm8250> |

### OnePlus 8 / 8T / 8 Pro (`oneplus8`)
**Official NetHunter registry variants**

| ROM | Android | Kernel | Author | Source |
|---|---|---|---|---|
| OxygenOS 11 / Custom A11 | eleven | 4.19 | flyP@TR!0T | <https://github.com/flypatriot/neutrino_kernel_oneplus_sm8250.git> |
| OxygenOS 12 / Custom A12 | twelve | 4.19 | flyP@TR!0T | <https://github.com/flypatriot/crdroid_12_kernel.git> |

### OnePlus 8 Pro (`instantnoodlep`)
No official NetHunter registry variant.

**Community projects**

| Project | Status | Boot evidence | Features claimed/tested | Source |
|---|---|---|---|---|
| Neternels | Developer claimed | Unknown | Unknown | <https://github.com/neternels/android_kernel_oneplus_sm8250> |

### OnePlus 8T (`kebab`)
No official NetHunter registry variant.

**Community projects**

| Project | Status | Boot evidence | Features claimed/tested | Source |
|---|---|---|---|---|
| alexparent062-bit | Unverified candidate | No explicit boot evidence | Unknown | <https://github.com/alexparent062-bit/kernel> |
| Mist3r-N0b0dy | Developer claimed | Developer-reported boot | external wifi support, monitor mode, packet injection, hid gadget, usb gadget | <https://github.com/Mist3r-N0b0dy/NetHunter_Kernel-OP8T-crDroid12-A16> |
| NickEngmann | Developer claimed | Unknown | external wifi support, monitor mode, packet injection | <https://github.com/nickengmann/kernel_oneplus_sm8250_nethunter> |
| app4rreplit-sys | Developer claimed | Unknown | Unknown | <https://github.com/app4rreplit-sys/oneplus8t-nethunter_kernel> |
| ViP3R-KERNELs | Developer claimed | Unknown | Unknown | <https://github.com/vip3r-kernels/kernel_oneplus_sm8250> |
| minhtftvn | Developer claimed | Unknown | Unknown | <https://github.com/minhtftvn/kebab-nethunter-kernel-a12> |

### OnePlus 9 / 9 Pro (`lemonade`)
**Official NetHunter registry variants**

| ROM | Android | Kernel | Author | Source |
|---|---|---|---|---|
| LineageOS | sixteen | 5.4.302 | varakumar01 | <https://github.com/varakumar01/Levion_kernel_OP9> |

**Community projects**

| Project | Status | Boot evidence | Features claimed/tested | Source |
|---|---|---|---|---|
| hairenjun | Developer claimed | Unknown | hid gadget | <https://github.com/hairenjun/android_kernel_oneplus_sm8350-nethunteredition> |

### OnePlus 9R (`lemonades`)
No official NetHunter registry variant.

**Community projects**

| Project | Status | Boot evidence | Features claimed/tested | Source |
|---|---|---|---|---|
| srezvee-hue | Unverified candidate | No explicit boot evidence | Unknown | <https://github.com/srezvee-hue/oneplus9r-kernel-autobuild> |

### OnePlus Ace 6T (`Unknown`)
No official NetHunter registry variant.

**Community projects**

| Project | Status | Boot evidence | Features claimed/tested | Source |
|---|---|---|---|---|
| Muet-ahup | Unverified candidate | No explicit boot evidence | Unknown | <https://github.com/Muet-ahup/Ace6T-NetHunter-Kernel> |

### OnePlus Ace 6T (`ce6t`)
No official NetHunter registry variant.

**Community projects**

| Project | Status | Boot evidence | Features claimed/tested | Source |
|---|---|---|---|---|
| back475 | Unverified candidate | No explicit boot evidence | hid gadget, usb gadget | <https://github.com/back475/ce6t-nethunter-kernel> |

### OnePlus Nord (`oneplus-nord`)
**Official NetHunter registry variants**

| ROM | Android | Kernel | Author | Source |
|---|---|---|---|---|
| OxygenOS 11 | eleven | 4.19 | kimocoder | Unknown |
| OxygenOS 12 | twelve | 4.19 | kimocoder | Unknown |
| OxygenOS 16 | sixteen | 4.19 | kimocoder | Unknown |

### OnePlus Nord N10 5G (`billie`)
No official NetHunter registry variant.

**Community projects**

| Project | Status | Boot evidence | Features claimed/tested | Source |
|---|---|---|---|---|
| jose-dev-tools | Unverified candidate | No explicit boot evidence | Unknown | <https://github.com/jose-dev-tools/OnePlus-Nord-N10-Kali-NetHunter> |
| Lordwanggolf | Developer claimed | Unknown | Unknown | <https://github.com/lordwanggolf/android_kernel_nethunter_billie> |

### OnePlus Nord N200 5G (`dre`)
No official NetHunter registry variant.

**Community projects**

| Project | Status | Boot evidence | Features claimed/tested | Source |
|---|---|---|---|---|
| Retardog | Developer claimed | Unknown | Unknown | <https://github.com/retardog/nethunter_kernel_nord_ac2001> |

### OnePlus One (`oneplus1`)
**Official NetHunter registry variants**

| ROM | Android | Kernel | Author | Source |
|---|---|---|---|---|
| CyanogenMod 12.1 | lollipop | 3.04 | Binkybear | <https://github.com/binkybear/AK-OnePone.git> |
| CyanogenMod 13 | marshmallow | 3.04 | Binkybear | <https://github.com/binkybear/AK-OnePone.git> |
| CyanogenMod 14.1 | nougat | 3.04 | yesimxev | <https://github.com/yesimxev/android_kernel_oneplus_msm8974.git> |
| LineageOS 15.1 | oreo | 3.04 | yesimxev | <https://github.com/yesimxev/android_kernel_oppo_msm8974.git> |
| LineageOS 16 | pie | 3.04 | yesimxev | <https://github.com/yesimxev/android_kernel_oppo_msm8974.git> |
| LineageOS 17.1 | ten | 3.04 | yesimxev | <https://github.com/yesimxev/android_kernel_oppo_msm8974.git> |
| LineageOS 18.1 | eleven | 3.04 | yesimxev | <https://github.com/yesimxev/android_kernel_oppo_msm8974.git> |

Search discoveries (metadata only, not inspected): 1. See `data/nethunter_search_candidates.csv`.

### OnePlus X (`oneplusx`)
**Official NetHunter registry variants**

| ROM | Android | Kernel | Author | Source |
|---|---|---|---|---|
| CyanogenMod 13 | marshmallow | 3.04 | jcadduono | <https://github.com/jcadduono/nethunter_kernel_onyx.git> |

**Community projects**

| Project | Status | Boot evidence | Features claimed/tested | Source |
|---|---|---|---|---|
| lvlrt | Abandoned | No explicit boot evidence | Unknown | <https://github.com/lvlrt/nethunter_kernel_oneplusx_cm> |

### OnePlus-9Pro (`lemonadep`)
**Official NetHunter registry variants**

| ROM | Android | Kernel | Author | Source |
|---|---|---|---|---|
| Lineage | fifteen | 5.4.302 | Madara273 | <https://github.com/Madara273/Sakura_Kernel_OP9Pro> |

### Oneplus 2 (`oneplus2`)
No official NetHunter registry variant.

**Community projects**

| Project | Status | Boot evidence | Features claimed/tested | Source |
|---|---|---|---|---|
| xNNism | Abandoned | No explicit boot evidence | Unknown | <https://github.com/xNNism/aosp_nethunter-kernel_oneplus_msm8994> |

### Oneplus 5T (`dumpling`)
No official NetHunter registry variant.

**Community projects**

| Project | Status | Boot evidence | Features claimed/tested | Source |
|---|---|---|---|---|
| zeusricote | Developer claimed | No explicit boot evidence | internal wifi support, packet injection | <https://github.com/zeusricote/kernel-dumpling> |


## Realme
Devices/codenames: 9. Official variants: 5. Community projects: 5.
### Realme 5 / 5i / 5s (`rmx1911`)
**Official NetHunter registry variants**

| ROM | Android | Kernel | Author | Source |
|---|---|---|---|---|
| Corvus vS4.1-Eclipse | twelve | 4.14 | Mikhail Simon | <https://github.com/mikhailsimon/nethunter-r5x> |

### Realme 5 Pro (`rmx1971`)
**Official NetHunter registry variants**

| ROM | Android | Kernel | Author | Source |
|---|---|---|---|---|
| Android 12 | twelve | 4.9 | Alynx | <https://github.com/V3rB0se/Alynx-RMX1971> |

### Realme 5 Pro (`rmx1971-rui2`)
**Official NetHunter registry variants**

| ROM | Android | Kernel | Author | Source |
|---|---|---|---|---|
| Android 16 (RUI2) | sixteen | 4.9 | halfclub | <https://github.com/halfclub58/rmx1971_kernel.git> |

### Realme 6 / 6i / 7 (RM6785) (`rm6785`)
No official NetHunter registry variant.

**Community projects**

| Project | Status | Boot evidence | Features claimed/tested | Source |
|---|---|---|---|---|
| Kirito6785 | Abandoned | Unknown | Unknown | <https://github.com/kirito6785/kali-nethunter-kernel-for-only-rm6785-> |

### Realme 9 Pro 5G (`oscar`)
No official NetHunter registry variant.

**Community projects**

| Project | Status | Boot evidence | Features claimed/tested | Source |
|---|---|---|---|---|
| sirt-sirt | Unverified candidate | No explicit boot evidence | external wifi support, usb gadget | <https://github.com/sirt-sirt/oscar-nethunter-kernel> |

### Realme C15 Mediatek (`rmx2180`)
**Official NetHunter registry variants**

| ROM | Android | Kernel | Author | Source |
|---|---|---|---|---|
| LineageOS 17.1 | ten | 4.9 | Frostleaft07 | <https://github.com/Frostleaft07/android_kernel_realme_mt6765> |

Search discoveries (metadata only, not inspected): 1. See `data/nethunter_search_candidates.csv`.

### Realme C3 / Narzo 10A (`rmx2020`)
No official NetHunter registry variant.

**Community projects**

| Project | Status | Boot evidence | Features claimed/tested | Source |
|---|---|---|---|---|
| ShorterKing | Developer claimed | No explicit boot evidence | internal wifi support, external wifi support, packet injection, hid gadget, usb gadget | <https://github.com/ShorterKing/ShorterKing-Nethunter-Kernel-Realme-RMX2020-27> |
| Neternels | Developer claimed | Unknown | Unknown | <https://github.com/neternels/android_kernel_realme_rmx2020> |

### Realme X (`rmx1901`)
No official NetHunter registry variant.

**Community projects**

| Project | Status | Boot evidence | Features claimed/tested | Source |
|---|---|---|---|---|
| ishashanknigam | Developer claimed | No explicit boot evidence | internal wifi support, packet injection, usb gadget | <https://github.com/ishashanknigam/kernel-realme-RMX1901> |

### Realme X7 Max 5G (`rmx3031`)
**Official NetHunter registry variants**

| ROM | Android | Kernel | Author | Source |
|---|---|---|---|---|
| Android 13 and firmware F.13 and EX01 | thirteen | 4.19 | dek0der | <https://github.com/dek0der/kernel_realme_RMX3031> |


## Samsung
Devices/codenames: 88. Official variants: 80. Community projects: 74.
### Galaxy A13 4G (`a137f`)
No official NetHunter registry variant.

**Community projects**

| Project | Status | Boot evidence | Features claimed/tested | Source |
|---|---|---|---|---|
| yesimxev | Developer claimed | Unknown | Unknown | <https://github.com/yesimxev/android_kernel_samsung_a137> |
| ravindu644 | Abandoned | Unknown | Unknown | <https://github.com/ravindu644/android_kernel_nethunter_sm-a137f> |

### Galaxy A15 (`a15`)
No official NetHunter registry variant.

**Community projects**

| Project | Status | Boot evidence | Features claimed/tested | Source |
|---|---|---|---|---|
| spidlerman | Developer claimed | Unknown | Unknown | <https://github.com/spidlerman/nethunter_kernel_galaxya15> |

### Galaxy A22 5G (`a22x`)
No official NetHunter registry variant.

**Community projects**

| Project | Status | Boot evidence | Features claimed/tested | Source |
|---|---|---|---|---|
| beronathan9-sudo | Developer claimed | Unknown | hid gadget | <https://github.com/beronathan9-sudo/kernel_a225f_nethunter> |

### Galaxy A30s (`a30s`)
No official NetHunter registry variant.

**Community projects**

| Project | Status | Boot evidence | Features claimed/tested | Source |
|---|---|---|---|---|
| Skillar369 | Developer claimed | Unknown | Unknown | <https://github.com/skillar369/galaxy_a30s_nethunter_kernel> |

### Galaxy A5 (2017) (`a5y17lte`)
No official NetHunter registry variant.

**Community projects**

| Project | Status | Boot evidence | Features claimed/tested | Source |
|---|---|---|---|---|
| cycoslave | Unverified candidate | No explicit boot evidence | Unknown | <https://github.com/cycoslave/a5y17lte-kali-nethunter> |

### Galaxy A51 (`a51`)
No official NetHunter registry variant.

**Community projects**

| Project | Status | Boot evidence | Features claimed/tested | Source |
|---|---|---|---|---|
| leonidas20145 | Developer claimed | Unknown | Unknown | <https://github.com/leonidas20145/lancer-kernel-galaxy-a51-kernel> |
| ValentinStars | Developer claimed | Unknown | external wifi support, hid gadget | <https://github.com/valentinstars/vsthunterkernel> |

### Galaxy A52 (`a52q`)
No official NetHunter registry variant.

**Community projects**

| Project | Status | Boot evidence | Features claimed/tested | Source |
|---|---|---|---|---|
| AzeAstro | Developer claimed | Unknown | Unknown | <https://github.com/azeastro/samsung_kernel_sm7125> |

### Galaxy A52s 5G (`a52sxq`)
No official NetHunter registry variant.

**Community projects**

| Project | Status | Boot evidence | Features claimed/tested | Source |
|---|---|---|---|---|
| MarkWatney04 | Developer claimed | Unknown | Unknown | <https://github.com/markwatney04/nethunter_kernel_a52sxq_linageos_23.2> |

### Galaxy A71 (`a71`)
No official NetHunter registry variant.

**Community projects**

| Project | Status | Boot evidence | Features claimed/tested | Source |
|---|---|---|---|---|
| Nougat-User | Developer claimed | No explicit boot evidence | monitor mode, packet injection, hid gadget | <https://github.com/Nougat-User/a71_nethunter> |

### Galaxy A72 (`a72q`)
No official NetHunter registry variant.

**Community projects**

| Project | Status | Boot evidence | Features claimed/tested | Source |
|---|---|---|---|---|
| vakula2004 | Unverified candidate | No explicit boot evidence | Unknown | <https://gitlab.com/vakula2004/a72q-nethunter-kernel> |
| vakula2004 | Unverified candidate | No explicit boot evidence | Unknown | <https://github.com/vakula2004/kernel_a72q> |

### Galaxy A8 (2018) (`jackpotlte`)
No official NetHunter registry variant.

**Community projects**

| Project | Status | Boot evidence | Features claimed/tested | Source |
|---|---|---|---|---|
| younesilbcher | Developer claimed | Unknown | Unknown | <https://github.com/younesilbcher/a530f-nethunter-kernel> |

### Galaxy J6 (`j6lte`)
No official NetHunter registry variant.

**Community projects**

| Project | Status | Boot evidence | Features claimed/tested | Source |
|---|---|---|---|---|
| L4FeeR | Abandoned | No explicit boot evidence | Unknown | <https://github.com/L4FeeR/j6lte-nethunter-kernel> |

### Galaxy J7 (`j7elte`)
No official NetHunter registry variant.

**Community projects**

| Project | Status | Boot evidence | Features claimed/tested | Source |
|---|---|---|---|---|
| Anonymop1 | Unverified candidate | No explicit boot evidence | Unknown | <https://github.com/Anonymop1/j7xelte-nethunter-rom1> |
| Anonymop1 | Unverified candidate | No explicit boot evidence | Unknown | <https://github.com/Anonymop1/j7xelte-nethunter-rom> |

### Galaxy J7 Prime (`on7xelte`)
No official NetHunter registry variant.

**Community projects**

| Project | Status | Boot evidence | Features claimed/tested | Source |
|---|---|---|---|---|
| ahmadkhan-git | Developer claimed | Unknown | monitor mode, packet injection, hid gadget | <https://github.com/ahmadkhan-git/android_kernel_samsung_on7xelte> |

### Galaxy J8 (2018) (`j8y18lte`)
No official NetHunter registry variant.

**Community projects**

| Project | Status | Boot evidence | Features claimed/tested | Source |
|---|---|---|---|---|
| AbhishekTor55 | Abandoned | Unknown | Unknown | <https://github.com/abhishektor55/android_nethunter_kernel_samsung_j8y18lte> |

### Galaxy M11 (`m11q`)
No official NetHunter registry variant.

**Community projects**

| Project | Status | Boot evidence | Features claimed/tested | Source |
|---|---|---|---|---|
| areuhack | Developer claimed | Unknown | Unknown | <https://github.com/areuhack/nethunter_kernel_samsung_m11q> |

### Galaxy M12 (`m127f`)
No official NetHunter registry variant.

**Community projects**

| Project | Status | Boot evidence | Features claimed/tested | Source |
|---|---|---|---|---|
| why4m3 | Developer claimed | Unknown | external wifi support, monitor mode, packet injection, hid gadget | <https://github.com/why4m3/nethunter-kernel-m127f> |

### Galaxy M20 (`m20lte`)
No official NetHunter registry variant.

**Community projects**

| Project | Status | Boot evidence | Features claimed/tested | Source |
|---|---|---|---|---|
| muhanmed-aksu | Developer claimed | No explicit boot evidence | hid gadget, usb gadget | <https://github.com/muhanmed-aksu/samsung-m20-hid-kernel> |

### Galaxy M30s (`m30s`)
No official NetHunter registry variant.

**Community projects**

| Project | Status | Boot evidence | Features claimed/tested | Source |
|---|---|---|---|---|
| Payal-sys | Developer claimed | Unknown | Unknown | <https://github.com/payal-sys/m30s-nethunter-kernel> |

### Galaxy Note 10 Plus (Exynos) (`d2s`)
No official NetHunter registry variant.

**Community projects**

| Project | Status | Boot evidence | Features claimed/tested | Source |
|---|---|---|---|---|
| Tkpointz | Unverified candidate | No explicit boot evidence | Unknown | <https://github.com/Tkpointz/exynos9820-25_kernel> |

### Galaxy Note 4 (`treltexx`)
No official NetHunter registry variant.

**Community projects**

| Project | Status | Boot evidence | Features claimed/tested | Source |
|---|---|---|---|---|
| PhilZ-cwm6 | Unverified candidate | No explicit boot evidence | Unknown | <https://github.com/PhilZ-cwm6/nethunter_kernel_trlte> |

### Galaxy Note 4 (Qualcomm) (`trltexx`)
No official NetHunter registry variant.

**Community projects**

| Project | Status | Boot evidence | Features claimed/tested | Source |
|---|---|---|---|---|
| PhilZ-cwm6 | Unverified candidate | No explicit boot evidence | Unknown | <https://github.com/PhilZ-cwm6/nethunter_kernel_trlte> |

### Galaxy Note 9 (`crownlte`)
No official NetHunter registry variant.

**Community projects**

| Project | Status | Boot evidence | Features claimed/tested | Source |
|---|---|---|---|---|
| Tkpointz | Abandoned | No explicit boot evidence | Unknown | <https://github.com/Tkpointz/exynos9810_crownlte_kernel> |

### Galaxy Note Edge (`tblte`)
No official NetHunter registry variant.

**Community projects**

| Project | Status | Boot evidence | Features claimed/tested | Source |
|---|---|---|---|---|
| xNNism | Developer claimed | Unknown | Unknown | <https://github.com/xnnism/noteedge-nethunter_kernel> |

### Galaxy Note10 Lite (`r7`)
No official NetHunter registry variant.

**Community projects**

| Project | Status | Boot evidence | Features claimed/tested | Source |
|---|---|---|---|---|
| abusdeen1991 | Developer claimed | Unknown | Unknown | <https://github.com/abusdeen1991/note10lite-kernel> |

### Galaxy S10 (`beyond1lte`)
No official NetHunter registry variant.

**Community projects**

| Project | Status | Boot evidence | Features claimed/tested | Source |
|---|---|---|---|---|
| Kernels-by-ravindu644 | Developer claimed | No explicit boot evidence | internal wifi support, external wifi support, packet injection, hid gadget, usb gadget | <https://github.com/Kernels-by-ravindu644/samsung_kernel_exynos9820_stockrom> |

### Galaxy S20 Ultra (`z3s`)
No official NetHunter registry variant.

**Community projects**

| Project | Status | Boot evidence | Features claimed/tested | Source |
|---|---|---|---|---|
| stanleysvk87 | Developer claimed | Unknown | external wifi support, monitor mode, hid gadget, usb gadget | <https://github.com/stanleysvk87/s20-nethunter-port> |

### Galaxy S20 Ultra (5G) (`z3s`)
No official NetHunter registry variant.

**Community projects**

| Project | Status | Boot evidence | Features claimed/tested | Source |
|---|---|---|---|---|
| ben443 | Unverified candidate | No explicit boot evidence | Unknown | <https://github.com/ben443/Nethunter_kernel_samsung_exynos990> |

### Galaxy S20 Ultra (Exynos) (`z3s`)
No official NetHunter registry variant.

**Community projects**

| Project | Status | Boot evidence | Features claimed/tested | Source |
|---|---|---|---|---|
| WhimsyGiga | Developer claimed | No explicit boot evidence | external wifi support | <https://github.com/WhimsyGiga/Samsung-S20-ultra-exynos-nethunter-kernel> |

### Galaxy S21 Ultra (`p3s`)
No official NetHunter registry variant.

**Community projects**

| Project | Status | Boot evidence | Features claimed/tested | Source |
|---|---|---|---|---|
| shandongtlb | Developer claimed | Unknown | hid gadget | <https://github.com/shandongtlb/kernel_samsung_sm8350_s21u> |

### Galaxy S4 (`jflte`)
No official NetHunter registry variant.

**Community projects**

| Project | Status | Boot evidence | Features claimed/tested | Source |
|---|---|---|---|---|
| fabiocogno | Developer claimed | No explicit boot evidence | packet injection | <https://github.com/fabiocogno/nethunter-jfltexx-los16> |

### Galaxy S4 (GT-I9505, SGH-I337M, SGH-M919/V) (`jfltexx`)
No official NetHunter registry variant.

**Community projects**

| Project | Status | Boot evidence | Features claimed/tested | Source |
|---|---|---|---|---|
| fabiocogno | Developer claimed | No explicit boot evidence | packet injection | <https://github.com/fabiocogno/nethunter-jfltexx-los16> |

### Galaxy S5 Plus (`kccat6`)
No official NetHunter registry variant.

**Community projects**

| Project | Status | Boot evidence | Features claimed/tested | Source |
|---|---|---|---|---|
| jcadduono | Unverified candidate | No explicit boot evidence | Unknown | <https://github.com/jcadduono/nethunter_kernel_kccat6> |

### Galaxy S9 / S9+ (`starlte`)
**Official NetHunter registry variants**

| ROM | Android | Kernel | Author | Source |
|---|---|---|---|---|
| LineageOS 20 | thirteen | 4.9 | v0lk3n | <https://github.com/v0lk3n/nethunter_kernel_samsung_exynos9810.git> |

**Community projects**

| Project | Status | Boot evidence | Features claimed/tested | Source |
|---|---|---|---|---|
| mildg0d | Unverified candidate | No explicit boot evidence | Unknown | <https://gitlab.com/mildg0d/exynos9810_starlte_kernel> |
| ouroboros420 | Unverified candidate | No explicit boot evidence | Unknown | <https://github.com/ouroboros420/android_kernel_samsung_exynos9810> |

Search discoveries (metadata only, not inspected): 2. See `data/nethunter_search_candidates.csv`.

### Galaxy Tab A 8.0 (2019) (`gta3xlwifi`)
No official NetHunter registry variant.

**Community projects**

| Project | Status | Boot evidence | Features claimed/tested | Source |
|---|---|---|---|---|
| scrattatattat | Developer claimed | Unknown | Unknown | <https://github.com/scrattatattat/gta3xlwifi-nethunter> |

### Galaxy Tab A7 Lite (`gta7lite`)
No official NetHunter registry variant.

**Community projects**

| Project | Status | Boot evidence | Features claimed/tested | Source |
|---|---|---|---|---|
| phoenixaegis | Developer claimed | Unknown | external wifi support, monitor mode, packet injection, hid gadget | <https://github.com/phoenixaegis/nethunter-sm-t220> |

### Galaxy Tab A8 10.5 (2021) (`gta8`)
No official NetHunter registry variant.

**Community projects**

| Project | Status | Boot evidence | Features claimed/tested | Source |
|---|---|---|---|---|
| Eetuheino03 | Developer claimed | Unknown | Unknown | <https://github.com/eetuheino03/kali-nethunter-kernel-sm-x200> |

### Galaxy Tab A9 LTE (`sm-x115`)
No official NetHunter registry variant.

**Community projects**

| Project | Status | Boot evidence | Features claimed/tested | Source |
|---|---|---|---|---|
| Anmol6002 | Developer claimed | Unknown | Unknown | <https://github.com/anmol6002/kernel_smx115_nethunter> |
| Anmol6002 | Developer claimed | Unknown | Unknown | <https://github.com/anmol6002/nethunter-kernel-smx115> |

### Galaxy Tab S3 LTE (`gts3llte`)
No official NetHunter registry variant.

**Community projects**

| Project | Status | Boot evidence | Features claimed/tested | Source |
|---|---|---|---|---|
| pinnace | Abandoned | Unknown | Unknown | <https://github.com/pinnace/sm-t825> |

### Galaxy Tab S6 Lite (LTE) (`gta4xl`)
No official NetHunter registry variant.

**Community projects**

| Project | Status | Boot evidence | Features claimed/tested | Source |
|---|---|---|---|---|
| mohammedddd5 | Unverified candidate | No explicit boot evidence | Unknown | <https://github.com/mohammedddd5/nethunter-kernel-gta4xl> |

### Galaxy Tab S6 Lite (WiFi) (`gts6lwifi`)
No official NetHunter registry variant.

**Community projects**

| Project | Status | Boot evidence | Features claimed/tested | Source |
|---|---|---|---|---|
| jakkunight | Developer claimed | Unknown | Unknown | <https://github.com/jakkunight/gts6lwifi-custom-kernel> |

### Galaxy XCover 4 (`xcover4lte`)
No official NetHunter registry variant.

**Community projects**

| Project | Status | Boot evidence | Features claimed/tested | Source |
|---|---|---|---|---|
| bspippi1337 | Developer claimed | Unknown | hid gadget | <https://github.com/bspippi1337/blckswan-xcover4s-nethunter-kernel> |

### Samsung Exynos 1380 devices (`s5e8835`)
No official NetHunter registry variant.

**Community projects**

| Project | Status | Boot evidence | Features claimed/tested | Source |
|---|---|---|---|---|
| TheBizarreAbhishek | Unverified candidate | No explicit boot evidence | Unknown | <https://github.com/TheBizarreAbhishek/android_kernel_samsung_s5e8835> |

### Samsung Galaxy A01 (`a01`)
No official NetHunter registry variant.

**Community projects**

| Project | Status | Boot evidence | Features claimed/tested | Source |
|---|---|---|---|---|
| ravindu644 | Abandoned | No explicit boot evidence | Unknown | <https://github.com/ravindu644/kernel_samsung_a01> |

### Samsung Galaxy A05 (`a05`)
No official NetHunter registry variant.

**Community projects**

| Project | Status | Boot evidence | Features claimed/tested | Source |
|---|---|---|---|---|
| amirtubayi-HACK | Unverified candidate | No explicit boot evidence | Unknown | <https://github.com/amirtubayi-HACK/nethunter-kernel-a05> |
| kllr98331-maker | Unverified candidate | No explicit boot evidence | Unknown | <https://github.com/kllr98331-maker/a05-kernel-nethunter> |

### Samsung Galaxy A10 (`a10`)
No official NetHunter registry variant.

**Community projects**

| Project | Status | Boot evidence | Features claimed/tested | Source |
|---|---|---|---|---|
| fast50 | Abandoned | No explicit boot evidence | Unknown | <https://github.com/fast50/NethunterKernel-Galaxy-A105xxx> |
| mwafik2002 | Unverified candidate | No explicit boot evidence | Unknown | <https://github.com/mwafik2002/Nethunter-Kernel-Exynos7885> |

### Samsung Galaxy A12 (`a12`)
No official NetHunter registry variant.

**Community projects**

| Project | Status | Boot evidence | Features claimed/tested | Source |
|---|---|---|---|---|
| greenxhatzgreyty | Unverified candidate | No explicit boot evidence | Unknown | <https://github.com/greenxhatzgreyty/samsung-a127f> |

### Samsung Galaxy A14 (`a14`)
No official NetHunter registry variant.

**Community projects**

| Project | Status | Boot evidence | Features claimed/tested | Source |
|---|---|---|---|---|
| xkzetsu2 | Unverified candidate | No explicit boot evidence | Unknown | <https://github.com/xkzetsu2/a14-nethunter-kernel> |

### Samsung Galaxy A21s (`a21s`)
No official NetHunter registry variant.

**Community projects**

| Project | Status | Boot evidence | Features claimed/tested | Source |
|---|---|---|---|---|
| BasGame1 | Abandoned | No explicit boot evidence | Unknown | <https://github.com/BasGame1/nethunter_kernel_a21s> |
| karamdev1 | Unverified candidate | No explicit boot evidence | Unknown | <https://github.com/karamdev1/nethunter_kernel_samsung_a21s> |

### Samsung Galaxy A23 (SM-A235F) (`a23`)
No official NetHunter registry variant.

**Community projects**

| Project | Status | Boot evidence | Features claimed/tested | Source |
|---|---|---|---|---|
| karamdev1 | Unverified candidate | No explicit boot evidence | Unknown | <https://github.com/karamdev1/nethunter_kernel_samsung_a235f> |

### Samsung Galaxy A32 / A22 / A22s (`a32/a22`)
No official NetHunter registry variant.

**Community projects**

| Project | Status | Boot evidence | Features claimed/tested | Source |
|---|---|---|---|---|
| karamdev1 | Developer claimed | No explicit boot evidence | internal wifi support, monitor mode, packet injection, hid gadget, usb gadget | <https://github.com/karamdev1/nethunter_kernel_samsung_mt6768> |

### Samsung Galaxy A5 (2015) (`a5ulte`)
**Official NetHunter registry variants**

| ROM | Android | Kernel | Author | Source |
|---|---|---|---|---|
| CyanogenMod 13 | marshmallow | 3.10 | DeadSquirrel01 | <https://github.com/DeadSquirrel01/nethunter-kernel-a5ulte.git> |
| TouchWiz 6.0 | marshmallow | 3.10 | DeadSquirrel01 | <https://github.com/DeadSquirrel01/nethunter-kernel-a5ulte.git> |

### Samsung Galaxy A5 (2016) (`a5xelte`)
**Official NetHunter registry variants**

| ROM | Android | Kernel | Author | Source |
|---|---|---|---|---|
| TouchWiz Grace | nougat | 3.10 | Re4son | <https://github.com/Re4son/android_kernel_samsung-a5xelte> |

Search discoveries (metadata only, not inspected): 1. See `data/nethunter_search_candidates.csv`.

### Samsung Galaxy A7 (2016) (`a7xelte`)
**Official NetHunter registry variants**

| ROM | Android | Kernel | Author | Source |
|---|---|---|---|---|
| LineageOS 18.1 | eleven | 3.10 | yesimxev | <https://github.com/yesimxev/android_kernel_samsung_universal7580> |

### Samsung Galaxy A8 (a8elte) (`a8elte`)
No official NetHunter registry variant.

**Community projects**

| Project | Status | Boot evidence | Features claimed/tested | Source |
|---|---|---|---|---|
| DeadSquirrel01 | Abandoned | No explicit boot evidence | Unknown | <https://github.com/DeadSquirrel01/nethunter-kernel-a8elte> |

### Samsung Galaxy J5 3G (2015) (`j53g`)
**Official NetHunter registry variants**

| ROM | Android | Kernel | Author | Source |
|---|---|---|---|---|
| LineageOS 14.1 | nougat | 3.10 | djkido316 | <https://github.com/djkido316/nethunter-kernel_j5> |

### Samsung Galaxy J5 LTE (2015) (`j5lte`)
**Official NetHunter registry variants**

| ROM | Android | Kernel | Author | Source |
|---|---|---|---|---|
| LineageOS 14.1 | nougat | 3.10 | djkido316 | <https://github.com/djkido316/nethunter-kernel_j5> |

### Samsung Galaxy J5 NFC LTE (2015) (`j5nlte`)
**Official NetHunter registry variants**

| ROM | Android | Kernel | Author | Source |
|---|---|---|---|---|
| LineageOS 14.1 | nougat | 3.10 | djkido316 | <https://github.com/djkido316/nethunter-kernel_j5> |

### Samsung Galaxy J7 Neo (`j7velte`)
No official NetHunter registry variant.

**Community projects**

| Project | Status | Boot evidence | Features claimed/tested | Source |
|---|---|---|---|---|
| asesoriaogam-collab | Unverified candidate | No explicit boot evidence | Unknown | <https://github.com/asesoriaogam-collab/nethunter-kernel-j701m> |

### Samsung Galaxy J7 Prime (`on7xlte`)
**Official NetHunter registry variants**

| ROM | Android | Kernel | Author | Source |
|---|---|---|---|---|
| One UI | pie | 3.18 | S133PY | <https://github.com/Thiviyan/KRAKEN_7870_Nethunter> |

### Samsung Galaxy J7 Pro (`j7y17lte`)
**Official NetHunter registry variants**

| ROM | Android | Kernel | Author | Source |
|---|---|---|---|---|
| One UI | pie | 3.18 | S133PY | <https://github.com/Thiviyan/KRAKEN_7870_Nethunter> |

### Samsung Galaxy J8 (2018) (`j8y18lte`)
No official NetHunter registry variant.

**Community projects**

| Project | Status | Boot evidence | Features claimed/tested | Source |
|---|---|---|---|---|
| Adrilaw | Unverified candidate | No explicit boot evidence | Unknown | <https://gitlab.com/Adrilaw/android_kernel_samsung_j8y18lte> |

### Samsung Galaxy M11 (`m11q`)
No official NetHunter registry variant.

**Community projects**

| Project | Status | Boot evidence | Features claimed/tested | Source |
|---|---|---|---|---|
| plabonroyofficial | Developer claimed | No explicit boot evidence | external wifi support, packet injection, hid gadget, usb gadget | <https://github.com/plabonroyofficial/Kali-NetHunter-Kernel-Galaxy-M11-EvoX> |

### Samsung Galaxy M52 5G (`m52xq`)
No official NetHunter registry variant.

**Community projects**

| Project | Status | Boot evidence | Features claimed/tested | Source |
|---|---|---|---|---|
| RebertiCS | Abandoned | No explicit boot evidence | packet injection | <https://github.com/RebertiCS/M52-NetHunter-Kernel> |

### Samsung Galaxy Note 10 Plus (`d2s`)
No official NetHunter registry variant.

**Community projects**

| Project | Status | Boot evidence | Features claimed/tested | Source |
|---|---|---|---|---|
| pho5nix | Developer claimed | Developer-reported boot | monitor mode, hid gadget | <https://github.com/pho5nix/d2s-los23-nethunter-kernel> |

### Samsung Galaxy Note 3 (`hlte`)
**Official NetHunter registry variants**

| ROM | Android | Kernel | Author | Source |
|---|---|---|---|---|
| CyanogenMod 12 (Canada, Mexico, and T-Mobile) | lollipop | 3.04 | jcadduono | <https://github.com/jcadduono/idleKernel-note3.git> |
| CyanogenMod 13 (Canada, Mexico, and T-Mobile) | marshmallow | 3.04 | jcadduono | <https://github.com/jcadduono/idleKernel-note3.git> |
| TouchWiz 5.0 (Canada, Mexico, and T-Mobile) | lollipop | 3.04 | jcadduono | <https://github.com/jcadduono/idleKernel-note3.git> |
| TouchWiz 5.0 (Japanese NTT Docomo) | lollipop | 3.04 | jcadduono | <https://github.com/jcadduono/idleKernel-note3.git> |
| CyanogenMod 12 (International / European) | lollipop | 3.04 | jcadduono | <https://github.com/jcadduono/idleKernel-note3.git> |
| CyanogenMod 13 (International / European) | marshmallow | 3.04 | jcadduono | <https://github.com/jcadduono/idleKernel-note3.git> |
| TouchWiz 5.0 (International / European) | lollipop | 3.04 | jcadduono | <https://github.com/jcadduono/idleKernel-note3.git> |
| LineageOS 14.1 (International / European) | nougat | 3.04 | 4E656F | <https://github.com/0x4E0x650x6F/android_kernel_samsung_msm8974.git> |
| TouchWiz 5.0 (Japanese NTT Docomo) | lollipop | 3.04 | jcadduono | <https://github.com/jcadduono/idleKernel-note3.git> |
| CyanogenMod 12 (Korean) | lollipop | 3.04 | jcadduono | <https://github.com/jcadduono/idleKernel-note3.git> |
| CyanogenMod 13 (Korean) | marshmallow | 3.04 | jcadduono | <https://github.com/jcadduono/idleKernel-note3.git> |
| TouchWiz 5.0 (Korean) | lollipop | 3.04 | jcadduono | <https://github.com/jcadduono/idleKernel-note3.git> |
| CyanogenMod 12 (Sprint) | lollipop | 3.04 | jcadduono | <https://github.com/jcadduono/idleKernel-note3.git> |
| CyanogenMod 13 (Sprint) | marshmallow | 3.04 | jcadduono | <https://github.com/jcadduono/idleKernel-note3.git> |
| TouchWiz 5.0 (Sprint) | lollipop | 3.04 | jcadduono | <https://github.com/jcadduono/idleKernel-note3.git> |
| TouchWiz 5.0 (Verizon) | lollipop | 3.04 | jcadduono | <https://github.com/jcadduono/idleKernel-note3.git> |

Search discoveries (metadata only, not inspected): 1. See `data/nethunter_search_candidates.csv`.

### Samsung Galaxy Note 7 (`gracelte`)
**Official NetHunter registry variants**

| ROM | Android | Kernel | Author | Source |
|---|---|---|---|---|
| Grace UI | marshmallow | 3.18 | jcadduono | <https://github.com/jcadduono/android_kernel_samsung_universal8890.git> |
| Grace UI | marshmallow | 3.18 | jcadduono | <https://github.com/jcadduono/android_kernel_samsung_universal8890/commits> |

### Samsung Galaxy Note 8 (`greatlte`)
No official NetHunter registry variant.

**Community projects**

| Project | Status | Boot evidence | Features claimed/tested | Source |
|---|---|---|---|---|
| Taha-Sheikh032 | Unverified candidate | No explicit boot evidence | Unknown | <https://github.com/Taha-Sheikh032/Note-8-nethunter-kernel> |

### Samsung Galaxy Note20 Ultra (Exynos) (`c2s`)
**Official NetHunter registry variants**

| ROM | Android | Kernel | Author | Source |
|---|---|---|---|---|
| One UI 5.1 | thirteen | 4.19 | Luka Gejak | <https://github.com/MocLG/android_kernel_samsung_exynos990_nethunter> |

**Community projects**

| Project | Status | Boot evidence | Features claimed/tested | Source |
|---|---|---|---|---|
| MocLG | Developer claimed | Developer-reported boot | external wifi support, packet injection, hid gadget | <https://github.com/MocLG/android_kernel_samsung_exynos990_nethunter> |

### Samsung Galaxy S10 (`beyond1lte`)
**Official NetHunter registry variants**

| ROM | Android | Kernel | Author | Source |
|---|---|---|---|---|
| LineageOS 21 | fourteen | 4.14 | v0lk3n | <https://github.com/v0lk3n/nethunter_kernel_samsung_exynos9820.git> |
| LineageOS 22.2 | fifteen | 4.14 | v0lk3n | <https://github.com/v0lk3n/nethunter_kernel_samsung_exynos9820.git> |
| LineageOS 23.2 | sixteen | 4.14 | v0lk3n | <https://github.com/v0lk3n/nethunter_kernel_samsung_exynos9820.git> |

Search discoveries (metadata only, not inspected): 2. See `data/nethunter_search_candidates.csv`.

### Samsung Galaxy S10 5G (`beyondx`)
**Official NetHunter registry variants**

| ROM | Android | Kernel | Author | Source |
|---|---|---|---|---|
| LineageOS 23.2 | sixteen | 4.14 | yesimxev and v0lk3n | <https://github.com/v0lk3n/nethunter_kernel_samsung_exynos9820.git> |

### Samsung Galaxy S10+ (`beyond2lte`)
**Official NetHunter registry variants**

| ROM | Android | Kernel | Author | Source |
|---|---|---|---|---|
| LineageOS 23.2 | sixteen | 4.14 | yesimxev and v0lk3n | <https://github.com/v0lk3n/nethunter_kernel_samsung_exynos9820.git> |

**Community projects**

| Project | Status | Boot evidence | Features claimed/tested | Source |
|---|---|---|---|---|
| muhammadfikri-dev | Unverified candidate | No explicit boot evidence | external wifi support, monitor mode, packet injection, hid gadget, usb gadget | <https://github.com/muhammadfikri-dev/laksanasoft-enterprise-beyond2lte-kernel> |

Search discoveries (metadata only, not inspected): 3. See `data/nethunter_search_candidates.csv`.

### Samsung Galaxy S10e (`beyond0lte`)
**Official NetHunter registry variants**

| ROM | Android | Kernel | Author | Source |
|---|---|---|---|---|
| LineageOS 23.2 | sixteen | 4.14 | yesimxev and v0lk3n | <https://github.com/v0lk3n/nethunter_kernel_samsung_exynos9820.git> |

Search discoveries (metadata only, not inspected): 1. See `data/nethunter_search_candidates.csv`.

### Samsung Galaxy S10e (SM-G970N) (`beyond0lte`)
No official NetHunter registry variant.

**Community projects**

| Project | Status | Boot evidence | Features claimed/tested | Source |
|---|---|---|---|---|
| unreliablecode | Developer claimed | No explicit boot evidence | external wifi support, packet injection, hid gadget | <https://github.com/unreliablecode/ArtisanROM-PomPomSU-NetHunter> |

### Samsung Galaxy S20 FE 5G (Snapdragon) (`r8q`)
**Official NetHunter registry variants**

| ROM | Android | Kernel | Author | Source |
|---|---|---|---|---|
| One UI 2.5 | ten | 4.19 | Svirusx | <https://github.com/Svirusx/Nethunter-Kernel-S20_FE_5G.git> |
| One UI 3.0 | eleven | 4.19 | Svirusx | <https://github.com/Svirusx/Nethunter-Kernel-S20_FE_5G.git> |
| One UI 4.0 | twelve | 4.19 | Svirusx | <https://github.com/Svirusx/Nethunter-Kernel-S20_FE_5G.git> |
| One UI 5.0 | thirteen | 4.19 | Svirusx | <https://github.com/Svirusx/Nethunter-Kernel-S20_FE_5G.git> |
| LineageOS 23.0 | sixteen | 4.19 | Svirusx | <https://github.com/Svirusx/Nethunter_LineageOS_Samsung_S20FE5G_sm8250.git> |

**Community projects**

| Project | Status | Boot evidence | Features claimed/tested | Source |
|---|---|---|---|---|
| Svirusx | Unverified candidate | No explicit boot evidence | Unknown | <https://github.com/Svirusx/Nethunter-Kernel-S20_FE_5G> |

Search discoveries (metadata only, not inspected): 2. See `data/nethunter_search_candidates.csv`.

### Samsung Galaxy S4 (`jflte`)
**Official NetHunter registry variants**

| ROM | Android | Kernel | Author | Source |
|---|---|---|---|---|
| CyanogenMod 13 | marshmallow | 3.04 | semsevens | <https://github.com/semsevens/nethunter_kernel_jfltexx.git> |
| CyanogenMod 14.1 | nougat | 3.04 | fasheng | <https://github.com/fasheng/nethunter_kernel_jfltexx.git> |

### Samsung Galaxy S5 (`klte`)
**Official NetHunter registry variants**

| ROM | Android | Kernel | Author | Source |
|---|---|---|---|---|
| LineageOS 14.1 (GSM) | nougat | 3.04 | jcadduono | <https://github.com/jcadduono/android_kernel_samsung_msm8974.git> |
| TouchWiz 5.1 (GSM) | lollipop | 3.04 | jcadduono | <https://github.com/jcadduono/nethunter_kernel_klte.git> |
| TouchWiz 6.0 (GSM) | marshmallow | 3.04 | jcadduono | <https://github.com/jcadduono/nethunter_kernel_klte.git> |
| LineageOS 14.1 (China) | nougat | 3.04 | jcadduono | <https://github.com/jcadduono/android_kernel_samsung_msm8974.git> |
| LineageOS 14.1 (China Duos) | nougat | 3.04 | jcadduono | <https://github.com/jcadduono/android_kernel_samsung_msm8974.git> |
| LineageOS 14.1 (LTE Duos) | nougat | 3.04 | jcadduono | <https://github.com/jcadduono/android_kernel_samsung_msm8974.git> |
| TouchWiz 5.1 (LTE Duos) | lollipop | 3.04 | jcadduono | <https://github.com/jcadduono/nethunter_kernel_klte.git> |
| LineageOS 14.1 (Japan) | nougat | 3.04 | jcadduono | <https://github.com/jcadduono/android_kernel_samsung_msm8974.git> |
| TouchWiz 5.1 (Japan) | lollipop | 3.04 | jcadduono | <https://github.com/jcadduono/nethunter_kernel_klte.git> |
| LineageOS 14.1 (Korea) | nougat | 3.04 | jcadduono | <https://github.com/jcadduono/android_kernel_samsung_msm8974.git> |
| TouchWiz 5.1 (Korea) | lollipop | 3.04 | jcadduono | <https://github.com/jcadduono/nethunter_kernel_klte.git> |
| TouchWiz 6.0 (Korea) | marshmallow | 3.04 | jcadduono | <https://github.com/jcadduono/nethunter_kernel_klte.git> |
| LineageOS 14.1 (US Sprint, UK Vodafone, and Oceanic) | nougat | 3.04 | jcadduono | <https://github.com/jcadduono/android_kernel_samsung_msm8974.git> |
| TouchWiz 5.1 (US Sprint, UK Vodafone, and Oceanic) | lollipop | 3.04 | jcadduono | <https://github.com/jcadduono/nethunter_kernel_klte.git> |
| TouchWiz 5.1 (US Cellular) | lollipop | 3.04 | jcadduono | <https://github.com/jcadduono/nethunter_kernel_klte.git> |
| TouchWiz 5.1 (US Verizon) | lollipop | 3.04 | jcadduono | <https://github.com/jcadduono/nethunter_kernel_klte.git> |

Search discoveries (metadata only, not inspected): 1. See `data/nethunter_search_candidates.csv`.

### Samsung Galaxy S5 LTE Duos (`klteduos`)
No official NetHunter registry variant.

**Community projects**

| Project | Status | Boot evidence | Features claimed/tested | Source |
|---|---|---|---|---|
| syfaldhbly38-ux | Unverified candidate | No explicit boot evidence | Unknown | <https://github.com/syfaldhbly38-ux/NetHunter-kernel-for-klteduos> |

### Samsung Galaxy S5 Mini (`kminilte`)
**Official NetHunter registry variants**

| ROM | Android | Kernel | Author | Source |
|---|---|---|---|---|
| LineageOS 14.1 | nougat | 3.04 | yesimxev | <https://github.com/yesimxev/android_kernel_samsung_kminilte.git> |
| LineageOS 15.0 | oreo | 3.04 | yesimxev | <https://github.com/yesimxev/android_kernel_samsung_kminilte.git> |
| LineageOS 16.0 | pie | 3.04 | yesimxev | <https://github.com/yesimxev/android_kernel_samsung_kminilte.git> |

### Samsung Galaxy S6 (`zeroflte`)
**Official NetHunter registry variants**

| ROM | Android | Kernel | Author | Source |
|---|---|---|---|---|
| LineageOS 14.1 | nougat | 3.10 | XXH3X | <https://github.com/XXH3X/Exynos7420_Nethunter> |
| Android 7.0 | nougat | 3.10 | XXH3X | <https://github.com/XXH3X/Ultimate-Kali> |

### Samsung Galaxy S6 Edge (`zerolte`)
**Official NetHunter registry variants**

| ROM | Android | Kernel | Author | Source |
|---|---|---|---|---|
| LineageOS 14.1 | nougat | 3.10 | XXH3X | <https://github.com/XXH3X/Exynos7420_Nethunter> |
| Android 7.0 | nougat | 3.10 | XXH3X | <https://github.com/XXH3X/Ultimate-Kali> |

### Samsung Galaxy S7 (`herolte`)
**Official NetHunter registry variants**

| ROM | Android | Kernel | Author | Source |
|---|---|---|---|---|
| TouchWiz 6.0 | marshmallow | 3.18 | jcadduono | <https://github.com/jcadduono/android_kernel_samsung_universal8890> |
| TouchWiz Grace | oreo | 3.18 | Svirusx | <https://github.com/Svirusx/NetHunter-s7-kernel-StockOreo.git> |
| LineageOS 14.1 | nougat | 3.18 | Svirusx | <https://github.com/Svirusx/NetHunter-s7-kernel-LineageOS14.1.git> |
| LineageOS 16.0 | pie | 3.18 | Svirusx | <https://github.com/Svirusx/Nethunter-s7-kernel-LineageOS16.0.git> |
| One UI 1.0 | pie | 3.18 | Svirusx | <https://github.com/Svirusx/Nethunter-s7-kernel-WirusMOD-AiO.git> |
| TouchWiz 6.0 | marshmallow | 3.18 | jcadduono | <https://github.com/jcadduono/android_kernel_samsung_universal8890> |

### Samsung Galaxy S7 (flat) (`herolte`)
No official NetHunter registry variant.

**Community projects**

| Project | Status | Boot evidence | Features claimed/tested | Source |
|---|---|---|---|---|
| syzh120 | Abandoned | No explicit boot evidence | Unknown | <https://github.com/syzh120/nethunter-kernel> |

### Samsung Galaxy S7 Edge (`hero2lte`)
**Official NetHunter registry variants**

| ROM | Android | Kernel | Author | Source |
|---|---|---|---|---|
| TouchWiz 6.0 | marshmallow | 3.18 | jcadduono | <https://github.com/jcadduono/android_kernel_samsung_universal8890> |
| TouchWiz Grace | oreo | 3.18 | Svirusx | <https://github.com/Svirusx/NetHunter-s7-kernel-StockOreo.git> |
| LineageOS 14.1 | nougat | 3.18 | Svirusx | <https://github.com/Svirusx/NetHunter-s7-kernel-LineageOS14.1.git> |
| LineageOS 16.0 | pie | 3.18 | Svirusx | <https://github.com/Svirusx/Nethunter-s7-kernel-LineageOS16.0.git> |
| One UI 1.0 | pie | 3.18 | Svirusx | <https://github.com/Svirusx/Nethunter-s7-kernel-WirusMOD-AiO.git> |
| TouchWiz 6.0 | marshmallow | 3.18 | jcadduono | <https://github.com/jcadduono/android_kernel_samsung_universal8890> |

### Samsung Galaxy S8 (`dreamlte`)
No official NetHunter registry variant.

**Community projects**

| Project | Status | Boot evidence | Features claimed/tested | Source |
|---|---|---|---|---|
| shainahum12-cloud | Developer claimed | No explicit boot evidence | packet injection, hid gadget | <https://github.com/shainahum12-cloud/android_kernel_samsung_dreamlte_nethunter> |

### Samsung Galaxy S9+ (`star2lte`)
**Official NetHunter registry variants**

| ROM | Android | Kernel | Author | Source |
|---|---|---|---|---|
| LineageOS 20 | thirteen | 4.9 | mylezgoose | <https://github.com/mylesgoose/android_kernel_samsung_exynos9810.git> |

### Samsung Galaxy Tab S4 LTE (`gts4llte`)
**Official NetHunter registry variants**

| ROM | Android | Kernel | Author | Source |
|---|---|---|---|---|
| Android 8.1 | oreo | 4.04 | Re4son | <https://github.com/Re4son/gts4lwifi> |

### Samsung Galaxy Tab S4 WiFi (`gts4lwifi`)
**Official NetHunter registry variants**

| ROM | Android | Kernel | Author | Source |
|---|---|---|---|---|
| Android 8.1 | oreo | 4.04 | Re4son | <https://github.com/Re4son/gts4lwifi> |


## Sony
Devices/codenames: 11. Official variants: 7. Community projects: 6.
### Sony Xperia 10 II (`pdx201`)
**Official NetHunter registry variants**

| ROM | Android | Kernel | Author | Source |
|---|---|---|---|---|
| LineageOS 20 | thirteen | 4.14 | Mashopy | <https://github.com/lineageos-on-pdx201/android_kernel_sony_sm6125> |

### Sony Xperia 10 V (`pdx235`)
**Official NetHunter registry variants**

| ROM | Android | Kernel | Author | Source |
|---|---|---|---|---|
| LineageOS 23.2 | sixteen | 5.4 | Tom60chat | <https://github.com/Tom60chat/android_kernel_sony_sm6375> |

### Sony Xperia XZ2 (`xz2`)
No official NetHunter registry variant.

**Community projects**

| Project | Status | Boot evidence | Features claimed/tested | Source |
|---|---|---|---|---|
| salk-cell | Unverified candidate | No explicit boot evidence | Unknown | <https://github.com/salk-cell/nethunter-kernel-xz2> |

### Sony Xperia Z (`yuga`)
**Official NetHunter registry variants**

| ROM | Android | Kernel | Author | Source |
|---|---|---|---|---|
| CyanogenMod 13 | marshmallow | 3.04 | Daedroza | <https://github.com/daedroza/nethunter_kernel_apq8064.git> |

### Sony Xperia Z1 (`honami`)
**Official NetHunter registry variants**

| ROM | Android | Kernel | Author | Source |
|---|---|---|---|---|
| LineageOS 13.1 | marshmallow | 3.04 | Re4son | <https://github.com/Re4son/android_kernel_Hanomi.git> |
| LineageOS 16 | pie | 3.04 | Re4son | <https://github.com/Re4son/android_kernel_Hanomi.git> |

### Sony Xperia Z3 (z3s) (`z3s`)
No official NetHunter registry variant.

**Community projects**

| Project | Status | Boot evidence | Features claimed/tested | Source |
|---|---|---|---|---|
| namegar | Developer claimed | No explicit boot evidence | packet injection | <https://github.com/namegar/nethunter-z3s-kernel> |

### Sony Xperia Z5 Compact (`suzuran`)
**Official NetHunter registry variants**

| ROM | Android | Kernel | Author | Source |
|---|---|---|---|---|
| LineageOS 14.1 | nougat | 3.10 | Re4son | <https://github.com/Re4son/android_kernel_sony_msm8994> |

### Sony Xperia ZR (`dogo`)
**Official NetHunter registry variants**

| ROM | Android | Kernel | Author | Source |
|---|---|---|---|---|
| CyanogenMod 13 | marshmallow | 3.04 | Daedroza | <https://github.com/daedroza/nethunter_kernel_apq8064.git> |

### Xperia 10 (`kirin`)
No official NetHunter registry variant.

**Community projects**

| Project | Status | Boot evidence | Features claimed/tested | Source |
|---|---|---|---|---|
| gibait | Developer claimed | No explicit boot evidence | hid gadget | <https://github.com/gibait/pdx201-nethunter-kernel-builder-docker> |

### Xperia 10 II (`pdx201`)
No official NetHunter registry variant.

**Community projects**

| Project | Status | Boot evidence | Features claimed/tested | Source |
|---|---|---|---|---|
| gibait | Developer claimed | No explicit boot evidence | hid gadget | <https://github.com/gibait/pdx201-nethunter-kernel-builder-docker> |
| howfan31 | Unverified candidate | No explicit boot evidence | Unknown | <https://github.com/howfan31/kali-nethunter-2026.2-pdx201-los-thirteen-full-repaired> |

### Xperia SP (`huashan`)
No official NetHunter registry variant.

**Community projects**

| Project | Status | Boot evidence | Features claimed/tested | Source |
|---|---|---|---|---|
| haleem254 | Abandoned | No explicit boot evidence | Unknown | <https://github.com/haleem254/nethuntersp> |


## Ulefone
Devices/codenames: 1. Official variants: 1. Community projects: 1.
### Ulefone Armor 34+ (`armor34plus`)
**Official NetHunter registry variants**

| ROM | Android | Kernel | Author | Source |
|---|---|---|---|---|
| Stock Android 16 (MT6878 / Dimensity 7300) | sixteen | 6.1 | art0181 | <https://gitlab.com/art0181/android_kernel_ulefone_armor34plus_gki.git> |

**Community projects**

| Project | Status | Boot evidence | Features claimed/tested | Source |
|---|---|---|---|---|
| art0181 | Unverified candidate | No explicit boot evidence | Unknown | <https://gitlab.com/art0181/android_kernel_ulefone_armor34plus_gki> |


## Xiaomi
Devices/codenames: 97. Official variants: 38. Community projects: 106.
### Mi 10 (`umi`)
No official NetHunter registry variant.

**Community projects**

| Project | Status | Boot evidence | Features claimed/tested | Source |
|---|---|---|---|---|
| Dylanmurzello | Developer claimed | Unknown | Unknown | <https://github.com/dylanmurzello/kali_kernel_mi10> |

### Mi 11 (`venus`)
No official NetHunter registry variant.

**Community projects**

| Project | Status | Boot evidence | Features claimed/tested | Source |
|---|---|---|---|---|
| shandongtlb | Developer claimed | Unknown | Unknown | <https://github.com/shandongtlb/kernel_xiaomi_sm8350_m11> |

### Mi 8 (`dipper`)
No official NetHunter registry variant.

**Community projects**

| Project | Status | Boot evidence | Features claimed/tested | Source |
|---|---|---|---|---|
| mamilux | Developer claimed | Unknown | external wifi support, monitor mode, hid gadget | <https://github.com/mamilux/mi8-nethunter-project> |

### Mi 9 (`cepheus`)
No official NetHunter registry variant.

**Community projects**

| Project | Status | Boot evidence | Features claimed/tested | Source |
|---|---|---|---|---|
| k0d14k | Developer claimed | Unknown | Unknown | <https://github.com/k0d14k/mi_9_cepheus_kali_nethunter_setup> |

### Mi A1 (`tissot`)
No official NetHunter registry variant.

**Community projects**

| Project | Status | Boot evidence | Features claimed/tested | Source |
|---|---|---|---|---|
| prorooter007 | Unverified candidate | No explicit boot evidence | Unknown | <https://github.com/prorooter007/Nethunter_Kernel_Xiaomi_msm8953> |

### Mi A2 Lite (`daisy`)
No official NetHunter registry variant.

**Community projects**

| Project | Status | Boot evidence | Features claimed/tested | Source |
|---|---|---|---|---|
| AzeAstro | Unverified candidate | No explicit boot evidence | Unknown | <https://github.com/AzeAstro/miA2Lite_kernel> |

### Mi MIX 3 (`perseus`)
No official NetHunter registry variant.

**Community projects**

| Project | Status | Boot evidence | Features claimed/tested | Source |
|---|---|---|---|---|
| kamstartech | Unverified candidate | No explicit boot evidence | Unknown | <https://github.com/kamstartech/perseus-kernel-modules> |

### Mi Pad 4 (`clover`)
No official NetHunter registry variant.

**Community projects**

| Project | Status | Boot evidence | Features claimed/tested | Source |
|---|---|---|---|---|
| DevKyurria | Unverified candidate | No explicit boot evidence | Unknown | <https://github.com/DevKyurria/nethunter_kernel_xiaomi_clover> |

### POCO F1 (`beryllium`)
No official NetHunter registry variant.

**Community projects**

| Project | Status | Boot evidence | Features claimed/tested | Source |
|---|---|---|---|---|
| hmonojit | Unverified candidate | No explicit boot evidence | Unknown | <https://github.com/hmonojit/Poco-F1-Dual-Boot-Nethunter-Pro-Android-13> |

### POCO F4 GT (`ingres`)
No official NetHunter registry variant.

**Community projects**

| Project | Status | Boot evidence | Features claimed/tested | Source |
|---|---|---|---|---|
| ruik3z | Developer claimed | No explicit boot evidence | external wifi support, monitor mode | <https://github.com/ruik3z/avalon-ingres> |

### POCO F5 (`marble`)
No official NetHunter registry variant.

**Community projects**

| Project | Status | Boot evidence | Features claimed/tested | Source |
|---|---|---|---|---|
| WeiguangTWK | Developer claimed | Unknown | Unknown | <https://github.com/weiguangtwk/cursed_melt_kernel_marble_patch> |

### POCO F5 (Global) (`marble`)
No official NetHunter registry variant.

**Community projects**

| Project | Status | Boot evidence | Features claimed/tested | Source |
|---|---|---|---|---|
| PARADOX-X20 | Unverified candidate | No explicit boot evidence | Unknown | <https://github.com/PARADOX-X20/kernel_xiaomi_sm8450> |

### POCO F6 (`peridot`)
No official NetHunter registry variant.

**Community projects**

| Project | Status | Boot evidence | Features claimed/tested | Source |
|---|---|---|---|---|
| malayalicoding | Developer claimed | Unknown | Unknown | <https://github.com/malayalicoding/poco-f6-nethunter-kernel> |

### POCO M2 Pro (`gram`)
No official NetHunter registry variant.

**Community projects**

| Project | Status | Boot evidence | Features claimed/tested | Source |
|---|---|---|---|---|
| 0x1k4rt1k | Unverified candidate | No explicit boot evidence | Unknown | <https://github.com/0x1k4rt1k/miatoll-nethunter-boot> |
| clarencelol | Developer claimed | Unknown | Unknown | <https://github.com/clarencelol/kernel_xiaomi_sm6250> |

### POCO M4 5G (`light`)
No official NetHunter registry variant.

**Community projects**

| Project | Status | Boot evidence | Features claimed/tested | Source |
|---|---|---|---|---|
| N3tm4t3 | Developer claimed | Unknown | external wifi support, monitor mode, hid gadget, usb gadget | <https://github.com/n3tm4t3/poco-m4-5g-nethunter> |

### POCO X5 5G (`moonstone`)
No official NetHunter registry variant.

**Community projects**

| Project | Status | Boot evidence | Features claimed/tested | Source |
|---|---|---|---|---|
| edbastida | Developer claimed | No explicit boot evidence | external wifi support, monitor mode, packet injection, hid gadget, usb gadget | <https://github.com/edbastida/Kernel_Stone_DarkHuntermoon-Reborn> |

### POCO X5 5G / Redmi Note 12 5G (crDroid 12) (`stone-crdroid12`)
**Official NetHunter registry variants**

| ROM | Android | Kernel | Author | Source |
|---|---|---|---|---|
| crDroid12 Android 16 | sixteen | 5.4.302 | harifhaqim(mikhailsimon) | <https://github.com/harifhaqim/crdroid_nethunter_stone> |

### Pocophone F1 (`beryllium`)
No official NetHunter registry variant.

**Community projects**

| Project | Status | Boot evidence | Features claimed/tested | Source |
|---|---|---|---|---|
| CyberRider69 | Developer claimed | No explicit boot evidence | external wifi support | <https://github.com/CyberRider69/nethunter-evolutionx-beryllium-no-kernel> |
| DX4GREY | Unverified candidate | No explicit boot evidence | Unknown | <https://github.com/DX4GREY/kernel_xiaomi_sdm845> |

### Redmi 10C (`fog`)
No official NetHunter registry variant.

**Community projects**

| Project | Status | Boot evidence | Features claimed/tested | Source |
|---|---|---|---|---|
| Dante-1993 | Developer claimed | Unknown | Unknown | <https://github.com/dante-1993/redmi-10c-fog-kernel-4.19.325> |

### Redmi 1S (`armani`)
**Official NetHunter registry variants**

| ROM | Android | Kernel | Author | Source |
|---|---|---|---|---|
| Redmi 1S for stock Android | kitkat | 3.04 | firstblooder | Unknown |

Search discoveries (metadata only, not inspected): 1. See `data/nethunter_search_candidates.csv`.

### Redmi 4A (`rolex`)
No official NetHunter registry variant.

**Community projects**

| Project | Status | Boot evidence | Features claimed/tested | Source |
|---|---|---|---|---|
| Thiviyan | Abandoned | No explicit boot evidence | Unknown | <https://github.com/Thiviyan/-Xiaomi-Redmi-4A-Nethunter> |

### Redmi 5 (`rosy`)
No official NetHunter registry variant.

**Community projects**

| Project | Status | Boot evidence | Features claimed/tested | Source |
|---|---|---|---|---|
| hellojonh9955 | Unverified candidate | No explicit boot evidence | Unknown | <https://github.com/hellojonh9955/rosy-android14ksu-nethunter-kernel> |
| p3h3n9-pr0j3ct | Unverified candidate | No explicit boot evidence | Unknown | <https://github.com/p3h3n9-pr0j3ct/NetHunter-vince-R-FINAL> |

### Redmi 5 Plus (`vince`)
No official NetHunter registry variant.

**Community projects**

| Project | Status | Boot evidence | Features claimed/tested | Source |
|---|---|---|---|---|
| kotkaaja | Unverified candidate | No explicit boot evidence | Unknown | <https://github.com/kotkaaja/NetHunter-kernel-vince-R-by-p3h3n9-Remake> |
| p3h3n9-pr0j3ct | Unverified candidate | No explicit boot evidence | Unknown | <https://github.com/p3h3n9-pr0j3ct/NetHunter-vince-R-FINAL> |
| kitkat-rek777013 | Abandoned | No explicit boot evidence | Unknown | <https://github.com/kitkat-rek777013/kernel-nethunter-vince-krypton-based> |
| rek777013 | Abandoned | Unknown | Unknown | <https://github.com/rek777013/kali_nethunter_kernel_vince> |

### Redmi 5A (`riva`)
No official NetHunter registry variant.

**Community projects**

| Project | Status | Boot evidence | Features claimed/tested | Source |
|---|---|---|---|---|
| ShorterKing | Developer claimed | Unknown | Unknown | <https://github.com/shorterking/kali-nethunter-redmi5a-kernel> |

### Redmi 8 (`olive`)
No official NetHunter registry variant.

**Community projects**

| Project | Status | Boot evidence | Features claimed/tested | Source |
|---|---|---|---|---|
| leoshanumber69 | Unverified candidate | No explicit boot evidence | Unknown | <https://github.com/leoshanumber69/AkameKernel-NetHunter> |

### Redmi 9 / 9 Prime (`lancelot`)
No official NetHunter registry variant.

**Community projects**

| Project | Status | Boot evidence | Features claimed/tested | Source |
|---|---|---|---|---|
| deepcomon | Unverified candidate | No explicit boot evidence | Unknown | <https://github.com/deepcomon/kernel-nethunter-for-Redmi-9A> |
| Neternels | Unverified candidate | No explicit boot evidence | Unknown | <https://github.com/Neternels/NetHunter-MT6768> |
| imranbendjaballah | Developer claimed | Unknown | Unknown | <https://github.com/imranbendjaballah/nethunter_kernel_lancelot> |

### Redmi K20 Pro (`raphael`)
No official NetHunter registry variant.

**Community projects**

| Project | Status | Boot evidence | Features claimed/tested | Source |
|---|---|---|---|---|
| DOITfit | Abandoned | No explicit boot evidence | Unknown | <https://github.com/DOITfit/Redmi-K20Pro-Nethunter-Project> |

### Redmi Note 10 Lite (`miatoll`)
No official NetHunter registry variant.

**Community projects**

| Project | Status | Boot evidence | Features claimed/tested | Source |
|---|---|---|---|---|
| clarencelol | Developer claimed | Unknown | Unknown | <https://github.com/clarencelol/kernel_xiaomi_sm6250> |

### Redmi Note 10 Pro (`sweet`)
No official NetHunter registry variant.

**Community projects**

| Project | Status | Boot evidence | Features claimed/tested | Source |
|---|---|---|---|---|
| piwwing23 | Developer claimed | No explicit boot evidence | monitor mode, packet injection, hid gadget | <https://github.com/piwwing23/sweet-kernel-NetHunter> |
| KirillTank | Developer claimed | Unknown | external wifi support, monitor mode, packet injection, hid gadget, usb gadget | <https://github.com/kirilltank/kernel-xiaomi_sm6150> |
| H-curio | Developer claimed | Unknown | monitor mode | <https://github.com/h-curio/redmi-note10pro-nethunter-h-curio> |

### Redmi Note 10 Pro Max (`sweetin`)
No official NetHunter registry variant.

**Community projects**

| Project | Status | Boot evidence | Features claimed/tested | Source |
|---|---|---|---|---|
| KirillTank | Developer claimed | Unknown | external wifi support, monitor mode, packet injection, hid gadget, usb gadget | <https://github.com/kirilltank/kernel-xiaomi_sm6150> |

### Redmi Note 11 spes (`spes_matrixx`)
**Official NetHunter registry variants**

| ROM | Android | Kernel | Author | Source |
|---|---|---|---|---|
| AOSPA | fifteen | 4.19.325 | Madara273 | <https://github.com/Madara273/Redmi-Note-11-Kernel> |

### Redmi Note 13 Pro 5G (`garnet`)
No official NetHunter registry variant.

**Community projects**

| Project | Status | Boot evidence | Features claimed/tested | Source |
|---|---|---|---|---|
| bollustrado | Developer claimed | Unknown | Unknown | <https://github.com/bollustrado/nethunter_kernel_xiaomi_garnet> |

### Redmi Note 4G (`dior`)
No official NetHunter registry variant.

**Community projects**

| Project | Status | Boot evidence | Features claimed/tested | Source |
|---|---|---|---|---|
| ViP3R-KERNELs | Developer claimed | Unknown | Unknown | <https://github.com/vip3r-kernels/kernel_source_n_dior> |

### Redmi Note 6 Pro (`tulip`)
No official NetHunter registry variant.

**Community projects**

| Project | Status | Boot evidence | Features claimed/tested | Source |
|---|---|---|---|---|
| satana666luciferka | Unverified candidate | No explicit boot evidence | Unknown | <https://github.com/satana666luciferka/KERNEL-NETHUNTER-REDMI-NOTE-6-PRO> |
| satana666luciferka | Abandoned | No explicit boot evidence | Unknown | <https://github.com/satana666luciferka/redmi-note-6-pro-kernel-nethunter-HELLP> |

### Redmi Note 7 (`lavender`)
No official NetHunter registry variant.

**Community projects**

| Project | Status | Boot evidence | Features claimed/tested | Source |
|---|---|---|---|---|
| Postcard7952 | Unverified candidate | No explicit boot evidence | Unknown | <https://github.com/Postcard7952/Lavender-Nethunter> |
| sauravsinha239 | Unverified candidate | No explicit boot evidence | Unknown | <https://github.com/sauravsinha239/nethunter-lavender> |

### Redmi Note 7 Pro (`violet`)
No official NetHunter registry variant.

**Community projects**

| Project | Status | Boot evidence | Features claimed/tested | Source |
|---|---|---|---|---|
| ryzen-kernel | Unverified candidate | No explicit boot evidence | Unknown | <https://github.com/ryzen-kernel/nethunter_kernel_xiaomi_violet> |

### Redmi Note 8 (`ginkgo`)
**Official NetHunter registry variants**

| ROM | Android | Kernel | Author | Source |
|---|---|---|---|---|
| ArrowOS 13 | thirteen | 4.14 | ikteach | <https://github.com/ikteach/ginkgo_kernel.git> |
| LineageOS 23.2 | sixteen | 4.14 | ikteach | <https://github.com/ikteach/ginkgo_nethunter_kernel.git> |

Search discoveries (metadata only, not inspected): 4. See `data/nethunter_search_candidates.csv`.

### Redmi Note 8 Pro (`begonia`)
No official NetHunter registry variant.

**Community projects**

| Project | Status | Boot evidence | Features claimed/tested | Source |
|---|---|---|---|---|
| tarq04125-lang | Unverified candidate | No explicit boot evidence | Unknown | <https://github.com/tarq04125-lang/begonia-nethunter-kernel1> |
| tarq04125-lang | Unverified candidate | No explicit boot evidence | Unknown | <https://github.com/tarq04125-lang/begonia-nethunter-kernel2> |
| peppedb92-dotcom | Developer claimed | No explicit boot evidence | external wifi support, monitor mode, hid gadget, usb gadget | <https://github.com/peppedb92-dotcom/begonia-nethunter-kernel> |
| Anonym3310 | Unverified candidate | No explicit boot evidence | Unknown | <https://github.com/Anonym3310/AkameKernel-begonia> |

### Redmi Note 8T (`willow`)
No official NetHunter registry variant.

**Community projects**

| Project | Status | Boot evidence | Features claimed/tested | Source |
|---|---|---|---|---|
| vaginessa | Unverified candidate | No explicit boot evidence | Unknown | <https://github.com/vaginessa/Cuh-Nethunter-Kernel-willow> |

### Redmi Note 9 (`merlinx`)
No official NetHunter registry variant.

**Community projects**

| Project | Status | Boot evidence | Features claimed/tested | Source |
|---|---|---|---|---|
| killindodo | Developer claimed | No explicit boot evidence | internal wifi support, monitor mode | <https://github.com/killindodo/merlin-net-hunter-kernel-MT7601U-WiFi-Adapter-Support-> |
| ritikthakur22 | Developer claimed | No explicit boot evidence | external wifi support, monitor mode, packet injection, hid gadget, usb gadget | <https://github.com/ritikthakur22/nethunter-kernel-merlin> |
| Neternels | Unverified candidate | No explicit boot evidence | Unknown | <https://github.com/Neternels/NetHunter-MT6768> |

### Redmi Note 9 Pro (`joyeuse`)
No official NetHunter registry variant.

**Community projects**

| Project | Status | Boot evidence | Features claimed/tested | Source |
|---|---|---|---|---|
| 0x1k4rt1k | Unverified candidate | No explicit boot evidence | Unknown | <https://github.com/0x1k4rt1k/miatoll-nethunter-boot> |
| dhiimr | Abandoned | No explicit boot evidence | Unknown | <https://github.com/dhiimr/NHunter_Joyeuse> |
| dhiimr | Unverified candidate | No explicit boot evidence | Unknown | <https://github.com/dhiimr/nethunter_note9pro> |
| Anonym3310 | Unverified candidate | No explicit boot evidence | Unknown | <https://github.com/Anonym3310/AkameKernel-joyeuse> |
| clarencelol | Developer claimed | Unknown | Unknown | <https://github.com/clarencelol/kernel_xiaomi_sm6250> |
| Naster17 | Developer claimed | Unknown | external wifi support, hid gadget | <https://github.com/naster17/nethunter-kernels> |

### Redmi Note 9 Pro Max (`excalibur`)
No official NetHunter registry variant.

**Community projects**

| Project | Status | Boot evidence | Features claimed/tested | Source |
|---|---|---|---|---|
| 0x1k4rt1k | Unverified candidate | No explicit boot evidence | Unknown | <https://github.com/0x1k4rt1k/miatoll-nethunter-boot> |
| clarencelol | Developer claimed | Unknown | Unknown | <https://github.com/clarencelol/kernel_xiaomi_sm6250> |

### Redmi Note 9S (`curtana`)
No official NetHunter registry variant.

**Community projects**

| Project | Status | Boot evidence | Features claimed/tested | Source |
|---|---|---|---|---|
| 0x1k4rt1k | Unverified candidate | No explicit boot evidence | Unknown | <https://github.com/0x1k4rt1k/miatoll-nethunter-boot> |
| clarencelol | Developer claimed | Unknown | Unknown | <https://github.com/clarencelol/kernel_xiaomi_sm6250> |

### Xiaomi 11 Lite 5G NE (`lisa`)
No official NetHunter registry variant.

**Community projects**

| Project | Status | Boot evidence | Features claimed/tested | Source |
|---|---|---|---|---|
| Kirolos124 | Unverified candidate | No explicit boot evidence | external wifi support, monitor mode, hid gadget, usb gadget | <https://github.com/Kirolos124/NH-Lisa> |

### Xiaomi 11T Pro (`vili`)
No official NetHunter registry variant.

**Community projects**

| Project | Status | Boot evidence | Features claimed/tested | Source |
|---|---|---|---|---|
| dinelo | Unverified candidate | No explicit boot evidence | Unknown | <https://github.com/dinelo/vili-nethunter-kernel> |

### Xiaomi Mi 10T Lite / Redmi Note 9 Pro 5G (`gauguin`)
No official NetHunter registry variant.

**Community projects**

| Project | Status | Boot evidence | Features claimed/tested | Source |
|---|---|---|---|---|
| Dqdd | Abandoned | No explicit boot evidence | Unknown | <https://github.com/Dqdd/gauguin_nethunter_kernel> |

### Xiaomi Mi 10i 5G (`gauguinpro`)
No official NetHunter registry variant.

**Community projects**

| Project | Status | Boot evidence | Features claimed/tested | Source |
|---|---|---|---|---|
| mashunterbd | Unverified candidate | No explicit boot evidence | Unknown | <https://github.com/mashunterbd/Nethunter_kernel_Gauguinpro> |

### Xiaomi Mi 3 / Mi 4 (`cancro`)
**Official NetHunter registry variants**

| ROM | Android | Kernel | Author | Source |
|---|---|---|---|---|
| CyanogenMod 13 | marshmallow | 3.04 | Binkybear | <https://github.com/binkybear/android_kernel_xiaomi_cancro.git> |

### Xiaomi Mi 8 (`dipper`)
No official NetHunter registry variant.

**Community projects**

| Project | Status | Boot evidence | Features claimed/tested | Source |
|---|---|---|---|---|
| TsingPeng03 | Developer claimed | No explicit boot evidence | monitor mode, packet injection, hid gadget | <https://github.com/TsingPeng03/Mi8-Nethunter-Project> |

### Xiaomi Mi 8 Lite (`platina`)
No official NetHunter registry variant.

**Community projects**

| Project | Status | Boot evidence | Features claimed/tested | Source |
|---|---|---|---|---|
| almost-nowhere | Unverified candidate | No explicit boot evidence | packet injection, usb gadget | <https://github.com/almost-nowhere/platina-ksunext-nethunter> |

### Xiaomi Mi 9 (`cepheus`)
No official NetHunter registry variant.

**Community projects**

| Project | Status | Boot evidence | Features claimed/tested | Source |
|---|---|---|---|---|
| shandongtlb | Developer claimed | No explicit boot evidence | monitor mode, packet injection | <https://github.com/shandongtlb/MI9-Nethunter-Project> |
| xxoolm | Developer claimed | No explicit boot evidence | packet injection, hid gadget, usb gadget | <https://github.com/xxoolm/kernel_xiaomi_sm8150_nethunter> |

### Xiaomi Mi 9 Lite / CC9 (`pyxis`)
**Official NetHunter registry variants**

| ROM | Android | Kernel | Author | Source |
|---|---|---|---|---|
| LineageOS 21 | fourteen | 4.9 | yesimxev | <https://github.com/yesimxev/android_kernel_xiaomi_sdm710> |
| LineageOS 22.2 | fifteen | 4.9 | yesimxev | <https://github.com/yesimxev/android_kernel_xiaomi_sdm710> |

### Xiaomi Mi 9 cepheus (PixelOS 15) (`cepheus`)
**Official NetHunter registry variants**

| ROM | Android | Kernel | Author | Source |
|---|---|---|---|---|
| PixelOS 15 | fifteen | 4.14.353-openela | k0d14k | <https://github.com/k0d14k/kernel_xiaomi_cepheus> |

Search discoveries (metadata only, not inspected): 2. See `data/nethunter_search_candidates.csv`.

### Xiaomi Mi 9T (`davinci`)
**Official NetHunter registry variants**

| ROM | Android | Kernel | Author | Source |
|---|---|---|---|---|
| MIUI Global 11 | ten | 4.14 | Re4son | <https://github.com/Re4son/android_kernel_xiaomi_davinci_hasty> |

Search discoveries (metadata only, not inspected): 1. See `data/nethunter_search_candidates.csv`.

### Xiaomi Mi A2 (`jasmine-sprout`)
**Official NetHunter registry variants**

| ROM | Android | Kernel | Author | Source |
|---|---|---|---|---|
| LineageOS 22.1 | fifteen | 4.19 | mr00k3 | <https://github.com/mr00k3/jasmine_sprout_nethunter> |

### Xiaomi Mi A3 (`laurel-sprout`)
**Official NetHunter registry variants**

| ROM | Android | Kernel | Author | Source |
|---|---|---|---|---|
| LineageOS 18.1 | eleven | 4.14 | yesimxev | <https://github.com/yesimxev/android_kernel_xiaomi_laurel_sprout> |
| LineageOS 19.1 | twelve | 4.14 | yesimxev | <https://github.com/yesimxev/android_kernel_xiaomi_laurel_sprout> |
| LineageOS 20 | thirteen | 4.14 | yesimxev | <https://github.com/yesimxev/android_kernel_xiaomi_laurel_sprout> |
| LineageOS 21 | fourteen | 4.14 | yesimxev | <https://github.com/yesimxev/android_kernel_laurel_sprout> |
| LineageOS 22 | fifteen | 4.14 | yesimxev | <https://github.com/yesimxev/android_kernel_laurel_sprout> |
| LineageOS 23.2 | sixteen | 4.14 | yesimxev | <https://github.com/yesimxev/android_kernel_xiaomi_sm6125> |

Search discoveries (metadata only, not inspected): 1. See `data/nethunter_search_candidates.csv`.

### Xiaomi Mi Max 2 (`oxygen`)
No official NetHunter registry variant.

**Community projects**

| Project | Status | Boot evidence | Features claimed/tested | Source |
|---|---|---|---|---|
| grzegorzpalczynski6-boop | Unverified candidate | No explicit boot evidence | Unknown | <https://github.com/grzegorzpalczynski6-boop/Build-NetHunter-kernel-for-Xiaomi-Mi-Max-2> |

### Xiaomi Mi Max 3 (`nitrogen`)
No official NetHunter registry variant.

**Community projects**

| Project | Status | Boot evidence | Features claimed/tested | Source |
|---|---|---|---|---|
| Jemacivan | Abandoned | No explicit boot evidence | Unknown | <https://github.com/Jemacivan/nitrogen-kernel> |

### Xiaomi Mi8937 family (`mi8937`)
No official NetHunter registry variant.

**Community projects**

| Project | Status | Boot evidence | Features claimed/tested | Source |
|---|---|---|---|---|
| mdkwork | Developer claimed | Unknown | Unknown | <https://github.com/mdkwork/nethunter_xiaomi_kernel_mi8937> |

### Xiaomi MiPad 1 (`mocha`)
**Official NetHunter registry variants**

| ROM | Android | Kernel | Author | Source |
|---|---|---|---|---|
| CyanogenMod 11 | kitkat | 3.10 | RahulTheVirus! | <https://github.com/RahulTheVirus/mocha-kernels.git> |
| CyanogenMod 12.1 | lollipop | 3.10 | RahulTheVirus! | <https://github.com/RahulTheVirus/mocha-kernels.git> |

Search discoveries (metadata only, not inspected): 1. See `data/nethunter_search_candidates.csv`.

### Xiaomi POCO F1 (`beryllium`)
No official NetHunter registry variant.

**Community projects**

| Project | Status | Boot evidence | Features claimed/tested | Source |
|---|---|---|---|---|
| DX4GREY | Developer claimed | No explicit boot evidence | internal wifi support, monitor mode, packet injection | <https://github.com/DX4GREY/android_kernel_xiaomi_sdm845> |

### Xiaomi POCO F6 (`peridot`)
No official NetHunter registry variant.

**Community projects**

| Project | Status | Boot evidence | Features claimed/tested | Source |
|---|---|---|---|---|
| pancikula69 | Unverified candidate | No explicit boot evidence | Unknown | <https://github.com/pancikula69/peridot-nethunter-kernel> |

### Xiaomi POCO X2 / Redmi K30 (`phoenix`)
No official NetHunter registry variant.

**Community projects**

| Project | Status | Boot evidence | Features claimed/tested | Source |
|---|---|---|---|---|
| MDXWAJID | Unverified candidate | No explicit boot evidence | Unknown | <https://github.com/MDXWAJID/phoenix-nethunter-kernel> |
| MDXWAJID | Unverified candidate | No explicit boot evidence | Unknown | <https://github.com/MDXWAJID/poco-x2-nethunter-kernel> |

### Xiaomi Pad 6 (`pipa`)
No official NetHunter registry variant.

**Community projects**

| Project | Status | Boot evidence | Features claimed/tested | Source |
|---|---|---|---|---|
| ruik3z | Developer claimed | Unknown | Unknown | <https://github.com/ruik3z/kernel-pipa> |

### Xiaomi Poco X3 NFC (PixelOS) (`surya-16`)
**Official NetHunter registry variants**

| ROM | Android | Kernel | Author | Source |
|---|---|---|---|---|
| PixelOS Android 16 QPR2 | sixteen | 4.14 | dr1408 | <https://github.com/dr1408/kernel_xiaomi_surya_16> |

### Xiaomi Pocophone F1 (`beryllium`)
**Official NetHunter registry variants**

| ROM | Android | Kernel | Author | Source |
|---|---|---|---|---|
| Xiaomi Pocophone F1 for stock Android | eleven | 4.9 | Hilledkinged & yesimxev | Unknown |
| LineageOS 21 | fourteen | 4.9 | Strix Vyxlor | <https://github.com/Strix-Vyxlor/android_kernel_xiaomi_sdm845> |

Search discoveries (metadata only, not inspected): 2. See `data/nethunter_search_candidates.csv`.

### Xiaomi Pocophone F3 (`alioth`)
**Official NetHunter registry variants**

| ROM | Android | Kernel | Author | Source |
|---|---|---|---|---|
| Android 14 | fourteen | 4.19 | Hani K. | <https://github.com/Hani-K/Bifr0st.git> |

Search discoveries (metadata only, not inspected): 1. See `data/nethunter_search_candidates.csv`.

### Xiaomi Pocophone X3 NFC (`surya`)
**Official NetHunter registry variants**

| ROM | Android | Kernel | Author | Source |
|---|---|---|---|---|
| LineageOS 20 | thirteen | 4.9 | r0ttenbeef | <https://github.com/r0ttenbeef/android_kernel_xiaomi_surya> |

Search discoveries (metadata only, not inspected): 3. See `data/nethunter_search_candidates.csv`.

### Xiaomi Pocophone X3 Pro (`vayu`)
**Official NetHunter registry variants**

| ROM | Android | Kernel | Author | Source |
|---|---|---|---|---|
| Xiaomi Pocophone X3 Pro for stock Android | eleven | 4.14 | cyberknight777 | Unknown |

Search discoveries (metadata only, not inspected): 4. See `data/nethunter_search_candidates.csv`.

### Xiaomi Redmi 10C (`fog`)
No official NetHunter registry variant.

**Community projects**

| Project | Status | Boot evidence | Features claimed/tested | Source |
|---|---|---|---|---|
| anomaly-4rc | Unverified candidate | No explicit boot evidence | Unknown | <https://github.com/anomaly-4rc/android_kernel_xiaomi_fog-nethunter> |

### Xiaomi Redmi 15 (`creek`)
No official NetHunter registry variant.

**Community projects**

| Project | Status | Boot evidence | Features claimed/tested | Source |
|---|---|---|---|---|
| dr1408 | Unverified candidate | No explicit boot evidence | internal wifi support, packet injection | <https://github.com/dr1408/Creek_Nethunter> |

### Xiaomi Redmi 3 / 3 Pro (`ido`)
**Official NetHunter registry variants**

| ROM | Android | Kernel | Author | Source |
|---|---|---|---|---|
| LineageOS 14.1 | nougat | 3.10 | ariafan | <https://github.com/ariafan/ido_kernel-kali.git> |

Search discoveries (metadata only, not inspected): 1. See `data/nethunter_search_candidates.csv`.

### Xiaomi Redmi 4 / 4X (`santoni`)
No official NetHunter registry variant.

**Community projects**

| Project | Status | Boot evidence | Features claimed/tested | Source |
|---|---|---|---|---|
| MomboteQ | Unverified candidate | No explicit boot evidence | Unknown | <https://github.com/MomboteQ/hackphone_kernel_xiaomi_msm8937> |

### Xiaomi Redmi 4 Prime (`markw`)
**Official NetHunter registry variants**

| ROM | Android | Kernel | Author | Source |
|---|---|---|---|---|
| LineageOS 15.1 | oreo | 3.18 | fasheng | <https://github.com/fasheng/nethunter_kernel_msm8953_markw> |
| LineageOS 16 | pie | 3.18 | fasheng | <https://github.com/fasheng/nethunter_kernel_msm8953_markw> |

### Xiaomi Redmi 4/4X (`santoni`)
**Official NetHunter registry variants**

| ROM | Android | Kernel | Author | Source |
|---|---|---|---|---|
| MIUI 9.0 | nougat | 3.18 | santoni | <https://github.com/DroidKali/santoni_kernel_nethunter.git> |
| VoltageOS 2.x (A13) | thirteen | 4.9.227 | MomboteQ | <https://github.com/MomboteQ/hackphone_kernel_xiaomi_msm8937> |

### Xiaomi Redmi 5A (`riva`)
**Official NetHunter registry variants**

| ROM | Android | Kernel | Author | Source |
|---|---|---|---|---|
| crDroid Android 14 | fourteen | 4.9 | ShorterKing | <https://github.com/ShorterKing/Nethunter-Kernel-Redmi5A-Riva> |

### Xiaomi Redmi 6 Pro (`sakura`)
**Official NetHunter registry variants**

| ROM | Android | Kernel | Author | Source |
|---|---|---|---|---|
| LineageOS | ten | 4.09 | dek0der | <https://github.com/dek0der/nethunter_kernel_redmi_6_pro_sakura> |
| LineageOS | eleven | 4.09 | dek0der | <https://github.com/dek0der/nethunter_kernel_redmi_6_pro_sakura> |

### Xiaomi Redmi 8 / 8A / 7A (SDM439) (`olive/olivelite/olivewood/pine`)
No official NetHunter registry variant.

**Community projects**

| Project | Status | Boot evidence | Features claimed/tested | Source |
|---|---|---|---|---|
| atsauban | Unverified candidate | No explicit boot evidence | Unknown | <https://github.com/atsauban/android_kernel_xiaomi_sdm439> |

### Xiaomi Redmi 8A (`olivelite`)
No official NetHunter registry variant.

**Community projects**

| Project | Status | Boot evidence | Features claimed/tested | Source |
|---|---|---|---|---|
| wolfxalpha4 | Developer claimed | No explicit boot evidence | external wifi support, packet injection, hid gadget, usb gadget | <https://github.com/wolfxalpha4/nethunter-kernel-olivelite> |

### Xiaomi Redmi 8A Dual (`olivelite`)
No official NetHunter registry variant.

**Community projects**

| Project | Status | Boot evidence | Features claimed/tested | Source |
|---|---|---|---|---|
| sunilkumardasdev | Unverified candidate | No explicit boot evidence | Unknown | <https://gitlab.com/sunilkumardasdev/redmi-8a-dual-nethunter-kernel> |

### Xiaomi Redmi 9 Power (`lime`)
No official NetHunter registry variant.

**Community projects**

| Project | Status | Boot evidence | Features claimed/tested | Source |
|---|---|---|---|---|
| l3tchupkt | Developer claimed | No explicit boot evidence | external wifi support, monitor mode, packet injection, hid gadget | <https://github.com/l3tchupkt/redmi9power-nethunter-kernel> |

### Xiaomi Redmi 9C NFC (`angelican`)
No official NetHunter registry variant.

**Community projects**

| Project | Status | Boot evidence | Features claimed/tested | Source |
|---|---|---|---|---|
| edmondseropyan6 | Unverified candidate | No explicit boot evidence | Unknown | <https://gitlab.com/edmondseropyan6/nethunter_kernel_xiaomi_angelican> |

### Xiaomi Redmi Note 10 Pro (`sweet`)
No official NetHunter registry variant.

**Community projects**

| Project | Status | Boot evidence | Features claimed/tested | Source |
|---|---|---|---|---|
| RiasJ1Dar | Developer claimed | No explicit boot evidence | external wifi support, monitor mode, packet injection, hid gadget, usb gadget | <https://github.com/RiasJ1Dar/sweet-nethunter-kernel> |
| RiasJ1Dar | Unverified candidate | No explicit boot evidence | Unknown | <https://gitlab.com/RiasJ1Dar/sweet-nethunter-kernel> |

### Xiaomi Redmi Note 11 (fleur) (`fleur`)
No official NetHunter registry variant.

**Community projects**

| Project | Status | Boot evidence | Features claimed/tested | Source |
|---|---|---|---|---|
| Sudarshanb789 | Unverified candidate | No explicit boot evidence | Unknown | <https://github.com/Sudarshanb789/fleur-nethunter-kernel> |

### Xiaomi Redmi Note 4 / 4X (`mido`)
No official NetHunter registry variant.

**Community projects**

| Project | Status | Boot evidence | Features claimed/tested | Source |
|---|---|---|---|---|
| chkndrp | Abandoned | No explicit boot evidence | Unknown | <https://github.com/chkndrp/device_xiaomi_mido-nethunter-kernel> |
| linlinger | Unverified candidate | No explicit boot evidence | Unknown | <https://github.com/linlinger/kernel_xiaomi_mido> |

### Xiaomi Redmi Note 4X (`mido`)
**Official NetHunter registry variants**

| ROM | Android | Kernel | Author | Source |
|---|---|---|---|---|
| Pixel Experience | eleven | 4.9 | linlinger | <https://github.com/linlinger/kernel_xiaomi_mido.git> |
| LineageOS kernel with NetHunter features enabled | fourteen | 4.9 | Serp3n7 | <https://github.com/Serp3n7/kernel_xiaomi_mido.git> |

Search discoveries (metadata only, not inspected): 4. See `data/nethunter_search_candidates.csv`.

### Xiaomi Redmi Note 5 Pro (`whyred`)
**Official NetHunter registry variants**

| ROM | Android | Kernel | Author | Source |
|---|---|---|---|---|
| LineageOS 18.1 | eleven | 4.4 | notatallnic189 | <https://github.com/notatallnic189/whyred-nethunter-kernel> |

Search discoveries (metadata only, not inspected): 2. See `data/nethunter_search_candidates.csv`.

### Xiaomi Redmi Note 6 Pro (`tulip`)
**Official NetHunter registry variants**

| ROM | Android | Kernel | Author | Source |
|---|---|---|---|---|
| Android 11 | eleven | 4.4 | TheKidBaby | Unknown |

### Xiaomi Redmi Note 7 (`lavender`)
No official NetHunter registry variant.

**Community projects**

| Project | Status | Boot evidence | Features claimed/tested | Source |
|---|---|---|---|---|
| sauravsinha239 | Unverified candidate | No explicit boot evidence | Unknown | <https://github.com/sauravsinha239/Nethunter_kernel_lavender> |

### Xiaomi Redmi Note 8 (`ginkgo`)
No official NetHunter registry variant.

**Community projects**

| Project | Status | Boot evidence | Features claimed/tested | Source |
|---|---|---|---|---|
| medlam1981 | Developer claimed | No explicit boot evidence | internal wifi support, monitor mode, packet injection, hid gadget, usb gadget | <https://github.com/medlam1981/ginkgo_ai_kernel> |

### Xiaomi Redmi Note 8 Pro (`begonia`)
No official NetHunter registry variant.

**Community projects**

| Project | Status | Boot evidence | Features claimed/tested | Source |
|---|---|---|---|---|
| artnigman-art | Developer claimed | No explicit boot evidence | external wifi support, monitor mode, hid gadget, usb gadget | <https://github.com/artnigman-art/begonia-nethunter-kernel> |
| bhindasinghcommunications123-sketch | Developer claimed | No explicit boot evidence | external wifi support, monitor mode, hid gadget, usb gadget | <https://github.com/bhindasinghcommunications123-sketch/begonia-nethunter-kernel> |
| fxritadicc | Developer claimed | No explicit boot evidence | external wifi support, monitor mode, packet injection, hid gadget, usb gadget | <https://github.com/fxritadicc/begonia-kali_nethunter-kernel> |
| tarq04125-lang | Unverified candidate | No explicit boot evidence | Unknown | <https://github.com/tarq04125-lang/begonia-nethunter-kernel> |
| tarq04125-lang | Unverified candidate | No explicit boot evidence | Unknown | <https://github.com/tarq04125-lang/begonia-NetHunter-Kernel-A14> |
| Thirushub | Unverified candidate | No explicit boot evidence | Unknown | <https://github.com/Thirushub/begonia-nethunter-kernel> |

### Xiaomi Redmi Note 9S (`curtana`)
No official NetHunter registry variant.

**Community projects**

| Project | Status | Boot evidence | Features claimed/tested | Source |
|---|---|---|---|---|
| Saamitk | Developer claimed | No explicit boot evidence | internal wifi support, external wifi support, monitor mode, packet injection, hid gadget, usb gadget | <https://github.com/Saamitk/NetHunter-Kernel-Kit-Xiaomi-Redmi-Note-9S-curtana-> |

### Xiaomi Redmi Note 9S/Pro (`miatoll`)
**Official NetHunter registry variants**

| ROM | Android | Kernel | Author | Source |
|---|---|---|---|---|
| crDroid 15.0 | fifteen | 4.14 | jolucas245 | <https://github.com/crdroidandroid/android_kernel_xiaomi_sm6250.git> |

Search discoveries (metadata only, not inspected): 1. See `data/nethunter_search_candidates.csv`.

### Xiaomi device (cas) (`cas`)
No official NetHunter registry variant.

**Community projects**

| Project | Status | Boot evidence | Features claimed/tested | Source |
|---|---|---|---|---|
| fahmigk | Unverified candidate | No explicit boot evidence | Unknown | <https://github.com/fahmigk/cas-nethunter-kernel> |

### Xiaomi device (sunny) (`sunny`)
No official NetHunter registry variant.

**Community projects**

| Project | Status | Boot evidence | Features claimed/tested | Source |
|---|---|---|---|---|
| Neternels | Unverified candidate | No explicit boot evidence | Unknown | <https://github.com/Neternels/android_kernel_xiaomi_sunny> |

### Xiaomi device (sunstone/moonstone) (`sunstone/moonstone`)
No official NetHunter registry variant.

**Community projects**

| Project | Status | Boot evidence | Features claimed/tested | Source |
|---|---|---|---|---|
| dare-devil-ex | Unverified candidate | No explicit boot evidence | Unknown | <https://github.com/dare-devil-ex/kernel_xiaomi_stone> |
| Adithyancoder | Unverified candidate | No explicit boot evidence | Unknown | <https://github.com/Adithyancoder/Stone-kernel-Nethunter-17> |

### Xiaomi juice (`juice`)
No official NetHunter registry variant.

**Community projects**

| Project | Status | Boot evidence | Features claimed/tested | Source |
|---|---|---|---|---|
| Jemacivan | Developer claimed | Unknown | Unknown | <https://github.com/jemacivan/android_nethunter_kernel_xiaomi_juice> |


## ZTE
Devices/codenames: 1. Official variants: 1. Community projects: 0.
### ZTE Axon 7 (`ailsa-ii`)
**Official NetHunter registry variants**

| ROM | Android | Kernel | Author | Source |
|---|---|---|---|---|
| Android 6 | marshmallow | 3.18 | jcadduono | <https://github.com/jcadduono/android_kernel_zte_msm8996.git> |


## vivo
Devices/codenames: 1. Official variants: 0. Community projects: 1.
### vivo iQOO Neo 9 (`neo9`)
No official NetHunter registry variant.

**Community projects**

| Project | Status | Boot evidence | Features claimed/tested | Source |
|---|---|---|---|---|
| meoflii | Unverified candidate | No explicit boot evidence | Unknown | <https://github.com/meoflii/nethunter-kernel-neo9> |


## Unknown
Devices/codenames: 10. Official variants: 13. Community projects: 17.
### F(x)tec Pro1 X (`pro1x`)
No official NetHunter registry variant.

**Community projects**

| Project | Status | Boot evidence | Features claimed/tested | Source |
|---|---|---|---|---|
| xokitten999 | Developer claimed | No explicit boot evidence | monitor mode, hid gadget, usb gadget | <https://github.com/xokitten999/pro1x-nethunter-kernel> |

### Jiayu S3 Advanced (`jiayus3a`)
**Official NetHunter registry variants**

| ROM | Android | Kernel | Author | Source |
|---|---|---|---|---|
| Android 6 | marshmallow | 3.10 | DKingCN | <https://github.com/DKingCN/android_kernel_jiayu_s3_h560.git> |

### Nubia Z17 (`nx563j`)
**Official NetHunter registry variants**

| ROM | Android | Kernel | Author | Source |
|---|---|---|---|---|
| LineageOS 22.2 | fifteen | 4.04 | luckylca | <https://github.com/luckylca/android_kernel_nubia_msm8998_nethunter> |

**Community projects**

| Project | Status | Boot evidence | Features claimed/tested | Source |
|---|---|---|---|---|
| HiterretiH | Abandoned | No explicit boot evidence | Unknown | <https://github.com/HiterretiH/nx589j_nougat_kernel_nethunter> |

### Planet Computers Gemini PDA (`gemini4g`)
**Official NetHunter registry variants**

| ROM | Android | Kernel | Author | Source |
|---|---|---|---|---|
| Android 7.1 Boot Partition 1 | nougat | 3.18 | Re4son | <https://github.com/Re4son/gemini-kali-linux-kernel-3.18> |
| Android 8.1 Boot Partition 1 | oreo | 3.18 | Re4son | <https://github.com/Re4son/gemini-kali-linux-kernel-3.18> |
| Android 7.1 Boot Partition 2 | nougat | 3.18 | Re4son | <https://github.com/Re4son/gemini-kali-linux-kernel-3.18> |
| Android 8.1 Boot Partition 2 | oreo | 3.18 | Re4son | <https://github.com/Re4son/gemini-kali-linux-kernel-3.18> |
| Android 7.1 Boot Partition 3 | nougat | 3.18 | Re4son | <https://github.com/Re4son/gemini-kali-linux-kernel-3.18> |
| Android 8.1 Boot Partition 3 | oreo | 3.18 | Re4son | <https://github.com/Re4son/gemini-kali-linux-kernel-3.18> |

### TicWatch Pro / Pro 4G/LTE / Pro 2020 (`ticwatchpro`)
**Official NetHunter registry variants**

| ROM | Android | Kernel | Author | Source |
|---|---|---|---|---|
| Wear OS 2.29 | wearos | 3.18 | yesimxev | <https://github.com/yesimxev/msm-catfish-9.0-wear-os> |

### TicWatch Pro 3 GPS/LTE / Pro 3 Ultra GPS/LTE (`ticwatchpro3`)
**Official NetHunter registry variants**

| ROM | Android | Kernel | Author | Source |
|---|---|---|---|---|
| OneOS (Wear OS 2.44) | wearos | 4.09 | yesimxev | <https://github.com/yesimxev/mobvoi-ticwatch-kernel> |

### Unknown (`Unknown`)
No official NetHunter registry variant.

**Community projects**

| Project | Status | Boot evidence | Features claimed/tested | Source |
|---|---|---|---|---|
| ahmed-alnassif | Developer claimed | No explicit boot evidence | external wifi support, packet injection | <https://github.com/ahmed-alnassif/GKID-Kernels> |
| arouf0 | Unverified candidate | No explicit boot evidence | Unknown | <https://github.com/arouf0/nethunter-kernel> |
| beronathan9-sudo | Unverified candidate | No explicit boot evidence | Unknown | <https://github.com/beronathan9-sudo/nethunter-kernel> |
| DEADMAN610716 | Unverified candidate | No explicit boot evidence | Unknown | <https://github.com/DEADMAN610716/my-nethunter-kernel> |
| deviljin05 | Unverified candidate | No explicit boot evidence | Unknown | <https://github.com/deviljin05/GKI-NETHUNTER-KERNEL> |
| deviljin05 | Developer claimed | No explicit boot evidence | external wifi support, monitor mode, packet injection | <https://github.com/deviljin05/GKI-NETHUNTER-KERNEL-5.10-REDEFINED> |
| deviljin05 | Unverified candidate | No explicit boot evidence | Unknown | <https://github.com/deviljin05/GKI-NETHUNTER-KERNEL-WITH-DRIVER-2> |
| deviljin05 | Unverified candidate | No explicit boot evidence | Unknown | <https://github.com/deviljin05/Kali-nethunter-kernel-gki-5.10> |
| deviljin05 | Unverified candidate | No explicit boot evidence | Unknown | <https://github.com/deviljin05/Kali-nethunter-kernel-testing-phase-> |
| deviljin05 | Unverified candidate | No explicit boot evidence | Unknown | <https://github.com/deviljin05/kali-nethunter-kernel-testing-phase-2-> |
| MechRocker | Abandoned | No explicit boot evidence | Unknown | <https://github.com/MechRocker/kernel-nethunter> |
| portuguezhj34-spec | Unverified candidate | No explicit boot evidence | Unknown | <https://github.com/portuguezhj34-spec/Nethunter-kernel> |
| secretoryx | Unverified candidate | No explicit boot evidence | Unknown | <https://github.com/secretoryx/nethunter-kernel> |
| zahirrayhan | Abandoned | No explicit boot evidence | Unknown | <https://github.com/zahirrayhan/Nethunter-Kernel> |

### Unknown (`lilium/chime`)
No official NetHunter registry variant.

**Community projects**

| Project | Status | Boot evidence | Features claimed/tested | Source |
|---|---|---|---|---|
| agussaepul0-cloud | Unverified candidate | No explicit boot evidence | Unknown | <https://github.com/agussaepul0-cloud/kernel-lilium-chime-nethunter-RT5370> |

### Yu Yunique (`jalebi`)
**Official NetHunter registry variants**

| ROM | Android | Kernel | Author | Source |
|---|---|---|---|---|
| LineageOS 14.1 | nougat | 3.10 | Satyabrat Sahoo | <https://github.com/thelazyindian/kernel_8916.git> |

### nVidea Shield Tablet (`shieldtablet`)
**Official NetHunter registry variants**

| ROM | Android | Kernel | Author | Source |
|---|---|---|---|---|
| Android 6.0 | marshmallow | 3.10 | jcadduono | <https://github.com/jcadduono/android_kernel_nvidia_shield.git> |
| Android 7.1 | nougat | 3.10 | SecurityAddicted | <https://github.com/SecurityAddicted/android_kernel_nvidia_shieldtablet> |

