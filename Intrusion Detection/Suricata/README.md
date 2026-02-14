# Suricata IDS Implementation

This folder contains documentation and evidence of implementing Suricata, a powerful open-source Intrusion Detection System (IDS), in a controlled lab environment.

## Tools Used

- **Suricata** - Open-source IDS/IPS engine for network security monitoring
- **Kali Linux** - Used as the attacker machine to simulate various attacks
- **Metasploitable 2** - Intentionally vulnerable target machine
- **Ubuntu** - Host system running Suricata IDS
- **Netdiscover** - Network discovery tool
- **Nmap** - Network scanner for reconnaissance
- **hping3** - TCP/IP packet assembler/analyzer for flood attacks

## Contents

- **Report.md** - Detailed report documenting the IDS implementation, configuration, attack simulation, and detection results
- **Captures/** - Screenshots and evidence of the implementation process and attack detection

## Overview

This project demonstrates the setup and configuration of Suricata IDS to detect various network attacks including:
- Network reconnaissance (Nmap scans)
- Denial of Service attacks (hping3 floods)
- ICMP network probing
- Unauthorized remote access attempts (SSH)

The implementation follows industry best practices for IDS deployment and includes custom rule creation for specific threat detection.
