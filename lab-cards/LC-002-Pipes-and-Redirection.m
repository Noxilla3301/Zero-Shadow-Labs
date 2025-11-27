# LC-002 — Pipes & Redirection

**What it is (2–3 lines):**  
Shell redirection saves command output to files; pipes send one command’s output into another. This lets you chain simple tools into powerful one-liners for quick text parsing.

**Why it matters (1–2 lines):**  
You’ll constantly need to sift logs, parse HTML, and chain tools during recon—pipes/redirects are the glue.

**How it works (bullets):**
- `>` overwrite file; `>>` append.
- `|` pipe STDOUT of left command to right command’s STDIN.
- Errors go to STDERR; redirect with `2>`.

---

## Commands I ran and outputs
Ayush@DESKTOP-3QJ262S MINGW64 ~/OneDrive/Documents/Zero-Shadow-Labs (main)
$ curl -s https://example.com > page.html

Ayush@DESKTOP-3QJ262S MINGW64 ~/OneDrive/Documents/Zero-Shadow-Labs (main)
$ grep -o 'href="[^"]*"' page.html | cut -d'"' -f2 | sort | uniq > links.txt

Ayush@DESKTOP-3QJ262S MINGW64 ~/OneDrive/Documents/Zero-Shadow-Labs (main)
$ wc -l links.txt
1 links.txt

Ayush@DESKTOP-3QJ262S MINGW64 ~/OneDrive/Documents/Zero-Shadow-Labs (main)
$ head -n 10 links.txt
https://www.iana.org/domains/example
