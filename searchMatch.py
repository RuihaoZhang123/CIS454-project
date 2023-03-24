import requests
from riotwatcher import LolWatcher, TftWatcher
import pandas as pd

lolApiKey = "RGAPI-0175be55-dcd4-4c8d-a300-57d5232f50e6"
tftApiKey = "RGAPI-00d5ca77-1f7c-4342-b8c0-0cbdebee23c7"


# class of searchMatch containing all function relate to API
class SearchMatch:
    def __init__(self, region, gameType, summonerName):
        self.region = self._translateRegion(region)
        self.gameType = gameType
        self.summonerName = summonerName
        self.searchComplete = True
        self.match_details = []
        self.rankedInfo = []
        self.me = {}
        self.errorCase = ""
        self._matchSearch()

    # matchSearch make requests to riot Api based on the given region, game and, summonerName Then update
    # information of the variables
    def _matchSearch(self):
        # identify the game mode searching for
        if self.gameType == "lol":
            watcher = LolWatcher(lolApiKey)
            # try to request data by api with given summonerName
            try:
                self.me = watcher.summoner.by_name(self.region, self.summonerName)
            except requests.exceptions.HTTPError as err:
                self.errorCase = err
                self.searchComplete = False
                return -1
            self.rankedInfo = watcher.league.by_summoner(self.region, self.me['id'])
            self.summonerName = self.me['name']
            # print(self.rankedInfo)
            # get a 20 matches' ID of the summoner
            my_matches = watcher.match.matchlist_by_puuid(self.region, self.me['puuid'], 0)
            # print(my_matches)
            for match in my_matches:
                match_detail = watcher.match.by_id(self.region, match)
                # print(match_detail['info']['participants'][0].keys())
                self.match_details.append(match_detail)
        elif self.gameType == "tft":
            watcher = TftWatcher(tftApiKey)
            try:
                self.me = watcher.summoner.by_name(self.region, self.summonerName)
            except requests.exceptions.HTTPError as err:
                self.errorCase = err
                self.searchComplete = False
                return -1
            self.rankedInfo = watcher.league.by_summoner(self.region, self.me['id'])
            # print(self.rankedInfo)
            self.summonerName = self.me['name']
            # get list of tft matches of the summoner
            my_matches = watcher.match.by_puuid(self.region, self.me['puuid'])
            # fetch at most 20 match detail
            for match in my_matches:
                match_detail = watcher.match.by_id(self.region, match)
                # print(match_detail['info']["participants"][0]["traits"])
                # print(match_detail['info']['participants'][0].keys())
                self.match_details.append(match_detail)
            # print(self.match_details[0]['metadata']['data_version'])
            # print(self.match_details[0]['info']['game_version'])
            # print(self.match_details[0]['info']['participants'][1]["units"][0].keys())
            # print(self.match_details[0]['info']['participants'][1]['units'])
            # print(self.match_details[0]['info']['participants'][2]['traits'])

    # translate region given to api readable region
    def _translateRegion(self, region):
        if region == "Brazil":
            return "br1"
        if region == "EU Nordic & East":
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

    def view_more(self, start_index):
        watcher = TftWatcher(tftApiKey)
        my_matches = watcher.match.by_puuid(self.region, self.me['puuid'], start=start_index, count=10)
        self.match_details = []
        for match in my_matches:
            match_detail = watcher.match.by_id(self.region, match)
            self.match_details.append(match_detail)

    # display specific detail of the match in the terminal
    def _matchDisplay(self, match_detail):
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


# hi = SearchMatch("North America", "tft", "The Donkey")
# hik = SearchMatch("Korea", "tft", "hide on bush")
