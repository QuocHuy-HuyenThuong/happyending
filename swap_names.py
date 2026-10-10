import json

with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

# Replace brideFirst boolean
content = content.replace(r'\"brideFirst\":false', r'\"brideFirst\":true')

# Replace the names
content = content.replace("Quốc Huy & Huyền Thương", "Huyền Thương & Quốc Huy")
content = content.replace("Quốc Huy &amp; Huyền Thương", "Huyền Thương &amp; Quốc Huy")
# Also handle any unicode encoded ones if they exist, but they likely aren't there.

with open("index.html", "w", encoding="utf-8") as f:
    f.write(content)

print("Done swapping names in happyending")
