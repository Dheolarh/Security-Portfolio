# SOC Analyst Journey

## Overview
This repository highlights my learning journey as a Security Operations Center (SOC) Analyst. It showcases hands-on projects I've worked on both independently and as part of a team, demonstrating practical skills in network security analysis, vulnerability assessment, incident response, and threat detection.

The projects documented here reflect real-world scenarios and industry-standard tools used in cybersecurity operations. Each project includes detailed analysis, findings, and actionable recommendations to improve security posture.

---

## Projects

### 1. [Network Analysis](Network%20Analysis/)
**Tools**: Wireshark  
**Frameworks**: CyBOK Incident Response Model, SANS Incident Handler's Handbook

This project involves deep packet inspection and analysis of network traffic to identify malicious activities and security threats. Using Wireshark, I analyzed multiple packet captures revealing critical security incidents including:

- **FTP Brute Force Attacks**: Multiple attempts to compromise systems using insecure FTP protocol
- **Internal Lateral Movement**: Evidence of compromised hosts performing reconnaissance and stealth scanning
- **Command & Control Communication**: Detection of potential C2 channels between internal hosts
- **Successful Credential Compromise**: Clear-text credential exposure leading to unauthorized access

**Key Findings**: The analysis identified critical vulnerabilities in the use of insecure protocols (FTP, Telnet) and inadequate network segmentation, resulting in a multi-vector attack with confirmed data breach.

**Outcome**: Provided comprehensive incident response evaluation using both CyBOK and SANS frameworks, with actionable remediation steps including protocol replacement, MFA implementation, and network segmentation.

---

### 2. [Vulnerability Assessment](Vulnerability%20Assessment/)
**Tools**: OpenVAS (Greenbone Security Assistant), Nessus Essentials  
**Target Systems**: Metasploitable 2, Windows 7

This project demonstrates comprehensive vulnerability scanning and assessment of network systems to identify security weaknesses. Using industry-standard tools, I performed in-depth vulnerability analysis on two target systems:

**Metasploitable 2 (192.168.98.128)**:
- Identified multiple critical vulnerabilities including UnrealIRCd backdoor (CVSS 10.0)
- Detected insecure services: rexec, VNC with default passwords, Telnet
- Found bind shell backdoor allowing unauthenticated remote access

**Windows 7 (192.168.98.129)**:
- Discovered end-of-life operating system with no security support
- Identified MS11-030 DNS vulnerability allowing remote code execution (CVSS 10.0)
- Detected numerous exposed DCE/RPC services increasing attack surface

**Key Findings**: Both systems present severe security risks with exploitable vulnerabilities scoring 10.0 on the CVSS scale. Immediate isolation and remediation required to prevent system compromise.

**Outcome**: Delivered detailed vulnerability report with prioritized remediation recommendations, including OS migration, service hardening, and implementation of security monitoring solutions.

---

## Other Projects

### Coming Soon
- **Intrusion Detection Systems (IDS)** - Snort and Suricata rule configuration and alert analysis
- **Security Information and Event Management (SIEM)** - Log aggregation and correlation
- **Threat Intelligence** - IOC analysis and threat hunting exercises
- **Incident Response Playbooks** - Documentation of IR procedures and case studies

---

## Skills Demonstrated
- Network traffic analysis and packet inspection
- Vulnerability assessment and management
- Incident detection and response
- Security tool proficiency (Wireshark, OpenVAS, Nessus)
- Risk assessment and prioritization
- Security documentation and reporting
- Framework application (CyBOK, SANS, NIST)

---

## Contact & Collaboration
This repository is continuously updated as I progress in my SOC analyst journey. Feel free to explore the projects, and I'm open to feedback, collaboration, and learning opportunities.

**Last Updated**: January 2026