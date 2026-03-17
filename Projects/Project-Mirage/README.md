Information on Project Mirage

# Project Mirage: Cloud Honeypot & Threat Intelligence Map 

## Objective
The goal of this project was to deploy a live SSH honeypot on AWS, intercept real-world automated attacks, and build a custom data pipeline to extract, parse, and visualize the threat intelligence on a global map.

## Architecture & Tools Used
* **Cloud Infrastructure:** AWS EC2 (Ubuntu)
* **Honeypot:** Cowrie (Dockerized)
* **Networking:** Custom `iptables` NAT routing to silently redirect Port 22 traffic.
* **Data Pipeline:** Python (Pandas, Requests, JSON parsing)
* **OSINT:** IP-API Geolocation
* **Visualization:** Folium (Interactive HTML Maps)

## The Process
1.  **Deployment:** Spun up an Ubuntu EC2 instance and deployed the Cowrie honeypot via Docker.
2.  **Firewall Engineering:** Configured Linux `iptables` to seamlessly reroute malicious SSH scanners from the default port into the isolated container.
3.  **Data Extraction:** Engineered a bypass for Docker volume permission locks to extract live JSON telemetry (`cowrie.json`) directly from the container's isolated file system.
4.  **Enrichment:** Wrote `parser.py` to ingest the raw logs, filter out local Docker network noise, and query an external API to resolve attacker IPs to their physical locations and ISPs.
5.  **Visualization:** Developed `map_builder.py` using Folium to generate an interactive `attack_map.html`, plotting attacker coordinates, attempted usernames, and captured payload commands.

## Key Findings
* Intercepted global attacks originating from multiple countries including Russia, Germany, Singapore, and the Netherlands.
* Captured automated enumeration scripts and DDoS botnet recruitment payloads dropping executable files (`chmod +x sshd`).
