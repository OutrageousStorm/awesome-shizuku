# Awesome Shizuku

Apps that use Shizuku to grant privileges without rooting.

## What is Shizuku?

Shizuku is an Android app that grants **ADB shell access** to other apps via IPC. No root needed. Works on Android 6+.

**GitHub:** https://github.com/RikkaApps/Shizuku

## Apps

| App | Category | Link |
|-----|----------|------|
| **App Manager** | System | [GitHub](https://github.com/muntashirakon/AppManager) |
| **Always On AMOLED** | UI | [GitHub](https://github.com/BasharatAliKing/Always-On-AMOLED) |
| **NetGuard** | Firewall | [F-Droid](https://f-droid.org/packages/eu.faircode.netguard/) |
| **MacroDroid** | Automation | [Play Store](https://play.google.com/store/apps/details?id=com.arlosoft.macrodroid) |

## Install

1. Download Shizuku from [GitHub](https://github.com/RikkaApps/Shizuku/releases)
2. Enable USB Debugging
3. Run: `adb shell sh /sdcard/Android/data/moe.shizuku.privileged.api/start.sh`
4. Grant permission in app

*See [Shizuku docs](https://shizuku.rikka.app) for full guide*
