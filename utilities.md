# Shizuku Utilities

Command-line and automation tools powered by Shizuku.

| Tool | What it does | GitHub |
|------|-------------|--------|
| **App Manager** | Full app control — perms, ops, components, sigcheck | [GitHub](https://github.com/muntashirakon/AppManager) |
| **Blocker** | Block components, services, receivers system-wide | [GitHub](https://github.com/niranjan94/blocker) |
| **Shelter** | Clone & isolate apps in work profile | [GitHub](https://github.com/PeterCxy/Shelter) |
| **Brevent** | Prevent apps from running in background | [XDA](https://forum.xda-developers.com/t/brevent-prevent-apps-from-background.3382936/) |
| **Greenify** | Aggressive app hibernation (via Shizuku) | [Play Store](https://play.google.com/store/apps/details?id=com.oasisfeng.greenify) |
| **NetGuard** | Per-app firewall without VPN (when used with Shizuku) | [GitHub](https://github.com/M66B/NetGuard) |
| **Tasker** | Automation — full integration with Shizuku for ADB commands | [Play Store](https://play.google.com/store/apps/details?id=net.dinglisch.android.taskerm) |
| **ScreenFilter** | Dim below minimum brightness | [GitHub](https://github.com/xjunz/ScreenFilter) |
| **InsertCoin** | Advanced settings tweaker | XDA Forum |

## How to use

1. Install Shizuku app + grant it ADB access (via `adb shell sh /sdcard/Android/data/moe.shizuku.privileged.api/start.sh` or UI button)
2. Grant each app permission to use Shizuku in the Shizuku manager
3. Open the tool — it now has elevated ADB shell capabilities
