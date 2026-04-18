import os
import re
import urllib.request
import urllib.error
from pathlib import Path

html_file = 'd:\\WEBSITES\\web_hotel\\menu.html'
img_dir = 'd:\\WEBSITES\\web_hotel\\assets\\img'
os.makedirs(img_dir, exist_ok=True)

with open(html_file, 'r', encoding='utf-8') as f:
    text = f.read()

pattern = re.compile(r'<img\s+src="([^"]+)"\s+alt="([^"]+)">')

def replace_img(match):
    url = match.group(1)
    alt = match.group(2)
    # create a safe filename
    filename = "".join([c for c in alt if c.isalpha() or c.isdigit() or c==' ']).rstrip().replace(' ', '_').lower() + ".jpg"
    filepath = os.path.join(img_dir, filename)
    rel_path = f"assets/img/{filename}"

    if url.startswith('http'):
        if not os.path.exists(filepath):
            print(f"Downloading {url} to {filepath}")
            req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
            try:
                with urllib.request.urlopen(req) as response, open(filepath, 'wb') as out_file:
                    data = response.read()
                    out_file.write(data)
            except Exception as e:
                print(f"Failed to download {url}: {e}")
                return match.group(0) # don't replace if failed
    
    return f'<img src="{rel_path}" alt="{alt}">'

new_text = pattern.sub(replace_img, text)

with open(html_file, 'w', encoding='utf-8') as f:
    f.write(new_text)

print("Images downloaded and HTML updated!")
