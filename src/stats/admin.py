from django.contrib import admin
from .models import PlayerInfo, ForwardStats, MidfielderStats, DefenderStats, GoalkeeperStats
# Register your models here.
admin.site.register(PlayerInfo)
admin.site.register(ForwardStats)
admin.site.register(MidfielderStats)
admin.site.register(DefenderStats)
admin.site.register(GoalkeeperStats)