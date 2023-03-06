import json


class gameStat:
    def __init__(self):
        self.queues = []
        self.summoner = []
        self.runesReforged = []
        self.tft_item = {}
        self.tft_trait = {}
        self.tft_queues = {}
        self.tft_tactician = {}
        self.tft_champion = {}
        self._get_data()

    # private methods
    # extract queues data from json file
    def _get_data(self):
        with open('data/queues.json') as json_file:
            self.queues = json.load(json_file)

        with open('data/summoner.json') as json_file:
            self.summonerSpell = json.load(json_file)

        with open('data/runesReforged.json') as json_file:
            self.runes = json.load(json_file)

        with open('data/tft-item.json') as json_file:
            self.tft_item = json.load(json_file)

        with open('data/tft-trait.json') as json_file:
            self.tft_trait = json.load(json_file)

        with open('data/tft-queues.json') as json_file:
            self.tft_queues = json.load(json_file)

        with open('data/tft-tactician.json') as json_file:
            self.tft_tactician = json.load(json_file)

        with open('data/tft-champion.json') as json_file:
            self.tft_champion = json.load(json_file)

    # public methods
    # return description of queue given queueID
    def identify_queue(self, queueID):
        for queue in self.queues:
            if queue['queueId'] == queueID:
                return queue['description']

    # return image path of summoner spell given spellKey
    def identify_Summoner_spell(self, spellKey):
        for i in self.summonerSpell['data'].values():
            if i['key'] == str(spellKey):
                return i["image"]['full']

    # return runes path given runeId
    def identify_runes(self, runeId):
        if runeId == 8369:
            return "perk-images/Styles/Inspiration/FirstStrike/FirstStrike.png"
        for i in self.runes:
            if i['id'] == runeId:
                return i['icon']
            for j in i['slots'][0]['runes']:
                if j['id'] == runeId:
                    return j["icon"]

    # return queue name given queueID
    def identify_tft_queue(self, queueID):
        return self.tft_queues['data'][str(queueID)]['name']

    # return trait image path given trait name
    def identify_tft_trait(self, traitName):
        return self.tft_trait['data'][traitName]['image']['full']

    # return trait image path given item name
    def identify_tft_item(self, itemName):
        return self.tft_item['data'][itemName]['image']['full']

    # return augment image path given augment name
    def identify_tft_champion(self, augmentName):
        champ = self.tft_champion['data'][augmentName]['image']['full']
        return champ if champ != "TFT8_WuKong.TFT_Set8.png" else "TFT8_Wukong.TFT_Set8.png"

    # return tactician image path given tactician ID
    def identify_tft_tactician(self, tacticianID):
        return self.tft_tactician['data'][str(tacticianID)]['image']['full']