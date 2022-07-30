from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import Team, Player, PlayerToTeam
from django.views.generic import ListView, DetailView

def index(request):
   # teams = Team.objects.all()
   # context = {'teams': teams}
   # return render(request, 'index.html', context)
   try:
       teams = Team.objects.all()
   except Team.DoesNotExist:
       raise Http404("Team does not exist")
   return render(request, 'KBA/index.html', {'teams': teams})


def detail(request, id):
    team = Team.objects.get(id=id)
    players = team.players.all()

    context = {'team': team,
               'players': players

               }
    return render(request, 'KBA/detail.html', context)


# class TeamDetailView(DetailView):
#     model = Team
#     field = ['name', 'year_formed', 'manager', 'players', 'content', 'no_titles']




# class AllModelList(ListView):
#     team = Team
#

#     p

    # model_detail.html is used since not declared with a 'template_name'

# Create your views here.
