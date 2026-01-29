# Define suspicion score - this can go up or down, but for
# now we can focus on how it goes up. Eg. if any IP tries to 
# log into root and fails, increase 'SS' x2. 

# Define a counter to determine how many consecutive 404
# errors make the log / line 'malicious' or 'suspicious'

# High path churn is almost certainly malicious activity, 
# but how to code this in is very much up in the air

# Real world logs won't always be clean, for now we start
# with the format in sample log file, but LS needs to 
# account for irregularities in formatting eventually

# Key note: we can only say what's abnormal if we know what
# is 'normal'. 

# Define thresholds - how many requests per min is too many?
# What does 'high path churn' actually look like?

# We will not use a binary 'good' or 'bad' metric. We'll use
# a point system. Lower points = less suspicious, and v.v

# Standard 404: +2 points.

# SSH/Auth Failure: +10 points.

# Root Target: x2 multiplier (or +10 bonus points).

# Critical Threshold: 30 points.

# Code architecture should look like this:
# Ingest: Read log line by line
# Extract: Pull IP, status code, and Path using Regex
# Track: Store counts in a dictionary
# Calculate: Run the math (Ratio = 404s / Total)
# Judge: TBD

# ------------------------------------------------------------

# Ingest

import sys
from pathlib import Path
import re

if len(sys.argv) < 2:
    print("Error: No log file provided.")
    print("Usage: python LS.py <filename>")
    sys.exit()

log_filename = sys.argv[1]

base_dir = Path(__file__).parent
file_path = base_dir / log_filename

if not file_path.exists():
    print(f"Error: The file '{log_filename} was not found.")
    sys.exit()

suspects = {}

with file_path.open("r") as infile:
    # counter = 0
    for line in infile:
        if "Failed password" in line:
            match = re.search(r"(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})", line)
            if match:
                ip = match.group(1)
                if "root" in line:
                    score_to_add = 20
                else:
                    score_to_add = 10
                suspects[ip] = suspects.get(ip, 0) + score_to_add
                
print("\n[+] Processing...")

for ip, score in suspects.items():
    if score >= 50:
        print(f" ALERT: SUSPICIOUS ACTIVITY FOUND | Source: {ip} | Score: {score}")
    else:
        print(f" Warning: Low-level activity from {ip} - ({score} points) ")  

