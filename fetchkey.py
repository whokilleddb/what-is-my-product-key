#!/usr/bin/env python3
import os
import re
import sys
import ctypes
import platform
import subprocess
from os import path

SYS_FILE = "/sys/firmware/acpi/tables/MSDM"

def is_admin():
    """Check if you are root/admin"""
    try:
        is_admin = (os.getuid() == 0)
    except AttributeError:
        is_admin = (ctypes.windll.shell32.IsUserAnAdmin() != 0)
    return is_admin


def check_key(key):
    pattern = r"^([A-Z0-9]{5}-){4}[A-Z0-9]{5}$"
    return re.match(pattern, key)


def windows():
    """Retireve Windows OEM Product Key from Windows"""
    print("[i] Platform Detected:\tWindows")

    out = subprocess.check_output("wmic path SoftwareLicensingService get OA3xOriginalProductKey", shell=True, universal_newlines=True)
    for key in out.split('\n'):
        if check_key(key.strip()):
            print("[i] Found Product Key\t", key)
            sys.exit(0)

    print("[!] Did not find Windows OEM product key!")
    sys.exit(-1)


def linux():
    """Retreieve Windows OEM Product key from Linux"""
    print("[i] Platform Detected\t Linux")

    # Check if file exists
    if not (path.exists(SYS_FILE) and path.isfile(SYS_FILE)):
        return -1

    print("[i] Trying to read MSDM table")
    out = subprocess.check_output(f"strings {SYS_FILE}", shell=True, universal_newlines=True)

    for key in out.split('\n'):
        if check_key(key.strip()):
            print("[i] Found Product Key\t", key)
            sys.exit(0)

    print("[!] Did not find Windows OEM product key!")
    sys.exit(-1)


def main():
    """Main function"""
    print("[i] Fetch Windows Product Key!")

    if not is_admin():
        print("[!] Run Program as Super User/Root", file=sys.stderr)
        sys.exit(-1)


    current_platform = platform.system()
    if current_platform == 'Windows':
        windows()

    elif current_platform == 'Linux':
        linux()

    else:
        print("[!] Unsupported Platform", file=sys.stderr)

if __name__ == '__main__':
    main()
