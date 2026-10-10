import json

files = ["index.html", "../wedding/index.html"]

for filename in files:
    with open(filename, "r", encoding="utf-8") as f:
        content = f.read()

    # Replace relative image paths for social meta tags to absolute Github Pages URL
    content = content.replace(
        'content="images/quochuy-thithuong.jpg"',
        'content="https://quochuy-huyenthuong.github.io/images/quochuy-thithuong.jpg"'
    )

    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)

print("Done updating og:image to absolute URL")
