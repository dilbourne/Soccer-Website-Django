import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
from plotly.offline import plot
from django_plotly_dash import DjangoDash
import pandas as pd
from stats.getters import get_pl_id, get_player_page
from stats.cleaners import clean_player_page
from django.conf import settings
import os

external_stylesheets = ['https://codepen.io/chriddyp/pen/bwlwgp.css']

app = DjangoDash('PolarScatter', external_stylesheets = external_stylesheets)

def ForwardAttributesScatterTrace(player):
            url = "https://www.premierleague.com/players/{}/player/stats"
            try:
                try:
                    d = clean_player_page(get_player_page(url,get_pl_id(player,os.path.join(settings.BASE_DIR,"static/dataframes/")+"pl_players_info.csv")))
                except Exception as e:
                    raise(e)
                
                goals = d['Goals']
                sp = go.Scatterpolar(
                    r = [d['Goals with left foot']/goals,d['Goals with right foot']/goals,d['Headed goals']/goals,
                    d['Penalties scored']/goals,d['Freekicks scored']/goals],
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
    dcc.Graph(id='polar-graph', style={"backgroundColor": "#1a2d46", "color": "#ffffff"}),
    dcc.Input(id='player-name', value='', type='text', placeholder='Write Player Name Here...')    
], className='embed-responsive embed-responsive-16by9 border border-dark rounded')

@app.callback(
    Output('polar-graph','figure'),
    [Input('player-name','value')]
)
def display_value(value):
    graph = ForwardAttributesScatterTrace(value)
    layout = ScatterPolarLayout()
    return {'data': [graph], 'layout': layout}