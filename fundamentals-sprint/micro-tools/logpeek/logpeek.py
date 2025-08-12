# logpeek.py — count top paths and status codes
# usage: python logpeek.py --file access.log
import argparse, collections, re

ap = argparse.ArgumentParser()
ap.add_argument("--file", required=True)
args = ap.parse_args()

path_counts = collections.Counter()
code_counts = collections.Counter()

line_re = re.compile(r'"\w+\s+([^"]+)\s+HTTP/[^"]+"\s+(\d{3})')

with open(args.file, "r", encoding="utf-8", errors="ignore") as f:
    for line in f:
        m = line_re.search(line)
        if not m: continue
        path, code = m.group(1), m.group(2)
        path_counts[path] += 1
        code_counts[code] += 1

print("Top paths:")
for p, c in path_counts.most_common(10):
    print(c, p)
print("\nTop status codes:")
for k, v in code_counts.most_common():
    print(v, k)
