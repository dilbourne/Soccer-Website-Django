from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('',include('frontend.urls')),
    path('news/',include(('news.urls','news'))),
    path('admin/', admin.site.urls),
    path('notes/', include(('notepad.urls','notepad'))),
    #path('daily-news/', include(('frontend.urls','daily-news'))),
    path('django_plotly_dash/', include('django_plotly_dash.urls')),
    path('stats/',include(('stats.urls','stats'))),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

