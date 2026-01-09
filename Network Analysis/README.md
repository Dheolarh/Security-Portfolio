# Network Analysis Project

## Overview
This project focuses on analyzing network traffic to identify and mitigate security threats. The analysis was conducted using packet capture (pcap) files and tools like Wireshark. The findings highlight critical vulnerabilities and provide actionable recommendations to improve network security.

## Objectives
- Detect and analyze malicious and suspicious network activities.
- Assess the impact and severity of identified threats.
- Evaluate the effectiveness of the CyBOK Incident Response Model.
- Provide clear mitigation and remediation recommendations.

## Tools and Frameworks
- **Tools Used**: Wireshark for deep packet inspection.
- **Frameworks Applied**: CyBOK Incident Response Model, SANS Incident Handler's Handbook.

## Key Findings
### Capture 1
1. **Brute Force Attack**
   - **Attacker IP**: 192.168.56.1
   - **Target IP**: 192.168.56.102
   - **Description**: Numerous repeated attempts to log into the FTP service on Port 21, resulting in clear-text credential exposure.
   - **Severity**: High

   ![Brute Force Attack - Capture 1](Analysis%20Report/Capture%201/1.jpg)
   ![Brute Force Attack - Capture 1 Details](Analysis%20Report/Capture%201/2.jpg)
   ![FTP Login Attempts - Capture 1](Analysis%20Report/Capture%201/3.jpg)

### Capture 2
1. **Stealth Scanning**
   - **Attacker IP**: 192.168.56.102
   - **Target IP**: 192.168.56.101
   - **Description**: Systematic probing of the target IP for open ports, indicating reconnaissance before a targeted internal attack.
   - **Severity**: Medium

   ![Stealth Scanning - Capture 2](Analysis%20Report/Capture%202/1.jpg)

2. **Control Communication**
   - **Attacker IP**: 192.168.56.102
   - **Target IP**: 192.168.56.101
   - **Description**: Small, patterned packet transfers consistent with a potential Command and Control (C2) channel.
   - **Severity**: High

   ![Control Communication - Capture 2](Analysis%20Report/Capture%202/2.jpg)

3. **Repeated FTP Login Attempts**
   - **Attacker IP**: 192.168.56.101
   - **Target IP**: 192.168.56.102
   - **Description**: Bi-directional brute force attacks targeting the insecure FTP service.
   - **Severity**: High

   ![FTP Login Attempts - Capture 2](Analysis%20Report/Capture%202/3.jpg)
   ![FTP Login Attempts - Capture 2 Details](Analysis%20Report/Capture%202/4.jpg)
   ![FTP Login Attempts - Capture 2 Stream](Analysis%20Report/Capture%202/5.jpg)

4. **Brute Force Attack (External IP)**
   - **Attacker IP**: 192.168.56.1
   - **Target IP**: 192.168.56.101
   - **Description**: A third brute force attempt involving an external IP targeting a new host.
   - **Severity**: High

   ![Brute Force Attack - External IP](Analysis%20Report/Capture%202/4.jpg)

5. **Suspicious Logins**
   - **Attacker IP**: 192.168.56.102
   - **Target IP**: 192.168.56.101
   - **Description**: Potential successful login attempts following brute force activity.
   - **Severity**: High

   ![Suspicious Logins - Capture 2](Analysis%20Report/Capture%202/5.jpg)
   ![Suspicious Logins - Capture 2 Stream](Analysis%20Report/Capture%202/3.jpg)

## Recommendations
1. **Decommission FTP Services**: Replace all FTP services with secure alternatives like SFTP/FTPS.
2. **Implement Multi-Factor Authentication (MFA)**: Enforce MFA to prevent credential compromise.
3. **Monitor Internal Traffic**: Use IDS/IPS solutions to detect and block lateral movement and C2 communication.
4. **Conduct Regular Security Audits**: Periodically review and update security configurations.

## Conclusion
The analysis revealed critical vulnerabilities that require immediate attention. By implementing the recommendations, the network's security posture can be significantly improved, reducing the risk of future attacks.

## SANS Incident Response Evaluation

### 1. Preparation
This stage occurs *before* the incident. Based on the report, the preparation was insufficient, which allowed the attacks to occur and succeed.

- **Insecure Protocols:** The primary vulnerability exploited was **FTP (Port 21)**, which is fundamentally insecure. It transmits credentials (usernames and passwords) in clear text.
  - **Report Evidence:** Captures 1, 4, 5, 6, and 7 all explicitly target FTP.
  - **IR Failure:** A robust preparation phase would have involved a policy of disallowing insecure protocols. FTP should be disabled and replaced with secure alternatives like **SFTP** or **FTPS**.
- **Weak Access Control & Segmentation:** The attacker IPs (192.168.56.1, .101, .102) are all on the same private subnet as the targets. This suggests the attack is either internal or one machine (.102) was compromised first (perhaps via Capture 2, "Stealth scanning") and then used to attack another (.101).
  - **Report Evidence:** Capture 2 shows .102 scanning .101.
  - **IR Failure:** Good preparation includes network segmentation (e.g., using VLANs) to prevent a single compromised machine from having free rein to scan and attack other critical assets on the same network segment.
- **Inadequate Monitoring:** The brute-force attacks (e.g., Capture 1, spanning over 80,000 packets) are extremely loud. A well-prepared organization would have an IDS or SIEM configured to automatically detect and alert on this anomalous number of failed logins in real-time.

### 2. Identification
This stage is where the incident is detected. The Wireshark analysis *is* the identification stage.

- **Indicators of Compromise (IoCs):** The report has successfully identified clear IoCs:
  - **IP Addresses:** 192.168.56.1, 192.168.56.101, 192.168.56.102.
  - **Protocols & Ports:** FTP on Port 21.
  - **Attack Signatures:** Massive volumes of login packets (brute-force) and port scanning (stealth scan).
- **Confirmation of Breach:** This is the most critical finding. The incident has escalated from an *attempt* to a confirmed *breach*.
  - **Report Evidence (Capture 6):** "Source IP successfully logs into system."
  - **Report Evidence (Capture 7):** "Source IP... successfully retrieves confidential file."
- **Triage:** The incident must be triaged as **High Severity**. The identification of data exfiltration (Capture 7) makes this a confirmed data breach, which requires immediate escalation.

### 3. Containment
The immediate goal is to stop the bleeding and prevent further damage.

- **Short-Term Containment (Immediate Actions):**
  1. **Isolate Affected Hosts:** Disconnect all three machines (192.168.56.1, 192.168.56.101, 192.168.56.102) from the network *immediately*.
  2. **Disable Vulnerable Service:** Shut down the FTP service on the target servers (.101 and .102).
  3. **Disable Compromised Accounts:** The full packet capture must be analyzed to identify the *specific* username that was successfully used in Capture 6. That account must be immediately disabled.
  4. **Create Firewall Blocks:** Add rules to block all communication between these three IPs until they can be cleaned.

### 4. Eradication
This stage focuses on finding the root cause of the incident and removing the attacker's presence.

- **Root Cause Analysis:** The root cause is clear:
  1. **Primary Cause:** Use of the insecure FTP protocol.
  2. **Secondary Cause:** A weak password for the compromised account, which allowed the brute-force attack (Capture 4 & 5) to succeed (Capture 6).
- **Cleanup:**
  - **Reimage Systems:** All three machines must be considered fully compromised. The only reliable eradication method is to wipe them and re-image them from a known-good, clean backup.
  - **Enforce Password Reset:** A network-wide password reset should be forced for all users, especially any user with access to the compromised servers.
  - **Scan for Persistence:** Before bringing the rebuilt systems back online, they must be scanned for any persistence mechanisms (e.g., malware, backdoors) the attacker may have left.

### 5. Recovery
This stage involves carefully restoring services to normal operation.

- **System Restoration:** Bring the clean, reimaged systems back online.
- **Vulnerability Remediation:** **Do not re-enable FTP.** The recovery process *must* involve replacing it with SFTP or FTPS. All applications and users must be updated to use the new, secure protocol.
- **Validation:** Test that the new secure file transfer service works as intended and that the old FTP port (21) is closed and inaccessible.
- **Enhanced Monitoring:** Place the recovered systems under heightened monitoring. Watch their logs and network traffic closely for any sign of the attacker's return.

### 6. Lessons Learned
This final stage (often held 1-2 weeks after the incident) is crucial for improving future defenses.

- **What went wrong?**
  - We allowed the use of an insecure, legacy protocol (FTP).
  - Our password policies were not strong enough to resist a brute-force attack.
  - Our monitoring systems (IDS/SIEM) failed to detect or block the attack automatically.
  - Our internal network segmentation was insufficient to prevent lateral movement (scanning from .102 to .101).
- **What could be done better?**
  - **Policy:** Implement a firm policy banning all insecure protocols (FTP, Telnet, etc.).
  - **Technology:**
    1. Deploy an **Intrusion Prevention System (IPS)**, which could have automatically blocked the brute-force attack.
    2. Enforce **Multi-Factor Authentication (MFA)**, which would have made the brute-force attack useless.
    3. Implement better internal network firewall rules and segmentation.
  - **Training:** Ensure system administrators understand the risks of legacy protocols.