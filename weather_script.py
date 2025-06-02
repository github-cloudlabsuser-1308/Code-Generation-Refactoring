import os
import requests
import tkinter as tk
from tkinter import messagebox

API_KEY = os.getenv('OPENWEATHER_API_KEY')
if not API_KEY:
    raise ValueError('API key not found. Please set the OPENWEATHER_API_KEY environment variable.')

BASE_URL = 'https://api.openweathermap.org/data/2.5/weather'

def get_weather(city_name):
    """Fetch weather data for a given city from OpenWeatherMap API."""
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
    if data.get('cod') != 200:
        msg = data.get('message', 'Unknown error.')
        print(f"Error fetching weather: {msg.capitalize()}")
        return None
    return data

def format_weather(data, city_name):
    """Format weather data for display."""
    weather_desc = data['weather'][0].get('description', 'N/A')
    temp = data['main'].get('temp', 'N/A')
    humidity = data['main'].get('humidity', 'N/A')
    wind_speed = data.get('wind', {}).get('speed', 'N/A')
    return (
        f"Weather in {city_name}: {weather_desc}\n"
        f"Temperature: {temp}°C\n"
        f"Humidity: {humidity}%\n"
        f"Wind: {wind_speed} m/s"
    )

def show_weather():
    city = city_entry.get().strip()
    if not city:
        messagebox.showwarning('Input Error', 'Please enter a city name.')
        return
    # Allow letters, spaces, hyphens, and apostrophes in city names
    import re
    if not re.match(r"^[A-Za-z\s\-']+$", city):
        messagebox.showerror('Input Error', 'City name should only contain letters, spaces, hyphens, or apostrophes.')
        result_label.config(text='')
        return
    data = get_weather(city)
    if data:
        result = format_weather(data, city)
        result_label.config(text=result)
    else:
        messagebox.showerror('City Not Found', f'Could not fetch weather data for "{city}". Please check the city name and try again.')
        result_label.config(text='')

if __name__ == "__main__":
    root = tk.Tk()
    root.title('Weather App')
    root.geometry('400x260')
    root.configure(bg='#e0f7fa')

    title_label = tk.Label(root, text='Weather App', font=('Arial', 18, 'bold'), bg='#e0f7fa', fg='#00796b')
    title_label.pack(pady=(15, 5))

    input_frame = tk.Frame(root, bg='#e0f7fa')
    input_frame.pack(pady=5)

    city_label = tk.Label(input_frame, text='Enter city name:', font=('Arial', 12), bg='#e0f7fa')
    city_label.pack(side='left', padx=(0, 8))
    city_entry = tk.Entry(input_frame, width=22, font=('Arial', 12))
    city_entry.pack(side='left')

    get_btn = tk.Button(
        root, text='Get Weather', command=show_weather,
        font=('Arial', 12, 'bold'), bg='#4dd0e1', fg='white',
        activebackground='#00bcd4', activeforeground='white', relief='raised', bd=2
    )
    get_btn.pack(pady=10)

    result_label = tk.Label(root, text='', justify='left', font=('Arial', 12), bg='#e0f7fa', fg='#004d40')
    result_label.pack(pady=10, fill='both', expand=True)

    root.mainloop()
