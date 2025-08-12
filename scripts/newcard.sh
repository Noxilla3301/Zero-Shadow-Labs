#!/usr/bin/env bash
# newcard.sh usage: ./newcard.sh 013 "Burp Repeater Tips"
n=$1; title=$2
safe=${title// /-}
fn=fundamentals-sprint/lab-cards/LC-$(printf "%03d" $n)-$safe.md
cat > "$fn" <<'EOF'
# <Topic> — Lab Card
What it is (2–3 lines):
Why it matters (1–2 lines):
How it works (bullets):
Commands / Requests I ran:
- ...
Common pitfalls:
Defender indicators (if offense):
Remediation (1–3 bullets):
EOF
echo "[+] Created $fn"
