# KBA/urls.py

from django.contrib import admin
from django.urls import path
import KBA.views

urlpatterns = [
    path('', KBA.views.index, name='index'),
    path('teams/', KBA.views.teams, name='team-list'),
    path('teams/<str:name>/', KBA.views.team_detail, name='team-detail'),


]