# NetHunter Feature Compatibility Matrix
The machine-readable matrix is `data/nethunter_feature_matrix.csv` (one row per official variant or community project).
## Evidence values
| Value | Meaning |
|---|---|
| `Developer-reported test` | The repository text describes an on-device test, measurement, or confirmed working state. Self-reported; not independently reproduced. |
| `Claimed by developer` | Repository text claims support, without a test result in the inspected text. |
| `Source/config evidence` | A driver, config option, or patch is present/mentioned; functionality is not established. |
| `Unknown` | No evidence found in the inspected text. Never filled by assumption. |

No row is marked independently verified. A kernel booting does not prove monitor mode, injection, or HID.

## Counts by feature (community projects)
| Feature | Developer-reported test | Claimed by developer | Source/config evidence | Unknown |
|---|---:|---:|---:|---:|
| internal wifi support | 3 | 3 | 10 | 294 |
| external wifi support | 4 | 10 | 15 | 267 |
| monitor mode | 7 | 7 | 22 | 259 |
| packet injection | 5 | 16 | 23 | 255 |
| hid gadget | 4 | 11 | 26 | 246 |
| usb gadget | 4 | 5 | 22 | 274 |

## Developer-reported monitor mode, packet injection, and HID
These rows contain an explicit positive claim in the inspected README/description. They are leads for reproduction, not verified compatibility.

### Monitor Mode

| Device | Project | Value | Evidence excerpt |
|---|---|---|---|
| Google Pixel 11 (`cubs`) | <https://github.com/Gajeel420/cubs-gki-rt2800usb> | Developer-reported test | \| Boot to Android 17 \| verified \| |
| Xiaomi Redmi Note 8 Pro (`begonia`) | <https://github.com/fxritadicc/begonia-kali_nethunter-kernel> | Developer-reported test | \| **USB HID Gadget (BadUSB)** \| ÇALIŞIYOR \| `/dev/hidg0` ve `/dev/hidg1` desteği ile Rubber Ducky (BadUSB) saldırıları. \| |
| OnePlus 8T (`kebab`) | <https://github.com/Mist3r-N0b0dy/NetHunter_Kernel-OP8T-crDroid12-A16> | Developer-reported test | > ## Status: SOLVED ✅ — kernel boots, monitor mode **and packet injection** work on both tested adapters |
| Pixel 9 Pro (`caiman`) | <https://github.com/shemed-mwangome/nethunter-komodo-usbwifi> | Developer-reported test | rides a `/vendor/firmware` overlay. Developed and verified on `6.1.162-android14-11-g2ec90535fa34-ab15810641`. > For authorized security testing on hardware and networks you own. Monitor mode / injection is a > penetrati |
| Pixel 9 Pro XL (`komodo`) | <https://github.com/shemed-mwangome/nethunter-komodo-usbwifi> | Developer-reported test | rides a `/vendor/firmware` overlay. Developed and verified on `6.1.162-android14-11-g2ec90535fa34-ab15810641`. > For authorized security testing on hardware and networks you own. Monitor mode / injection is a > penetrati |
| Pixel 9a (`tegu`) | <https://github.com/GPTmadeit/nethunter-pixel9a-rt2800usb> | Developer-reported test | hields.io/badge/kernel-GKI%206.1.145-38bdf8"> <img alt="driver" src="https://img.shields.io/badge/driver-rt2800usb-a78bfa"> <img alt="status" src="https://img.shields.io/badge/monitor%20mode-verified%20%E2%9C%93-22c55e"> |
| F(x)tec Pro1 X (`pro1x`) | <https://github.com/xokitten999/pro1x-nethunter-kernel> | Developer-reported test | # pro1x-nethunter-kernel A custom, NetHunter-patched Android kernel for the Fxtec Pro1X (SM6115/Bengal platform), built from source with Wi-Fi injection (confirmed working monitor mode) and USB HID/BadUSB gadget support  |

### Packet Injection

| Device | Project | Value | Evidence excerpt |
|---|---|---|---|
| Google Pixel 4a 5G (`bramble`) | <https://github.com/Hotelk52339/nethunter_kernel_google_redbull> | Developer-reported test | - **WiFi monitor mode** — native RX on internal WCN3998 (`con_mode=4`) |
| Realme X (`rmx1901`) | <https://github.com/ishashanknigam/kernel-realme-RMX1901> | Developer-reported test | \| WCN3998 packet injection (controlled Probe Requests) \| ✅ Verified \| Phase 7 independently captured all 20 controlled broadcast Probe Request transmissions over the air on channel 6; 20/20 exact frame matches \| |
| OnePlus 8T (`kebab`) | <https://github.com/Mist3r-N0b0dy/NetHunter_Kernel-OP8T-crDroid12-A16> | Developer-reported test | > ## Status: SOLVED ✅ — kernel boots, monitor mode **and packet injection** work on both tested adapters |
| Samsung Galaxy S10e (SM-G970N) (`beyond0lte`) | <https://github.com/unreliablecode/ArtisanROM-PomPomSU-NetHunter> | Developer-reported test | - USB HID, ACM, generic serial, RNDIS and mass storage. |
| POCO X5 5G (`moonstone`) | <https://github.com/edbastida/Kernel_Stone_DarkHuntermoon-Reborn> | Developer-reported test | atures ### WiFi & Injection - **wlan0 native frame injection** — qcacld-3.0 Madara273 5.4.302 series, validated 100% with `aireplay-ng --test` - mac80211 packet injection patch - wlan0 monitor mode support (QCACLD-3.0) - |

### Hid Gadget

| Device | Project | Value | Evidence excerpt |
|---|---|---|---|
| Xiaomi Redmi Note 8 Pro (`begonia`) | <https://github.com/fxritadicc/begonia-kali_nethunter-kernel> | Developer-reported test | \| **USB HID Gadget (BadUSB)** \| ÇALIŞIYOR \| `/dev/hidg0` ve `/dev/hidg1` desteği ile Rubber Ducky (BadUSB) saldırıları. \| |
| Nothing Phone (1) (`spacewar`) | <https://github.com/thw01f/nethunter-spacewar-kernel> | Developer-reported test | It boots on **crDroid 11 (Android 15)** and preserves working WiFi, touch, and Bluetooth while enabling NetHunter's attack surface. |
| F(x)tec Pro1 X (`pro1x`) | <https://github.com/xokitten999/pro1x-nethunter-kernel> | Developer-reported test | # pro1x-nethunter-kernel A custom, NetHunter-patched Android kernel for the Fxtec Pro1X (SM6115/Bengal platform), built from source with Wi-Fi injection (confirmed working monitor mode) and USB HID/BadUSB gadget support  |
| Redmi Note 10 Pro (`sweet`) | <https://github.com/piwwing23/sweet-kernel-NetHunter> | Developer-reported test | ctive* & *Performance* untuk menjaga stabilitas FPS (Zero Stuttering). * **GPU Boost:** Optimalisasi Adreno 618 untuk beban grafis intensif. ### 🛡️ Security & Pentesting * **Full Monitor Mode:** Dukungan penuh untuk audi |

## Official variants
The 275 official registry variants are published kernels with source links. Their feature columns are `Unknown` because the registry does not publish per-feature test results. They should not be read as evidence that a feature works.
