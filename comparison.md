# Shizuku vs Other Root Methods

Comprehensive comparison of Shizuku and alternatives.

## Shizuku vs Magisk vs Root

| Feature | Shizuku | Magisk | Full Root |
|---------|---------|--------|-----------|
| No bootloader unlock | ✅ | ✗ | ✗ |
| Per-app scope | ✅ | Limited | N/A |
| OTA safe | ✅ | Survives | ✗ |
| Detection resistance | ✅ Very high | Good | Poor |
| Module ecosystem | Growing | Massive | Many |
| Kernel tweaks | ✗ | ✅ | ✅ |
| Custom ROM needed | ✗ | ✗ | ✅ |
| App permission level | shell (UID 2000) | root (UID 0) | Unlimited |
| Device modifications | None | Minimal | Extensive |

## What Each Can Do

### Shizuku (Shell UID 2000)
✅ Package manager (`pm`) operations  
✅ Activity manager (`am`) commands  
✅ Settings access  
✅ Dumpsys queries  
✅ Input simulation  
✅ Per-app permissions via Shizuku  
❌ Kernel patches  
❌ Insmod (load kernel modules)  
❌ Rw access to /system  

### Magisk (Root UID 0)
✅ Everything Shizuku can do  
✅ Kernel tweaks  
✅ Module system  
✅ Init.d scripts  
✅ /system modifications (systemless)  
✅ Advanced root hiding  
❌ Without custom ROM requires bootloader unlock  

### Full Root (Rooted Device)
✅ Absolute control  
✅ Direct filesystem access  
✅ Kernel modification  
✅ SELinux bypass  
⚠️ Device becomes unstable/unsecure  
❌ Most apps detect and block you  

## Real-World Use Cases

| Use Case | Best Tool | Why |
|----------|-----------|-----|
| Debloat apps | Shizuku | No root needed, per-app safe |
| Privacy audit | Shizuku + App Manager | Shell access enough |
| Battery optimization | Magisk (GMS Doze) | Needs modules |
| Custom ROM tweaks | Magisk | Module system |
| Banking (sensitive) | Shizuku | Lowest detection risk |
| Gaming | None needed | ROM should be enough |
| Video recording | Shizuku + scrcpy | No root required |
| Frida hooking | Full root | Needs ptrace |

## Device Support

| OS Version | Shizuku Available | Magisk Available |
|-----------|-------------------|-----------------|
| Android 6-7 | ✗ (adb only) | ✅ |
| Android 8-10 | ✅ (wireless debug) | ✅ |
| Android 11+ | ✅ (wireless debug) | ✅ |
| GrapheneOS | ✅ (Sandboxed Play) | ❌ (locked) |
| Stock Samsung | ✅ | ⚠️ (Knox) |
| Stock Pixel | ✅ | ✅ |

## Recommendation Matrix

Choose based on your device + goal:

```
Need kernel tweaks?
  YES  → Magisk (bootloader unlock required)
  NO   → Check next

Banking/sensitive apps?
  YES  → Shizuku (lowest detection)
  NO   → Check next

Want module ecosystem?
  YES  → Magisk
  NO   → Shizuku

Running GrapheneOS?
  YES  → Shizuku only
  NO   → Your choice

Can unlock bootloader?
  YES  → Magisk + Shizuku (best of both)
  NO   → Shizuku + custom ROM or ADB only
```
