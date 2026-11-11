import os
import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("WEATHER_API_KEY")

def get_exchange_rate(currency_code):
    url = f"https://v6.exchangerate-api.com/v6/{API_KEY}/latest/USD"
    print(f"Requesting exchange rate for {currency_code}...")
    
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        print("Success! The code works perfectly.")
        rate = data["conversion_rates"].get(currency_code)
        print(f"1 USD = {rate} {currency_code}")
    else:
        print(f"Failed. Status code: {response.status_code}")

if __name__ == "__main__":
    currency = input("Enter a currency code (e.g., UGX): ")
    get_exchange_rate(currency)