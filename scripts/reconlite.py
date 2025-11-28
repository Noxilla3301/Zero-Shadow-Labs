# reconlite.py — extract forms to JSON
# usage: python reconlite.py --url https://example.com --out forms.json
import argparse, json, requests
from bs4 import BeautifulSoup

def extract_forms(url):
    r = requests.get(url, timeout=10)
    soup = BeautifulSoup(r.text, "html.parser")
    forms = []
    for f in soup.find_all("form"):
        action = f.get("action") or ""
        method = (f.get("method") or "GET").upper()
        inputs = []
        for i in f.find_all(["input","textarea","select"]):
            inputs.append({"name": i.get("name"), "type": i.get("type"), "id": i.get("id")})
        forms.append({"action": action, "method": method, "inputs": inputs})
    return {"url": url, "forms": forms}

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--url", required=True)
    ap.add_argument("--out", default="forms.json")
    args = ap.parse_args()
    data = extract_forms(args.url)
    with open(args.out, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
    print(f"[+] wrote {args.out} with {len(data['forms'])} forms")
