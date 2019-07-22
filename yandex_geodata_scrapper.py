import requests
import pandas as pd

def parser(API_URL, api_key, address):
    response = requests.get(
        API_URL, params=dict(geocode=address, apikey = api_key, format = 'json'))
    if response.status_code != 200:
        return tuple('--')
        
    
    resp = response.json()["response"]
    data = resp["GeoObjectCollection"]["featureMember"]
    if not data:
        return tuple('--')
        
    coordinates = data[0]["GeoObject"]["Point"]["pos"]  # type: str
    return tuple(coordinates.split(" "))

def create_df():
    data = pd.DataFrame({'address': [], 'longitude': [], 'latitude': []})
    return data
def exctract_coordinates(df, col_with_address, data, api_key):
        
    for j in range(1,len(df)):
        geod = parser("https://geocode-maps.yandex.ru/1.x/",api_key, df.loc[j, col_with_address])
        data = data.append({'address': df.loc[j, col_with_address],
                     'longitude': geod[0],
                    'latitude': geod[1]},
                    ignore_index = True
                   )
        
    return data