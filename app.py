# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
import datetime as dt
import dash_daq as daq
import weather as w
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output

#external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
tester = w.fore_cast()
app = dash.Dash(
    __name__, external_stylesheets=[dbc.themes.BOOTSTRAP]
)
server = app.server
colors = {
    'background': '#0a0808',
    'text': '#d1d2d6'
}


app.layout = html.Div([
   # className = "3 columns",
    dbc.Row([
        dbc.Col(
            html.Div(
                daq.LEDDisplay(
                    id="operator-led",
                    value='12:34',
                    color="#92e0d3",
                    backgroundColor="#1e2130",
                    size=50
                ),
            ),        
            width = {"size": 6, "offset": 5},
        ),
    ]),
    dbc.Row([
        dbc.Col(
            html.Div(id='date'),
            width={"size": 6, "offset": 5},
        ),
    ]),
    dbc.Row([
        dbc.Col(
            daq.Thermometer(
            id='thermometer',
            value=98.6,
            min=95,
            max=105
            ) , 
        width={'size':1, "offset":1},
        ),
        dbc.Col(
            daq.Thermometer(
            id='thermometer2',
            value=98.6,
            min=95,
            max=105
            ) , 
        width={'size':1},
        ),
    ]),
        

    dcc.Interval(
                id='interval-component',
                interval=1*1000, # in milliseconds
                n_intervals=0
            ),
    dbc.Row([
        dbc.Col(
            dcc.Graph(
            #className="graphs-container",
            figure={
                
                'data': [
                    {'x': tester[2][0:6].index, 'y': tester[2][0:6].values, 'type': 'bar', 'name': 'Temp_max'}
                ],
                'layout': {
                    'plot_bgcolor': colors['background'],
                    'paper_bgcolor': colors['background'],
                    'coloraxis':{
                        'colorbar': -90,
                    },
                    'font': {
                        'color': colors['text'],
                        'size': 10,
                        }
                    }
            }),
        width = 4),          
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