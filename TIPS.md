# Shizuku Tips & Tricks

Advanced usage patterns for Shizuku.

---

## 1. Auto-start Shizuku via ADB

Save a script to your PC:

```bash
#!/bin/bash
# start-shizuku.sh
adb shell sh /sdcard/Shizuku/start.sh
```

Run whenever you need Shizuku:
```bash
./start-shizuku.sh
```

---

## 2. Combine with Tasker for Automation

Use **Tasker** plugin or script executor to run Shizuku commands on schedule or trigger:

```
Profile: Time-based
Task: Run shell command via Shizuku
  pm grant com.facebook.katana android.permission.ACCESS_FINE_LOCATION deny
```

---

## 3. Grant Dangerous Permissions Programmatically

Via Shizuku UserService (app code):

```kotlin
if (ShizukuHelper.isGranted()) {
    val result = ShizukuHelper.exec("pm grant ${packageName} android.permission.CAMERA")
    Log.d("Shizuku", result.output)
}
```

---

## 4. Persistent Background Tasks

Shizuku + WorkManager for periodic system commands:

```kotlin
val work = PeriodicWorkRequestBuilder<ShizukuWorker>(
    15, TimeUnit.MINUTES
).build()
WorkManager.getInstance(context).enqueueUniquePeriodicWork(
    "shizuku_task", ExistingPeriodicWorkPolicy.KEEP, work
)
```

---

## 5. No-Root Analytics Blocking

Disable telemetry dynamically:

```bash
# Via Shizuku terminal
pm revoke com.google.android.gms android.permission.BODY_SENSORS
settings put global limit_ad_tracking 1
```

---

## 6. Shizuku + Magisk Coexistence

Both can run together:

1. Install Magisk (root)
2. Install Shizuku from Magisk repo OR keep ADB version running
3. Both have their own permission domains

For apps: prefer Magisk root if available, fall back to Shizuku.

```kotlin
val hasRoot = Shell.getShell().isRoot
if (!hasRoot) {
    // Fall back to Shizuku
    requestShizukuPermission()
}
```

---

## 7. Monitor Shizuku Status

Check if Shizuku is running:

```bash
adb shell ps aux | grep shizuku
# or
adb shell getprop init.svc.shizuku
```

---

## 8. Wireless Debugging + Shizuku (Android 11+)

Start Shizuku once over USB, then:

```bash
adb tcpip 5555
adb connect <device-ip>:5555
# Shizuku persists over wireless ADB
```

---

## 9. Batch Permission Revocation

Revoke location + mic from all installed apps:

```bash
for pkg in $(adb shell pm list packages -3 | cut -d: -f2); do
  adb shell pm revoke "$pkg" android.permission.ACCESS_FINE_LOCATION 2>/dev/null
  adb shell pm revoke "$pkg" android.permission.RECORD_AUDIO 2>/dev/null
done
```

---

## 10. Custom Notifications via Shizuku

Show system notifications without root:

```bash
adb shell cmd notification post -S bigtext -t "Title" "Text"
```

---

See also: [awesome-shizuku](README.md)
