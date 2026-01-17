from django.db import models

class Summoner(models.Model):
    puuid = models.CharField(max_length=78, unique=True)
    username = models.CharField(max_length=16)
    tagline = models.CharField(max_length=5)

class Match(models.Model):
    match_id = models.CharField(max_length=50, unique=True)
    queue_type = models.IntegerField()

class ParticipantStats(models.Model):
    summoner = models.ForeignKey(Summoner, on_delete=models.CASCADE)
    match = models.ForeignKey(Match, on_delete=models.CASCADE)
    champion = models.CharField(max_length=30)
    kills = models.IntegerField()
    deaths = models.IntegerField()
    assists = models.IntegerField()
    winloss = models.BooleanField()