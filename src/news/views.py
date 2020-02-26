from django.shortcuts import render, redirect
from django.conf import settings
# url fetching & web scraping libraries
import requests
from bs4 import BeautifulSoup
requests.packages.urllib3.disable_warnings()

from datetime import timedelta, timezone, datetime
#import time
#from time import mktime
from .models import UserProfile, Headline
import os
import shutil
import math

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

def scrape(request):
    user_p, created = UserProfile.objects.get_or_create(user=request.user)
    user_p.last_scrape = datetime.now(timezone.utc)
    user_p.save()

    url = "https://premierleague.com"
    session = requests.Session()
    session.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36"}
    content = session.get(url+"/news", verify=False).content # .content grabs all html
    
    soup = BeautifulSoup(content,'html.parser')
    articles = soup.find_all("section",{"class":"featuredArticle"})
    
    for item in articles:
        news_link = url + item.find("a",{"class":"thumbnail thumbLong"})['href']
        title = item.find("span",{"class":"title"}).text
        img_src = item.find("img")['src'].strip()

        new_headline = Headline()
        new_headline.title = title
        new_headline.url = news_link
        new_headline.pub_date = datetime.now()
        # use img_src to get the link,
        # then use the link to get the actual image,
        # and save the image in BASE_DIR/src/static

        media_root_path = settings.MEDIA_ROOT
        local_fname = img_src.split("/")[-1].split("?")[0]
        try:
            if not local_fname.startswith("audioboomgraphics") and local_fname not in os.listdir(media_root_path):
                r = session.get(img_src,stream=True,verify=False)
                with open(local_fname,'wb') as f:
                    for chunk in r.iter_content(chunk_size=1024):
                        f.write(chunk)
                cur_img_abspath = os.path.abspath(local_fname)
                shutil.move(cur_img_abspath,media_root_path)
                new_headline.image = local_fname
            elif local_fname in os.listdir(media_root_path):
                new_headline.image = local_fname
        except:
            pass

        new_headline.save()

    return redirect('/news/')