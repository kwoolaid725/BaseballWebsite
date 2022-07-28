# KBA/urls.py

from django.contrib import admin
from django.urls import path
import KBA.views

urlpatterns = [
    path('', KBA.views.index, name='index')
    # path('players/<int:pk>', views.as_view(), name='cordless-detail')

]