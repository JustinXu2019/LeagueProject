from rest_framework import serializers
from .models import Summoner, Match, ParticipantStats

class summonerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Summoner
        fields = ['puuid', 'username', 'tagline']

class matchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Match
        fields = '__all__'

class participantStatsSerializer(serializers.ModelSerializer):
    summoner = summonerSerializer(read_only=True)
    match = matchSerializer(read_only=True)
    
    class Meta:
        model = ParticipantStats
        fields = '__all__'

