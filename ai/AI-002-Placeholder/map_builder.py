import pandas as pd
import folium
import requests
import time

print(" - PROJECT MIRAGE: GENERATING THREAT MAP - ")

try:
    df = pd.read_csv('threat_intel.csv')
except FileNotFoundError:
    print("[-] Could not find threat_intel.csv. Run parser.py first")
    exit()

unique_ips = df['IP Address'].dropna().unique()
ip_data = {}

print(f"[*] Geocoding {len(unique_ips)} unique attacking IPs...")

for ip in unique_ips:
    try:
        response = requests.get(f"http://ip-api.com/json/{ip}", timeout=3).json()
        if response.get('status') == 'success':
            ip_data[ip] = {
                'lat': response['lat'],
                'lon': response['lon'],
                'city': response['city'],
                'country': response['country']
            }
        time.sleep(1) 
    except Exception as e:
        print(f"[-] Failed to geolocate {ip}")

m = folium.Map(location=[20, 0], zoom_start=2, tiles='CartoDB dark_matter')

for index, row in df.iterrows():
    ip = row['IP Address']
    if ip in ip_data:
        lat = ip_data[ip]['lat']
        lon = ip_data[ip]['lon']
        city = ip_data[ip]['city']
        
        folium.CircleMarker(
            location=[lat, lon],
            radius=6,
            popup=f"IP: {ip}<br>Location: {city}<br>User: {row['Username']}",
            color='red',
            fill=True,
            fill_color='red',
            fill_opacity=0.6
        ).add_to(m)

m.save('attack_map.html')
print("Map successfully generated: attack_map.html")
print("Open attack_map.html in your web browser to view the War Room")