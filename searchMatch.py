import requests
from riotwatcher import LolWatcher, TftWatcher
lolApiKey = "RGAPI-0175be55-dcd4-4c8d-a300-57d5232f50e6"
tftApiKey = "RGAPI-00d5ca77-1f7c-4342-b8c0-0cbdebee23c7"


# class of searchMatch containing all function relate to API
class SearchMatch:
    def __init__(self, region, gameType, summonerName):
        self.region = region     # region can only be string readable by tranlsateRegion
        self.gameType = gameType    # lol or tft
        self.summonerName = summonerName    # any string
        self.searchComplete = True
        self.match_details = []
        self.rankedInfo = []
        self.me = {}
        self.errorCase = ""
        self._lol_watcher = LolWatcher(lolApiKey)
        self._tft_watcher = TftWatcher(tftApiKey)
        self.region = self._translateRegion(region)
        self._matchSearch()

    # matchSearch make requests to riot Api based on the given region, game and, summonerName Then update
    # information of the variables. Require self.region, self.gameType with valid input
    def _matchSearch(self):
        # identify the game mode searching for
        if self.gameType == "lol":
            # try to request data by api with given summonerName
            try:
                self.me = self._lol_watcher.summoner.by_name(self.region, self.summonerName)
            except requests.exceptions.HTTPError as err:
                self.errorCase = "Summoner name not found in region"
                self.searchComplete = False
            # check whether
            if not self.searchComplete:
                return -1
            else:
                pass
            self.rankedInfo = self._lol_watcher.league.by_summoner(self.region, self.me['id'])
            self.summonerName = self.me['name']
            # get a 20 matches' ID of the summoner
            my_matches = self._lol_watcher.match.matchlist_by_puuid(self.region, self.me['puuid'], 0)
            # print(my_matches)
            for match in my_matches:
                match_detail = self._lol_watcher.match.by_id(self.region, match)
                self.match_details.append(match_detail)
        elif self.gameType == "tft":
            try:
                self.me = self._tft_watcher.summoner.by_name(self.region, self.summonerName)
            except requests.exceptions.HTTPError as err:
                self.errorCase = "Summoner name not found in region"
                self.searchComplete = False
                return -1
            self.rankedInfo = self._tft_watcher.league.by_summoner(self.region, self.me['id'])
            # print(self.rankedInfo)
            self.summonerName = self.me['name']
            # get list of tft matches of the summoner
            my_matches = self._tft_watcher.match.by_puuid(self.region, self.me['puuid'])
            # fetch at most 20 match detail
            for match in my_matches:
                match_detail = self._tft_watcher.match.by_id(self.region, match)
                self.match_details.append(match_detail)

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
        else:
            self.searchComplete = False
            self.errorCase = "region not valid"

    # based on given how many match has been provided, add details of the following 10 games to self.match_details
    def lol_view_more(self, start_index):
        my_matches = self._lol_watcher.match.matchlist_by_puuid(self.region, self.me['puuid'], start=start_index, count=10)
        self.match_details = []
        for match in my_matches:
            match_detail = self._lol_watcher.match.by_id(self.region, match)
            self.match_details.append(match_detail)

    # based on given how many match has been provided, add details of the following 10 games to self.match_details
    def tft_view_more(self, start_index):
        my_matches = self._tft_watcher.match.by_puuid(self.region, self.me['puuid'], start=start_index, count=10)
        self.match_details = []
        for match in my_matches:
            match_detail = self._tft_watcher.match.by_id(self.region, match)
            self.match_details.append(match_detail)
