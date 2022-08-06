# KBA/urls.py

from django.contrib import admin
from django.urls import path
import KBA.views

urlpatterns = [
    path('', KBA.views.index, name='index'),
    path('teams/', KBA.views.teams, name='team-list'),
    path('teams/<str:name>/', KBA.views.team_detail, name='team-detail'),
    path('players', KBA.views.AllPlayerList.as_view(), name='player-list'),
    path('players/<str:uuid>/', KBA.views.player_detail, name='player-detail'),


]