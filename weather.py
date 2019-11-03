import pyowm
import pandas as pd
import numpy as np
from datetime import datetime
import plotly.express as px
import sys



owm = pyowm.OWM('9f6afd479b6ab3d98a1ce2ed91815b0a')  # You MUST provide a valid API key
test1 = []
temp = []
def fore_cast():
    fc = owm.three_hours_forecast('Fürstenfeldbruck,GER')
    f = fc.get_forecast()
    labels = ['date','time','datetime','temp','cat']
    for weather in f:
        #code is not nice requires update soon
        date_time = weather.get_reference_time()
        date = datetime.utcfromtimestamp(date_time).strftime('%Y-%m-%d')
        time = datetime.utcfromtimestamp(date_time).strftime('%H:%M')
        alltemp = weather.get_temperature('celsius')
        dateTime = date + ' '+ time
        #print(dateTime)
        temp.append([date,time,dateTime, alltemp['temp'],'temp'])
        temp.append([date,time,dateTime, alltemp['temp_max'],'temp_max'])
        temp.append([date,time,dateTime, alltemp['temp_min'],'temp_min'])
        
        #pd_data_group = pd_data_raw.groupby('date').max()
        #data_forecast = [pd_data_group.index, pd_data_group.time,pd_data_group.temp]
    pd_data_raw = pd.DataFrame(temp, columns = labels)
    return pd_data_raw
#

def current_weather():
    observation = owm.weather_at_place('Fürstenfeldbruck,GER')
    w = observation.get_weather()
    curr_wind=w.get_wind()                  # {'speed': 4.6, 'deg': 330}
    curr_hum= w.get_humidity()              # 87
    curr_temp= w.get_temperature('celsius')  # {'temp_max': 10.5, 'temp': 9.7, 'temp_min': 9.0}
    curr_rain = w.get_rain()
    if (not curr_rain):
        curr_rain = 0
    

    curr_cloud = w.get_clouds()
    curr_snow = w.get_snow()
    curr_w = [curr_temp, curr_wind, curr_hum, curr_rain,curr_cloud, curr_snow]
    return  curr_w
 



#fig.show()
