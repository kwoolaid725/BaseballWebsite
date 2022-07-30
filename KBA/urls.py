# KBA/urls.py

from django.contrib import admin
from django.urls import path
import KBA.views

urlpatterns = [
    path('', KBA.views.index, name='index'),
    path('<int:id>', KBA.views.detail, name='detail'),
    # path('<int:pk>', KBA.views.TeamDetailView.as_view(), name='team-detail'),


]