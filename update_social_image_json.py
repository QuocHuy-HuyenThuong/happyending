import json
import re

files = ["index.html", "../wedding/index.html"]

for filename in files:
    with open(filename, "r", encoding="utf-8") as f:
        content = f.read()

    # Replace JSON payload OG image URLs with absolute Github Pages URL
    # Find patterns like: https://chungdoi.com/backend-api/api/og/quochuy-thithuong?v=1791563529552
    content = re.sub(
        r'https://chungdoi\.com/backend-api/api/og/quochuy-thithuong\?v=\d+',
        r'https://quochuy-huyenthuong.github.io/images/quochuy-thithuong.jpg',
        content
    )
    
    # Also replace it for ogImage inside initialData (which is used by some components)
    # "ogImage":"https://cdn.chungdoi.com/uploads/97a167e6-9a27-4f8b-a3de-df4d6b1e13a4.jpg"
    # Actually they might want the exact thumbnail image to be quochuy-thithuong.jpg for all.
    content = re.sub(
        r'https://cdn\.chungdoi\.com/uploads/97a167e6-9a27-4f8b-a3de-df4d6b1e13a4\.jpg',
        r'https://quochuy-huyenthuong.github.io/images/quochuy-thithuong.jpg',
        content
    )
    
    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)

print("Done updating json payload OG images")
