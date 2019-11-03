import pandas as pd
import requests

def spiegel_news():
    headlines = requests.get("https://newsapi.org/v2/top-headlines?sources=spiegel-online&apiKey=a9301f44fe9f45acb462f585b16ad850").json()
    return headlines["articles"]
#print(headlines.keys())
#print(headlines["status"])
#print(headlines["articles"][1]['title'])
