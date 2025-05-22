"""
school announcements for display on the dashboard.
"""

from datetime import datetime

# announcements can be date speciific or general
announcements = [
    {"date": "2024-05-22", "text": "1st, 2nd, and 6th period Finals Today."},
    {"date": "2024-05-23", "text": "8th, 3rd, and 4th period Finals Today."},
    {"date": None, "text": "1st, 2nd, and 6th period Finals on Thursday."},
    {"date": None, "text": "8th, 3rd, and 4th period Finals on Friday."},
    {"date": None, "text": "7th and 5th period finals on Tuesday next week."},
    {"date": "2024-06-01", "text": "Date-Test"}
]

def get_todays_announcements():
    """
    returns a list of announcements for today (date-specific and general)
    """
    today_str = datetime.now().strftime('%Y-%m-%d')
    todays = [a["text"] for a in announcements if a["date"] == today_str or a["date"] is None]
    return todays 