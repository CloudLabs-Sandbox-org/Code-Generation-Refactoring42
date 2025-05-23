import requests

def fetch_weather(city_name: str, api_key: str) -> dict:
    """
    Fetch current weather data for a given city from OpenWeatherMap API.

    Args:
        city_name (str): Name of the city.
        api_key (str): Your OpenWeatherMap API key.

    Returns:
        dict: Weather data as returned by the API.
    """
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city_name,
        "appid": api_key,
        "units": "metric"
    }
    response = requests.get(base_url, params=params)
    response.raise_for_status()
    return response.json()

def display_weather_info(weather_data: dict) -> None:
    """
    Display relevant weather information from the API response.
    """
    temp = weather_data['main']['temp']
    humidity = weather_data['main']['humidity']
    condition = weather_data['weather'][0]['description']
    print(f"Temperature: {temp}°C")
    print(f"Humidity: {humidity}%")
    print(f"Conditions: {condition}")

if __name__ == "__main__":
    city = "London"
    api_key = "3e783f1c5de4d888126d68ad91addc24"  # Replace with your valid API key
    data = fetch_weather(city, api_key)
    display_weather_info(data)