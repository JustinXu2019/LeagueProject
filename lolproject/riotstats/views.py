from django.shortcuts import render, HttpResponse
from .gather_data import get_match_details, get_match_ids, get_summoner_puuid
from django.shortcuts import render, get_object_or_404
from .models import Summoner, Match, ParticipantStats
from .serializers import summonerSeralizer, matchSeralizer, participantStatsSeralizer
from rest_framework import viewsets

class participantModelViewSet(viewsets.ModelViewSet):
    querySet = ParticipantStats.objects.all()
    serializer_class = participantStatsSeralizer

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
