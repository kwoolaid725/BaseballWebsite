from django.contrib import admin

# Register your models here.

from KBA.models import Team, Roster, Player

admin.site.register(Team)
admin.site.register(Roster)
# admin.site.register(Position)
admin.site.register(Player)