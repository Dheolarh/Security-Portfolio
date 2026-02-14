**Assets:**
1. **Defender (Sensor):** Ubuntu Host (Suricata  IDS)  
2. **Attacker:** Kali Linux  
3. **Target:** Metasploitable 2 (Vulnerable Linux Target)

## **1\. Overview**

This report details the deployment and configuration of the **Suricata Intrusion Detection System** on a Ubuntu environment. The project utilized a three-node virtualized network architecture to simulate real-world attack scenarios. By developing custom detection signatures, the system was successfully tested against ICMP probing, Nmap stealth scanning, hping3 flood attacks, and unauthorized SSH connection attempts. The results confirm Suricata's effectiveness in providing high-fidelity network visibility and real-time alerting.

## **2\. Laboratory Environment Setup**

### **2.1 Virtual Machine Configuration**

The lab environment was constructed using three distinct virtual machines connected via a NAT network to ensure communication while maintaining isolation from the host’s physical network.

1. **Attacker:** Kali Linux (192.168.40.129)  
2. **Defender (Sensor):** Ubuntu 24.04 (192.168.40.130) running Suricata  
3. **Target:** Metasploitable 2 (192.168.40.131)

### **2.2 Network Identification**

Network discovery was performed using the netdiscover utility to map the MAC addresses to the assigned IP addresses within the NAT subnet.

![Fig 1. Netdiscover was used to get ip addresses on the same network](Captures/1%20-%20netdiscover%20IPs.png)

###### **Fig 1\. Netdiscover was used to get ip addresses on the same network** 

## **3\. Suricata Installation and Configuration**

### **3.1 Installation Procedure**

Suricata was installed via the official OISF stable PPA to ensure access to the latest engine features (Version 8.0.3).

**sudo add-apt-repository ppa:oisf/suricata-stable**  
**sudo apt update && sudo apt install suricata \-y**

### **3.2 System Configuration (suricata.yaml)**

The primary configuration file was modified to define the network scope and the sniffing interface (ens33).

1. **Home Network Definition:** Set to 192.168.40.0/24.  
2. **Interface Binding:** Configured af-packet to listen on the primary network interface.

![Fig 2. Configure Home Net](Captures/2%20-%20Configure%20Home%20Net.png)

![Fig 3. Configure Interface](Captures/3%20-%20Configure%20Interface.png)

###### **Fig 2\. Network Rules and Interface Configurations.**

### **3.3 Custom Rule Development**

To meet the project requirements, detection logic was split into modular rule files located in **/var/lib/suricata/rules/.**

| Rule File | Detection Objective | Logic Description |
| :---- | :---- | :---- |
| scans.rules | ICMP, Nmap, hping3 | Targets protocol flags and threshold-based flooding. |
| ssh\_monitor.rules | SSH Unauthorized Access | Targets TCP SYN packets directed at port 22\. |

![Fig 4. Creating Scans rules](Captures/4%20-%20Creating%20Scans%20rules.png)

![Fig 5. Creating SSH rules](Captures/5%20-%20creating%20SSH%20rules.png)

![Fig 6. Check or set the default rule path](Captures/6%20-%20check%20or%20set%20the%20default%20rule%20path%20and%20add%20your%20rules%20file%20names.png)

###### **Fig 3\. Network Monitoring Rules Configurations.**

### **3.4 Verification of Engine Integrity**

Before deployment, the Suricata test harness (-T) was used to verify signature syntax and YAML validity.

![Fig 7. Confirm Configuration Loads Successfully](Captures/7%20-%20Confirm%20Configuration%20Loads%20Succesfully.png)

![Fig 8. Start Suricata Engine](Captures/8%20-%20Start%20Suricata%20Engine.png)

###### **Fig 4\. Starting Suricata Engine**

## **4\. Threat Simulation and Detection Findings**

The following simulations were conducted from the Kali Linux attacker machine. Real-time alerts were monitored using the fast.log output on the Ubuntu sensor.

![Fig 9. Open Another Terminal to detect logs](Captures/9%20-%20Open%20Another%20Terminal%20to%20detect%20logs.png)

###### **Fig 5\. Open terminal for network log entry**

### **4.1 Threat: Nmap Stealth Scanning**

**Attack Vector:** A TCP SYN stealth scan was initiated to map open ports on the Metasploitable target.

1. **Command:** sudo nmap \-sS 192.168.40.131  
2. **Detection Status:** SUCCESS.  
3. **Analysis:** Suricata successfully identified the high frequency of SYN packets without ACKs.

![Fig 6. Do Nmap scan on target](Captures/10%20-%20Do%20Nmap%20scan%20on%20target.png)

###### **Fig 6\. Performing Nmap scan from kali OS**

![Fig 7. Suricata Detected Nmap Scan](Captures/11%20-%20Suricata%20Detected%20Nmap%20Scan.png)

###### **Fig 7\. Suricata detects Nmap scan.**

### **4.2 Threat: Denial of Service (hping3 Flood)**

**Attack Vector:** A high-speed TCP SYN flood was directed at the target to exhaust system resources.

1. **Command:** sudo hping3 \-S \--flood 192.168.40.131  
2. **Detection Status:** SUCCESS.  
3. **Analysis:** The detection\_filter triggered an alert once the packet count exceeded 20 within a 10-second window.

![Fig 8. Do hping flooding on target](Captures/12%20-%20Do%20hping%20flooding%20on%20target.png)

###### **Fig 8\. high-speed TCP SYN flood directed to target from Kali OS**

![Fig 9. Detect hping flood](Captures/13%20-%20detect%20hping%20flood.png)

###### **Fig 9\. Potential hping3 flood detected on** 

### **4.3 Threat: ICMP Network Probing**

**Attack Vector:** Standard echo requests used for host discovery.

1. **Command:** ping \-c 4 192.168.40.131  
2. **Detection Status:** SUCCESS.

![Fig 10. Ping target](Captures/14%20-%20ping%20target.png)

###### **Fig 10\. Standard echo requests used for host discovery sent from Kali OS**

![Fig 11. Detect ping](Captures/15%20-%20detect%20ping.png)

###### **Fig 11\. ICMP ping detected on Suricata.**

### **4.4 Threat: Unauthorized Remote Access (SSH)**

**Attack Vector:** Attempting to establish an encrypted shell session to the target.

1. **Command:** ssh \-o HostKeyAlgorithms=+ssh-rsa \-o PubkeyAcceptedAlgorithms=+ssh-rsa msfadmin@192.168.40.131  
2. **Detection Status:** SUCCESS.  
3. **Analysis:** The IDS flagged the connection attempt even though the SSH handshake failed due to legacy key mismatches.

![Fig 12. SSH into target](Captures/16%20-%20ssh%20into%20target.png)

###### **Fig 12\. Attempt to establish shell session to metasploitable from kali OS**

![Fig 13. Detect SSH attempt](Captures/17%20-%20Detect%20SSH%20attempt.png)

###### **Fig 13\. SSH connection attempt discovered by Suricata**

## **5\. Critical Analysis of IDS and IPS**

### **5.1 Effectiveness as an IDS**

The implementation demonstrated that Suricata is highly effective at providing **situational awareness**. By utilizing signature-based detection, the system provided immediate notification of every attack vector tested. The use of modular rules allowed for specific targeting of malicious flags (like the Nmap SYN flag) while ignoring standard traffic.

### **5.2 Transitioning to IPS (Intrusion Prevention)**

While the current configuration successfully **detected** attacks, it was **passive**. The hping3 flood and Nmap scans still reached the Metasploitable target. To transform this into an **IPS**:

1. The deployment mode must change from IDS (listening on a copy of traffic) to IPS (inline, where traffic flows through the sensor).  
2. Suricata would be integrated with NFQUEUE on the Ubuntu firewall.  
3. Rules would be updated from alert to drop.

### **5.3 Quality Research & Quality Analysis**

Recent research highlights that signature-based IDS remains a cornerstone of defense-in-depth but faces challenges with encrypted traffic (SSL/TLS). Modern implementations of Suricata now utilize **JA3 Fingerprinting** to identify malicious clients even when traffic is encrypted. Furthermore, integrating Suricata with ELK Stack (Elasticsearch, Logstash, Kibana) for graphical analysis is the industry standard for managing the high volume of alerts generated by tools like hping3.

## **6\. Conclusion**

The project successfully fulfilled all requirements of Task-2. The Ubuntu-based Suricata sensor was properly configured to monitor a multi-machine network and provided distinct, accurate alerts for ICMP, Nmap, hping3, and SSH traffic. This environment provides a robust foundation for further exploration into automated threat response and network forensics.