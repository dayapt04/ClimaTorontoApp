import requests
import csv
from datetime import datetime, timezone

# Configuración
API_KEY = 'c6185820a6c5cd5977498d9079994b33'
LATITUDE = 43.651070
LONGITUDE = -79.347015
FILE_NAME = 'clima-toronto-hoy.csv'

def get_weather(lat, lon, api):
    URL = f'http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api}'
    response = requests.get(URL)
    return response.json()

def process(json):
    weather_data = {
        'datetime': datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S'),
        'coord_lon': json.get('coord', {}).get('lon', 'N/A'),
        'coord_lat': json.get('coord', {}).get('lat', 'N/A'),
        'weather_id': json.get('weather', [{}])[0].get('id', 'N/A'),
        'weather_main': json.get('weather', [{}])[0].get('main', 'N/A'),
        'weather_description': json.get('weather', [{}])[0].get('description', 'N/A'),
        'weather_icon': json.get('weather', [{}])[0].get('icon', 'N/A'),
        'base': json.get('base', 'N/A'),
        'main_temp': json.get('main', {}).get('temp', 'N/A'),
        'main_feels_like': json.get('main', {}).get('feels_like', 'N/A'),
        'main_temp_min': json.get('main', {}).get('temp_min', 'N/A'),
        'main_temp_max': json.get('main', {}).get('temp_max', 'N/A'),
        'main_pressure': json.get('main', {}).get('pressure', 'N/A'),
        'main_humidity': json.get('main', {}).get('humidity', 'N/A'),
        'main_sea_level': json.get('main', {}).get('sea_level', 'N/A'),
        'main_grnd_level': json.get('main', {}).get('grnd_level', 'N/A'),
        'visibility': json.get('visibility', 'N/A'),
        'wind_speed': json.get('wind', {}).get('speed', 'N/A'),
        'wind_deg': json.get('wind', {}).get('deg', 'N/A'),
        'wind_gust': json.get('wind', {}).get('gust', 'N/A'),
        'clouds_all': json.get('clouds', {}).get('all', 'N/A'),
        'sys_type': json.get('sys', {}).get('type', 'N/A'),
        'sys_id': json.get('sys', {}).get('id', 'N/A'),
        'sys_country': json.get('sys', {}).get('country', 'N/A'),
        'sys_sunrise': json.get('sys', {}).get('sunrise', 'N/A'),
        'sys_sunset': json.get('sys', {}).get('sunset', 'N/A'),
        'timezone': json.get('timezone', 'N/A'),
        'id': json.get('id', 'N/A'),
        'name': json.get('name', 'N/A'),
        'cod': json.get('cod', 'N/A')
    }
    return weather_data

def write2csv(data, csv_filename):
    with open(csv_filename, mode='a', newline='') as file:
        writer = csv.writer(file)

        # Escribo la cabecera si el archivo está vacío
        if file.tell() == 0:
            writer.writerow([
                'datetime', 'coord_lon', 'coord_lat', 'weather_id', 'weather_main', 'weather_description', 'weather_icon',
                'base', 'main_temp', 'main_feels_like', 'main_temp_min', 'main_temp_max', 'main_pressure', 'main_humidity',
                'main_sea_level', 'main_grnd_level', 'visibility', 'wind_speed', 'wind_deg', 'wind_gust', 'clouds_all',
                'sys_type', 'sys_id', 'sys_country', 'sys_sunrise', 'sys_sunset', 'timezone', 'id', 'name', 'cod'
            ])

        writer.writerow([
            data.get('datetime'),
            data.get('coord_lon'),
            data.get('coord_lat'),
            data.get('weather_id'),
            data.get('weather_main'),
            data.get('weather_description'),
            data.get('weather_icon'),
            data.get('base'),
            data.get('main_temp'),
            data.get('main_feels_like'),
            data.get('main_temp_min'),
            data.get('main_temp_max'),
            data.get('main_pressure'),
            data.get('main_humidity'),
            data.get('main_sea_level'),
            data.get('main_grnd_level'),
            data.get('visibility'),
            data.get('wind_speed'),
            data.get('wind_deg'),
            data.get('wind_gust'),
            data.get('clouds_all'),
            data.get('sys_type'),
            data.get('sys_id'),
            data.get('sys_country'),
            data.get('sys_sunrise'),
            data.get('sys_sunset'),
            data.get('timezone'),
            data.get('id'),
            data.get('name'),
            data.get('cod')
        ])

def main():
    print("===== Bienvenido a Toronto Weather =====")
    weather_data = get_weather(lat=LATITUDE, lon=LONGITUDE, api=API_KEY)
    if weather_data.get('cod') != 404:
        processed_data = process(weather_data)
        write2csv(processed_data, FILE_NAME)
    else:
        print("Ciudad no disponible o API KEY no válida")

if __name__ == '__main__':
    main()

