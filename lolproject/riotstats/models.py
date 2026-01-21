from django.db import models

class Summoner(models.Model):
    puuid = models.CharField(max_length=78, unique=True)
    username = models.CharField(max_length=16)
    tagline = models.CharField(max_length=5)

class Match(models.Model):
    match_id = models.CharField(max_length=50, unique=True)
    queue_type = models.IntegerField()
    game_start = models.IntegerField()
    game_duration = models.IntegerField()
    game_version = models.CharField(max_length=20)

class ParticipantStats(models.Model):
    summoner = models.ForeignKey(Summoner, on_delete=models.CASCADE)
    match = models.ForeignKey(Match, on_delete=models.CASCADE)
    champion = models.CharField(max_length=30)
    championLevel = models.IntegerField()
    kills = models.IntegerField()
    deaths = models.IntegerField()
    assists = models.IntegerField()
    winloss = models.BooleanField()
    roleItem = models.IntegerField()
    item0 = models.IntegerField()
    item1 = models.IntegerField()
    item2 = models.IntegerField()
    item3 = models.IntegerField()
    item4 = models.IntegerField()
    item5 = models.IntegerField()
    item6 = models.IntegerField()
    summonerSpell1 = models.IntegerField()
    summonerSpell2 = models.IntegerField()
    mainPerk = models.IntegerField()
    subPerk = models.IntegerField()
    profileIcon = models.IntegerField()
    summonerLevel = models.IntegerField()
    
