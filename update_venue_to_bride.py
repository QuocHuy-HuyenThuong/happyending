import json

with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

# Replace address strings
content = content.replace("TDP Nguyễn Thiện, Phường Phù Vân, Tỉnh Ninh Bình", "TDP Hương Cát, Phường Duy Hà, Tỉnh Ninh Bình")

# Replace partyVenueTitle
content = content.replace("Tiệc cưới sẽ tổ chức tại tư gia nhà trai", "Tiệc cưới sẽ tổ chức tại tư gia nhà gái")
content = content.replace("TƯ GIA NHÀ TRAI", "TƯ GIA NHÀ GÁI") # Just in case

with open("index.html", "w", encoding="utf-8") as f:
    f.write(content)

print("Done updating address to bride's side")
