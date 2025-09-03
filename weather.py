import requests
import os
from dotenv import load_dotenv

# API configuration
load_dotenv()
api_key = os.getenv("OPENWEATHER_KEY")
user_cn = str(input("Type the country name: "))
user_sc = str(input("Type the state code: "))
user_cc = str(input("Type the country code: "))

def fetch_json(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error fetching data: {response.status_code}")
            return None
    except Exception as e:
        print(f"Error: {e}")
        return None

 
def get_location(country_name, state_code, country_code, api_key):
    url = f"http://api.openweathermap.org/geo/1.0/direct?q={country_name},{state_code},{country_code}&appid={api_key}&limit=1"
    data = fetch_json(url)
    if data is None:
        print("Request failed")
        return None
    if len(data) == 0:
        print(f"No location found for {country_name}, {state_code}, {country_code}")
        return None
    return {"lat": data[0]["lat"], "lon": data[0]["lon"]}
    
def get_weather(lat, lon, api_key):
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}&units=metric"
    data = fetch_json(url)
    if not data:
        return None
    return data

def main():
    local = get_location(user_cn, user_sc, user_cc, api_key)
    if not local:
        print("Location not found")
        return None
    weather = get_weather(local["lat"], local["lon"], api_key)
    if not weather:
        print("No weather data available")
        return None
    for k, v in weather["main"].items():
        if isinstance(v, (int, float)):
            color = "\033[34m" if v < 21 else "\033[31m"
        else:
            color = "\033[33m"
        print(f"{k}: {color}{v}\033[m")

if __name__ == "__main__":
    main()