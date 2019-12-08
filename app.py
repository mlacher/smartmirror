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
import calendar
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

#Widget Calendar

i = 0
date = []
active = []
x = 0
str_year = dt.datetime.now().strftime('%B')
year = (int) (dt.datetime.now().strftime('%Y'))
month = (int) (dt.datetime.now().strftime('%m'))
day = (int) (dt.datetime.now().strftime('%d'))
mo_ra =(calendar.monthrange(year,month))


while i<42:  
    a = 'n'
    if (i == (day+mo_ra[0]-1)):
        a = 'a'
    if ((i < mo_ra[0]) or ((i-mo_ra[0])>=mo_ra[1])):
        x = ''
    elif (i==mo_ra[0]):
        x = 1
    elif (i>mo_ra[0]):
        x +=1
    date.append(x)
    active.append(a)
    i+=1

calendar = html.Div([
    html.Div(className = 'month', children= 
        html.Ul(children= 
            html.Li(str_year))),
    html.Div(className = 'weekdays', children= 
        html.Ul(children= [
            html.Li('M'),
            html.Li('D'),
            html.Li('M'),
            html.Li('D'),
            html.Li('F'),
            html.Li('S'),
            html.Li('S')])),
    html.Div(className = 'days', children= 
        html.Ul(children= [
            html.Li(children= html.Span(str(date[0]),className= str(active[0]))),
            html.Li(children= html.Span(str(date[1]),className= str(active[1]))),
            html.Li(children= html.Span(str(date[2]),className= str(active[2]))),
            html.Li(children= html.Span(str(date[3]),className= str(active[3]))),
            html.Li(children= html.Span(str(date[4]),className= str(active[4]))),
            html.Li(children= html.Span(str(date[5]),className= str(active[5]))),
            html.Li(children= html.Span(str(date[6]),className= str(active[6]))),
            html.Li(children= html.Span(str(date[7]),className= str(active[7]))),
            html.Li(children= html.Span(str(date[8]),className= str(active[8]))),
            html.Li(children= html.Span(str(date[9]),className= str(active[9]))),
            html.Li(children= html.Span(str(date[10]),className= str(active[10]))),
            html.Li(children= html.Span(str(date[11]),className= str(active[11]))),
            html.Li(children= html.Span(str(date[12]),className= str(active[12]))),
            html.Li(children= html.Span(str(date[13]),className= str(active[13]))),
            html.Li(children= html.Span(str(date[14]),className= str(active[14]))),
            html.Li(children= html.Span(str(date[15]),className= str(active[15]))),
            html.Li(children= html.Span(str(date[16]),className= str(active[16]))),
            html.Li(children= html.Span(str(date[17]),className= str(active[17]))),
            html.Li(children= html.Span(str(date[18]),className= str(active[18]))),
            html.Li(children= html.Span(str(date[19]),className= str(active[19]))),
            html.Li(children= html.Span(str(date[20]),className= str(active[20]))),
            html.Li(children= html.Span(str(date[21]),className= str(active[21]))),
            html.Li(children= html.Span(str(date[22]),className= str(active[22]))),
            html.Li(children= html.Span(str(date[23]),className= str(active[23]))),
            html.Li(children= html.Span(str(date[24]),className= str(active[24]))),
            html.Li(children= html.Span(str(date[25]),className= str(active[25]))),
            html.Li(children= html.Span(str(date[26]),className= str(active[26]))),
            html.Li(children= html.Span(str(date[27]),className= str(active[27]))),
            html.Li(children= html.Span(str(date[28]),className= str(active[28]))),
            html.Li(children= html.Span(str(date[29]),className= str(active[29]))),
            html.Li(children= html.Span(str(date[30]),className= str(active[30]))),
            html.Li(children= html.Span(str(date[31]),className= str(active[31]))),
            html.Li(children= html.Span(str(date[32]),className= str(active[32]))),
            html.Li(children= html.Span(str(date[33]),className= str(active[33]))),
            html.Li(children= html.Span(str(date[34]),className= str(active[34]))),
            html.Li(children= html.Span(str(date[35]),className= str(active[35]))),
            html.Li(children= html.Span(str(date[36]),className= str(active[36]))),
            html.Li(children= html.Span(str(date[37]),className= str(active[37]))),
            html.Li(children= html.Span(str(date[38]),className= str(active[38]))),
            html.Li(children= html.Span(str(date[39]),className= str(active[39]))),
            html.Li(children= html.Span(str(date[40]),className= str(active[40]))),
            html.Li(children= html.Span(str(date[41]),className= str(active[41])))
           ])),
    html.Div('Notes:',className= 'actions', style = {'color':'red', 'font-size':'14px'})
])




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
    dbc.ListGroup(
        [
            dbc.ListGroupItem(html.Div(id = 'fabrizio'),
                html.A(href= "http://fabrizio.co"),
                html.Div(className = 'cloudy'),),
            dbc.ListGroupItem("Item 2"),
            dbc.ListGroupItem("Item 3"),
        ],
        flush=True,
    ),
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
            'color': 'white',
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

#Widget weather2.0
w_dic = {
        '01d':'sunny','01n':'starry',
        '02d':'cloudy','02n':'starry',
        '03d':'cloudy','03n':'starry',
        '04d':'cloudy','04n':'starry',
        '09d':'rainy','09n':'starry',
        '10d':'rainy','10n':'starry',
        '11d':'stormy','11n':'starry',
        '13d':'snowy','13n':'starry',
        '50d':'snowy','50n':'starry'
        }
weather = html.Div([
    html.Div(id = 'fabrizio'),
    html.A(href= "http://fabrizio.co"),
    html.Div(className = w_dic[temp_c[3]]),
    html.Div(   
        html.P(
                str(temp_c[0]['temp'])+" °C",
                style = {'color':'white','font-size':'18px'}
        )
    )
])

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
        html.P()
    ]),

    #3rd ROW
    dbc.Row([
        dbc.Col(
            calendar,
        width={'size':3},
        ),
        dbc.Col(
            weather,      
        width={'size':3, 'offset':6},
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
            #maps,
            News,  
        width={'size':3, 'offset':5},
        align="center"
        #style={'backgroundColor':'white'}
        )     
    ]),

    #5th Row
    
    dbc.Row([
        dbc.Col(
            #News, 
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


if __name__ == '__main__':
    app.run_server(debug=True,dev_tools_ui=False,dev_tools_props_check=False)
