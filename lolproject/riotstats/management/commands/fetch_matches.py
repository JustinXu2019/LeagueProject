from django.core.management.base import BaseCommand
from riotstats.gather_data import get_summoner_puuid, get_match_ids, extract_champion_wr, headers
from riotstats.models import Summoner

API_REGION = "americas"

class Command(BaseCommand):
    help = "Fetch matches for a given summoner and store them in the database"

    def add_arguments(self, parser):
        parser.add_argument("gameName", type=str, help="Summoner gameName")
        parser.add_argument("tagLine", type=str, help="Summoner tagLine")

    def handle(self, *args, **options):
        gameName = options["gameName"]
        tagLine = options["tagLine"]

        # 1. Get PUUID
        puuid = get_summoner_puuid(gameName, tagLine, API_REGION, headers)

        # 2. Fetch match IDs
        matchids = get_match_ids(puuid, API_REGION)

        # 3. Store in DB
        extract_champion_wr(puuid, matchids, API_REGION, username=gameName, tagline=tagLine)

        self.stdout.write(self.style.SUCCESS(f"Data fetched and stored for {gameName}#{tagLine}"))
