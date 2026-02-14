import os
import sys

def get_visible_pids():
    """
    VIEW A: The 'Polite' View.
    Mimics 'ps' by trying to verify the process actually exists and is readable.
    """
    pids = set()
    try:
        # Iterate over /proc looking for numbered directories
        for filename in os.listdir('/proc'):
            if filename.isdigit():
                pid = int(filename)
                
                # CHECK: Can we actually read the process details?
                # If the directory is empty (mount bind trick) or permissions are weird,
                # this will fail, just like 'ps' would fail.
                try:
                    with open(f'/proc/{filename}/comm', 'r') as f:
                        _ = f.read()
                    pids.add(pid)
                except (FileNotFoundError, IOError):
                    # If we can't read the comm file, we consider it "invisible"
                    # or "broken" to the user-space.
                    continue
    except Exception as e:
        print(f"Error reading /proc: {e}")
    return pids

def get_real_pids():
    """
    VIEW B: The 'Raw' View.
    Reads from our custom kernel module interface (/proc/rk_detector).
    """
    pids = set()
    try:
        with open('/proc/rk_detector', 'r') as f:
            for line in f:
                # Split the line to handle "PID NAME" format or just "PID"
                parts = line.strip().split()
                if parts and parts[0].isdigit():
                    pids.add(int(parts[0]))
    except FileNotFoundError:
        print("Error: Kernel module not loaded. Run 'sudo insmod rk_detector.ko' first.")
        sys.exit(1)
    return pids

def main():
    # 1. Check for Root Privileges
    if os.geteuid() != 0:
        print("[-] This script must be run as root to access kernel modules.")
        sys.exit(1)

    print("[-] Taking snapshot of visible processes (User-Land)...")
    visible = get_visible_pids()
    print(f"    Found {len(visible)} visible processes.")

    print("[-] Taking snapshot of actual kernel processes (Kernel-Land)...")
    real = get_real_pids()
    print(f"    Found {len(real)} actual processes.")

    # 2. The Detection Logic
    # If it is in REAL but NOT in VISIBLE, it is hidden.
    hidden = real - visible

    if hidden:
        print("\n" + "="*40)
        print("[!] ROOTKIT DETECTED!")
        print("="*40)
        print(f"[!] The following PIDs are hidden from the OS:")
        for pid in hidden:
            print(f"    -> PID: {pid}")
            
            # Optional: Try to read the name from the Kernel Module output if you want
            # This requires cross-referencing the lists again, but for now, the PID is enough.
    else:
        print("\n[+] System appears clean. No PIDs are hidden.")

if __name__ == "__main__":
    main()