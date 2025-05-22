import os
from dotenv import load_dotenv
from flask import Flask, render_template
from datetime import datetime, timedelta
import requests
from schedule import *
from quotes import get_daily_quote
from no_school_days import no_school_dates
from announcements import get_todays_announcements

#load .env environment variables (protects api key i dont wanna lose money from this)
load_dotenv()

app = Flask(__name__)

def get_today_schedule():
    today = datetime.now().strftime('%A')
    today_str = datetime.now().strftime('%Y-%m-%d')
    
    if today in ["Saturday", "Sunday"]:
        return "No School Today - Weekend", []
    elif today_str in no_school_dates:
        return "No School Today", []
    else:
        return "Today's Schedule", schedules.get(today, [])

def calculate_time():
    now = datetime.now()
    schedule_title, today_schedule = get_today_schedule()

    if not today_schedule:
        return schedule_title, "--:--"
    
    for period in today_schedule:
        start_time = datetime.strptime(period["start"], "%H:%M")
        end_time = datetime.strptime(period["end"], "%H:%M")
        start_time = start_time.replace(year=now.year, month=now.month, day=now.day)
        end_time = end_time.replace(year=now.year, month=now.month, day=now.day)

        if start_time <= now < end_time:
            remaining_time = end_time - now
            minutes = int(remaining_time.total_seconds() // 60)
            seconds = int(remaining_time.total_seconds() % 60)
            time_str = f"{minutes:02d}:{seconds:02d}"
            period_name = period["name"]
            period["current"] = True
            return f"Time left until {period_name} ends:", time_str

        elif now < start_time:
            remaining_time = start_time - now
            minutes = int(remaining_time.total_seconds() // 60)
            seconds = int(remaining_time.total_seconds() % 60)
            time_str = f"{minutes:02d}:{seconds:02d}"
            period_name = period["name"]
            return f"Next period ({period_name}) starts in:", time_str

    return "School is over for today!", "--:--"

def get_weather():
    API_KEY = os.getenv("OPENWEATHERMAP_API_KEY")
    url = f"http://api.openweathermap.org/data/2.5/weather?zip=60563,us&appid={API_KEY}&units=imperial"
    
    try:
        response = requests.get(url)
        data = response.json()
        
        weather_description = data['weather'][0]['description'].lower()
        temp = round(data['main']['temp'], 1)  # Keep one decimal place
        wind_speed = data['wind']['speed']
        precipitation = data.get('rain', {}).get('1h', 0)

        weather_emoji = {
            "clear sky": "☀️",
            "few clouds": "🌤️",
            "scattered clouds": "🌥️",
            "broken clouds": "☁️",
            "shower rain": "🌦️",
            "rain": "🌧️",
            "thunderstorm": "⛈️",
            "snow": "🌨️",
            "mist": "🌫️"
        }.get(weather_description, "☁️")

        # Always return in Fahrenheit - client-side JS will handle conversion if needed
        return f"{weather_emoji} {temp}°F, 🌬️ {wind_speed} mph, 💧 {precipitation} mm"
    except Exception as e:
        # default for if the api key stops working
        return "☁️ Weather data unavailable"

@app.route('/')
def index():
    schedule_title, today_schedule = get_today_schedule()
    time_left_title, time_left_display = calculate_time()
    weather = get_weather()
    current_date = datetime.now().strftime('%Y-%m-%d')
    daily_quote = get_daily_quote()
    announcements = get_todays_announcements()
    
    return render_template('index.html', 
                         schedule_title=schedule_title, 
                         schedule=today_schedule, 
                         time_left=time_left_title, 
                         time_left_display=time_left_display, 
                         weather=weather, 
                         current_date=current_date,
                         daily_quote=daily_quote,
                         announcements=announcements)

if __name__ == '__main__':
    app.run(debug=False)