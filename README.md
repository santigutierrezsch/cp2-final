# 🗓️ School Schedule Dashboard

A clean, daily dashboard web app for students, built with Flask.  
Displays the current date, schedule, time left in the current period, weather outside the school, school announcements, and a motivational quote of the day.

---

## 📸 Features

- **Date display** at the top
- **Class schedule** in the center
- **Live time remaining** for the current period (top-left)
- **Current weather** (bottom-left, uses OpenWeather API)
- **Daily announcements** (right side)
- **Quote of the day** (bottom)

---

## 📁 Project Structure

```
Schedule-Dashboard
├── static
│   ├── style.css                  # CSS styling
│   ├── scripts.js                  # JS functionality
├── templates
│   ├── index.html                 # HTML template for dashboard
├── .env.example                   # Example for required env variables
├── announcements.py               # Manages daily announcements
├── main.py                        # Flask entry point
├── no_school_days.py             # Handles holidays / no-school days
├── quotes.py                      # Handles quote of the day
├── schedule.py                    # Contains bell schedules
```
---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/santigutierrezsch/cp2-final.git
cd schedule-dashboard
````

### 2. Install Dependencies

Make sure you have Python 3 installed.

```bash
pip install flask python-dotenv requests
```

### 3. Setup Environment Variables

Create a `.env` file in the root directory (or rename `.env.example`) with the following content:

```env
OPENWEATHER_API_KEY=your_openweather_api_key_here
```

Get a free API key at [openweathermap.org](https://openweathermap.org/api).

---

## 🏃 Run the App

```bash
python main.py
```

The dashboard will be available at `http://127.0.0.1:5000/`.

---

## 📌 Notes

* This app is designed to be run locally.
* Make sure your system clock is accurate to display the correct time left and schedule.

---

## 📚 Technologies Used

* **Python 3**
* **Flask**
* **HTML / CSS / JS**
* **OpenWeather API**
* **dotenv**
* **requests**
* **datetime**

---

## 🧠 Author & License

Created by Santiago Gutierrez.
Licensed under the MIT License.
