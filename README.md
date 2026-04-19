# 🚀 Awesome Shizuku

Curated list of the best apps that leverage Shizuku — the ADB root alternative.

**What is Shizuku?** A bridge to Android system APIs that normally require root. Started once via ADB or wireless debugging, any app can request Shizuku permission for elevated access without true root.

---

## 🔑 Best Shizuku Apps

### System Control & Tweaking
| App | Description | Link |
|-----|-------------|------|
| **App Manager** | Full control over apps — permissions, ops, components | [GitHub](https://github.com/MuntashirAkon/AppManager) |
| **Blocker** | Block apps, activities, services at system level | [GitHub](https://github.com/blokadaorg/blocker) |
| **Shelter** | Create isolated work profile | [GitHub](https://github.com/e1025298/Shelter) |
| **Warden** | Monitor & control app requests | [GitHub](https://github.com/theavege/warden) |
| **System Updater** | Flash OTA updates from file | [XDA](https://forum.xda-developers.com) |

### Privacy & Security
| App | Description | Link |
|-----|-------------|------|
| **Revoker** | Bulk-revoke permissions via Shizuku | [GitHub](https://github.com/zyx930/Revoker) |
| **Blocker** | Block network requests system-wide | [GitHub](https://github.com/blokada/blokada) |
| **NetGuard** | No-root firewall via Shizuku | [GitHub](https://github.com/M66B/NetGuard) |
| **TrackerControl** | Block trackers in all apps | [GitHub](https://github.com/TrackerControl/tracker-control-android) |

### Customization
| App | Description | Link |
|-----|-------------|------|
| **Iconify** | System-wide icon/UI theming | [GitHub](https://github.com/Mahmud0808/Iconify) |
| **Always On AMOLED** | Custom always-on-display | [Play Store](https://play.google.com/store/apps/details?id=com.tomer.alwaysonamoled) |
| **StatusBar Customization** | Tweak status bar | Various |

### Development & Debugging
| App | Description | Link |
|-----|-------------|------|
| **AppWatcher** | Monitor app updates & version changes | [GitHub](https://github.com/jokermonn/AppWatcher) |
| **Logcat Reader** | Full system logcat viewer | [GitHub](https://github.com/MuntashirAkon/LogcatReader) |

---

## How to Set Up Shizuku

### Method 1: Wireless Debugging (Android 11+, easiest)
```bash
# Enable wireless debugging on device
# Connect via:
adb pair <ip>:<pair_port> <pair_code>
adb connect <ip>:<port>

# Open Shizuku, it will detect the connection
```

### Method 2: USB Debugging
```bash
# Connect device via USB
adb shell sh /sdcard/shizuku_starter.sh
# Run this once, then apps can use Shizuku
```

---

*Want to add an app? Submit a PR!*
