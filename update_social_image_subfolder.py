import os

for repo in ["happyending", "wedding"]:
    filepath = f"../{repo}/index.html"
    if repo == "happyending":
        filepath = "index.html"
        
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    # The current URL is https://quochuy-huyenthuong.github.io/images/quochuy-thithuong.jpg
    # We want to change it to include the subfolder (repo name)
    correct_url = f"https://quochuy-huyenthuong.github.io/{repo}/images/quochuy-thithuong.jpg"
    
    # Replace in HTML tags and JSON payload
    content = content.replace(
        "https://quochuy-huyenthuong.github.io/images/quochuy-thithuong.jpg",
        correct_url
    )

    # Insert secure_url and type after og:image if they don't exist
    if 'property="og:image:secure_url"' not in content:
        insert_text = f'\n  <meta property="og:image:secure_url" content="{correct_url}">\n  <meta property="og:image:type" content="image/jpeg">'
        content = content.replace(
            f'<meta property="og:image" content="{correct_url}">',
            f'<meta property="og:image" content="{correct_url}">{insert_text}'
        )

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)

print("Done updating social image URLs with subfolders")
