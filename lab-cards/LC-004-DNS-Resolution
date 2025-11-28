# LC-004 — DNS Resolution (A/AAAA/CNAME/NS/MX/TXT)

**What it is (2–3 lines):**  
DNS maps names to data (often IPs). Resolvers ask authoritative name servers for records like **A** (IPv4), **AAAA** (IPv6), **CNAME** (alias), **NS** (name servers), **MX** (mail), **TXT** (SPF/DMARC), **SOA** (zone info).

**Why it matters (1–2 lines):**  
Every web target sits behind DNS. Recon starts here (subdomains, mail, cloud providers). Blue teams catch abuse via NXDOMAIN spikes and weird TXT/MX.

**How it works (bullets):**
- Your **stub resolver** asks a **recursive** resolver (ISP/DoH) which walks root → TLD → authoritative.
- Answers have **TTL**; caches reuse until TTL expires.
- Nonexistent names return **NXDOMAIN**.

---

## Commands I ran (Git Bash on Windows; uses built-in `nslookup`)
```bash
# A/AAAA (IPv4/IPv6)
nslookup -type=A example.com
nslookup -type=AAAA example.com

# CNAME (alias) — try a known alias like www.google.com
nslookup -type=CNAME www.google.com

# NS (authoritative name servers)
nslookup -type=NS example.com

# MX (mail exchangers) and TXT (SPF/DMARC)
nslookup -type=MX google.com
nslookup -type=TXT google.com

# SOA (zone meta: primary NS, contact, serial)
nslookup -type=SOA example.com

# Nonexistent -> NXDOMAIN (use a random subdomain)
nslookup -type=A nosuch-$(date +%s).example.com

## Notes
DNS has diff records:

- A record = IPv4 (multiple A records / ip addresses shown means there is load balancing happening for website - resolver path is local -> authoritative)

- AAAA record = IPV6 (the ip addresses here are longer because ipv6 uses 128-bit addresses - resolver path is the same as A record)

- CNAME (canonical name) record - an 'alias' that points one domain to another. 

- MX (mail exchanger) record - tells what servers handle 'email' for a domain. For output -> MX preference = 10, mail exchanger = smtp.google.com | lower number = higher priority. Google usees multiple IPv4/IPv6 mail servers. 

- TXT records - arbitrary text data stored in DNS. Basically mischellaneous info - used for security, ownership, verification. 

- SOA (start of authority) records - Defines primary DNS server for a domain and metadata about the zone - ie: "who owns/manages the zone, and timing rules". Serial = version number.

- nosuch-$(date +%s).example.com generates a nonexistent hostname (because $(date +%s) expands to a timestamp). Expected output: NXDOMAIN (non-existent domain). Shows how DNS reports invalid queries. Security aspect: (attackers probing often hit NXDOMAINs).

## Output summaries

**A Record (IPv4)**  
- Query: `nslookup -type=A example.com`  
- Result: Multiple IPv4 addresses returned (e.g., 23.192.228.80, 96.7.128.175).  
- Resolver: local gateway (192.168.1.1).  

**AAAA Record (IPv6)**  
- Query: `nslookup -type=AAAA example.com`  
- Result: Several IPv6 addresses (e.g., 2600:1406:bc00:53::b29e, 2600:1406:bc00:63::b29e).  

**CNAME Record**  
- Query: `nslookup -type=CNAME www.google.com`  
- Result: No direct CNAME; instead returned SOA-like info: primary = ns1.google.com, admin = dns-admin.google.com, serial = 701007581.  

**MX Record (Mail)**  
- Query: `nslookup -type=MX google.com`  
- Result: MX preference 10 → smtp.google.com, with both IPv4 + IPv6 addresses.  

**TXT Records**  
- Query: `nslookup -type=TXT google.com`  
- Result (examples):  
  - `"v=spf1 include:_spf.google.com ~all"` (SPF anti-spam).  
  - `"google-site-verification=..."`  
  - `"facebook-domain-verification=..."`  
  (Many more similar verification/security TXT entries omitted for brevity).  

**SOA Record (Start of Authority)**  
- Query: `nslookup -type=SOA example.com`  
- Result: primary = ns.icann.org, admin = noc.dns.icann.org, serial = 2025011752, refresh = 7200, retry = 3600, expire = 1209600, TTL = 3600.  

**NXDOMAIN Test**  
- Query: `nslookup -type=A nosuch-$(date +%s).example.com`  
- Result: Non-existent domain → `NXDOMAIN`.  

