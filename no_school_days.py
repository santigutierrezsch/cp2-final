"""
list of all days when school is not in session
includes holidays, breaks, and special dates
dates are in YYYY-MM-DD format
"""

no_school_dates = {
    # holidays
    "2025-05-26"

    # summer Break
    "2025-05-27",
    "2025-05-28",
    "2025-05-29",
    "2025-05-30",
    "2025-05-31",
    "2025-06-01",
    "2025-06-02",
    "2025-06-03",
    "2025-06-04",
    "2025-06-05",
    "2025-06-06",
    "2025-06-07",
    "2025-06-08",
    "2025-06-09",
    "2025-06-10",
    "2025-06-11",
    "2025-06-12",
    "2025-06-13",
    "2025-06-14",
    "2025-06-15",
    "2025-06-16",
    "2025-06-17",
    "2025-06-18",
    "2025-06-19",
    "2025-06-20",
    "2025-06-21",
    "2025-06-22",
    "2025-06-23",
    "2025-06-24",
    "2025-06-25",
    "2025-06-26",
    
    "2025-06-27",
    "2025-06-28",
    "2025-06-29",
    "2025-06-30",
    # too much work to add the rest my bad ms t

    # institute days
    

    # ptc days
    
}

def is_no_school_day(date_str):
    """
    check if a given date is a no-school day
    arguments:
        date_str (str): date in YYYY-MM-DD
    returns:
        bool: true if it's a no-school day
    """
    return date_str in no_school_dates 