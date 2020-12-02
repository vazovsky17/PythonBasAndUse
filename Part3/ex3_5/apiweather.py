import requests

city = input('City?')
api_url = 'https://api.openweathermap.org/data/2.5/weather'
params = {
    'q': city,
    'appid': 'af8196fcd37295f01e26276b2dda79fc',
    'units': 'metric'
}

res = requests.get(api_url, params=params)
data = res.json()['main']['temp']
print(f'Current temperature in {city} is {data}C')
