import requests
import json
from pprint import pprint


NAME = "KimiGets0FPS_YT"

UUID = "bfd0da1ed34f4887aa7c643258539fa0"
DASHED_UUID = "bfd0da1e-d34f-4887-aa7c-643258539fa0"

API_KEY = "6ddfb004-aea1-42e8-9e6e-896ba00a160a"

uuid_link = f"https://api.hypixel.net/player?key={API_KEY}&uuid={DASHED_UUID}"
name_link = f"https://api.hypixel.net/player?key={API_KEY}&name={NAME}"

print(uuid_link)


def getinfo(call):
    req = requests.get(call)
    return req.json()


pprint(getinfo(name_link))
