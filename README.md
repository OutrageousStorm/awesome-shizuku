# Awesome Shizuku

Curated list of the best Shizuku-powered Android apps — elevated privileges without root.

## What is Shizuku?

Shizuku is a service that uses ADB (Android Debug Bridge) grants to give apps elevated permissions without requiring traditional root. Apps can request Shizuku access and get shell-level privileges for system operations.

**Official site:** https://shizuku.rikka.app

---

## System Administration

| App | What it does | GitHub |
|-----|-------------|--------|
| **App Manager** | Full app control — uninstall, permissions, component management | [MuntashirAkon](https://github.com/MuntashirAkon/AppManager) |
| **Bloatware Remover** | Safe debloat with rollback | [Gizmondian](https://github.com/Gizmondian/bloatware-remover) |
| **Button Mapper** | Remap physical buttons without root | [sds100](https://github.com/sds100/KeyMapper) |
| **Tasker** | Advanced automation via Shizuku | [joaomgcd](https://tasker.joaoapps.com) |
| **Shelter** | Profile isolation + work profile management | [evilkost](https://github.com/evilkost/Shelter) |

## Privacy & Security

| App | What it does |
|-----|-------------|
| **NetGuard** | Per-app firewall and traffic monitor |
| **TrackerControl** | Block trackers at network level |
| **PCAPdroid** | Packet capture and analysis |
| **Universal Android Debloater** | Mass app removal with safety checks |

## Device Control

| App | What it does |
|-----|-------------|
| **Macro Recorder** | Record and replay touch sequences |
| **AOD Suite** | Always-On Display customization |
| **SamFw Downloader** | Download Samsung firmware OTA |
| **Clipboard Manager** | Clipboard history and sync |

## Development Tools

| App | What it does |
|-----|-------------|
| **Logcat** | System logs with filtering |
| **Accessibility Inspector** | Debug accessibility services |
| **DatabaseInspector** | Browse device databases |

---

## Installing Apps with Shizuku

1. **Setup Shizuku:**
   - Install Shizuku app from F-Droid or Play Store
   - On first run, connect via USB ADB: `adb shell sh /sdcard/Android/data/moe.shizuku.privileged.api/start.sh`
   - Or enable Wireless Debugging (Android 11+) and pair directly

2. **Grant Shizuku access:**
   - Open app → Settings → Shizuku → enable
   - Shizuku Manager app will show a prompt
   - Tap to grant

3. **Result:** App gets shell-level access without the security risks of traditional root

---

## Why Shizuku instead of root?

| Feature | Shizuku | Magisk/Root |
|---------|---------|------------|
| Setup | ADB once, then wireless | Complex, risky |
| Detection | Very hidden | Detectable by apps |
| Safety | Can be revoked per-app | All-or-nothing |
| Updates | Survives OTA | Need to re-patch |
| Stability | Very stable | Can break things |

---

## Resources

- **Official docs:** https://shizuku.rikka.app
- **GitHub:** https://github.com/RikkaApps/Shizuku
- **XDA discussion:** https://forum.xda-developers.com/t/shizuku.4213519/

*Maintained by OutrageousStorm*
