from django.shortcuts import render, redirect
from django.conf import settings
# url fetching & web scraping libraries
import requests
from bs4 import BeautifulSoup
requests.packages.urllib3.disable_warnings()
from datetime import timedelta, timezone, datetime
from .models import UserProfile, Headline
import os
import shutil
import math
from rest_framework import viewsets
from rest_framework.response import Response 
from .serializers import DailyNewsSerializer
from .helpers import scrape, get_summary
import nltk
from newspaper import Article
import re
nltk.download('punkt')
from django.contrib.sessions.backends.db import SessionStore
from django.contrib.sessions.models import Session

class DailyNewsViewSet(viewsets.ViewSet):
    
    def list(self, request):
        if request.user.is_authenticated:
            user_p, created = UserProfile.objects.get_or_create(user=request.user)
            now = datetime.now(timezone.utc)
            if not created:
                time_diff = now - user_p.last_scrape
                hrs = time_diff / timedelta(minutes=60)
                time_remaining = 12 - hrs
                print("Hours since last scrape => ",hrs)
            else:
                time_remaining = 0
            
            if time_remaining <= 0:
                scrape()
                user_p.last_scrape = datetime.now(timezone.utc)
                user_p.save()
                queryset = Headline.objects.filter(pub_date = datetime.today().date())
                serializer = DailyNewsSerializer(queryset, many=True)
                print("Fresh News")
                return Response(serializer.data)
            else:
                queryset = Headline.objects.filter(pub_date = datetime.today().date())
                serializer = DailyNewsSerializer(queryset, many=True)
                print("Old News")
                return Response(serializer.data)
        elif request.session.get('scraped',False):
            queryset = Headline.objects.filter(pub_date = datetime.today().date())
            serializer = DailyNewsSerializer(queryset, many=True)
            print("Old News")
            return Response(serializer.data)
        else:
            scrape()
            request.session['last_scraped'] = str(datetime.now(timezone.utc))
            request.session['scraped'] = True
            request.session.set_expiry(43200) # 12 hours

            queryset = Headline.objects.filter(pub_date = datetime.today().date())
            serializer = DailyNewsSerializer(queryset, many=True)
            print("Fresh News")
            return Response(serializer.data)

# Create your views here.
def news_list(request):
    # user can only scrape every 24 hours
    user_p, created = UserProfile.objects.get_or_create(user=request.user)
    now = datetime.now(timezone.utc)
    try:
        time_diff = now - user_p.last_scrape
        time_diff_in_hrs = time_diff / timedelta(minutes=60)
        time_remaining = 24 - time_diff_in_hrs
    except:
        time_diff_in_hrs = 24
        time_remaining = 24 - time_diff_in_hrs
        
    if time_diff_in_hrs < 24:
        hide = True
    else:
        hide = False
    
    # get all headlines from model
    recent_headlines = Headline.objects.order_by('-pub_date')[:6]
    context = {
        'headlines': recent_headlines,
        'hide': hide,
        'next_scrape': math.ceil(time_remaining)
    }
    return render(request, "news/news.html", context)


