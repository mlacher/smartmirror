import requests
import json

r = requests.get("https://api.sunrise-sunset.org/json?lat=36.7201600&lng=-4.4203400&date=today")
rt = r.text
rtj = json.loads(rt)
print(rtj['results']['sunrise'])
