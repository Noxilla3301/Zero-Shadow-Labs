import json
import requests
import csv
import time

ip_cache = {}

def get_location(ip):
    if ip in ip_cache:
        return ip_cache[ip]

    try:
        response = requests.get(f"http://ip-api.com/json/{ip}", timeout=3)
        data = response.json()
        
        if data.get('status') == 'success':
            location = f"{data['country']} - {data['isp']}"
            ip_cache[ip] = location 
            time.sleep(1.5) 
            return location
        else:
            return "Unknown"
    except Exception:
        return "API Error"

def parse_and_export(file_path, output_csv):
    print("--- PROJECT MIRAGE: INGESTING TELEMETRY ---")
    
    with open(file_path, 'r') as infile, open(output_csv, 'w', newline='', encoding='utf-8') as outfile:
        writer = csv.writer(outfile)
        writer.writerow(["Timestamp", "Event Type", "IP Address", "Location", "Username", "Password", "Command"])
        
        for line in infile:
            try:
                log = json.loads(line.strip())
                ip = log.get('src_ip', '')
                
                if ip.startswith('172.') or ip.startswith('192.168.') or ip.startswith('10.'):
                    continue
                
                timestamp = log.get('timestamp', '')
                
                if log.get('eventid') in ['cowrie.login.success', 'cowrie.login.failed']:
                    event_type = "LOGIN SUCCESS" if log.get('eventid') == 'cowrie.login.success' else "LOGIN FAILED"
                    user = log.get('username', '')
                    password = log.get('password', '')
                    location = get_location(ip)
                    
                    writer.writerow([timestamp, event_type, ip, location, user, password, ""])
                    print(f"Logged: {ip} | {event_type} | {location}")
                    
                elif log.get('eventid') == 'cowrie.command.input':
                    command = log.get('input', '')
                    location = get_location(ip)
                    
                    writer.writerow([timestamp, "COMMAND ISSUED", ip, location, "", "", command])
                    print(f"Logged: {ip} | COMMAND | {location}")
                    
            except json.JSONDecodeError:
                continue
                
    print(f"\n[+] Extraction complete. Data saved to {output_csv}")

parse_and_export('cowrie.json', 'threat_intel.csv')