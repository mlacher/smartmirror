import pyowm
import pandas as pd
import numpy as np

import plotly.express as px



owm = pyowm.OWM('9f6afd479b6ab3d98a1ce2ed91815b0a')  # You MUST provide a valid API key
test1 = []
temp = []
def fore_cast():
    fc = owm.three_hours_forecast('Fürstenfeldbruck,GER')
    f = fc.get_forecast()
    for weather in f:
        #print (weather.get_reference_time('iso'),weather.get_temperature('celsius'))
        #test.append({'Time':weather.get_reference_time('iso'),'Temp':weather.get_temperature('celsius')})
        date = weather.get_reference_time()
        new = weather.get_temperature('celsius')
        temp.append([date, new['temp'], new['temp_max'],new['temp_min']])
        
    
    return temp
#observation = owm.weather_at_place('Fürstenfeldbruck,GER')
#w = observation.get_weather()


# Weather details
#w.get_wind()                  # {'speed': 4.6, 'deg': 330}
#w.get_humidity()              # 87
#print(w.get_temperature('celsius'))  # {'temp_max': 10.5, 'temp': 9.7, 'temp_min': 9.0}
data1 = fore_cast()
labels = ['date','temp','max','min']
#data= np.array(data1).T.tolist()]

data = pd.DataFrame(data1, columns = labels)
#data = pd.DataFrame(data).set_index("n","b","q","s")
print(data)

fig = px.line(data ,  x='date', y=('temp'))

fig.show()