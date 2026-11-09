import os
import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("WEATHER_API_KEY")

def get_weather(city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    
    print(f"Requesting weather for {city}...")
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        print(data)
    else:
        print(f"Failed to get data. Status code: {response.status_code}")
        
if __name__ == "__main__":
    city_name = input("enter a city name: ")
    get_weather(city_name)