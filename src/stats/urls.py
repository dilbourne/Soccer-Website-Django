from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from . import views
from stats.dash_apps import polarscatter_goalsrc
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'info',views.PlayerInfoViewSet, basename="playerinfo")
router.register(r'F',views.ForwardStatsViewSet)
router.register(r'M',views.MidfielderStatsViewSet)
router.register(r'D',views.DefenderStatsViewSet)
router.register(r'G',views.GoalkeeperStatsViewSet)


urlpatterns = [
    path('standings/',views.TableStandingsViewSet.as_view(), name="standings"),
    path('players/',include((router.urls,'players'))),
    path('nationality_count/',views.NationalityCountViewSet.as_view(),name="nationality_count"),
    path('nationality_count/<int:n>/',views.NationalityCountViewSet.as_view(),name="nationality_count")
]