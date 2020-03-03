from background_task import background
from stats.models import PlayerInfo, ForwardStats, MidfielderStats, DefenderStats, GoalkeeperStats
from stats.getters import get_player_page, get_pl_id, get_player_role, get_player_overview
from stats.cleaners import clean_player_page, clean_player_overview
import pandas as pd
import requests as r
import re
from bs4 import BeautifulSoup

def bc_player_info():
    # bc_list of PlayerInfo objects
    players_list = []
    # define urls
    base_url = "https://www.premierleague.com"
    clubs_url = "https://www.premierleague.com/clubs"
    squad_url = "https://www.premierleague.com/clubs/{_id}/{name}/squad"
    ##### gather current premier league clubs names and ids #####
    response = r.get(clubs_url)
    soup = BeautifulSoup(response.content,'html.parser')
    clubs_list = soup.find_all("a")
    #extract href links because they contain club number
    clubs_links = [link['href'] for link in clubs_list]
    #narrow down to links that have this regex pattern
    clubs = [link for link in clubs_links if re.search('clubs/[0-9]+',link)]
    #tidy-up club names
    """for i in range(len(clubs)):
        clubs[i] = clubs[i].replace('-and-','-&-')
        clubs[i] = clubs[i].replace('-',' ')"""
    #split link to get club number & club name in tuples
    club_and_num = [(i.split("/")[2],i.split("/")[3]) for i in clubs]
    ##### get squad list pages by using the club name and ids #####
    for num,name in club_and_num:
            # get each club's squad list page
            _content = r.get(squad_url.format(_id=num,name=name)).content
            # create soup
            soup = BeautifulSoup(_content, 'html.parser')
            # extract overview link
            raw_cards = soup.find_all("a",{"class":"playerOverviewCard"})
            ovr_links = [link['href'] for link in raw_cards]
            # iterate through the player links (overview) for each team
            for link in ovr_links:
                # get id from link
                _id = int(link.split("/")[2])
                try:
                    tmp = clean_player_overview(get_player_overview(base_url+link))
                    tmp['pl_id'] = _id
                    # call getter & cleaner function for the overview page
                    players_list.append(PlayerInfo(
                        pl_id = _id,
                        club = tmp['Club'],
                        country = tmp['Country'],
                        dob = tmp['Dob'],
                        name = tmp['Name'],
                        shirt_num = tmp['Shirtnum'],
                        role = tmp['Role']
                    ))
                except:
                    pass
    PlayerInfo.objects.bulk_create(players_list)




# NEED PlayerInfo's web scraping functionality overhauled before this can work
def bulk_create_models(url):
    # for bulk_create
    forward_list = []
    midfielder_list = []
    defender_list = []
    goalkeeper_list = []
    for p in PlayerInfo.objects.all():                           
        data = clean_player_page(get_player_page(url,get_pl_id(p.name)))
        try:
            if p.role == 'F':    
                forward_list.append(ForwardStats(
                    appearances = data['Appearances'],
                    assists = data['Assists'],
                    big_chances_created = data['Big chances created'],
                    big_chances_missed = data['Big chances missed'],
                    blocked_shots = data['Blocked shots'],
                    clearances = data['Clearances'],
                    crosses = data['Crosses'],
                    fouls = data['Fouls'],
                    freekicks_scored = data['Freekicks scored'],
                    goals = data['Goals'],
                    goals_per_match = data['Goals per match'],
                    goals_with_left_foot = data['Goals with left foot'],
                    goals_with_right_foot = data['Goals with right foot'],
                    headed_clearance = data['Headed Clearance'],
                    headed_goals = data['Headed goals'],
                    hit_woodwork = data['Hit woodwork'],
                    interceptions = data['Interceptions'],
                    losses = data['Losses'],
                    offsides = data['Offsides'],
                    passes = data['Passes'],
                    passes_per_match = data['Passes per match'],
                    penalties_scored = data['Penalties scored'],
                    red_cards = data['Red cards'],
                    shooting_accuracy = data['Shooting accuracy %'],
                    shots = data['Shots'],
                    shots_on_target = data['Shots on target'],
                    tackles = data['Tackles'],
                    wins = data['Wins'],
                    yellow_cards = data['Yellow cards']
                ))
            elif p.role == 'M':
                midfielder_list.append(MidfielderStats(
                    appearances = data['Appearances'],
                    wins = data['Wins'],
                    losses = data['Losses'],
                    # team play
                    assists = data['Assists'],
                    passes = data['Passes'],
                    passes_per_match = data['Passes per match'],
                    big_chances_created = data['Big chances created'],
                    crosses = data['Crosses'],
                    cross_accuracy = data['Cross accuracy %'],
                    through_balls = data['Through balls'],
                    accurate_long_balls = data['Accurate long balls'],
                    # discipline
                    yellow_cards = data['Yellow cards'],
                    red_cards = data['Red cards'],
                    fouls = data['Fouls'],
                    offsides = data['Offsides'],
                    #attack
                    big_chances_missed = data['Big chances missed'],
                    freekicks_scored = data['Freekicks scored'],
                    goals = data['Goals'],
                    goals_per_match = data['Goals per match'],
                    goals_with_left_foot = data['Goals with left foot'],
                    goals_with_right_foot = data['Goals with right foot'],
                    headed_goals = data['Headed goals'],
                    hit_woodwork = data['Hit woodwork'],
                    penalties_scored = data['Penalties scored'],
                    shooting_accuracy = data['Shooting accuracy %'],
                    shots = data['Shots'],
                    shots_on_target = data['Shots on target'],
                    # defence
                    tackles = data['Tackles'],
                    tackle_success = data['Tackle success %'],
                    blocked_shots = data['Blocked shots'],
                    interceptions = data['Interceptions'],
                    clearances = data['Clearances'],
                    headed_clearance = data['Headed Clearance'],
                    recoveries = data['Recoveries'],
                    duels_won = data['Duels won'],
                    duels_lost = data['Duels lost'],
                    successful_50_50 = data['Successful 50/50s'],
                    aerial_battles_won = data['Aerial battles won'],
                    aerial_battles_lost = data['Aerial battles lost'],
                    errors_leading_to_goal = data['Errors leading to goal']
                            ))
            elif p.role=='D':
                defender_list.append(DefenderStats(
                    appearances = data['Appearances'],
                    wins = data['Wins'],
                    losses = data['Losses'],
                    # defence
                    clean_sheets = data['Clean sheets'],
                    goals_conceded = data['Goals conceded'],
                    tackles = data['Tackles'],
                    tackle_success = data['Tackle success %'],
                    last_man_tackles = data['Last man tackles'],
                    blocked_shots = data['Blocked shots'],
                    interceptions = data['Interceptions'],
                    clearances = data['Clearances'],
                    headed_clearance = data['Headed Clearance'],
                    clearances_off_line = data['Clearances off line'],
                    recoveries = data['Recoveries'],
                    duels_won = data['Duels won'],
                    duels_lost = data['Duels lost'],
                    successful_50_50 = data['Successful 50/50s'],
                    aerial_battles_won = data['Aerial battles won'],
                    aerial_battles_lost = data['Aerial battles lost'],
                    own_goals = data['Own goals'],
                    errors_leading_to_goal = data['Errors leading to goal'],
                    # team play
                    assists = data['Assists'],
                    passes = data['Passes'],
                    passes_per_match = data['Passes per match'],
                    big_chances_created = data['Big chances created'],
                    crosses = data['Crosses'],
                    cross_accuracy = data['Cross accuracy %'],
                    through_balls = data['Through balls'],
                    accurate_long_balls = data['Accurate long balls'],
                    # discipline
                    yellow_cards = data['Yellow cards'],
                    red_cards = data['Red cards'],
                    fouls = data['Fouls'],
                    offsides = data['Offsides'],
                    # attack
                    goals = data['Goals'],
                    headed_goals = data['Headed goals'],
                    goals_with_right_foot = data['Goals with right foot'],
                    goals_with_left_foot = data['Goals with left foot'],
                    hit_woodwork = data['Hit woodwork']
                ))
            elif p.role == 'G':
                goalkeeper_list.append(GoalkeeperStats(
                    appearances = data['Appearances'],
                    wins = data['Wins'],
                    losses = data['Losses'],
                    # goalkeeping
                    saves = data['Saves'],
                    penalties_saved = data['Penalties saved'],
                    punches = data['Punches'],
                    high_claims = data['High Claims'],
                    catches = data['Catches'],
                    sweeper_clearances = data['Sweeper clearances'],
                    throw_outs = data['Throw outs'],
                    goal_kicks = data['Goal Kicks'],
                    # defence
                    clean_sheets = data['Clean sheets'],
                    goals_conceded = data['Goals conceded'],
                    errors_leading_to_goal = data['Errors leading to goal'],
                    own_goals = data['Own goals'],
                    # discipline
                    yellow_cards = data['Yellow cards'],
                    red_cards = data['Red cards'],
                    fouls = data['Fouls'],
                    # team player
                    goals = data['Goals'],
                    assists = data['Assists'],
                    passes = data['Passes'],
                    passes_per_match = data['Passes per match'],
                    accurate_long_balls = data['Accurate long balls']
                ))
        except KeyError:
            print(p.name,":",p.role)
    ForwardStats.objects.bulk_create(forward_list)
    MidfielderStats.objects.bulk_create(midfielder_list)
    DefenderStats.objects.bulk_create(defender_list)
    GoalkeeperStats.objects.bulk_create(goalkeeper_list)