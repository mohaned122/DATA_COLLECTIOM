import requests
import flask
################# Legal way ###################
#if you thimk about it , it is just another type of api data collection

url = "https://api.thingspeak.com/channels/9/feeds.json?results=5"
response = requests.get(url)
data = response.json()

for feed in data["feeds"]:
    print(f"Time: {feed['created_at']}  Temp: {feed['field1']}°C  Humidity: {feed['field2']}%")
