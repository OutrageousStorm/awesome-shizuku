#!/usr/bin/env python3
"""
battery_limit.py -- Charge limiter using Shizuku shell access
Sets a charge limit (e.g., 80%) to preserve battery health
Requires: Shizuku running
Usage: python3 battery_limit.py --limit 80
"""
import subprocess, sys, argparse, time

def shizuku_adb(cmd):
    """Execute command via Shizuku shell access"""
    r = subprocess.run(['adb', 'shell', cmd], capture_output=True, text=True)
    return r.stdout.strip()

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--limit', type=int, default=80, help='Charge limit percentage (default: 80)')
    args = parser.parse_args()

    print(f"🔋 Battery Charge Limiter (Shizuku)")
    print(f"Setting limit to {args.limit}%")

    # Get current battery level
    level = shizuku_adb("dumpsys battery | grep level")
    print(f"Current: {level}")

    # Write to battery charger limit file (device-dependent path)
    # Common paths: /sys/class/power_supply/battery/charge_control_limit_max
    paths = [
        "/sys/class/power_supply/battery/charge_control_limit_max",
        "/sys/class/power_supply/bms/charge_control_limit_max",
        "/sys/class/power_supply/charge/charge_control_limit_max",
    ]

    for path in paths:
        try:
            # Calculate max charge limit (0-100)
            limit_val = int(args.limit)
            result = shizuku_adb(f"su -c 'echo {limit_val} > {path}'")
            if "Permission denied" not in result:
                print(f"✓ Limit set via {path}")
                return
        except:
            continue

    print("✗ Could not set limit (device may not support charge limiting)")

if __name__ == "__main__":
    main()
