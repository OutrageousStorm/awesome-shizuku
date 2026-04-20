# Installing Shizuku

## What is Shizuku?
Shizuku grants apps ADB-level shell access without rooting.

## Setup

### First time (one-time setup)
```bash
# 1. Enable USB Debugging on device
adb shell sh /sdcard/Android/data/moe.shizuku.privileged.api/start.sh
```

### Wireless Shizuku (Android 11+)
```bash
# Enable Wireless Debugging in Developer Options
adb pair <device-ip>:port <pairing-code>
adb connect <device-ip>:port
adb shell sh /sdcard/.../start.sh
```

### For developers: using Shizuku in your app
```kotlin
val binder = ShizukuSystemServerBinderCode.getSystemServerBinder()
val ipc = IShellService.Stub.asInterface(binder)
ipc.execute("pm list packages")  // now has adb privileges
```

See [Docs](https://shizuku.rikka.app/guide/setup/) for detailed walkthrough.
