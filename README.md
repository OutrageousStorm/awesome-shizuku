# Awesome Shizuku

Curated list of the best Shizuku-powered Android apps. [What is Shizuku?](https://shizuku.rikka.app)

Shizuku allows apps to access ADB-level APIs **without root** — you grant permission once via the Shizuku UI.

## Installation

1. Install [Shizuku Manager](https://github.com/RikkaApps/Shizuku) from Play Store or F-Droid
2. (Easiest) Use wireless ADB: Settings → Developer Options → Wireless Debugging
3. Or USB: `adb shell sh /sdcard/Android/data/moe.shizuku.privileged.api/files/start.sh`
4. Grant Shizuku permission to each app that requests it

## Featured Apps

### System & Management
- **[App Manager](https://muntashirakon.github.io/AppManager/)** — Full app control: uninstall, backup, permission audit
- **[Shelter](https://exyed.github.io/Shelter/)** — Work profile isolation — freeze/unfreeze apps instantly
- **[BusyBox Installer](https://play.google.com/store/apps/details?id=ru.meefik.busybox)** — Linux utilities on Android
- **[Storage Scopes](https://play.google.com/store/apps/details?id=com.xayah.spacein)** — Granular storage permissions

### Battery & Performance
- **[AccA](https://github.com/MatteCarra/AccA)** — Charging limits, temperature control, diagnostics
- **[System Tuner Pro](https://play.google.com/store/apps/details?id=rs.Inthehand.Frequency)** — CPU/GPU frequency scaling

### Network & Privacy
- **[NetGuard](https://netguard.me)** — Per-app VPN firewall (full network blocking per-app)
- **[TrackerControl](https://trackercontrol.org)** — Monitor and block tracker servers
- **[DNS Changer](https://play.google.com/store/apps/details?id=com.frostnerd.smokescreen)** — System-wide encrypted DNS

### Customization
- **[KWGT](https://play.google.com/store/apps/details?id=org.kustom.widget)** — Powerful widget builder with system data access

## Why Shizuku Instead of Root?

| Feature | Root | Shizuku |
|---------|------|---------|
| Requires bootloader unlock | Yes | No |
| Survives updates | Sometimes | Yes |
| Easier to disable | No | Yes (revoke in Settings) |
| Can install system apps | Yes | Via App Manager |
| Less invasive | No | Yes |

---

*Last updated: 2026-04-18*
**Maintained by [OutrageousStorm](https://github.com/OutrageousStorm)**
