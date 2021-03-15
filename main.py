import requests
from twilio.rest import Client
import os

OWM_KEY = os.environ.get("OWM_API_KEY")  # Open Weather Map API Key

URL = "https://api.openweathermap.org/data/2.5/onecall"
weather_param = {
    "lat": 52.375599,
    "lon": 13.348274,
    "appid": OWM_KEY
}

account_sid = os.environ.get("TWILIO_SID")
auth_token = os.environ.get("TWILIO_AUTH")

weather_data = requests.get(URL, params=weather_param)

data = weather_data.json()["hourly"][:12]

for i in range(12):
    if data[i]["weather"][0]["id"] < 700:
        client = Client(account_sid, auth_token)

        message = client.messages \
            .create(
            body="Please Bring an Umbrella.☂️",
            from_='+14133155580',
            to=os.environ.get("MOBILE_NO")
        )

        print(message.sid)
        break
print(data)
