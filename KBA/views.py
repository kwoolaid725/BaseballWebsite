from django.shortcuts import render
from django.http import HttpResponse, Http404

from django.views.generic import ListView, DetailView, CreateView, UpdateView, FormView
from django.urls import reverse, reverse_lazy
from django.views.generic.edit import FormMixin, DeleteView

from django.contrib.auth.mixins import LoginRequiredMixin

from KBA.forms import CommentForm
from .models import Team, Player, PlayerToTeam, Blog, Match


# def index(request):
#    # teams = Team.objects.all()
#    # context = {'teams': teams}
#    # return render(request, 'index.html', context)
#    try:
#        teams = Team.objects.all()
#    except Team.DoesNotExist:
#        raise Http404("Team does not exist")
#    return render(request, 'index.html', {'teams': teams})

def index(request):
    teams = Team.objects.all()
    context = {'teams': teams}
    return render(request, 'index.html', context)


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
    model = Player


def player_detail(request, uuid):
    player = Player.objects.get(uuid=uuid)
    team = Team.objects.all()

    context = {'player': player,
               'team': team
               }
    return render(request, 'KBA/player_detail.html', context)


class AllMatchList(ListView):
    model = Match



# Blog0

class AllBlogList(ListView):
    model = Blog


class BlogDetailView(DetailView):
    model = Blog



class BlogCreateView(CreateView):
    model = Blog
    field = ['title', 'content']
    template_name = 'KBA/blog_create_form.html'

    def form_valid(self, form):
        form.instance_blog_user = self.request.user
        return super().form_valid(form)

class BlogUpdateView(UpdateView):
    model = Blog
    fields = ['title', 'content']
    template_name = 'KBA/blog_update_form.html'

    def form_valid(self, form):
        user = self.request.user
        form_blog = Blog.objects.get(pk=self.kwargs.get("pk"))

        if user == form_blog.blog_user:
            return super().form_valid(form)
        else:
            return HttpResponse("<h3>You don't have a permission</h3>")


class BlogDeleteView(DeleteView):
    model = Blog
    success_url = reverse_lazy('blog-index')

    def form_valid(self, form):
        # 권한 검증
        user = self.request.user
        form_blog = Blog.objects.get(pk=self.kwargs.get("pk"))
        if user == form_blog.blog_user:
            return super().form_valid(form)
        else:
            return HttpResponse("<h3>You dont have a permission</h3>")


class BlogFormView(FormView):
    template_name = 'KBA/blog_comment.html'
    form_class = CommentForm

    def get_success_url(self):
        return reverse('blog-detail', kwargs={'pk': self.kwargs.get("pk")})

    def form_valid(self, form):
        form.instance.blog = Blog.objects.get(pk=self.kwargs.get("pk"))
        form.instance.comment_user = self.request.user
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
