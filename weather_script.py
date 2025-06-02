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

def show_weather():
    city = city_entry.get()
    if not city:
        messagebox.showwarning('Input Error', 'Please enter a city name.')
        return
    data = get_weather(city)
    if data:
        weather_desc = data['weather'][0].get('description', 'N/A')
        temp = data['main'].get('temp', 'N/A')
        humidity = data['main'].get('humidity', 'N/A')
        wind_speed = data.get('wind', {}).get('speed', 'N/A')
        result = f"Weather in {city}: {weather_desc}\nTemperature: {temp}°C\nHumidity: {humidity}%\nWind: {wind_speed} m/s"
        result_label.config(text=result)
    else:
        result_label.config(text='Could not fetch weather data.')

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

    get_btn = tk.Button(root, text='Get Weather', command=show_weather, font=('Arial', 12, 'bold'), bg='#4dd0e1', fg='white', activebackground='#00bcd4', activeforeground='white', relief='raised', bd=2)
    get_btn.pack(pady=10)

    result_label = tk.Label(root, text='', justify='left', font=('Arial', 12), bg='#e0f7fa', fg='#004d40')
    result_label.pack(pady=10, fill='both', expand=True)

    root.mainloop()
