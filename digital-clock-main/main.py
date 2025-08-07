from tkinter import *
import requests

user_agent = "Daily News App/1.0 (gabeashah@gmail.com)"
headers = {"User-Agent": user_agent}

def get_location_from_ip():
    try:
        resp = requests.get("https://ipinfo.io/json")
        resp.raise_for_status()
        loc = resp.json()["loc"]  # e.g., "37.3860,-122.0838"
        lat, lon = map(float, loc.split(","))
        return lat, lon
    except Exception as e:
        print(f"Could not get location: {e}")
        return None, None

def fetch_weather(lat, lon):
    try:
        points_url = f"https://api.weather.gov/points/{lat},{lon}"
        response = requests.get(points_url, headers=headers)
        response.raise_for_status()
        data = response.json()
        forecast_url = data["properties"]["forecast"]
        forecast_response = requests.get(forecast_url, headers=headers)
        forecast_response.raise_for_status()
        return forecast_response.json()
    except Exception as e:
        print(f"Error fetching weather data: {e}")
        return None

def update_weather(use_geo):
    if use_geo:
        lat, lon = get_location_from_ip()
        if lat is None:
            weather_text.set("Could not get your location")
            return
    else:
        lat, lon = 37.334606, -122.009102  # Default location
    data = fetch_weather(lat, lon)
    if data:
        period = data["properties"]["periods"][0]
        text = f"{period['name']}: {period['temperature']}°{period['temperatureUnit']}, {period['shortForecast']}"
    else:
        text = "Weather unavailable"
    weather_text.set(text)

from time import strftime

root = Tk()
root.title("Clock")

def time():
    string = strftime('%H:%M:%S %p')
    label.config(text=string)
    label.after(1000, time)

label = Label(root, font=("ds-digital", 80), background="lightblue", foreground="white", bd=0, width=30, padx=0, pady=20)
label.pack(anchor="center")

weather_text = StringVar()
weather_label = Label(root, textvariable=weather_text, font=("ds-digital", 24), background="lightblue", foreground="white", bd=0, width=98, padx=0, pady=20)
weather_label.pack(anchor="center")

def toggle_weather():
    global use_geo
    use_geo = not use_geo
    update_weather(use_geo)
    toggle_btn.config(text="Use Default Location" if use_geo else "Use My Location")

use_geo = False
toggle_btn = Button(root, text="Use My Location", command=toggle_weather, font=("Arial", 16))
toggle_btn.pack(anchor="center")

update_weather(use_geo)
time()
mainloop()
# This code creates a simple digital clock and shows the current weather using Tkinter in Python.

