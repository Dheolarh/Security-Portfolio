#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/mount.h>
#include <sys/stat.h>
#include <string.h>
#include <signal.h>

void become_ghost() {
    printf("[*] Ghost Process Started. PID: %d\n", getpid());
    
    // 1. Change our name so the Detector sees something specific
    // This is the "Hello, I'm a hidden process" part.
    char *new_name = "GHOST_ROOTKIT";
    // We can't easily change argv[0] in C without hacks, but we can change the
    // process name that the Kernel knows (comm).
    // The detector reads task->comm, so it will see this name.
    
    // 2. Prepare the hiding spot
    char target_dir[64];
    sprintf(target_dir, "/proc/%d", getpid());
    
    // 3. The "Poorman's Cloak" - Mount an empty directory over our /proc entry
    // This makes 'ps' fail to read our info.
    // Create a dummy empty directory
    if (mkdir("/tmp/empty_void", 0777) != 0) {
        // Ignore error if it exists
    }

    printf("[*] Hiding footprint by mounting over %s...\n", target_dir);
    if (mount("/tmp/empty_void", target_dir, "none", MS_BIND, NULL) != 0) {
        perror("[-] Failed to cloak process (are you root?)");
        exit(1);
    }

    printf("[+] SUCCESS: I am now invisible to 'ps' and standard tools.\n");
    printf("[+] I am staying alive in memory. Run your detector now!\n");
    printf("[!] Press Ctrl+C to stop me (and unhide).\n");

    // 4. Stay alive in memory
    while(1) {
        sleep(10);
    }
}

int main() {
    if (geteuid() != 0) {
        fprintf(stderr, "[-] You must be root to perform the hiding trick.\n");
        return 1;
    }
    become_ghost();
    return 0;
}
