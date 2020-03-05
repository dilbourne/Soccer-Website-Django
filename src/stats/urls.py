from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from . import views
from stats.dash_apps import polarscatter_goalsrc
from rest_framework import routers

router = routers.DefaultRouter()
router.register('info',views.PlayerInfoViewSet, basename="playerinfo")
#router.register('info/<str:name>',views.PlayerInfoNameViewSet, basename="PlayerInfo")
router.register('F',views.ForwardStatsViewSet)
router.register('M',views.MidfielderStatsViewSet)
router.register('D',views.DefenderStatsViewSet)
router.register('G',views.GoalkeeperStatsViewSet)


urlpatterns = [
    path('',views.stats_home, name="stats"),
    path('polar_scatter/',views.polar_scatter, name="polar_scatter"),
    path('players/',include((router.urls,'players')))
]