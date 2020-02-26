from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from . import views
from stats.dash_apps import polarscatter_goalsrc

urlpatterns = [
    path('',views.stats_home, name="stats"),
    path('polar_scatter/',views.polar_scatter, name="polar_scatter")
]