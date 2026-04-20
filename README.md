# Awesome Shizuku

Curated list of awesome Android apps using **Shizuku** — ADB access without root.

**What is Shizuku?** A framework that grants apps ADB-level privileges without rooting. Set up once via USB/wireless ADB, then launch Shizuku to expose the binder to apps.

[Official site](https://shizuku.rikka.app) | [GitHub](https://github.com/RikkaApps/Shizuku)

---

## System Tools

| App | What it does | Developer |
|-----|-------------|-----------|
| **App Manager** | Full app control — permissions, APK extraction, backup, component control | muntashirakon |
| **Shelter** | Work profile manager — isolate apps in a separate profile | Rikka |
| **Blocker** | Block apps, intents, and system components | Rikka |
| **Storage Isolator** | Restrict app access to specific folders | Rikka |

## Customization

| App | What it does |
|-----|-------------|
| **Tapir** | Custom quick settings tiles |
| **Icon Remixer** | Advanced icon packs and launchers integration |

## Privacy & Security

| App | What it does |
|-----|-------------|
| **NetGuard** | Per-app firewall — block internet access per app |
| **Trackercontrol** | Block trackers and monitor network connections |
| **PCAPdroid** | Full network traffic capture and analysis |

## Automation

| App | What it does |
|-----|-------------|
| **Tasker** (with Shizuku) | Advanced task automation via ADB actions |
| **KWGT** | Custom widgets with Shizuku actions |

---

## How to set up Shizuku

1. **Install the Shizuku app** from [F-Droid](https://f-droid.org/packages/moe.shizuku.privileged.api/) or [Play Store](https://play.google.com/store/apps/details?id=moe.shizuku.privileged.api)

2. **Via USB (one-time setup):**
   ```bash
   adb shell sh /sdcard/Android/data/moe.shizuku.privileged.api/files/start.sh
   ```

3. **Via wireless (easier):**
   - Settings → Developer Options → Wireless debugging (Android 11+)
   - In Shizuku app → Pair via adb
   - Done!

4. **Apps using Shizuku** can now request ADB-level access in their settings.

---

> **No root needed!** Shizuku = ADB access without bootloader unlock, custom ROM, or Magisk.
