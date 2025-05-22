"""
school day schedules
dictionary with list with dictionaries inside structured as schedules{day:[{start:time, end:time, name:name}]}
accounts for finals week and the senior assembly
"""

schedules = {
    "Monday": [
        {"start": "07:45", "end": "08:35", "name": "1st Period"}, 
        {"start": "08:41", "end": "09:34", "name": "2nd Period"}, 
        {"start": "09:40", "end": "10:30", "name": "3rd Period"}, 
        {"start": "10:36", "end": "11:26", "name": "4th Period"}, 
        {"start": "11:32", "end": "12:22", "name": "5th Period"}, 
        {"start": "12:28", "end": "13:18", "name": "6th Period"}, 
        {"start": "13:24", "end": "14:14", "name": "7th Period"}, 
        {"start": "14:20", "end": "15:10", "name": "8th Period"}, 
    ],
    "Tuesday": [
        {"start": "07:45", "end": "08:30", "name": "1st Period"}, 
        {"start": "08:35", "end": "09:20", "name": "2nd Period"}, 
        {"start": "09:25", "end": "10:10", "name": "Homeroom/WIN"}, 
        {"start": "10:15", "end": "11:00", "name": "3rd Period"}, 
        {"start": "11:05", "end": "11:50", "name": "4th Period"}, 
        {"start": "11:55", "end": "12:40", "name": "5th Period"}, 
        {"start": "12:45", "end": "13:30", "name": "6th Period"}, 
        {"start": "13:35", "end": "14:20", "name": "7th Period"}, 
        {"start": "14:25", "end": "15:10", "name": "8th Period"}, 
    ],
    "Wednesday": [
        {"start": "09:00", "end": "09:42", "name": "1st Period"}, 
        {"start": "09:47", "end": "10:29", "name": "2nd Period"}, 
        {"start": "10:34", "end": "11:16", "name": "3rd Period"}, 
        {"start": "11:21", "end": "12:03", "name": "4th Period"}, 
        {"start": "12:08", "end": "12:49", "name": "5th Period"}, 
        {"start": "12:54", "end": "13:36", "name": "6th Period"}, 
        {"start": "13:41", "end": "14:23", "name": "7th Period"}, 
        {"start": "14:28", "end": "15:10", "name": "8th Period"}, 
    ],
    "Thursday": [
        {"start": "07:45", "end": "08:30", "name": "1st Period"}, 
        {"start": "08:35", "end": "09:20", "name": "2nd Period"}, 
        {"start": "09:25", "end": "10:10", "name": "Homeroom/WIN"}, 
        {"start": "10:15", "end": "11:00", "name": "3rd Period"}, 
        {"start": "11:05", "end": "11:50", "name": "4th Period"}, 
        {"start": "11:55", "end": "12:40", "name": "5th Period"}, 
        {"start": "12:45", "end": "13:30", "name": "6th Period"}, 
        {"start": "13:35", "end": "14:20", "name": "7th Period"}, 
        {"start": "14:25", "end": "15:10", "name": "8th Period"}, 
    ],
    "Friday": [
        {"start": "07:45", "end": "08:35", "name": "1st Period"}, 
        {"start": "08:41", "end": "09:34", "name": "2nd Period"}, 
        {"start": "09:40", "end": "10:30", "name": "3rd Period"}, 
        {"start": "10:36", "end": "11:26", "name": "4th Period"}, 
        {"start": "11:32", "end": "12:22", "name": "5th Period"}, 
        {"start": "12:28", "end": "13:18", "name": "6th Period"}, 
        {"start": "13:24", "end": "14:14", "name": "7th Period"}, 
        {"start": "14:20", "end": "15:10", "name": "8th Period"}, 
    ],

    "Day 1 Finals": [
        {"start": "07:45", "end": "09:25", "name": "1st Period"}, 
        {"start": "09:35", "end": "11:15", "name": "2nd Period"}, 
        {"start": "11:25", "end": "13:05", "name": "6th Period"}, 
    ],

    "Day 2 Finals": [
        {"start": "07:45", "end": "09:25", "name": "8th Period"}, 
        {"start": "09:35", "end": "11:15", "name": "3rd Period"}, 
        {"start": "11:25", "end": "13:05", "name": "4th Period"}, 
    ],

    "Day 3 Finals": [
        {"start": "07:45", "end": "09:25", "name": "7th Period"}, 
        {"start": "09:35", "end": "11:15", "name": "5th Period"}, 
        {"start": "11:25", "end": "13:05", "name": "Exam Makeup Period"}, 
    ],

    "Assembly": [
        {"start": "07:45", "end": "08:15", "name": "1st Period"}, 
        {"start": "08:19", "end": "08:21", "name": "Homeroom"}, 
        {"start": "08:39", "end": "10:59", "name": "Assembly"}, 
        {"start": "11:10", "end": "11:40", "name": "2nd Period"}, 
        {"start": "11:45", "end": "12:15", "name": "3rd Period"}, 
        {"start": "12:20", "end": "12:50", "name": "4th Period"}, 
        {"start": "12:55", "end": "13:25", "name": "5th Period"}, 
        {"start": "13:30", "end": "14:00", "name": "6th Period"}, 
        {"start": "14:05", "end": "14:35", "name": "7th Period"}, 
        {"start": "14:40", "end": "15:10", "name": "8th Period"}, 
    ]
}

# no school dates (holidays, breaks, etc.)
no_school_dates = {
    "2024-12-25",
} 