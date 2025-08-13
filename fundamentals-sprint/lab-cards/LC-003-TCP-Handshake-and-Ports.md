# LC-003 — TCP Handshake & Ports

**What it is:** TCP establishes a reliable connection using a 3-way handshake: SYN → SYN/ACK → ACK. Ports identify application endpoints (e.g., 80/HTTP, 443/HTTPS).

**Why it matters:** Understanding the handshake and ports explains many findings from nmap and logs (e.g., filtered vs closed) and helps you reason about network behavior and blocking.

**How it works (bullets):**
- Client sends SYN to server: "I'd like to start a connection."
- Server replies SYN/ACK: "Yes, and I acknowledge."
- Client sends ACK: "Acknowledged" → connection is established.
- RST (reset) indicates abrupt termination; no handshake for UDP.

## Commands I ran
```bash
# Check open TCP listeners on localhost (Git Bash + Windows tools)
netstat -ano | head -n 20

# TCP handshake capture (if you have Wireshark or tcpdump on WSL)
# tcpdump -i any 'tcp[tcpflags] & (tcp-syn|tcp-ack) != 0' -c 10
```

**Common pitfalls:**
- Confusing TCP (connection-oriented) with UDP (connectionless).
- Assuming "closed" vs "filtered" mean the same in scans.

**Defender indicators:**
- Repeated SYNs without ACKs → possible scanning.
- SYN floods (lots of half-open connections).

**Remediation:**
- Rate-limit suspicious source IPs; SYN cookies on servers.
- Log connection attempts and failures for anomaly detection.

## Findings (filled)
- :80 HTTP status = **200 OK** ; :443 HTTPS status = **200 OK**
- :81 result = **timed out** → treated as **filtered** (no TCP RST)
- netstat sample (local listeners):
  - TCP 0.0.0.0:135      0.0.0.0:0   LISTENING   1872
  - TCP 0.0.0.0:445      0.0.0.0:0   LISTENING   4
  - TCP 0.0.0.0:49664    0.0.0.0:0   LISTENING   7036

## Notes (so it sticks)
- **Closed** = host actively refuses (RST). **Filtered** = no reply (timeout).
- Ports 80/443 are the normal web surface; odd ports (like 81) often get blocked.
- `0.0.0.0` listeners = potential attack surface if exposed; NAT/firewall usually shields them.
