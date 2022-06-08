import requests
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

API_TOKEN = os.environ.get('API_TOKEN')

url = "http://api.openweathermap.org/data/2.5/weather?q=Odesa,ua&APPID={}".format(API_TOKEN)
response = requests.get(url)
data = response.json()

print('Country:', data.get('sys').get('country'))
print('City:', data.get('name'))
print('Weather:', data.get('weather')[0].get('main'))
print('Temperature:', data.get('main').get('temp'))
print('Wind speed:', data.get('wind').get('speed'))