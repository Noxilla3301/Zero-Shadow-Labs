# LC-005 — Cookies, Sessions, and SameSite

**What it is (2–3 lines):**  
Cookies are small key–value pairs a server sets via `Set-Cookie` for the browser to send back on later requests. Session cookies usually carry a random **session ID**. Attributes (Secure, HttpOnly, SameSite, Domain, Path, Expires/Max-Age) control when cookies are sent and how resilient they are to attacks.

**Why it matters (1–2 lines):**  
Auth on the web = cookies and sessions. **HttpOnly** reduces XSS token theft; **SameSite** reduces CSRF; **Secure** forces HTTPS; tight **Domain/Path** scopes reduce exposure.

---

## Commands I ran (Git Bash)

###  See a Set-Cookie from the server
```bash
# Headers only (-D - dumps headers); you may see a redirect
curl -sS -D - https://httpbingo.org/cookies/set?demo=123 > /dev/null

## Findings (LC-005)

- **Set-Cookie observed:** `demo=123; HttpOnly` (server instructed client to store cookie).  
- **Jar capture:** Stored cookie in `jar.txt`, then sent it back; `/cookies` echoed `{ "demo": "123" }`.  
- **Overwrite behavior:** Adding `role=user` with `-c jar.txt` replaced the file, so only `role=user` remained.  
  - Lesson: curl’s `-c` flag **overwrites** unless combined with `-b jar.txt -c jar.txt`. Browsers automatically merge cookies.  
- **Flags seen:** HttpOnly present. No Secure or SameSite observed here.

---

## Key Notes & Security Context

- **Cookies = state on the web.** HTTP is stateless by default; cookies let servers “remember” you (e.g., login session IDs).  
- **Session cookies:** Usually hold a random unique token, not your actual data. That token maps to server-side state.  
- **HttpOnly:** Defends against XSS (JavaScript cannot read cookies marked HttpOnly). Critical for protecting session tokens.  
- **Secure flag:** Forces cookie transmission only over HTTPS, preventing theft via sniffing.  
- **SameSite flag:** Controls cross-site sending. Protects against CSRF by limiting when cookies attach to requests.  
- **Domain/Path:** Control scope of where cookies are sent. Tighter scopes reduce risk of exposure.

---

## What I Learned

- I saw firsthand how a server sets cookies and how a client stores/returns them.  
- I now understand the role of security flags:
  - HttpOnly → protects against XSS cookie theft.  
  - Secure → protects against sniffing on plaintext HTTP.  
  - SameSite → mitigates CSRF.  
- The behavior of tools like curl (overwriting vs merging) is important when simulating browsers.  
- In real-world security, **broken cookie practices = broken auth.** Attackers target misconfigured cookies for session hijacking.

