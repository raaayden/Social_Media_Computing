import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import plotly.express as px
import pandas as pd
import numpy as np
from dash.dependencies import Input, Output
from app import app

#Pizza
pizza = pd.read_csv('../data/pizza.csv')
pos_tweets = [ tweet for index, tweet in enumerate(pizza['tweets']) if pizza['label'][index] > 0]
neu_tweets = [ tweet for index, tweet in enumerate(pizza['tweets']) if pizza['label'][index] == 0]
neg_tweets = [ tweet for index, tweet in enumerate(pizza['tweets']) if pizza['label'][index] < 0]

pos = len(pos_tweets)*100/len(pizza['tweets'])
neg = len(neg_tweets)*100/len(pizza['tweets'])
neu = len(neu_tweets)*100/len(pizza['tweets'])

popPizza = pd.read_csv('../data/Poppizza.csv')
popPizza2 = pd.read_csv('../data/Poppizza2.csv')


#Dominos
dominos = pd.read_csv('../data/dominos.csv')
dom_pos_tweets = [ tweet for index, tweet in enumerate(dominos['tweets']) if dominos['label'][index] > 0]
dom_neu_tweets = [ tweet for index, tweet in enumerate(dominos['tweets']) if dominos['label'][index] == 0]
dom_neg_tweets = [ tweet for index, tweet in enumerate(dominos['tweets']) if dominos['label'][index] < 0]

dom_pos = len(dom_pos_tweets)*100/len(dominos['tweets'])
dom_neg = len(dom_neg_tweets)*100/len(dominos['tweets'])
dom_neu = len(dom_neu_tweets)*100/len(dominos['tweets'])

#pizzahut
pizzahut = pd.read_csv('../data/pizzahut.csv')
ph_pos_tweets = [ tweet for index, tweet in enumerate(pizzahut['tweets']) if pizzahut['label'][index] > 0]
ph_neu_tweets = [ tweet for index, tweet in enumerate(pizzahut['tweets']) if pizzahut['label'][index] == 0]
ph_neg_tweets = [ tweet for index, tweet in enumerate(pizzahut['tweets']) if pizzahut['label'][index] < 0]

ph_pos = len(ph_pos_tweets)*100/len(pizzahut['tweets'])
ph_neg = len(ph_neg_tweets)*100/len(pizzahut['tweets'])
ph_neu = len(ph_neu_tweets)*100/len(pizzahut['tweets'])

#papajohns
papajohns = pd.read_csv('../data/papajohns.csv')
pj_pos_tweets = [ tweet for index, tweet in enumerate(papajohns['tweets']) if papajohns['label'][index] > 0]
pj_neu_tweets = [ tweet for index, tweet in enumerate(papajohns['tweets']) if papajohns['label'][index] == 0]
pj_neg_tweets = [ tweet for index, tweet in enumerate(papajohns['tweets']) if papajohns['label'][index] < 0]

pj_pos = len(pj_pos_tweets)*100/len(papajohns['tweets'])
pj_neg = len(pj_neg_tweets)*100/len(papajohns['tweets'])
pj_neu = len(pj_neu_tweets)*100/len(papajohns['tweets'])

#littlecaesars
littlecaesars = pd.read_csv('../data/littlecaesars.csv')
lt_pos_tweets = [ tweet for index, tweet in enumerate(littlecaesars['tweets']) if littlecaesars['label'][index] > 0]
lt_neu_tweets = [ tweet for index, tweet in enumerate(littlecaesars['tweets']) if littlecaesars['label'][index] == 0]
lt_neg_tweets = [ tweet for index, tweet in enumerate(littlecaesars['tweets']) if littlecaesars['label'][index] < 0]

lt_pos = len(lt_pos_tweets)*100/len(littlecaesars['tweets'])
lt_neg = len(lt_neg_tweets)*100/len(littlecaesars['tweets'])
lt_neu = len(lt_neu_tweets)*100/len(littlecaesars['tweets'])

#cali
cali = pd.read_csv('../data/calpizzakitchen.csv')
c_pos_tweets = [ tweet for index, tweet in enumerate(cali['tweets']) if cali['label'][index] > 0]
c_neu_tweets = [ tweet for index, tweet in enumerate(cali['tweets']) if cali['label'][index] == 0]
c_neg_tweets = [ tweet for index, tweet in enumerate(cali['tweets']) if cali['label'][index] < 0]

c_pos = len(c_pos_tweets)*100/len(cali['tweets'])
c_neg = len(c_neg_tweets)*100/len(cali['tweets'])
c_neu = len(c_neu_tweets)*100/len(cali['tweets'])



colors = {
    'background' : '#111111'
}

pizza = ['Dominos','PizzaHut','PapaJohns','LittleCaesars','CaliforniaPizzaKitchen']

##################################################Radar Chart - user sentiments####################################################

fig = go.Figure()
fig.add_trace(go.Scatterpolar(
    r=[dom_neg,ph_neg,pj_neg,lt_neg,c_neg],
    theta=pizza,
    fill='toself',
    name='Negative'
))

fig.add_trace(go.Scatterpolar(
    r=[dom_neu,ph_neu,pj_neu,lt_neu,c_neu],
    theta=pizza,
    fill='toself',
    name='Neutral'
))

fig.add_trace(go.Scatterpolar(
    r=[dom_pos,ph_pos,pj_pos,lt_pos,c_pos],
    theta=pizza,
    fill='toself',
    name='Positive'
))

fig.update_layout(
    title_text="Users' sentiment towards the industry",
    title_x=0.5
)

##################################################Radar Chart - user sentiments####################################################

##################################################Popular Pizza####################################################

figPopM = px.bar(
    popPizza, x='Pizza', y='mentions',color='Pizza',text='mentions'
)

figPopR = px.bar(
    popPizza, x='Pizza', y='retweets',color='Pizza', text='retweets'
)

figPopL = px.bar(
    popPizza, x='Pizza', y='likes',color='Pizza', text='likes'
)

figPopP = go.Figure(data=[
    go.Bar(name='Followers', x=popPizza2['Pizza'], y=popPizza2['Followers'], text=popPizza2['Followers'], textposition='auto'),
    go.Bar(name='Friends', x=popPizza2['Pizza'], y=popPizza2['Friends'], text=popPizza2['Friends'], textposition='auto'),
    go.Bar(name='Status', x=popPizza2['Pizza'], y=popPizza2['Status'], text=popPizza2['Status'], textposition='auto')
])

figPopM.update_layout(
    title_text="Brands Mentions",
    title_x=0.5
)
figPopR.update_layout(
    title_text="Brands Retweets",
    title_x=0.5
)
figPopL.update_layout(
    title_text="Brands Favourites",
    title_x=0.5
)
figPopP.update_layout(
    barmode='group',
    title_text="Brands Demographics",
    title_x=0.5
)

##################################################Popular Pizza####################################################

##################################################Hot Topic########################################################

domSA_pos = pd.read_csv('../data/dominosSA.csv')
domSA_neg = pd.read_csv('../data/dominosSA2.csv')
figDom1 = px.bar(
    domSA_pos, x='Words', y='Count',color='Count'
)
figDom2 = px.bar(
    domSA_neg, x='Words', y='Count',color='Count'
)

figDom1.update_layout(
    title_text='Positive word frequency',
    title_x=0.5
)
figDom2.update_layout(
    title_text='Negative word frequency',
    title_x=0.5
)


##################################################Hot Topic########################################################






##################################################################################################################
layout = html.Div([
    html.Div([
        html.A('Home', className='active', href='/apps/as1'),
        html.A('Assignment-2', className='as1', href='/apps/as1'),
        html.A('Assignment-3', className='as2', href='/apps/as2')
    ], className='topnav'),
    
############################################Users' towards industry######################################
    html.P('Industry:Pizza Chain', className='title-1', style={'fontSize':70,'font-weight':'bold', 'text-align':'center'}),
    html.Div([
        dcc.Graph(
        id='pizza_SA',
        figure={
            'data': [
                {'x':['Negative'],'y':[neg],'type':'bar','name':'negative'},
                {'x':['Neutral'],'y':[neu],'type':'bar','name':'neutral'},
                {'x':['Positive'],'y':[pos],'type':'bar','name':'positive'},
            ],
            'layout': {
                'title': 'Sentiment Analysis Pizza Chains'
                }
            }
        ),  
    ],
    style={'width': '50%', 'display': 'inline-block'}),

    html.Div([
        dcc.Graph(
        id='pizza-SA',
        figure=fig
        )
    ],
    style={'width': '50%', 'display': 'inline-block'}),

############################################Popular brands######################################
    html.Div([
        html.P('Popular Brands', className='title-2', style={'fontSize':50,'font-weight':'bold', 'text-align':'center'}),
        dcc.Tabs(id='tabs', children=[
            dcc.Tab(label='Profile', children=[
                html.Div([
                    dcc.Graph(
                    id='PopularBrandsP',
                    figure=figPopP
                    )
                ],
                style={'width':'100%','display': 'inline-block'}),
            ]),
            dcc.Tab(label='Engagement', children=[
                html.Div([
                    dcc.Graph(
                    id='PopularBrandsM',
                    figure=figPopM
                    )
                ],
                style={'width': '33%', 'display': 'inline-block'}),

                html.Div([
                    dcc.Graph(
                    id='PopularBrandsM',
                    figure=figPopR
                    )
                ],
                style={'width': '33%', 'display': 'inline-block'}),

                html.Div([
                    dcc.Graph(
                    id='PopularBrandsM',
                    figure=figPopL
                    )
                ],
                style={'width': '33%', 'display': 'inline-block'})
            ])
        ],
        style={
        'fontFamily': 'system-ui'
    },
        content_style={
        'borderLeft': '1px solid #d6d6d6',
        'borderRight': '1px solid #d6d6d6',
        'borderBottom': '1px solid #d6d6d6'
    },
        parent_style={
        'margin': '0 auto'
    }
    )
    ]),

##################################################Hot Topic########################################################

    html.Div([
        html.P('Hot Topics', className='title-2', style={'fontSize':50,'font-weight':'bold', 'text-align':'center'}),
        dcc.Tabs(id='Tabs', children=[
            dcc.Tab(label='Positive Sentiment', children=[
                html.Div([
                    html.P('From top left (Pizza Hut, Papa John and Little Caesars)',style={'fontSize':20, 'font-weight':'bold', 'text-align':'center'}),
                    html.Img(src=app.get_asset_url('pos_cloud_pizzahut.png'), style={'height':'33%','width':'33%'}),
                    html.Img(src=app.get_asset_url('pos_cloud_pj.png'), style={'height':'33%','width':'33%'}),
                    html.Img(src=app.get_asset_url('pos_cloud_lc.png'), style={'height':'33%','width':'33%'})  
                ])
            ]),
            dcc.Tab(label='Negative sentiment', children=[
                html.Div([
                    html.P('From top left (Pizza Hut, Papa John and Little Caesars)',style={'fontSize':20, 'font-weight':'bold', 'text-align':'center'}),
                    html.Img(src=app.get_asset_url('neg_cloud_ph.png'), style={'height':'33%','width':'33%'}),
                    html.Img(src=app.get_asset_url('neg_cloud_pj.png'), style={'height':'33%','width':'33%'}),
                    html.Img(src=app.get_asset_url('neg_cloud_lc.png'), style={'height':'33%','width':'33%'})  
                ])
            ])
        ])
    ]),

    html.Div([
        html.P('Dominos most discussed', className='dominos-discussed', style={'fontSize':50,'font-weight':'bold', 'text-align':'center'}),
        html.Div([
            dcc.Graph(
                id='domSA_pos',
                figure=figDom1
                )
        ],style={'width': '50%', 'display': 'inline-block'}),
        html.Div([
            dcc.Graph(
                id='domSA_neg',
                figure=figDom2
                )
        ],style={'width': '50%', 'display': 'inline-block'})
    ])


    
])