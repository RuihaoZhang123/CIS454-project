import requests
from riotwatcher import LolWatcher, ApiError, TftWatcher


def matchSearch(region, game, summonerName):
    lolApiKey = "RGAPI-0175be55-dcd4-4c8d-a300-57d5232f50e6"
    tftApiKey = "RGAPI-00d5ca77-1f7c-4342-b8c0-0cbdebee23c7"
    if game == "lol":
        watcher = LolWatcher(lolApiKey)
        me = watcher.summoner.by_name(region, summonerName)
        print(me)
    elif game == "tft":
        watcher = TftWatcher(tftApiKey)
        me = watcher.summoner.by_name(region, summonerName)
        print(me)


matchSearch("na1", "lol", "Doublelift")
matchSearch("na1", "tft", "Doublelift")