# Kali NetHunter Kernel Database - Batch 1

Generated October 2026. Conservative evidence model: no entry is marked "Verified boot" without an explicit boot report. `Claimed` means the repository text says so; it is not independent verification.

Rows: 560. Sources: official registry + public GitHub/GitLab/Codeberg search.

## Status distribution

| Status | Rows |
|---|---:|
| Source confirmed | 275 |
| Unverified candidate | 248 |
| Abandoned | 26 |
| Developer claimed | 11 |

## Feature claims (not verification)

| Feature | Rows claiming |
|---|---:|
| monitor_mode | 9 |
| packet_injection | 8 |
| hid_gadget | 5 |
| external_wifi_support | 9 |
| usb_gadget | 1 |

## Fields

All fields requested by the mission are present. `Unknown` means no evidence was found; it is never filled by assumption.

`device_name, model_number, codename, chipset, android_version, kernel_version, rom_compatibility, nethunter_features, internal_wifi_support, external_wifi_support, monitor_mode, packet_injection, hid_gadget, usb_gadget, required_drivers, required_patches, root_requirements, bootloader_requirements, installation_method, developer, repository_url, release_url, discussion_url, last_update, evidence_level, verification_status, known_limitations, confidence, notes`

## Machine-readable

- `data/nethunter_database_batch1.csv` - full database
- `data/android_device_inventory.csv` - device inventory across sources
- `data/nethunter_batch1_summary.json` - counts
- `data/nethunter_independent_kernels.csv` - discovery layer
