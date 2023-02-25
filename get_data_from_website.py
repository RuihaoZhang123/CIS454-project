import requests
e = requests.get(f"https://raw.communitydragon.org/latest/plugins/rcp-be-lol-game-data/global/default/v1/champion-icons/1.ogg")
errorcode = e.status_code
with open(f"1.ogg", "wb") as file:
    file.write(e.content)
"""
for i in range(1000):
    r = requests.get(f"https://raw.communitydragon.org/latest/plugins/rcp-be-lol-game-data/global/default/v1/champion-icons/{i}.png")
    if r.status_code == errorcode:
        continue
    with open(f"{i}.png", "wb") as file:
        file.write(r.content)
"""