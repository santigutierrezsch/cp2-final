"""
Collection of motivational quotes for students.
A new quote is shown each day based on the current date.
"""

quotes = [
    "The only way to do great work is to love what you do. - Steve Jobs",
    "Success is not final, failure is not fatal: it is the courage to continue that counts. - Winston Churchill",
    "Believe you can and you're halfway there. - Theodore Roosevelt",
    "Education is the most powerful weapon which you can use to change the world. - Nelson Mandela",
    "The future belongs to those who believe in the beauty of their dreams. - Eleanor Roosevelt",
    "Don't watch the clock; do what it does. Keep going. - Sam Levenson",
    "The only limit to our realization of tomorrow is our doubts of today. - Franklin D. Roosevelt",
    "You are never too old to set another goal or to dream a new dream. - C.S. Lewis",
    "The harder you work for something, the greater you'll feel when you achieve it. - Unknown",
    "Success is the sum of small efforts, repeated day in and day out. - Robert Collier",
    "Your time is limited, don't waste it living someone else's life. - Steve Jobs",
    "The best way to predict your future is to create it. - Abraham Lincoln",
    "Don't let what you cannot do interfere with what you can do. - John Wooden",
    "The only person you are destined to become is the person you decide to be. - Ralph Waldo Emerson",
    "Education is not preparation for life; education is life itself. - John Dewey",
    "The difference between ordinary and extraordinary is that little extra. - Jimmy Johnson",
    "You don't have to be great to start, but you have to start to be great. - Zig Ziglar",
    "The expert in anything was once a beginner. - Helen Hayes",
    "Dream big and dare to fail. - Norman Vaughan",
    "The road to success and the road to failure are almost exactly the same. - Colin R. Davis",
    "Success is walking from failure to failure with no loss of enthusiasm. - Winston Churchill",
    "The only way to do great work is to be passionate about what you do. - Steve Jobs",
    "Your attitude, not your aptitude, will determine your altitude. - Zig Ziglar",
    "The future depends on what you do today. - Mahatma Gandhi",
    "Don't count the days, make the days count. - Muhammad Ali",
    "The best revenge is massive success. - Frank Sinatra",
    "You miss 100% of the shots you don't take. - Wayne Gretzky",
    "The only limit to the height of your achievements is the reach of your dreams and your willingness to work for them. - Michelle Obama",
    "Success is not in what you have, but who you are. - Bo Bennett",
    "The only person you should try to be better than is the person you were yesterday. - Unknown"
]

def get_daily_quote():
    """
    gets a quote from the list of quotes
    uses the day to pick a quote
        """
    from datetime import datetime
    today = datetime.now()
    # Use the day of the year (1-366) to select a quote
    day_of_year = today.timetuple().tm_yday
    # Cycle through the quotes using modulo
    quote_index = (day_of_year - 1) % len(quotes)
    return quotes[quote_index] 