import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_table as dt
import base64
import plotly.graph_objs as go
import plotly.express as px
import pandas as pd
import numpy as np
from dash.dependencies import Input, Output
from app import app

eigen = pd.read_csv('../data/eigenvector.csv')
eigen2 = pd.read_csv('../data/eigenvector2.csv')


layout = html.Div([
    html.Div([
        html.A('Home', className='active', href='/apps/as1'),
        html.A('Assignment-2', className='as1', href='/apps/as1'),
        html.A('Assignment-3', className='as2', href='/apps/as2')
    ], className='topnav'),

    html.Div([
        html.P('Top 10 Nodes for Dominos, by eigenvector centrality', className='title-1', style={'fontSize':30,'font-weight':'bold', 'text-align':'center'}),
        dt.DataTable(
            id='table',
            columns = [{"name":i, "id":i} for i in eigen.columns],
            data=eigen.to_dict('rows'),
            style_cell={
                'textAlign': 'center',
                'border':'1px solid grey',
                'fontSize':20
            },
            style_header={
                'border':'1px solid black',
                'fontSize':30,
                'font-weight':'bold'
            },
            style_cell_conditional=[
                {
                    'if':{'column_id':c},
                    'textAlign': 'left'
                } for c in ['Nodes']
            ]
        )
    ],style={'width':'65%', 'margin':'auto'}),

    
    html.Div([
        html.P('Most Central Node in Class 1 - Class 5 ', className='title-1', style={'fontSize':30,'font-weight':'bold', 'text-align':'center'}),
        dt.DataTable(
            id='table',
            columns = [{"name":i, "id":i} for i in eigen2.columns],
            data=eigen2.to_dict('rows'),
            style_cell={
                'textAlign': 'center',
                'border':'1px solid grey',
                'fontSize':20
            },
            style_header={
                'border':'1px solid black',
                'fontSize':30,
                'font-weight':'bold'
            },
            style_cell_conditional=[
                {
                    'if':{'column_id':c},
                    'textAlign': 'left'
                } for c in ['Class','Node']
            ]
        )
    ],style={'width':'65%', 'margin':'auto'}),

    html.Div([
        html.P('Social Network of the Graph', className='title-1', style={'fontSize':30,'font-weight':'bold', 'text-align':'center'}),
        html.Img(src=app.get_asset_url('dmnetwork.png'), style={'width':'49%'}),
        html.Img(src=app.get_asset_url('dmnetwork2.jpeg'), style={'width':'49%'})
    ])

    
])