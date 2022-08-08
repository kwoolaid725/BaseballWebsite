from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import Team, Player, PlayerToTeam, Blog
from django.views.generic import ListView, DetailView, CreateView, UpdateView, FormView
from django.urls import reverse, reverse_lazy
from django.views.generic.edit import FormMixin, DeleteView
from KBA.forms import CommentForm

# def index(request):
#    # teams = Team.objects.all()
#    # context = {'teams': teams}
#    # return render(request, 'index.html', context)
#    try:
#        teams = Team.objects.all()
#    except Team.DoesNotExist:
#        raise Http404("Team does not exist")
#    return render(request, 'index.html', {'teams': teams})

def home(request):
    teams = Team.objects.all()
    context = {'teams': teams}
    return render(request, 'KBA/home.html', context)


def about(request):
    return render(request, 'KBA/about.html')


def teams(request):
    try:
        teams = Team.objects.all()
    except Team.DoesNotExist:
        raise Http404("Team does not exist")
    return render(request, 'KBA/teams.html', {'teams': teams})


def team_detail(request, name):
    team = Team.objects.get(name=name)
    players = team.players.all()

    context = {'team': team,
               'players': players

               }
    return render(request, 'KBA/team_detail.html', context)


class AllPlayerList(ListView):
    player = Player


def player_detail(request, uuid):
    player = Player.objects.get(uuid=uuid)
    team = Team.objects.all()

    context = {'player': player,
               'team': team
               }
    return render(request, 'KBA/player_detail.html', context)

class AllBlogList(ListView):
    model = Blog


class BlogDetailView(DetailView):
    model = Blog
    field = ['title', 'content', 'updated']


class BlogCreateView(CreateView):
    model = Blog
    field = ['title', 'content']

    def form_valid(self, form):
        return super().form_valid(form)

class BlogUpdateView(UpdateView):
    model = Blog
    fields = ['title', 'content']

    def form_valid(self, form):
        return super().form_valid(form)


class BlogDeleteView(DeleteView):
    model = Blog
    success_url = reverse_lazy('blog-list')


class BlogFormView(FormView):
    template_name = 'KBA/blog_comment.html'
    form_class = CommentForm

    def get_success_url(self):
        return reverse('blog-detail', kwargs={'pk': self.kwargs.get("pk")})


    def form_valid(self, form):
        form.save()
        return super().form_valid(form)



# def create





# class PlayerDetailView(DetailView):
#     model = Player
#     field = ['id', 'name', 'primary_position' ]

# class TeamDetailView(DetailView):
#
#     model = Team
#     slug_field = 'team'
#     field = ['name', 'year_formed', 'manager', 'players', 'content', 'no_titles']




# class AllModelList(ListView):
#     team = Team
#

#     p

    # model_detail.html is used since not declared with a 'template_name'

# Create your views here.
