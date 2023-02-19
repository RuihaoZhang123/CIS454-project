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
            participants_row = {'champion': row['championId'], 'spell1': row['spell1Casts'],
                                'spell2': row['spell2Casts'], 'win': row['win'], 'kills': row['kills'],
                                'deaths': row['deaths'], 'assists': row['assists'],
                                'totalDamageDealt': row['totalDamageDealt'], 'goldEarned': row['goldEarned'],
                                'champLevel': row['champLevel'], 'totalMinionsKilled': row['totalMinionsKilled'],
                                'item0': row['item0'], 'item1': row['item1'], 'item2': row['item2'],
                                'role': row['role']}
            participants.append(participants_row)
        df = pd.DataFrame(data=participants)
        print(df.to_string())
    elif game == "tft":
        watcher = TftWatcher(tftApiKey)
        me = watcher.summoner.by_name(region, summonerName)
        print(me)
        my_matches = watcher.match.by_puuid(region, me['puuid'])
        print(my_matches)
        # fetch last match detail
        last_match = my_matches[0]
        match_detail = watcher.match.by_id(region, last_match)
        print(match_detail['info']["participants"][0]["traits"])
        print(match_detail['info']['participants'][0].keys())


matchSearch("na1", "lol", "Llama Smoothie")
