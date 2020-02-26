import pandas as pd
import requests as r
from bs4 import BeautifulSoup

# GETTERS 
def get_player_page(url,id_no):
    soup = BeautifulSoup(r.get(url.format(id_no)).content,'html.parser')
    return soup.find_all("span",{"class":"stat"})

def get_pl_id(name,path_to_file):
    df = pd.read_csv(path_to_file)
    return int(df[df['Name']==name]['id'])