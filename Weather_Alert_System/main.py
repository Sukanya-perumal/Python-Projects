import requests
import smtplib
import os
from dotenv import load_dotenv
load_dotenv()

my_email = os.getenv("My_EMAIL")
password = os.getenv("PASSWORD")

api_key = os.getenv("API_KEY")
parameters = {'lat': 38.256081,
              'lon': -85.751572,
              'appid': api_key,
              'cnt': 4,}

response = requests.get(url="http://api.openweathermap.org/data/2.5/forecast",params=parameters)
response.raise_for_status()
print(response.status_code)
weather_data = response.json()
will_rain = False
for hour_data in weather_data['list']:
    condition_code = hour_data['weather'][0]['id']
    if int(condition_code) <700:
        will_rain = True
if will_rain:
    connection = smtplib.SMTP("smtp.gmail.com")
    connection.starttls()
    connection.login(my_email, password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs=my_email,
        msg="subject:Raining Outside \n\n Bring an Umbrella."
    )
