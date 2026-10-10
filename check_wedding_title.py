import re

with open("../wedding/index.html", "r", encoding="utf-8") as f:
    content = f.read()

# Let's see what the title is in wedding project
title_match = re.search(r"<title>(.*?)</title>", content)
if title_match:
    print(f"Title in wedding: {title_match.group(1)}")
else:
    print("Title not found in wedding")
