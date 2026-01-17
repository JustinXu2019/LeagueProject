from django.urls import path
from . import views

urlpatterns = [
    path("matches/", views.match_list, name="match_list"),
    path("api/search/", views.get_and_return_summoner_data, name="summoner_search")
]