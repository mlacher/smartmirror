# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
import datetime as dt
import dash_table
import dash_daq as daq
import weather as w
import dash_bootstrap_components as dbc
import news as ns
#import nfl
from dash.dependencies import Input, Output
import plotly.express as px
import plotly.graph_objects as go

#get temp values
temp_fc = w.fore_cast()
temp_c = w.current_weather()
#get news
news = ns.spiegel_news()
#get nfl
#nfl_s = nfl.nfl_stats()

#get mapbox
mapbox_access_token = "pk.eyJ1IjoibXgtbGNociIsImEiOiJjazJwMnBwOHoxMm1iM21uempkbWUxMmRvIn0._5SM_JZ4YO46nEg-F6-psA"
mapbox_style = "mapbox://styles/mx-lchr/ck2p4pjk91b8f1cnytdrmy5gh/draft"


app = dash.Dash(
    __name__, external_stylesheets=[dbc.themes.BOOTSTRAP]
)
server = app.server
colors = {
    #'background': '#0a0808',
    'text': '#33c3f0'
}
#-------------------------------------------------------------------------#
#---------------------START of WIDGETS------------------------------------#
#-------------------------------------------------------------------------#

#widget Maps
maps=dcc.Graph(
    id="county-choropleth",
    figure=dict(
        data=[
            dict(
                lat=48,
                lon=11,
                text="d",
                type="scattermapbox",
            )
        ],
        layout=dict(
            mapbox=dict(
                layers=[],
                accesstoken=mapbox_access_token,
                style=mapbox_style,
                center=dict(
                    lat=48.1782219, lon=11.2781526
                ),
                pitch=0,
                zoom=12,
            ),
            margin=dict(r=0, l=0, t=0, b=0),
            autosize=True,
        ),
       ),
    style={
        "backgroundColor": "#000000"
    },
)



#Widget Temperature
card = dbc.Card(
    [
        dbc.CardImg(src="/assets/images/"+ str(temp_c[3]) +".png", top=True),
        dbc.CardBody(
            [
                html.P(
                    'Temp.:'+str(temp_c[0]['temp'])+" °C",
                    className="card-text",
                )
            ]
        ),
    ],
    style={
        "width": "20rem",
        "backgroundColor": "#000000"
    },
)  

#Widget Time
Time_LED = daq.LEDDisplay(
    id="operator-led",
    value='12:34',
    color="#E4085C",
    backgroundColor="#000000",
    size=50
)

#Widget News
News = dbc.Toast(
    [html.P(str(news[0]['title']), className="mb-0"),
    html.P(str(news[1]['title']), className="mb-0")],
    header="Spiegel News",
    style={'width': '100%',
            'color': '#E4085C',
            'backgroundColor':'#000000',
            'font-size':'14px'}
)

#Widget Temp_Graph
Temp_Graph = dcc.Graph(
    figure={
        'data': [{
            'x': temp_fc['datetime'],
            'y': temp_fc['temp'],
            'type': 'scatter',
            'fill': 'tonexty',
            'marker':{
            'color': '#E4085C'}
        }],
        'layout': {
            'plot_bgcolor':'#000000',
            'paper_bgcolor':'#000000',
            'xaxis': {
                'nticks': 5,
                'tickformat': '     (%a)',
                #'gridcolor': 'darkgrey',
                'gridwidth': 0.1,
                'showticklabes': False,
                'tickfont' :{
                    'color': 'grey'
                }
            },
            'yaxis': {
                'title':{
                    'text':"Temperature in °C"
                },
                'tickfont' : {
                    'color': 'grey'
                }
            }
        }
    }
)

'''
#Widget NFL_Stats
NFL_Stats = dash_table.DataTable(
    id='table',
    columns=[{"name": i, "id": i} for i in nfl_s[0]],
    data=nfl_s[0].to_dict('records'),
    style_table= {'width':1,
                    'height':10},
    style_cell= {'width':1,
                'height':10,
                'backgroundColor': '#000000',
                'color': '#33c3f0'},
    style_as_list_view=True,
    style_header={'backgroundColor': '#000000'}
)
'''

#-----------------------------------------------------------------------------#
#------------------------------------app--------------------------------------#
#-----------------------------------------------------------------------------#


app.layout = dbc.Container([
    #1st ROW
    dbc.Row([
        dbc.Col(
            html.Div(
            Time_LED
            ),        
            width = {"size": 6, "offset": 3},
            style={'text-align': 'center'}
        ),
    ]),
    #2nd ROW
    dbc.Row([
        dbc.Col(
            html.Div(id='date'),
            width={"size": 2, "offset": 5},
            style={'text-align': 'center',
                'color':'#E4085C'}
            #style={'backgroundColor':'white'}
        ),
    ]),
    #3rd ROW
    dbc.Row([
        dbc.Col(
            card,
        width={'size':3},
        ),
        dbc.Col(
            News,        
        width={'size':2, 'offset':6},
        #style={'backgroundColor':'white'}
        ),
    ]),
    dbc.Row(),
    dcc.Interval(
                id='interval-component',
                interval=1*1000, # in milliseconds
                n_intervals=0
            ),
    #4th ROW

    dbc.Row([
        dbc.Col(
            Temp_Graph,   
        width = 4),

        dbc.Col(
            maps,
        width={'size':3, 'offset':5},
        #style={'backgroundColor':'white'}
        )     
    ]),

    #5th Row
    
    dbc.Row([
        dbc.Col(
           # maps,
            width={'size':5},
            #style={'backgroundColor':'white'}
        ),

    ])
], fluid=True)




@app.callback(Output('operator-led', 'value'),
              [Input('interval-component', 'n_intervals')])
def update_LED(n):
    time = dt.datetime.now().strftime('%H:%M')
    return [
        str(time)
    ]


@app.callback(Output('date', 'children'),
              [Input('interval-component', 'n_intervals')])
def update_time(n):
    time = dt.datetime.now().strftime('%Y-%m-%d')
    style = {'padding': '8px', 'fontSize': '24px'}
    return [
        html.Span(time, style=style)
    ]

if __name__ == '__main__':
    app.run_server(debug=True,dev_tools_ui=False,dev_tools_props_check=False)
