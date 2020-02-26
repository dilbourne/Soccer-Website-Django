from django.urls import path, include
from django.conf.urls.static import static


from . import views

urlpatterns = [
    path('',views.news_list, name="news"),
    path('scrape',views.scrape, name="scrape")
]