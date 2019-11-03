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
import nfl
from dash.dependencies import Input, Output
import plotly.express as px

#get temp values
temp_fc = w.fore_cast()
temp_c = w.current_weather()
#get news
news = ns.spiegel_news()
#get nfl
nfl_s = nfl.nfl_stats()

app = dash.Dash(
    __name__, external_stylesheets=[dbc.themes.BOOTSTRAP]
)
server = app.server
colors = {
    #'background': '#0a0808',
    'text': '#d1d2d6'
}
#-------------------------------------------------------------------------#
#---------------------START of WIDGETS------------------------------------#
#-------------------------------------------------------------------------#

#Widget Temperature
card = dbc.Card(
    [
        dbc.CardImg(src="/assets/images/test.jpg", top=True),
        dbc.CardBody(
            [
                html.P(
                    'Temp.:'+str(temp_c[0]['temp'])+' °C'+ '\n '+
                    'Rain.:'+str(temp_c[3])+' %',
                    className="card-text",
                )
            ]
        ),
    ],
    style={
        "width": "20rem",
        "backgroundColor": "#0a0808"
    },
)  

#Widget Time
Time_LED = daq.LEDDisplay(
    id="operator-led",
    value='12:34',
    #color="#92e0d3",
    backgroundColor="#0a0808",
    size=50
)

#Widget News
News = dbc.Toast(
    [html.P(str(news[0]['title']+ news[1]['title'] + '\n '+ news[2]['title']), className="mb-0")],
    header="Spiegel News",
    style={'width': '100%',
            'color': '#7FDBFF',
            'backgroundColor':'white',
            'font-size':'14px'}
)

#Widget Temp_Graph
Temp_Graph = dcc.Graph(
    figure={
        'data': [{
            'x': temp_fc['datetime'],
            'y': temp_fc['temp'],
            'type': 'scatter',
            'fill': 'tonexty'
        }],
        'layout': {
            'plot_bgcolor':'#0a0808',
            'paper_bgcolor':'#0a0808',
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

#Widget NFL_Stats
NFL_Stats = dash_table.DataTable(
    id='table',
    columns=[{"name": i, "id": i} for i in nfl_s[0]],
    data=nfl_s[0].to_dict('records'),
    style_table= {'width':1,
                    'height':10},
    style_cell= {'width':1,
                'height':10,
                'backgroundColor': '#0a0808',
                'color': 'white'},
    style_as_list_view=True,
    style_header={'backgroundColor': '#0a0808'}
)

#-----------------------------------------------------------------------------#
#------------------------------------app--------------------------------------#
#-----------------------------------------------------------------------------#


app.layout = html.Div([
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
            style={'text-align': 'center'}
            #style={'backgroundColor':'white'}
        ),
    ]),
    #3rd ROW
    dbc.Row([
        dbc.Col(
            card,
        width={'size':3,'offset':1},
        ),
        dbc.Col(
            News,        
        width={'size':4, 'offset':4},
        ),
    ]),
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
            NFL_Stats,
        width={'size':2, 'offset':5},
        #style={'backgroundColor':'white'}
        )     
    ]),
])




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
    app.run_server(debug=True)
