from riotstats.models import Summoner, Match, ParticipantStats
from django.utils.dateparse import parse_datetime
from riotwatcher import RiotWatcher, LolWatcher, ApiError
from riotstats.serializers import summonerSerializer, matchSerializer, participantStatsSerializer
from datetime import datetime

API_KEY = "RGAPI-4e72f636-45d7-48db-9575-b85f6ca198ea"

lol_watcher = LolWatcher(f'{API_KEY}')
riot_watcher = RiotWatcher(f'{API_KEY}')

def get_summoner_puuid(username, tag, accRegion):
    accountData = riot_watcher.account.by_riot_id(accRegion, username, tag)
    puuid = accountData['puuid']
    summonerObj, _ = Summoner.objects.get_or_create(
        puuid=puuid, 
        defaults={
            "username": username or "", 
            "tagline": tag or "",
            }
        )
    return summonerObj

def get_match_ids(region, id):
    matchIds = lol_watcher.match.matchlist_by_puuid(region, id, queue='420')
    return matchIds

def get_match_details(summonerObj, matchIds, region):  
    for match in matchIds:
        details = lol_watcher.match.by_id(region, match)
        match_info = details['info']
        match_obj, _ = Match.objects.get_or_create(
            match_id = details['metadata']['matchId'],
            defaults={
                "queue_type": match_info.get("queueId", 0),
                "game_duration": match_info['gameDuration'],
                "game_start": match_info['gameStartTimestamp'],
                "game_version": match_info['gameVersion'],

            }
        )

        for player in match_info['participants']:
            if player['puuid'] == summonerObj.puuid:
                ParticipantStats.objects.get_or_create(
                    summoner=summonerObj,
                    match=match_obj,
                    defaults={
                        "champion": player['championName'],
                        "championLevel": player['champLevel'],
                        "kills": player['kills'],
                        "deaths": player['deaths'],
                        "assists": player['assists'],
                        "winloss": player['win'],
                        "roleItem": player['roleBoundItem'],
                        "item0": player['item0'],
                        "item1": player['item1'],
                        "item2": player['item2'],
                        "item3": player['item3'],
                        "item4": player['item4'],
                        "item5": player['item5'],
                        "item6": player['item6'],
                        "summonerSpell1": player['summoner1Id'],
                        "summonerSpell2": player['summoner2Id'],
                        "mainPerk": player['perks']['styles'][0]['selections'][0]['perk'],
                        "subPerk": player['perks']['styles'][1]['style'],
                        "profileIcon": player['profileIcon'],
                        "summonerLevel": player['summonerLevel']
                    }
                )
        
# accountRegion = "AMERICAS"
# summonerRegion = "NA1"
# gameName = "Caseoh"
# tagLine = "NA1"

# sumObject = get_summoner_puuid(gameName, tagLine, accountRegion)
# # print(sumObject.puuid)
# match_ids = get_match_ids(summonerRegion, sumObject.puuid)
# # print(match_ids)
# get_match_details(sumObject, match_ids, summonerRegion)
# firstSum = Summoner.objects.first()
# firstMatch = Match.objects.first()
# print(firstSum)
# print(firstMatch)
# stats = ParticipantStats.objects.get(summoner=firstSum, match=firstMatch)
# import json
# data = participantStatsSerializer(stats)
# print(json.dumps(data.data, indent=4))
# Summoner.objects.all().delete()
# Match.objects.all().delete()
# ParticipantStats.objects.all().delete()

