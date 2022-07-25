# use exporting environment variables to keep sensitive data out of code
import requests
from twilio.rest import Client

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"

parameters = {
    "lat": 37.719810,
    "lon": -97.151890,
    # "lat": 41.081444,
    # "lon": -81.519005,
    "appid": api_key,
    "exclude": "current,minutely,daily",
}

response = requests.get(OWM_Endpoint, parameters)
# print(response.status_code)
response.raise_for_status()
data = response.json()
hourly = data["hourly"][:12]
# print(hourly)

weather_ids = []
umbrella = False

for hour in hourly:
    weather_id = hour["weather"][0]["id"]
    weather_ids.append(weather_id)
    if weather_id < 700:
        umbrella = True

# print(weather_ids)

if umbrella:
    # print("Bring an umbrella.")
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It's going to rain today. Remember to bring an ☔.",
        from_="+19706453202",
        to= "+13162183080"
    )

    print(message.status)
