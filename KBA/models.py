import uuid

from django.db import models
from django.utils import timezone
import datetime
from multiselectfield import MultiSelectField
from django.urls import reverse
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User



# Team history/roster/stats reamin even when it's deleted from ...


# class Roster(models.Model):
#     team = models.ForeignKey(Team, on_delete=models.CASCADE)
#     players = 'Player'
#     updated = models.DateTimeField(default=timezone.now())
#
#     def __str__(self):
#         return self.team

class Player(models.Model):
    PRIMARY_CHOICES = [
        ('Right', 'Right'),
        ('Left', 'Left'),
        ('Both', 'Both')]

    POSITION_CHOICES = [
        ('Pitcher', (
            ('P', 'Pitcher'),
            ('SP', 'Starting Pitcher'),
            ('RP', 'Relief Pitcher'),
        )
         ),
        ('Catcher', (
            ('C', 'Catcher'),
        )
         ),
        ('Infielder', (
            ('IF', 'Infield'),
            ('1B', 'First Base'),
            ('2B', 'Second Base'),
            ('3B', 'Third Base'),
            ('SS', 'Shortstop'),
        )
         ),
        ('Outfielder', (
            ('OF', 'Outfield'),
            ('LF', 'Left Field'),
            ('RF', 'Right Field'),
            ('CF', 'Center Field'),
        )
         ),
        ('Utility', (
            ('Util', 'Utility'),
        )
         ),
    ]

    EXPERIENCE_CHOICES = [
        ('HS', 'High School'),
        ('COLL', 'College'),
        ('D1', 'Division 1'),
        ('INDY', 'Independent League'),
        ('MILB', 'Minor League'),
        ('MLB', 'Major League'),
        ('PRO', 'Other Professional League')
    ]

    YEAR_CHOICES = []

    uuid = models.UUIDField('UUID', primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50)
    team = models.ManyToManyField('Team', through='PlayerToTeam', related_name='player')
    primary_position = models.CharField(max_length=30, choices=POSITION_CHOICES, default=POSITION_CHOICES[4][0][0])
    other_position= MultiSelectField(choices=POSITION_CHOICES, null=True, blank=True)
    bats = models.CharField(max_length=10, choices=PRIMARY_CHOICES)
    throws = models.CharField(max_length=10, choices=PRIMARY_CHOICES)
    DOB = models.DateField()

    for r in range(2000, (datetime.datetime.now().year)):
        YEAR_CHOICES.append((r,r))
    dateJoined = models.IntegerField('Year Joined', choices=YEAR_CHOICES, default=datetime.datetime.now().year)
    experience = models.CharField(max_length=30, choices=EXPERIENCE_CHOICES, null=True, blank=True)
    updated = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('player-detail', kwargs={'uuid': self.uuid})


class Team(models.Model):
    name = models.CharField(max_length=20)
    year_formed = models.IntegerField()
    manager = models.CharField(max_length=20)
    players = models.ManyToManyField(Player, through='PlayerToTeam', related_name='teams') ## how do I use related_name for reverse relationship?
    content = models.TextField()
    no_titles = models.IntegerField(help_text="Number of Championship Title")
    updated = models.DateTimeField(default=timezone.now)
    # picture = models.ImageField(upload_to='images/team_pics')

    def __str__(self):
        return self.name

class PlayerToTeam(models.Model):
    team = models.ForeignKey(Team, null= True, on_delete=models.SET_NULL)
    players = models.ForeignKey(Player, null=True, on_delete=models.SET_NULL)
    back_number = models.IntegerField(unique=True)                       ## How do I show back_number in team and player details?
    current_team = models.BooleanField(default=False)
    manager = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.players} to {self.team}'

class Field(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Match(models.Model):
    slug = models.SlugField(null=True, blank=True, unique=True)
    home_team = models.ForeignKey(Team, null=True, on_delete=models.SET_NULL, related_name='home_matches')
    away_team = models.ForeignKey(Team, null=True, on_delete=models.SET_NULL, related_name='away_matches')
    field = models.ForeignKey(Field, on_delete=models.CASCADE)
    date = models.DateTimeField()

    def __str__(self):
        return f'{self.away_team} at {self.home_team}'

    def save(self, *args, **kwargs):  # new
        if not self.slug:
            self.slug = slugify(f'{self.away_team} - {self.home_team}')
        return super().save(*args, **kwargs)

class BoxScore(models.Model):
    match = models.OneToOneField(Match, on_delete=models.CASCADE)
    score_hometeam = models.IntegerField()
    score_awayteam = models.IntegerField()
    hits_hometeam = models.IntegerField()
    hits_awayteam = models.IntegerField()
    error_hometeam = models.IntegerField()
    error_awayteam = models.IntegerField()

    def __str__(self):
        return self.match

class MatchStats(models.Model):
    match = models.ForeignKey(Match, on_delete=models.CASCADE)
    player = models.ForeignKey(Player, null=True, on_delete=models.SET_NULL, related_name='stats')
    PA = models.IntegerField()
    R = models.IntegerField()
    H = models.IntegerField()
    double = models.IntegerField()
    triple = models.IntegerField()
    HR = models.IntegerField()
    RBI = models.IntegerField()
    BB = models.IntegerField()
    SO = models.IntegerField()
    GDP = models.IntegerField()
    HBP = models.IntegerField()
    SF = models.IntegerField()
    sac_bunt = models.IntegerField()

    @property
    def AB(self):
        # PA - (BB + HBP + SF + sac_bunt)
        return self.AB - (self.BB + self.HBP + self.SF + self.sac_bunt)

    def __str__(self):
        return self.match

    # players = models.ManyToManyField(Player, related_name='games')

class PlayerStats(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    MatchStats = models.ForeignKey(MatchStats, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.player

class Blog(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    updated = models.DateTimeField(default=timezone.now)
    blog_user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog-detail', kwargs={'pk': self.pk})


class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    comment_title = models.CharField(max_length=200)
    comment_text = models.TextField()
    comment_updated = models.DateTimeField(default=timezone.now)
    comment_user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.comment_title





# player history shows previous teams / stats
# 블로그
# 선수 스탯,
# 경기 스케쥴
# 경기 결과
# 메인페이지에 지역 비지니스 스폰서 광고
# about 페이지 + 구글 지도
# 로그인 관리





# Stats

# class StatsBase(models.Model):
#     class Meta:
#         abstract = True
#
#     PA = models.IntegerField()
#     AB =