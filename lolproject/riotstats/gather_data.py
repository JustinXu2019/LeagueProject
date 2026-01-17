import requests
from riotstats.models import Summoner, Match, ParticipantStats
from django.utils.dateparse import parse_datetime
from riotwatcher import RiotWatcher, LolWatcher, ApiError
from riotstats.serializers import summonerSerializer, matchSerializer, participantStatsSerializer

API_KEY = "RGAPI-e08dce26-7d6b-47b2-863a-8e2737e8b916"
accountRegion = "AMERICAS"
summonerRegion = "NA1"
gameName = "Caseoh"
tagLine = "NA1"
lol_watcher = LolWatcher(f'{API_KEY}')
riot_watcher = RiotWatcher(f'{API_KEY}')

def get_summoner_puuid(username, tag, region):
    accountData = riot_watcher.account.by_riot_id(region, username, tag)
    puuid = accountData['puuid']
    summonerObj, _ = Summoner.objects.get_or_create(
        puuid=puuid, 
        defaults={"username": username or "", "tagline": tag or ""}
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
            }
        )

        for player in match_info['participants']:
            if player['puuid'] == summonerObj.puuid:
                ParticipantStats.objects.get_or_create(
                    summoner=summonerObj,
                    match=match_obj,
                    defaults={
                        "champion": player['championName'],
                        "kills": player['kills'],
                        "deaths": player['deaths'],
                        "assists": player['assists'],
                        "winloss": player['win'],
                    }
                )
    

# Function creates a list of dictionaries with champ name, k, d, a, win/loss status
# def extract_champion_wr(puuid, matchids, region, username=None, tagline=None):
#     summoner, _ = Summoner.objects.get_or_create(
#         puuid=puuid, 
#         defaults={"username": username or "", "tagline": tagline or ""}
#         )
    
#     for match in matchids:
#         details = get_match_details(match, region)
#         match_info = details['info']
#         match_obj, _ = Match.objects.get_or_create(
#             match_id = details['metadata']['matchId'],
#             defaults={
#                 "queue_type": match_info.get("queueId", 0),
#             }
#         )

#         for player in match_info['participants']:
#             if player['puuid'] == puuid:
#                 ParticipantStats.objects.get_or_create(
#                     summoner=summoner,
#                     match=match_obj,
#                     defaults={
#                         "champion": player['championName'],
#                         "kills": player['kills'],
#                         "deaths": player['deaths'],
#                         "assists": player['assists'],
#                         "winloss": player['win'],
#                     }
#                 )

        


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
