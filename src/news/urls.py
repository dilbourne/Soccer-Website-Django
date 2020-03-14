from django.urls import path, include
from django.conf.urls.static import static
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'daily',views.DailyNewsViewSet,basename="headline")



urlpatterns = [
    #path('',views.news_list, name="news"),
    #path('scrape',views.scrape, name="scrape"),
    path('api/',include((router.urls,'api')))
]