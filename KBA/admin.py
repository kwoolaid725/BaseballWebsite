from django.contrib import admin

# Register your models here.

from KBA.models import Team, Player, PlayerToTeam


class TeamInline(admin.TabularInline):
    model = Team.players.through

class PlayerAdmin(admin.ModelAdmin):
    inlines = [TeamInline,]

admin.site.register(Team)
# admin.site.register(Position)
admin.site.register(Player, PlayerAdmin)
admin.site.register(PlayerToTeam)