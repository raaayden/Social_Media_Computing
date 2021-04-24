import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from app import app
from apps import app1, app2, as1, as2

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])

@app.callback(
    Output('page-content','children'),
    [Input('url','pathname')]
)
def display_page(pathname):
    if pathname == '/':
        return html.Div([
            html.Div([
            html.A('Home', className='active', href='/apps/as1'),
            html.A('Assignment-2', className='as1', href='/apps/as1'),
            html.A('Assignment-3', className='as3', href='/apps/as2')
        ], className='topnav'),
        html.Div([
            html.P('Nothing here', style={'size':'120','font-weight':'bold'})
        ])
        ])
    if pathname == '/apps/as1':
        return as1.layout
    elif pathname == '/apps/as2':
        return as2.layout
    else:
        return as1.layout

if __name__ == '__main__':
    app.run_server(debug=True)