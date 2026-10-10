import json

files = ["index.html", "../wedding/index.html"]

for filename in files:
    with open(filename, "r", encoding="utf-8") as f:
        content = f.read()

    # Next.js metadata strings
    # We want to replace "Huyền Thương \u0026 Quốc Huy" with "Huyền Thương \u0026 Quốc Huy ❤️"
    content = content.replace(r"Huyền Thương \u0026 Quốc Huy", r"Huyền Thương \u0026 Quốc Huy ❤️")
    content = content.replace(r"Quốc Huy \u0026 Huyền Thương", r"Quốc Huy \u0026 Huyền Thương ❤️")
    
    # Just in case there are double hearts from previous attempts
    content = content.replace("❤️ ❤️", "❤️")
    
    # Same for \\u0026
    content = content.replace(r"Huyền Thương \\u0026 Quốc Huy", r"Huyền Thương \\u0026 Quốc Huy ❤️")
    content = content.replace(r"Quốc Huy \\u0026 Huyền Thương", r"Quốc Huy \\u0026 Huyền Thương ❤️")
    content = content.replace("❤️ ❤️", "❤️")
    
    # Also verify there are no missing hearts on the standard strings
    content = content.replace("Huyền Thương & Quốc Huy", "Huyền Thương & Quốc Huy ❤️")
    content = content.replace("Quốc Huy & Huyền Thương", "Quốc Huy & Huyền Thương ❤️")
    content = content.replace("Huyền Thương &amp; Quốc Huy", "Huyền Thương &amp; Quốc Huy ❤️")
    content = content.replace("Quốc Huy &amp; Huyền Thương", "Quốc Huy &amp; Huyền Thương ❤️")
    content = content.replace("❤️ ❤️", "❤️")

    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)

print("Done fixing hearts")
