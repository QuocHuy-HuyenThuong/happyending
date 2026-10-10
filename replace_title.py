import json

with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

# Replacements for happyending
content = content.replace("Huyền Thương &amp; Quốc Huy", "Huyền Thương &amp; Quốc Huy ❤️")
content = content.replace("Quốc Huy &amp; Huyền Thương", "Quốc Huy &amp; Huyền Thương ❤️")
content = content.replace("Quốc Huy & Huyền Thương", "Quốc Huy & Huyền Thương ❤️")
content = content.replace("Huyền Thương & Quốc Huy", "Huyền Thương & Quốc Huy ❤️")

# Remove double hearts if any
content = content.replace("❤️ ❤️", "❤️")

with open("index.html", "w", encoding="utf-8") as f:
    f.write(content)

print("Done happyending")
