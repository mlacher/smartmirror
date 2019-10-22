# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
import datetime as dt
import dash_daq as daq
import weather as w

from dash.dependencies import Input, Output

#external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
tester = w.fore_cast()
app = dash.Dash(
    __name__, meta_tags=[{"name": "viewport", "content": "width=device-width"}]
)
server = app.server
colors = {
    'background': '#0a0808',
    'text': '#d1d2d6'
}


app.layout = html.Div(
   # className = "3 columns",
    children=[
        html.Div(
            id="graphs-container",
            className="two rows",
            children=[
                html.Div(
                    className="two columns",
                    children=[
                        html.Div(id='date'),
                        html.Div(
                            id="card-1",
                            children=[
                                daq.LEDDisplay(
                                    id="operator-led",
                                    value='12:34',
                                    color="#92e0d3",
                                    backgroundColor="#1e2130",
                                    size=50
                                ),
                            ],
                        ),
                        
                        dcc.Interval(
                            id='interval-component',
                            interval=1*1000, # in milliseconds
                            n_intervals=0
                        ),
                        dcc.Graph(
                        
                        className="second column",
                        figure={
                            
                            'data': [
                                {'x': [1,2,3,4,5,6], 'y': tester[0:6,1], 'type': 'bar', 'name': 'SF'}
                            ],
                            'layout': {
                                'plot_bgcolor': colors['background'],
                                'paper_bgcolor': colors['background'],
                                'font': {
                                    'color': colors['text']
                                    }
                                }
                        })
                    ],
                )
            ],
        )
    ],
)

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