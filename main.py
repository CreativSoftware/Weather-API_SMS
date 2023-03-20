import requests
from twilio.rest import Client


account_sid = ''
auth_token = ""
api_key = ""
latitude = 
longitude = 

will_rain = False

response = requests.get(url=f"https://api.openweathermap.org/data/2.5/forecast?lat={latitude}&lon={longitude}&appid={api_key}")
response.raise_for_status()
weather_data = response.json()
weather_list = weather_data["list"][0:5]
for weather in weather_list:
   condition_code = weather['weather'][0]['id']
   if int(condition_code) < 700:
      will_rain = True

if will_rain:
   client = Client(account_sid, auth_token)
   message = client.messages \
      .create(
      body="It's going to rain today. Remember to take your ☂️",
      from_='+18885966435',
      to='+16462406720'
   )
   print(message.status)
