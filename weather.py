import requests

# API configuration
api_key = "295fe3b84571983649e6e3bbfed8e9e4"
user_cn = str(input("Type the country name: "))
user_sc = str(input("Type the state code: "))
user_cc = str(input("Type the country code: "))
def get_location(country_name, state_code, country_code, api_key):
    try:
        response = requests.get(f"http://api.openweathermap.org/geo/1.0/direct?q={country_name},{state_code},{country_code}&appid={api_key}&limit=1")
        if response.status_code == 200:
            data = response.json()
            if data:
                lon = data[0]["lon"]
                lat = data[0]["lat"]
                return {"lat": lat, "lon": lon}
            else:
                return "No location found"
        else:
            return f"Error fetching data: {response.status_code}"
    except Exception as e:
        return f"Error: {e}"
    
def get_weather(lon, lat, api_key):
    try:
        response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}&units=metric")
        if response.status_code == 200:
            data = response.json()
            if data:
                return data["main"]
        else:
            return "No weather data"
    except Exception as e:
        return f"Error: {e}"

def main():
    local = get_location(user_cn, user_sc, user_cc, api_key)
    weather = get_weather(local["lon"], local["lat"], api_key)
    for i, j in weather.items():
        print(f"{i}: \033[31m{j}\033[m")
if __name__ == "__main__":
    main()