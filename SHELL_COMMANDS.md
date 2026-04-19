# Shizuku Shell Commands Guide

Use Shizuku to run ADB commands without a PC.

## Install Shizuku

1. Download: [F-Droid](https://f-Droid.org/packages/moe.shizuku.privileged.api) or [GitHub](https://github.com/RikkaApps/Shizuku)
2. Set it up: enable Wireless debugging (Settings → Developer Options)
3. Pair code from the system prompt

## Commands that work via Shizuku

### Permission management
```bash
pm revoke com.facebook.katana android.permission.ACCESS_FINE_LOCATION
pm revoke com.instagram.android android.permission.READ_CONTACTS
pm grant com.example.app android.permission.CAMERA
```

### Settings tweaks
```bash
settings put global limit_ad_tracking 1
settings put secure location_mode 0
settings put system screen_brightness 128
settings put global wifi_scan_always_enabled 0
```

### App management
```bash
pm uninstall -k --user 0 com.bloatware.app
pm clear com.example.app
am force-stop com.example.app
am start -n com.example.app/com.example.MainActivity
```

### Device info
```bash
getprop ro.build.version.release        # Android version
getprop ro.product.cpu.abi              # CPU architecture
dumpsys battery | grep level            # Battery percent
```

### Network diagnostics
```bash
netstat -tulnp | grep ESTABLISHED
ip addr show
ping -c 4 8.8.8.8
```

## Apps that use Shizuku

| App | Repo | Function |
|-----|------|----------|
| Weixin Jump Game Bot | XDA | Auto-play WeChat Moments game |
| Island | Play Store | App isolation & cloning |
| Tasker | Play Store | Automation (limited) |
| App Manager | GitHub | Full app control |
| Hail | GitHub | App freezer |

---

**Pro tip:** Combine Shizuku with Tasker for scheduled system tweaks!
