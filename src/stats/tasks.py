from background_task import background
from stats.models import PlayerInfo, ForwardStats, MidfielderStats, DefenderStats, GoalkeeperStats
from stats.getters import get_player_stats, get_pl_id, get_player_role, get_player_overview
from stats.cleaners import clean_player_stats, clean_player_overview
import pandas as pd
import requests as r
import re
from bs4 import BeautifulSoup
from django.utils import timezone

def create_or_update_player_info(first_time=False):
    # bc_list of PlayerInfo objects
    players_list = []
    # define urls
    base_url = "https://www.premierleague.com"
    squad_url = "https://www.premierleague.com/clubs/{_id}/{name}/squad"
    ##### gather current premier league clubs names and ids #####
    club_and_num = get_pl_clubs()
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
            if first_time:
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
                            role = tmp['Role'],
                            last_update = timezone.now()
                        ))
                    except:
                        pass
                PlayerInfo.objects.bulk_create(players_list)
            else:
                for link in ovr_links:
                # get id from link
                    _id = int(link.split("/")[2])
                    try:
                        tmp = clean_player_overview(get_player_overview(base_url+link))
                        tmp['pl_id'] = _id
                        # call getter & cleaner function for the overview page
                        obj, created = PlayerInfo.objects.update_or_create(
                            pl_id = _id,
                            defaults = {
                            'club': tmp['Club'],
                            'country': tmp['Country'],
                            'dob': tmp['Dob'],
                            'name': tmp['Name'],
                            'shirt_num': tmp['Shirtnum'],
                            'role': tmp['Role'],
                            'last_update': timezone.now()
                            }
                        )
                        obj.save()
                    except Exception as e:
                        print(e)
                        print(obj.pl_id,":",obj.name)
                        pass


def create_or_update_player_stats(first_time=False):
    # for bulk_create
    forward_list = []
    midfielder_list = []
    defender_list = []
    goalkeeper_list = []
    url = "https://www.premierleague.com/players/{}/player/stats"
    if first_time:
        for p in PlayerInfo.objects.all():
            _id = int(get_pl_id(p.name))                        
            data = clean_player_stats(get_player_stats(url,get_pl_id(p.name)))
            try:
                if get_player_role(_id) == 'F':    
                    forward_list.append(ForwardStats(
                        pl_id = p,
                        last_update = timezone.now(),
                        appearances = r_('Appearances',data),
                        assists = r_('Assists',data),
                        big_chances_created = r_('Big chances created',data),
                        big_chances_missed = r_('Big chances missed',data),
                        blocked_shots = r_('Blocked shots',data),
                        clearances = r_('Clearances',data),
                        crosses = r_('Crosses',data),
                        fouls = r_('Fouls',data),
                        freekicks_scored = r_('Freekicks scored',data),
                        goals = r_('Goals',data),
                        goals_per_match = r_('Goals per match',data),
                        goals_with_left_foot = r_('Goals with left foot',data),
                        goals_with_right_foot = r_('Goals with right foot',data),
                        headed_clearance = r_('Headed Clearance',data),
                        headed_goals = r_('Headed goals',data),
                        hit_woodwork = r_('Hit woodwork',data),
                        interceptions = r_('Interceptions',data),
                        losses = r_('Losses',data),
                        offsides = r_('Offsides',data),
                        passes = r_('Passes',data),
                        passes_per_match = r_('Passes per match',data),
                        penalties_scored = r_('Penalties scored',data),
                        red_cards = r_('Red cards',data),
                        shooting_accuracy = r_('Shooting accuracy %',data),
                        shots = r_('Shots',data),
                        shots_on_target = r_('Shots on target',data),
                        tackles = r_('Tackles',data),
                        wins = r_('Wins',data),
                        yellow_cards = r_('Yellow cards',data)
                    ))
                elif get_player_role(_id) == 'M':
                    midfielder_list.append(MidfielderStats(
                        pl_id = p,
                        last_update = timezone.now(),
                        appearances = r_('Appearances',data),
                        wins = r_('Wins',data),
                        losses = r_('Losses',data),
                        # team play
                        assists = r_('Assists',data),
                        passes = r_('Passes',data),
                        passes_per_match = r_('Passes per match',data),
                        big_chances_created = r_('Big chances created',data),
                        crosses = r_('Crosses',data),
                        cross_accuracy = r_('Cross accuracy %',data),
                        through_balls = r_('Through balls',data),
                        accurate_long_balls = r_('Accurate long balls',data),
                        # discipline
                        yellow_cards = r_('Yellow cards',data),
                        red_cards = r_('Red cards',data),
                        fouls = r_('Fouls',data),
                        offsides = r_('Offsides',data),
                        #attack
                        big_chances_missed = r_('Big chances missed',data),
                        freekicks_scored = r_('Freekicks scored',data),
                        goals = r_('Goals',data),
                        goals_per_match = r_('Goals per match',data),
                        goals_with_right_foot = r_('Goals with right foot',data),
                        goals_with_left_foot = r_('Goals with left foot',data),
                        headed_goals = r_('Headed goals',data),
                        hit_woodwork = r_('Hit woodwork',data),
                        penalties_scored = r_('Penalties scored',data),
                        shooting_accuracy = r_('Shooting accuracy %',data),
                        shots = r_('Shots',data),
                        shots_on_target = r_('Shots on target',data),
                        # defence
                        tackles = r_('Tackles',data),
                        tackle_success = r_('Tackle success %',data),
                        blocked_shots = r_('Blocked shots',data),
                        interceptions = r_('Interceptions',data),
                        clearances = r_('Clearances',data),
                        headed_clearance = r_('Headed Clearance',data),
                        recoveries = r_('Recoveries',data),
                        duels_won = r_('Duels won',data),
                        duels_lost = r_('Duels lost',data),
                        successful_50_50 = r_('Successful 50/50s',data),
                        aerial_battles_won = r_('Aerial battles won',data),
                        aerial_battles_lost = r_('Aerial battles lost',data),
                        errors_leading_to_goal = r_('Errors leading to goal',data)
                                ))
                elif get_player_role(_id) =='D':
                    defender_list.append(DefenderStats(
                        pl_id = p,
                        last_update = timezone.now(),
                        appearances = r_('Appearances',data),
                        wins = r_('Wins',data),
                        losses = r_('Losses',data),
                        # defence
                        clean_sheets = r_('Clean sheets',data),
                        goals_conceded = r_('Goals conceded',data),
                        tackles = r_('Tackles',data),
                        tackle_success = r_('Tackle success %',data),
                        last_man_tackles = r_('Last man tackles',data),
                        blocked_shots = r_('Blocked shots',data),
                        interceptions = r_('Interceptions',data),
                        clearances = r_('Clearances',data),
                        headed_clearance = r_('Headed Clearance',data),
                        clearances_off_line = r_('Clearances off line',data),
                        recoveries = r_('Recoveries',data),
                        duels_won = r_('Duels won',data),
                        duels_lost = r_('Duels lost',data),
                        successful_50_50 = r_('Successful 50/50s',data),
                        aerial_battles_won = r_('Aerial battles won',data),
                        aerial_battles_lost = r_('Aerial battles lost',data),
                        own_goals = r_('Own goals',data),
                        errors_leading_to_goal = r_('Errors leading to goal',data),
                        # team play
                        assists = r_('Assists',data),
                        passes = r_('Passes',data),
                        passes_per_match = r_('Passes per match',data),
                        big_chances_created = r_('Big chances created',data),
                        crosses = r_('Crosses',data),
                        cross_accuracy = r_('Cross accuracy %',data),
                        through_balls = r_('Through balls',data),
                        accurate_long_balls = r_('Accurate long balls',data),
                        # discipline
                        yellow_cards = r_('Yellow cards',data),
                        red_cards = r_('Red cards',data),
                        fouls = r_('Fouls',data),
                        offsides = r_('Offsides',data),
                        # attack
                        goals = r_('Goals',data),
                        headed_goals = r_('Headed goals',data),
                        goals_with_right_foot = r_('Goals with right foot',data),
                        goals_with_left_foot = r_('Goals with left foot',data),
                        hit_woodwork = r_('Hit woodwork',data)
                    ))
                elif get_player_role(_id) == 'G':
                    goalkeeper_list.append(GoalkeeperStats(
                        pl_id = p,
                        last_update = timezone.now(),
                        appearances = r_('Appearances',data),
                        wins = r_('Wins',data),
                        losses = r_('Losses',data),
                        # goalkeeping
                        saves = r_('Saves',data),
                        penalties_saved = r_('Penalties saved',data),
                        punches = r_('Punches',data),
                        high_claims = r_('High Claims',data),
                        catches = r_('Catches',data),
                        sweeper_clearances = r_('Sweeper clearances',data),
                        throw_outs = r_('Throw outs',data),
                        goal_kicks = r_('Goal Kicks',data),
                        # defence
                        clean_sheets = r_('Clean sheets',data),
                        goals_conceded = r_('Goals conceded',data),
                        errors_leading_to_goal = r_('Errors leading to goal',data),
                        own_goals = r_('Own goals',data),
                        # discipline
                        yellow_cards = r_('Yellow cards',data),
                        red_cards = r_('Red cards',data),
                        fouls = r_('Fouls',data),
                        # team player
                        goals = r_('Goals',data),
                        assists = r_('Assists',data),
                        passes = r_('Passes',data),
                        passes_per_match = r_('Passes per match',data),
                        accurate_long_balls = r_('Accurate long balls',data)
                    ))
            except Exception as e:
                print(p.name)
                print(p.role)
                print(e)
                raise(e)
            ForwardStats.objects.bulk_create(forward_list)
            MidfielderStats.objects.bulk_create(midfielder_list)
            DefenderStats.objects.bulk_create(defender_list)
            GoalkeeperStats.objects.bulk_create(goalkeeper_list)
    else:
        for p in PlayerInfo.objects.all():
            data = clean_player_stats(get_player_stats(url,get_pl_id(p.name)))
            try:
                if p.role == 'F':
                    obj, created = ForwardStats.objects.update_or_create(
                        pl_id = p,
                        defaults = {
                        'last_update': timezone.now(),
                        'appearances': r_('Appearances',data),
                        'assists': r_('Assists',data),
                        'big_chances_created': r_('Big chances created',data),
                        'big_chances_missed': r_('Big chances missed',data),
                        'blocked_shots': r_('Blocked shots',data),
                        'clearances': r_('Clearances',data),
                        'crosses': r_('Crosses',data),
                        'fouls': r_('Fouls',data),
                        'freekicks_scored': r_('Freekicks scored',data),
                        'goals': r_('Goals',data),
                        'goals_per_match': r_('Goals per match',data),
                        'goals_with_left_foot': r_('Goals with left foot',data),
                        'goals_with_right_foot': r_('Goals with right foot',data),
                        'headed_clearance': r_('Headed Clearance',data),
                        'headed_goals': r_('Headed goals',data),
                        'hit_woodwork': r_('Hit woodwork',data),
                        'interceptions': r_('Interceptions',data),
                        'losses': r_('Losses',data),
                        'offsides': r_('Offsides',data),
                        'passes': r_('Passes',data),
                        'passes_per_match': r_('Passes per match',data),
                        'penalties_scored': r_('Penalties scored',data),
                        'red_cards': r_('Red cards',data),
                        'shooting_accuracy': r_('Shooting accuracy %',data),
                        'shots': r_('Shots',data),
                        'shots_on_target': r_('Shots on target',data),
                        'tackles': r_('Tackles',data),
                        'wins': r_('Wins',data),
                        'yellow_cards': r_('Yellow cards',data)
                        }
                    )
                    
                    obj.save() 
                elif p.role == 'M':
                    obj,created = MidfielderStats.objects.update_or_create(
                        pl_id = p,
                        defaults = {
                        'last_update': timezone.now(),
                        'appearances': r_('Appearances',data),
                        'wins': r_('Wins',data),
                        'losses': r_('Losses',data),
                        # team play
                        'assists': r_('Assists',data),
                        'passes': r_('Passes',data),
                        'passes_per_match': r_('Passes per match',data),
                        'big_chances_created': r_('Big chances created',data),
                        'crosses': r_('Crosses',data),
                        'cross_accuracy': r_('Cross accuracy %',data),
                        'through_balls': r_('Through balls',data),
                        'accurate_long_balls': r_('Accurate long balls',data),
                        # discipline
                        'yellow_cards': r_('Yellow cards',data),
                        'red_cards': r_('Red cards',data),
                        'fouls': r_('Fouls',data),
                        'offsides': r_('Offsides',data),
                        #attack
                        'big_chances_missed': r_('Big chances missed',data),
                        'freekicks_scored': r_('Freekicks scored',data),
                        'goals': r_('Goals',data),
                        'goals_per_match': r_('Goals per match',data),
                        'goals_with_right_foot': r_('Goals with right foot',data),
                        'goals_with_left_foot': r_('Goals with left foot',data),
                        'headed_goals': r_('Headed goals',data),
                        'hit_woodwork': r_('Hit woodwork',data),
                        'penalties_scored': r_('Penalties scored',data),
                        'shooting_accuracy': r_('Shooting accuracy %',data),
                        'shots': r_('Shots',data),
                        'shots_on_target': r_('Shots on target',data),
                        # defence
                        'tackles': r_('Tackles',data),
                        'tackle_success': r_('Tackle success %',data),
                        'blocked_shots': r_('Blocked shots',data),
                        'interceptions': r_('Interceptions',data),
                        'clearances': r_('Clearances',data),
                        'headed_clearance': r_('Headed Clearance',data),
                        'recoveries': r_('Recoveries',data),
                        'duels_won': r_('Duels won',data),
                        'duels_lost': r_('Duels lost',data),
                        'successful_50_50': r_('Successful 50/50s',data),
                        'aerial_battles_won': r_('Aerial battles won',data),
                        'aerial_battles_lost': r_('Aerial battles lost',data),
                        'errors_leading_to_goal': r_('Errors leading to goal',data)
                    }
                    )
                    obj.save()
                elif p.role == 'D':
                    obj, created = DefenderStats.objects.update_or_create(
                        pl_id = p,
                        defaults = {
                        'last_update': timezone.now(),
                        'appearances': r_('Appearances',data),
                        'wins': r_('Wins',data),
                        'losses': r_('Losses',data),
                        # defence
                        'clean_sheets': r_('Clean sheets',data),
                        'goals_conceded': r_('Goals conceded',data),
                        'tackles': r_('Tackles',data),
                        'tackle_success': r_('Tackle success %',data),
                        'last_man_tackles': r_('Last man tackles',data),
                        'blocked_shots': r_('Blocked shots',data),
                        'interceptions': r_('Interceptions',data),
                        'clearances': r_('Clearances',data),
                        'headed_clearance': r_('Headed Clearance',data),
                        'clearances_off_line' : r_('Clearances off line',data),
                        'recoveries': r_('Recoveries',data),
                        'duels_won': r_('Duels won',data),
                        'duels_lost': r_('Duels lost',data),
                        'successful_50_50': r_('Successful 50/50s',data),
                        'aerial_battles_won': r_('Aerial battles won',data),
                        'aerial_battles_lost': r_('Aerial battles lost',data),
                        'own_goals': r_('Own goals',data),
                        'errors_leading_to_goal': r_('Errors leading to goal',data),
                        # team play
                        'assists': r_('Assists',data),
                        'passes': r_('Passes',data),
                        'passes_per_match': r_('Passes per match',data),
                        'big_chances_created': r_('Big chances created',data),
                        'crosses': r_('Crosses',data),
                        'cross_accuracy':  r_('Cross accuracy %',data),
                        'through_balls': r_('Through balls',data),
                        'accurate_long_balls': r_('Accurate long balls',data),
                        # discipline
                        'yellow_cards': r_('Yellow cards',data),
                        'red_cards': r_('Red cards',data),
                        'fouls': r_('Fouls',data),
                        'offsides': r_('Offsides',data),
                        # attack
                        'goals': r_('Goals',data),
                        'headed_goals': r_('Headed goals',data),
                        'goals_with_right_foot': r_('Goals with right foot',data),
                        'goals_with_left_foot': r_('Goals with left foot',data),
                        'hit_woodwork': r_('Hit woodwork',data)
                        }
                    )
                    obj.save()
                elif p.role == 'G':
                    obj, created = GoalkeeperStats.objects.update_or_create(
                        pl_id = p,
                        defaults = {
                        'last_update': timezone.now(),
                        'appearances': r_('Appearances',data),
                        'wins': r_('Wins',data),
                        'losses': r_('Losses',data),
                        # goalkeeping
                        'saves': r_('Saves',data),
                        'penalties_saved': r_('Penalties saved',data),
                        'punches': r_('Punches',data),
                        'high_claims' : r_('High Claims',data),
                        'catches': r_('Catches',data),
                        'sweeper_clearances': r_('Sweeper clearances',data),
                        'throw_outs': r_('Throw outs',data),
                        'goal_kicks': r_('Goal Kicks',data),
                        # defence
                        'clean_sheets': r_('Clean sheets',data),
                        'goals_conceded': r_('Goals conceded',data),
                        'errors_leading_to_goal': r_('Errors leading to goal',data),
                        'own_goals': r_('Own goals',data),
                        # discipline
                        'yellow_cards': r_('Yellow cards',data),
                        'red_cards': r_('Red cards',data),
                        'fouls': r_('Fouls',data),
                        # team player
                        'goals': r_('Goals',data),
                        'assists': r_('Assists',data),
                        'passes': r_('Passes',data),
                        'passes_per_match': r_('Passes per match',data),
                        'accurate_long_balls': r_('Accurate long balls',data)
                        }
                    )
                    obj.save()
                
            except Exception as e:
                print(e)
                print("Bulk Creating : ",first_time)
                print(p.pl_id,":",p.name)
                raise(e)
                pass
            


def r_(key,data):
    return float(data[key]) if key in data else None

def get_pl_clubs():
    """
        Returns list of tuples of current premier league clubs containing (club_id, club_name) 
    """
    base_url = "https://www.premierleague.com"
    clubs_url = "https://www.premierleague.com/clubs"

    response = r.get(clubs_url)
    soup = BeautifulSoup(response.content,'html.parser')
    clubs_list = soup.find_all("a")
    #extract href links because they contain club number
    clubs_links = [link['href'] for link in clubs_list]
    #narrow down to links that have this regex pattern
    clubs = [link for link in clubs_links if re.search('clubs/[0-9]+',link)]
    #split link to get club number & club name in tuples
    return [(i.split("/")[2],i.split("/")[3]) for i in clubs]