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
                            'role': row['role'], 'item6': row['item6']}
        participants.append(participants_row)
    df = pd.DataFrame(data=participants)
    print(df.to_string())
    return


def translateRegion(region):
    if region == "Brazil":
        return "br1"
    if region == "EU Nordic&East":
        return "eun1"
    if region == "EU West":
        return "euw1"
    if region == "Japan":
        return "jp1"
    if region == "Korea":
        return "kr"
    if region == "Latin America North":
        return "la1"
    if region == "Latin America South":
        return "la2"
    if region == "North America":
        return "na1"
    if region == "Oceania":
        return "OC1"
    if region == "Philippines":
        return "PH2"
    if region == "Russia":
        return "RU"
    if region == "singapore":
        return "SG2"
    if region == "Thailand":
        return "TH2"
    if region == "Turkey":
        return "TR1"
    if region == "Taiwan":
        return "TW2"
    if region == "Vietnam":
        return "VN2"


# return a dictionary of data or -1 on failure
def matchSearch(region, game, summonerName):
    # identify the game mode searching for
    if game == "lol":
        watcher = LolWatcher(lolApiKey)
        try:
            me = watcher.summoner.by_name(translateRegion(region), summonerName)
        except requests.exceptions.HTTPError as err:
            print(err)
            return -1
        print(me)
        rankedStatus = watcher.league.by_summoner(region, me['id'])
        # print(me)
        # get a list of matches from the summoner
        my_matches = watcher.match.matchlist_by_puuid(translateRegion(region), me['puuid'], 0)
        # print(my_matches)
        match_list = []
        # fetch at most 20 match detail
        for match in my_matches:
            match_detail = watcher.match.by_id(translateRegion(region), match)
            # print(match_detail['info']['participants'][0].keys())
            print(match_detail['info'].keys())
            print(match_detail['info']['queueId'])
            print(match_detail['info']['gameDuration'])
            matchDisplay(match_detail)
            match_list.append(match_detail)
        return match_list
    elif game == "tft":
        watcher = TftWatcher(tftApiKey)
        try:
            me = watcher.summoner.by_name(translateRegion(region), summonerName)
        except ApiError:
            return -1
        print(me)
        # get list of tft matches of the summoner
        my_matches = watcher.match.by_puuid(translateRegion(region), me['puuid'])
        print(my_matches)
        # fetch at most 20 match detail
        match_list = []
        for match in my_matches:
            match_detail = watcher.match.by_id(translateRegion(region), match)
            print(match_detail['info']["participants"][0]["traits"])
            print(match_detail['info']['participants'][0].keys())
            match_list.append(match)
        return match_list

matchSearch("Korea", "lol", "hide on bush")
