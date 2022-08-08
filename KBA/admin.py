from django.contrib import admin

# Register your models here.

from KBA.models import Team, Player, PlayerToTeam, Field, Match, Blog


class TeamInline(admin.TabularInline):
    model = Team.players.through

class PlayerAdmin(admin.ModelAdmin):
    inlines = [TeamInline,]

class MatchAdmin(admin.ModelAdmin):
    exclude = ('slug',)



admin.site.register(Team)
# admin.site.register(Position)
admin.site.register(Player, PlayerAdmin)
admin.site.register(PlayerToTeam)
admin.site.register(Field)
admin.site.register(Match, MatchAdmin)
admin.site.register(Blog)