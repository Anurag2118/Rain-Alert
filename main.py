import requests
from twilio.rest import Client

account_sid = "AC4c8970bab2c4a66c52d48a61704c5739"
auth_token = "004764d6aea956bbef081714ade21e32"


OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = "a07a084c19d011bfb587669105c93ca4"

weather_params={
    "lat": 44.8125,
    "lon": 20.4612,
    "appid": api_key,
    "cnt" : 4,
}

response = requests.get(OWM_Endpoint,params=weather_params)
response.raise_for_status()
weather_data = response.json()

will_rain = False

for hour_data in weather_data["list"]:
    weather_code = hour_data["weather"][0]["id"]
    if int(weather_code) <700 :
        will_rain=True
       
if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages\
        .create(
        body="It is going to rain today. Remember to bring an ☔",
        from_="Twilio generated number",
        to="Your Number"
        )
    print(message.status)
        
