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

## Recommendations
1. **Decommission FTP Services**: Replace all FTP services with secure alternatives like SFTP/FTPS.
2. **Implement Multi-Factor Authentication (MFA)**: Enforce MFA to prevent credential compromise.
3. **Monitor Internal Traffic**: Use IDS/IPS solutions to detect and block lateral movement and C2 communication.
4. **Conduct Regular Security Audits**: Periodically review and update security configurations.

## Conclusion
The analysis revealed critical vulnerabilities that require immediate attention. By implementing the recommendations, the network's security posture can be significantly improved, reducing the risk of future attacks.