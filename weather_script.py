import requests

API_KEY = '87657b969cd8d7d7eaef219391ee45ab'  # Your API key kept in code
BASE_URL = 'https://api.openweathermap.org/data/2.5/weather'

def get_weather(city_name):
    params = {
        'q': city_name,
        'appid': API_KEY,
        'units': 'metric'
    }
    try:
        response = requests.get(BASE_URL, params=params, timeout=5)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Network or HTTP error: {e}")
        return None

    data = response.json()
    # Handle city-not-found or other API errors
    if data.get('cod') != 200:
        msg = data.get('message', 'Unknown error.')
        print(f"Error fetching weather: {msg.capitalize()}")
        return None

    weather_desc = data['weather'][0].get('description', 'N/A')
    temp = data['main'].get('temp', 'N/A')
    humidity = data['main'].get('humidity', 'N/A')
    wind_speed = data.get('wind', {}).get('speed', 'N/A')

    print(f"Weather in {city_name}: {weather_desc}")
    print(f"Temperature: {temp}°C  Humidity: {humidity}%  Wind: {wind_speed} m/s")
    return data

if __name__ == "__main__":
    city = input("Enter city name: ")
    get_weather(city)
