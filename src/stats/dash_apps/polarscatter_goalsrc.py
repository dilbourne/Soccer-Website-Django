import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
from plotly.offline import plot
from django_plotly_dash import DjangoDash
import pandas as pd
from stats.getters import get_pl_id, get_player_stats
from stats.cleaners import clean_player_stats
from django.conf import settings
import requests as r
import os

external_stylesheets = [
    'https://codepen.io/chriddyp/pen/bwlwgp.css',
]

app = DjangoDash('PolarScatter', external_stylesheets = external_stylesheets)

def ForwardAttributesScatterTrace(player):
            url = "https://www.premierleague.com/players/{}/player/stats"
            # os.path.join(settings.BASE_DIR,"static/dataframes/")+"pl_players_info.csv"
            try:
                try:
                    #d = clean_player_stats(get_player_stats(url,get_pl_id(player)))
                    d_info = r.get("http://localhost:8000/stats/players/info/{p}/".format(p=player)).json()
                    d = r.get("http://localhost:8000/stats/players/{role}/{_id}/".format(role=d_info['role'],_id=d_info['pl_id'])).json()
                    
                except Exception as e:
                    print(e)
                    raise(e)
                
                goals = d['goals']
                sp = go.Scatterpolar(
                    r = [d['goals_with_left_foot']/goals,d['goals_with_right_foot']/goals,d['headed_goals']/goals,
                    d['penalties_scored']/goals,d['freekicks_scored']/goals],
                    theta = ['Goals with Left-Foot','Goals with Right-Foot','Goals from Header','Goals from Penalty','Goals from Freekick'],
                    fill = 'toself',
                    name = player
                )
                print('scatter polar graph with player made')
            except:
                sp = go.Scatterpolar(
                    r = [],
                    theta = [],
                    fill = 'toself',
                    name = 'Player Not Found'  
                )
            return sp

def ScatterPolarLayout():
            layout = go.Layout(
                polar = dict(
                    radialaxis = dict(
                          visible = True,
                          range = [0, 1]
                        )
                ),
                #xaxis = dict(domain=[0,1]),
                #yaxis = dict(domain=[0,1]),
                showlegend = True,
                title = 'Player Ability',
                paper_bgcolor='#27293d',
                plot_bgcolor='rgba(0,0,0,0)',
                font=dict(color='white')
            )
            return layout
           

app.layout = html.Div([
    dcc.Graph(id='polar-graph', style={"backgroundColor": "#1a2d46", "color": "#ffffff", "padding-bottom": "10px"}),
    dcc.Input(id='player-name', value='', type='text', placeholder='Write Player Name Here...')    
], className="plot-div")

@app.callback(
    Output('polar-graph','figure'),
    [Input('player-name','value')]
)
def display_value(value):
    graph = ForwardAttributesScatterTrace(value)
    layout = ScatterPolarLayout()
    return {'data': [graph], 'layout': layout}