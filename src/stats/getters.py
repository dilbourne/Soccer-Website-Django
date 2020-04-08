import pandas as pd
import requests as r
from bs4 import BeautifulSoup
from .models import PlayerInfo
# GETTERS 
def get_player_stats(url,id_no):
    soup = BeautifulSoup(r.get(url.format(id_no)).content,'html.parser')
    return soup.find_all("span",{"class":"stat"})

def get_player_overview(url):
    _content = r.get(url).content
    soup = BeautifulSoup(_content,'html.parser')
    return [*soup.find_all("div",{"class":"info"}),*soup.find_all("div",{"class":"number t-colour"},limit=1),*soup.find_all("div",{"class":"name t-colour"},limit=1)]


def get_pl_id(name):
    obj = PlayerInfo.objects.get(name=name)
    return obj.pl_id

def get_player_role(_id):
    obj = PlayerInfo.objects.get(pl_id=_id)
    return obj.role

# get and clean table standings headings
def getHeadingsAndAbbreviations():
    import requests
    from bs4 import BeautifulSoup
    import re
    
    url = "http://premierleague.com/tables"
    content_ = requests.get(url).content
    soup = BeautifulSoup(content_,'html.parser')

    thead = soup.find_all("thead")
    th_soup = BeautifulSoup(str(thead[0]),'html.parser')
    ths = th_soup.find_all("th",{"scope":"col"})
    almost_ = [th.text.replace('\n',"") for th in ths][2:-2]

    pattern = '([a-z]|[0-9])[A-Z]'
    final_ = ['Position']
    for i in almost_:
        # if i has a shorter version, ignore it / cut it out
        if re.search(pattern,i):
            # get start and end indices of where the pattern matches from span
            span = re.search(pattern,i).span()
            final_.append(i[:(span[1]-1)])
        # else just add it
        else:
            final_.append(i)
    return final_

def getTableBodyData(thead_data):
    import requests
    from bs4 import BeautifulSoup
    import re
    
    url = "http://premierleague.com/tables"
    content_ = requests.get(url).content
    soup = BeautifulSoup(content_,'html.parser')
    
    tables = soup.find_all("tr",{"data-compseason":"274"})
    tbody_data = []

    for index, row in enumerate(tables):
        row_soup = BeautifulSoup(str(row),'html.parser')
        badge_src = row_soup.find("img",{"class":"badge-image"})['src']
        a = str([tr for tr in row])
        s = BeautifulSoup(a,'html.parser')
        tds = s.find_all("td")
        almost = [t.text.replace('\n',"").strip() for t in tds][2:-2]
        pattern = '([a-z]|[0-9])[A-Z]'
        if re.search(pattern,almost[0]):
            span = re.search(pattern,almost[0]).span()
            after = [almost[0][:(span[1]-1)],almost[0][(span[1]-1):].strip(),badge_src]
            final = [str(index+1),*[after],*almost[1:]]
            tbody_data.append({ key: value for (key,value) in zip(thead_data,final)})

    return tbody_data