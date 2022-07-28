from django.shortcuts import render
from .models import Team, Player
from django.views.generic import ListView, DetailView

def index(request):
   teams = Team.objects.all()

   context = {
       'teams': teams
   }
   return render(request, 'index.html', context)


# class AllModelList(ListView):
#     team = Team
#
#
# class TeamDetailView(DetailView):
#     # model = Model
#     p

    # model_detail.html is used since not declared with a 'template_name'

# Create your views here.
