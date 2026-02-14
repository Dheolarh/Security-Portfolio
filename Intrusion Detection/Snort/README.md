# Snort IDS Implementation

This folder contains documentation and evidence of implementing Snort, one of the world's most widely deployed open-source Intrusion Detection Systems (IDS), in a controlled lab environment.

## Tools Used

- **Snort** - Industry-leading open-source IDS/IPS engine for network threat detection and prevention
- **Kali Linux** - Used as the attacker machine to simulate various network attacks
- **Metasploitable 2** - Intentionally vulnerable target machine for testing IDS capabilities
- **Ubuntu** - Host system running Snort IDS as the network sensor
- **Netdiscover** - Network discovery tool for identifying active hosts
- **Nmap** - Network scanner for reconnaissance and port scanning
- **hping3** - TCP/IP packet assembler/analyzer for simulating flood attacks

## Contents

- **Report.md** - Detailed technical report documenting the complete IDS implementation process, including installation, configuration, rule creation, attack simulation, and detection results
- **Captures/** - Screenshots and visual evidence of network discovery, Snort configuration, and real-time attack detection

## Overview

This project demonstrates professional-grade deployment and configuration of Snort IDS in a 3-device topology (Attacker, Defender, Target) to detect and alert on multiple network security threats including:
- ICMP network probing and reconnaissance
- Port scanning attacks (Nmap with SYN flag detection)
- Denial of Service attacks (hping3 flood attacks)
- Unauthorized remote access attempts (SSH)

The implementation showcases industry-standard practices for IDS deployment:
- Custom rule creation for specific threat detection
- Passive network traffic monitoring and analysis
- Real-time alerting and log generation
- Multi-vector attack detection and correlation

This hands-on technical assessment successfully validated Snort's capability to identify all simulated threat vectors, demonstrating practical skills in intrusion detection, network defense operations, and security monitoring.
