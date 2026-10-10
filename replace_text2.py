import json

with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

# Replacements
content = content.replace(r'\"startDate\":\"2026-10-27T18:00:00\"', r'\"startDate\":\"2026-10-27T17:00:00\"')
content = content.replace(r'\"date\":\"2026-10-27\",\"time\":\"18:00\"', r'\"date\":\"2026-10-27\",\"time\":\"17:00\"')
content = content.replace(r'\"time\":\"08:45\",\"header\":{\"vi\":\"LỄ THÀNH HÔN ĐƯỢC TỔ CHỨC TẠI\\nTƯ GIA NHÀ TRAI\"}', r'\"time\":\"08:00\",\"header\":{\"vi\":\"LỄ THÀNH HÔN ĐƯỢC TỔ CHỨC TẠI\\nTƯ GIA NHÀ GÁI\"}')
content = content.replace(r'\"id\":\"97006ad6\",\"time\":\"18:00\"', r'\"id\":\"97006ad6\",\"time\":\"17:00\"')
content = content.replace(r'\"id\":\"4a19120d\",\"time\":\"18:30\"', r'\"id\":\"4a19120d\",\"time\":\"17:30\"')
content = content.replace(r'\"id\":\"f2e21a86\",\"time\":\"09:00\"', r'\"id\":\"f2e21a86\",\"time\":\"08:00\"')

with open("index.html", "w", encoding="utf-8") as f:
    f.write(content)

print("Done")
