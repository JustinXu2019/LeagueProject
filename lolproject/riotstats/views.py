from django.shortcuts import render, HttpResponse, get_object_or_404
from .gather_data import get_match_details, get_match_ids, get_summoner_puuid
from .models import Summoner, Match, ParticipantStats
from .serializers import participantStatsSerializer
from rest_framework import response
from django.http import JsonResponse

def match_list(request):
    # Get the summoner from the database
    summoner = get_object_or_404(Summoner, username="Caseoh")  # Change username as needed

    # Get all participant stats for this summoner, including related match info
    stats = ParticipantStats.objects.filter(summoner=summoner).select_related('match')

    # Pass both summoner and stats to the template
    return render(request, "riotstats/match_list.html", {
        "summoner": summoner,
        "stats": stats,
    })

def get_and_return_summoner_data(request):
    accountRegion = {
        'NA1': "AMERICAS",
        'EUW1': "EUROPE",
        'KR': "ASIA"
    }
    username = request.GET.get("username")
    tagline = request.GET.get("tagline")
    region = request.GET.get("region")

    print(f"username is {username}, tagline is {tagline}, region is {region}")


    if not username or not tagline:
        return JsonResponse({'error': 'Missing username or tagline'}, status=400)

    summonerObj = get_summoner_puuid(username, tagline, accountRegion[region])
    matchIds = get_match_ids(region, summonerObj.puuid)
    get_match_details(summonerObj, matchIds, region)

    summonerStats = ParticipantStats.objects.filter(summoner=summonerObj)
    print(len(summonerStats))
    seralizer = participantStatsSerializer(summonerStats, many=True)

    data = seralizer.data

    return JsonResponse(data, safe=False)







