import os
import requests
import datetime
import re
from dotenv import load_dotenv

load_dotenv() # Load .env file

def weather_check(func): # Decorator
    def wrapper(*args, **kwargs):
        print(f"Checking environment at {datetime.datetime.now()}...")
        return func(*args, **kwargs)
    return wrapper

class World:
    def __init__(self, lat=45.5, lon=-122.6):
        self.lat = lat
        self.lon = lon

    @weather_check
    def get_humidity(self):
        # Open-Meteo's free endpoint
        url = "https://api.open-meteo.com/v1/forecast"
        
        # Set coordinates (e.g., 45.5, -122.6 for Portland) and request 'relative_humidity_2m'
        params = {
            "latitude": self.lat,
            "longitude": self.lon,
            "current": "relative_humidity_2m",
            "timezone": "auto"
        }
        
        try:
            # Make the actual request
            response = requests.get(url, params=params, timeout=10)
            response.raise_for_status() # Raise error for bad status codes
            
            data = response.json()
            # Extract current humidity from the 'current' key
            return data["current"]["relative_humidity_2m"]
            
        except Exception as e:
            print(f"API Error: {e}. Falling back to default.")
            return 85 # Safe fallback if the internet or API is down