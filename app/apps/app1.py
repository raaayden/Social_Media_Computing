import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import numpy as np
from dash.dependencies import Input, Output
from app import app


data = pd.read_csv('../data/dominos.csv')
pos_tweets = [ tweet for index, tweet in enumerate(data['tweets']) if data['label'][index] > 0]
neu_tweets = [ tweet for index, tweet in enumerate(data['tweets']) if data['label'][index] == 0]
neg_tweets = [ tweet for index, tweet in enumerate(data['tweets']) if data['label'][index] < 0]

positive = len(pos_tweets)*100/len(data['tweets'])
negative = len(neg_tweets)*100/len(data['tweets'])
neutral = len(neu_tweets)*100/len(data['tweets'])

colors = {
    'background' : '#1111111'
}

layout = html.Div([
    html.Div([
        html.A('Home', className='active', href='/apps/as1'),
        html.A('Assignment-2', className='as1', href='/apps/app1'),
        html.A('Assignment-3', className='as3', href='/apps/app2')
    ], className='topnav'),
    
    html.Div([
        dcc.Graph(
        id='dominos_SA',
        figure={
            'data': [
                {'x':['Positive'],'y':[positive],'type':'bar','name':'positive'},
                {'x':['Neutral'],'y':[neutral],'type':'bar','name':'neutral'},
                {'x':['Negative'],'y':[negative],'type':'bar','name':'negative'},
            ],
            'layout': {
                'title': 'Sentiment Analysis Dominos',
                'paper_bgcolor': colors['background']
                }
            }
        ),  
    ],
    style={'width': '49%', 'display': 'inline-block'}),
    html.Div([
        dcc.Graph(
        id='dominos_SA',
        figure={
            'data': [
                {'x':['Positive'],'y':[positive],'type':'bar','name':'positive'},
                {'x':['Neutral'],'y':[neutral],'type':'bar','name':'neutral'},
                {'x':['Negative'],'y':[negative],'type':'bar','name':'negative'},
            ],
            'layout': {
                'title': 'Sentiment Analysis Dominos',
                'paper_bgcolor': colors['background']
                }
            }
        )
    ],
    style={'width': '49%', 'display': 'inline-block'})
])