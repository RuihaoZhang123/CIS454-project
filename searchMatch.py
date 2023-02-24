import requests
from riotwatcher import LolWatcher, ApiError, TftWatcher
import pandas as pd

lolApiKey = "RGAPI-0175be55-dcd4-4c8d-a300-57d5232f50e6"
tftApiKey = "RGAPI-00d5ca77-1f7c-4342-b8c0-0cbdebee23c7"


# display specific detail of the match
def matchDisplay(match_detail):
    # set dictionaries with useful information for chart display
    participants = []
    for row in match_detail['info']['participants']:
        participants_row = {'summonerName': row['summonerName'], 'champion': row['championId'],
                            'unrealKills': row['unrealKills'], 'spell1': row['spell1Casts'],
                            'spell2': row['spell2Casts'], 'win': row['win'], 'kills': row['kills'],
                            'deaths': row['deaths'], 'assists': row['assists'],
                            'totalDamageDealt': row['totalDamageDealt'], 'goldEarned': row['goldEarned'],
                            'champLevel': row['champLevel'], 'totalMinionsKilled': row['totalMinionsKilled'],
                            'item0': row['item0'], 'item1': row['item1'], 'item2': row['item2'],
                            'role': row['role']}
        participants.append(participants_row)
    df = pd.DataFrame(data=participants)
    print(df.to_string())
    return


# return a dictionary of data or -1 on failure
def matchSearch(region, game, summonerName):
    # identify the game mode searching for
    if game == "lol":
        watcher = LolWatcher(lolApiKey)
        try:
            me = watcher.summoner.by_name(region, summonerName)
        except requests.exceptions.HTTPError as err:
            print(err)
            return -1
        print(me)
        # print(me)
        # get a list of matches from the summoner
        my_matches = watcher.match.matchlist_by_puuid(region, me['puuid'], 0)
        # print(my_matches)
        # fetch last match detail
        last_match = my_matches[0]
        match_detail = watcher.match.by_id(region, last_match)
        print(match_detail['info']['participants'][0].keys())
        matchDisplay(match_detail)
        return my_matches
    elif game == "tft":
        watcher = TftWatcher(tftApiKey)
        try:
            me = watcher.summoner.by_name(region, summonerName)
        except ApiError:
            return -1
        print(me)
        # get list of tft matches of the summoner
        my_matches = watcher.match.by_puuid(region, me['puuid'])
        print(my_matches)
        # fetch last match detail
        last_match = my_matches[0]
        match_detail = watcher.match.by_id(region, last_match)
        print(match_detail['info']["participants"][0]["traits"])
        print(match_detail['info']['participants'][0].keys())
        return match_detail


matchSearch("na1", "lol", "llama Smoothie")
