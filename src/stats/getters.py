import pandas as pd
import requests as r
from bs4 import BeautifulSoup
from .models import PlayerInfo
# GETTERS 
def get_player_page(url,id_no):
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