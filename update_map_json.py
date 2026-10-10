import json

with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

# Update mapAddress to point to the new coordinates
content = content.replace(r'\"mapAddress\":\"https://maps.app.goo.gl/gh3TjMBwVNHcBrzQ8\\\\n\"', r'\"mapAddress\":\"https://www.google.com/maps?q=20.660867,105.903496\"')
content = content.replace(r'\"latitude\":20.5633316', r'\"latitude\":20.660867')
content = content.replace(r'\"longitude\":105.9118741', r'\"longitude\":105.903496')

with open("index.html", "w", encoding="utf-8") as f:
    f.write(content)

print("Done updating json map links")
