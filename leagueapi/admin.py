from django.contrib import admin
from .models import Tournament
from .models import Game
from .models import GamePlayerScore
from .models import GameTeamStatistics
from .models import Team
from .models import Player
from .models import Round
from .models import Coach
from .models import Admin

# Register your models here.
admin.site.register(Tournament)
admin.site.register(Game)
admin.site.register(GameTeamStatistics)
admin.site.register(GamePlayerScore)
admin.site.register(Round)
admin.site.register(Team)
admin.site.register(Player)
admin.site.register(Coach)
admin.site.register(Admin)
