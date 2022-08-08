# KBA/urls.py

from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('teams/', views.teams, name='team-list'),
    path('teams/<str:name>/', views.team_detail, name='team-detail'),
    path('players', views.AllPlayerList.as_view(), name='player-list'),
    path('players/<str:uuid>/', views.player_detail, name='player-detail'),
    path('blog/', views.AllBlogList.as_view(), name='blog-list'),
    path('blog/<int:pk>', views.BlogDetailView.as_view(), name='blog-detail'),
    path('blog/new', views.BlogCreateView.as_view(), name='blog-create'),
    path('blog/<int:pk>/update', views.BlogUpdateView.as_view(), name='blog-update'),
    path('blog/<int:pk>/delete', views.BlogCreateView.as_view(), name='blog-delete'),
    path('blog/<int:pk>/comment', views.BlogCreateView.as_view(), name='blog-form-comment'),




]