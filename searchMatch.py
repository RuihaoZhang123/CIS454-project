import requests
from riotwatcher import LolWatcher, ApiError, TftWatcher
import pandas as pd


def matchSearch(region, game, summonerName):
    lolApiKey = "RGAPI-0175be55-dcd4-4c8d-a300-57d5232f50e6"
    tftApiKey = "RGAPI-00d5ca77-1f7c-4342-b8c0-0cbdebee23c7"
    if game == "lol":
        watcher = LolWatcher(lolApiKey)
        me = watcher.summoner.by_name(region, summonerName)
        print(me)

        my_matches = watcher.match.matchlist_by_puuid(region, me['puuid'])
        print(my_matches)
        # fetch last match detail
        last_match = my_matches[0]
        match_detail = watcher.match.by_id(region, last_match)
        print(match_detail['info']['participants'][0].keys())
        participants = []
        for row in match_detail['info']['participants']:
            participants_row = {}
            participants_row['champion'] = row['championId']
            participants_row['spell1'] = row['spell1Casts']
            participants_row['spell2'] = row['spell2Casts']
            participants_row['win'] = row['win']
            participants_row['kills'] = row['kills']
            participants_row['deaths'] = row['deaths']
            participants_row['assists'] = row['assists']
            participants_row['totalDamageDealt'] = row['totalDamageDealt']
            participants_row['goldEarned'] = row['goldEarned']
            participants_row['champLevel'] = row['champLevel']
            participants_row['totalMinionsKilled'] = row['totalMinionsKilled']
            participants_row['item0'] = row['item0']
            participants_row['item1'] = row['item1']
            participants_row['item2'] = row['item2']
            participants_row['role'] = row['role']
            participants.append(participants_row)
        df = pd.DataFrame(data=participants)
        print(df.to_string())
    elif game == "tft":
        watcher = TftWatcher(tftApiKey)
        me = watcher.summoner.by_name(region, summonerName)
        print(me)


matchSearch("na1", "lol", "Llama Smoothie")
