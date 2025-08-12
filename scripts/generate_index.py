# generate_index.py – lists Lab Cards to website/cards.md
import os, re
root = 'fundamentals-sprint/lab-cards'
items = sorted([f for f in os.listdir(root) if f.endswith('.md')])
os.makedirs('website', exist_ok=True)
with open('website/cards.md','w',encoding='utf-8') as f:
    f.write('# Lab Cards\n\n')
    for fn in items:
        title = re.sub(r'^LC-\d+-','',fn).replace('.md','').replace('-',' ')
        f.write(f'- [{fn}](../{root}/{fn}) — {title}\n')
print('[+] wrote website/cards.md')