import uuid

from django.db import models
from django.utils import timezone
import datetime
from multiselectfield import MultiSelectField

# Team history/roster/stats reamin even when it's deleted from ...


# class Roster(models.Model):
#     team = models.ForeignKey(Team, on_delete=models.CASCADE)
#     players = 'Player'
#     updated = models.DateTimeField(default=timezone.now())
#
#     def __str__(self):
#         return self.team

class Team(models.Model):
    name = models.CharField(max_length=20)
    year_formed = models.IntegerField(max_length=4)
    manager = models.CharField(max_length=20)
    content = models.TextField()
    no_titles = models.IntegerField(help_text="Number of Championship Title")
    updated = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return self.name

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

    id = models.UUIDField('UUID', primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50)
    team = models.ForeignKey(Team, on_delete=models.SET_NULL, null=True, blank=True)
    primary_position = models.CharField(max_length=30, choices=POSITION_CHOICES, default=POSITION_CHOICES[4][0][0])
    other_position= MultiSelectField(choices=POSITION_CHOICES, null=True, blank=True)
    bats = models.CharField(max_length=10, choices=PRIMARY_CHOICES)
    throws = models.CharField(max_length=10, choices=PRIMARY_CHOICES)
    DOB = models.DateField()

    for r in range(2000, (datetime.datetime.now().year)):
        YEAR_CHOICES.append((r,r))
    dateJoined = models.IntegerField('Year Joined', choices=YEAR_CHOICES, default=datetime.datetime.now().year)
    experience = models.CharField(max_length=30, choices=EXPERIENCE_CHOICES, null=True, blank=True)
    updated = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return self.name



# Stats

# class StatsBase(models.Model):
#     class Meta:
#         abstract = True
#
#     PA = models.IntegerField()
#     AB =