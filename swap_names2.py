import json

with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

# Replace brideFirst boolean with various escape levels just to be safe
content = content.replace(r'\"brideFirst\":false', r'\"brideFirst\":true')
content = content.replace(r'\\"brideFirst\\":false', r'\\"brideFirst\\":true')
content = content.replace(r'\"brideFirst\": false', r'\"brideFirst\": true')
content = content.replace(r'"brideFirst":false', r'"brideFirst":true')
content = content.replace(r'"brideFirst": false', r'"brideFirst": true')

# Replace names
content = content.replace("Quốc Huy & Huyền Thương", "Huyền Thương & Quốc Huy")
content = content.replace("Quốc Huy &amp; Huyền Thương", "Huyền Thương &amp; Quốc Huy")
content = content.replace(r"Quốc Huy \u0026 Huyền Thương", r"Huyền Thương \u0026 Quốc Huy")
content = content.replace(r"Quốc Huy \\u0026 Huyền Thương", r"Huyền Thương \\u0026 Quốc Huy")

# Replace names with heart if any was already replaced incorrectly or needs to be swapped
# Actually, the previous step just replaced Quốc Huy & Huyền Thương with Huyền Thương & Quốc Huy, 
# so if it was "Quốc Huy & Huyền Thương ❤️", it became "Huyền Thương & Quốc Huy ❤️". 
# But the \u0026 versions were missed. This script catches them.

with open("index.html", "w", encoding="utf-8") as f:
    f.write(content)

print("Done swapping names completely")
