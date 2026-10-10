import json

files = ["index.html", "../wedding/index.html"]

svg_url = "data:image/svg+xml,<svg xmlns=%22http://www.w3.org/2000/svg%22 viewBox=%220 0 100 100%22><text y=%22.9em%22 font-size=%2290%22>❤️</text></svg>"

for filename in files:
    with open(filename, "r", encoding="utf-8") as f:
        content = f.read()

    # Replace HTML head links
    content = content.replace('href="images/favicon.ico"', f'href="{svg_url}"')
    content = content.replace('href="images/icon-v2.png"', f'href="{svg_url}"')
    content = content.replace('href="images/icon-512-v2.png"', f'href="{svg_url}"')
    content = content.replace('href="images/icon-180-v2.png"', f'href="{svg_url}"')
    content = content.replace('href="images/icon-48-v2.png"', f'href="{svg_url}"')
    content = content.replace('href="js/favicon.ico"', f'href="{svg_url}"')

    # Replace JSON payload links (escaping \")
    content = content.replace(r'\"href\":\"/favicon.ico\"', f'\\\"href\\\":\\\"{svg_url}\\\"')
    content = content.replace(r'\"href\":\"/icon-v2.png\"', f'\\\"href\\\":\\\"{svg_url}\\\"')
    content = content.replace(r'\"href\":\"/icon-512-v2.png\"', f'\\\"href\\\":\\\"{svg_url}\\\"')
    content = content.replace(r'\"href\":\"/icon-180-v2.png\"', f'\\\"href\\\":\\\"{svg_url}\\\"')
    content = content.replace(r'\"href\":\"/icon-48-v2.png\"', f'\\\"href\\\":\\\"{svg_url}\\\"')

    # Replace JSON payload links with just one level of escape if present
    content = content.replace(r'"href":"/favicon.ico"', f'"href":"{svg_url}"')
    content = content.replace(r'"href":"/icon-v2.png"', f'"href":"{svg_url}"')
    
    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)

print("Done updating favicons to heart")
