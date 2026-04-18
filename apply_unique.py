import re

html_file = 'd:\\WEBSITES\\web_hotel\\menu.html'
with open(html_file, 'r', encoding='utf-8') as f:
    text = f.read()

count = 1
def replace_img(match):
    global count
    res = f'<img src="https://loremflickr.com/400/300/indian,food,meal?lock={count}" alt="{match.group(2)}">'
    count += 1
    return res

pattern = re.compile(r'<img\s+src="([^"]+)"\s+alt="([^"]+)">')
new_text = pattern.sub(replace_img, text)

with open(html_file, 'w', encoding='utf-8') as f:
    f.write(new_text)

# Do the same for index.html
count2 = 100
with open('d:\\WEBSITES\\web_hotel\\index.html', 'r', encoding='utf-8') as f:
    idx_text = f.read()

def replace_idx(match):
    global count2
    res = f'<img src="https://loremflickr.com/600/400/indian,food,meal?lock={count2}" alt="{match.group(2)}">'
    count2 += 1
    return res

new_idx = pattern.sub(replace_idx, idx_text)

with open('d:\\WEBSITES\\web_hotel\\index.html', 'w', encoding='utf-8') as f:
    f.write(new_idx)

print("Unique placeholders applied successfully!")
