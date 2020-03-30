import nltk
from newspaper import Article
import re
nltk.download('punkt')

def get_summary(url):
    article = Article(url)
    article.download()
    article.parse()
    article.nlp()
    a = ','.join([i for i in article.summary.split("\n") if 'Ones to watch' not in i and not re.search(':',i) and not re.search('\\[a-z][0-9]*$',i)])
    pattern = '([a-z]|[0-9])+[A-Z]+'
    if re.search(pattern,a):
        span = re.search(pattern,a).span()
        after_match1 = a[:(span[1]-1)] + '. ' + a[(span[1]-1):]
        after_match2 = re.findall('.*?[.!\?]',after_match1)
    else:
        after_match2 = re.findall('.*?[.!\?]',a)
        
    final_text_arr = []
    for s in after_match2:
        if not s[0].isalpha():
            final_text_arr.append(s.replace(s[0],'',1))
        else:
            final_text_arr.append(s)

    return {'title': article.title, 'summary': ' '.join(final_text_arr)}



def scrape():
    import requests
    from bs4 import BeautifulSoup
    from django.conf import settings
    import os
    import shutil
    from news.models import Headline, UserProfile
    from datetime import datetime
    #user_p, created = UserProfile.objects.get_or_create(user=request.user)
    #user_p.last_scrape = datetime.now(timezone.utc)
    #user_p.save()
    url = "https://premierleague.com"
    session = requests.Session()
    session.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36"}
    content = session.get(url+"/news", verify=False).content # .content grabs all html
    
    soup = BeautifulSoup(content,'html.parser')
    articles = soup.find_all("section",{"class":"featuredArticle"})
    
    for item in articles:
        url_suffix = item.find("a",{"class":"thumbnail thumbLong"})['href']
        news_link = url + url_suffix if not re.search('^https://',url_suffix) else url_suffix
        img_src = item.find("img")['src'].strip()

        new_headline = Headline()
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
        info = get_summary(news_link)
        new_headline.title = info['title']
        new_headline.summary = info['summary']
        try:
            new_headline.save()
        except:
            pass
