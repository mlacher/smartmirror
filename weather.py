import pyowm
import pandas as pd
import numpy as np
from datetime import datetime
import plotly.express as px


owm = pyowm.OWM('9f6afd479b6ab3d98a1ce2ed91815b0a')  # You MUST provide a valid API key
test1 = []
temp = []
def fore_cast():
    fc = owm.three_hours_forecast('Fürstenfeldbruck,GER')
    f = fc.get_forecast()
    for weather in f:
        #code is not nice requires update soon
        date_time = weather.get_reference_time()
        date = datetime.utcfromtimestamp(date_time).strftime('%Y-%m-%d')
        time = datetime.utcfromtimestamp(date_time).strftime('%H:%M')
        alltemp = weather.get_temperature('celsius')
        temp.append([date,time, alltemp['temp'],'temp'])
        temp.append([date,time, alltemp['temp_max'],'temp_max'])
        temp.append([date,time, alltemp['temp_min'],'temp_min'])
        labels = ['date','time','temp','cat']
        pd_data_raw = pd.DataFrame(temp, columns = labels)
        pd_data_group = pd_data_raw.groupby('date').max()
        data_forecast = [pd_data_group.index, pd_data_group.time,pd_data_group.temp]
    return data_forecast
#
def current_weather():
    observation = owm.weather_at_place('Fürstenfeldbruck,GER')
    w = observation.get_weather()
    curr_wind=w.get_wind()                  # {'speed': 4.6, 'deg': 330}
    #curr_hum= w.get_humidity()              # 87
    curr_temp= w.get_temperature('celsius')  # {'temp_max': 10.5, 'temp': 9.7, 'temp_min': 9.0}
    curr_w = [curr_temp, curr_wind]
    #print(curr_w[0]['temp']) example for current temperature
