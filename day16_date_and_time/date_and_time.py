from datetime import datetime
now = datetime.now()
print(now)                      # 2021-07-08 07:34:46.549883
day = now.day                   # 8
month = now.month               # 7
year = now.year                 # 2021
hour = now.hour                 # 7
minute = now.minute             # 38
second = now.second
timestamp = now.timestamp()
print(day, month, year, hour, minute)
print('timestamp', timestamp)
print(f'{day}/{month}/{year}, {hour}:{minute}')  # 8/7/2021, 7:38


# current date and time
now = datetime.now()
t = now.strftime("%H:%M:%S")
print("time:", t)
time_one = now.strftime("%m/%d/%Y, %H:%M:%S")
# mm/dd/YY H:M:S format
print("time one:", time_one)
time_two = now.strftime("%d/%m/%Y, %H:%M:%S")
# dd/mm/YY H:M:S format
print("time two:", time_two)


date_string = "5 December, 2019"
print("date_string =", date_string)
date_object = datetime.strptime(date_string, "%d %B, %Y")
print("date_object =", date_object)

from datetime import date
d = date(2020, 1, 1)
print(d)
print('Current date:', d.today())    # 2019-12-05


today = date.today()
print("Current year:", today.year)   # 2019
print("Current month:", today.month) # 12
print("Current day:", today.day)     # 5


from datetime import time
# time(hour = 0, minute = 0, second = 0)
a = time()
print("a =", a)
# time(hour, minute and second)
b = time(10, 30, 50)
print("b =", b)
# time(hour, minute and second)
c = time(hour=10, minute=30, second=50)
print("c =", c)
# time(hour, minute, second, microsecond)
d = time(10, 30, 50, 200555)
print("d =", d)



today = date(year=2019, month=12, day=5)
new_year = date(year=2020, month=1, day=1)
time_left_for_newyear = new_year - today
# Time left for new year:  27 days, 0:00:00
print('Time left for new year: ', time_left_for_newyear)

t1 = datetime(year = 2019, month = 12, day = 5, hour = 0, minute = 59, second = 0)
t2 = datetime(year = 2020, month = 1, day = 1, hour = 0, minute = 0, second = 0)
diff = t2 - t1
print('Time left for new year:', diff) # Time left for new year: 26 days, 23: 01: 00


from datetime import timedelta
t1 = timedelta(weeks=12, days=10, hours=4, seconds=20)
t2 = timedelta(days=7, hours=5, minutes=3, seconds=30)
t3 = t1 - t2
print("t3 =", t3)
print("t3 =", t2)
print("t3 =", t1)

#* Exercises: Day 16
#Ex 1 Get the current day, month, year, hour, minute and timestamp from datetime module
from datetime import datetime
current = datetime.now()
day = current.day
month = current.month
year = current.year
hour = current.hour
minute = current.minute
second = current.second
timestamp = current.timestamp()
print(f"Today is {day}/{month}/{year}. \nCurrent time: {hour}/{minute}/{second}")
print("How much secound passed from 1st January 1970:", timestamp)

#Ex 2 Format the current date using this format: "%m/%d/%Y, %H:%M:%S")
now1 = datetime.now()
format1 = now1.strftime("%m/%d/%Y, %H:%M:%S")
print(format1)

#Ex 3 Today is 5 December, 2019. Change this time string to time.
datestr = '5 December, 2019'
dtime = datetime.strptime(datestr, "%d %B, %Y")
print(dtime)
#Ex 4 Calculate the time difference between now and new year.
today = date(year=2025, month=10, day=14)
new_year = date(year=2026, month=1, day=1)
hmuch = new_year - today
print(hmuch)

#Ex 5 Calculate the time difference between 1 January 1970 and now.
differ = date(day=1, month=1, year=1970)
today = date.today()
print(f"How much time passed between 1 January 1970 and now {today} - {differ}")
#Ex 6 Think, what can you use the datetime module for? Examples:
# 1 Time series analysis
'''
Comparing timestamps, calculating trends, or plotting time-based data.
'''
# 2 To get a timestamp of any activities in an application
'''
You can see how much time did activition in application took to maybe improve time complexity
'''
# 3 Adding posts on a blog
'''
You can track time from when a post was added and track the watchs on post by time 
'''


#* Chat GPT Exercises
#Begginer
from datetime import datetime
currentdt = datetime.now()
print(currentdt)
print(f"Today is {datetime.strftime(currentdt, "%A, %d %B %Y")}")
time1 = datetime.strftime(currentdt, '%H:%M:%S')
if time1 > '12:00:00':
    stime = currentdt.hour - 12
    print(f"{stime}:{datetime.strftime(currentdt,'%M:%S')} PM")
else:
    print(f"{time1} AM")
print(time1)

datestr = "2025-10-15 14:30:00"
dateobj = datetime.strptime(datestr, "%Y-%m-%d %H:%M:%S")
print(dateobj)
ndatestr = datetime.strftime(dateobj, "%d %b %Y, %#I:%M %p")
print(ndatestr)

# Comparing Dates
# Write a program that takes two dates and prints which one comes earlier.
date1 = date(year=2009, month=12, day=5)
date2 = date(year=2000, month=1, day=12)
if date1 < date2:
    print(f'date1: {date1} comes earlier then date2: {date2}')
else:
    print(f'date2: {date2} comes earlier then date1: {date1}')
    
# 🟡 Intermediate Exercises
# Days Until a Given Date
# Ask the user for their next birthday (e.g. "2025-12-10") and calculate how many days are left until that date.
datau = '2026-05-11'# datau = input('Input date of your birthday (e.g. "YYYY-MM-DD") ')
datau = datetime.strptime(datau, "%Y-%m-%d")
datanow = datetime.now()
hmuchis = datau - datanow
print(hmuchis)

# Working with timedelta
# Given a meeting that starts at "2025-10-15 09:00:00" and lasts 2 hours 30 minutes, calculate the end time.
meetdate = datetime(year=2025, month=10, day=15, hour=9, minute=00, second=00)
howlong = timedelta(hours=2, minutes=30)
print(meetdate + howlong)

# Find the Difference Between Two Dates
# Calculate how many days, hours, and minutes have passed since "2020-01-01".
kiedy = datetime(year=2020, month=1, day=1)
now = datanow - kiedy
total_seconds = now.total_seconds()
dni = now.days
godziny = int((total_seconds // 3600) % 24)   # pełne godziny po odjęciu dni
minuty = int((total_seconds // 60) % 60)  
print(f"From {kiedy} passed {dni} days, {godziny} hours and {minuty} minutes")

# Parse Multiple Date Formats
# Write a function that can correctly parse any of the following:
# "2025-10-15"
# "15/10/2025"
# "October 15, 2025"
datestr = "2025-10-15"
def date_changer(date1):
    formats = ["%Y-%m-%d", "%d/%m/%Y", "%B %d, %Y"]
    dateobj = None
    for f in formats:
        try:
            dateobj = datetime.strptime(date1, f)
        except ValueError:
            continue
    if dateobj is None:
        return "Unknown date format"
    else:
        return dateobj
print(date_changer(datestr))

# Generate a List of Dates
# Create a list of all dates between two given dates (inclusive).
dat1 = date(2025,11,5)
dat2 = date(2025,11,10)
times = (dat2 - dat1).days 
a = [dat1 + timedelta(days=i) for i in range(times + 1)]
print(a)
print([d.isoformat() for d in a])

# 🔵 Advanced Exercises
# Week Number and Day of the Year
# Print the current week number (ISO calendar) and the day number of the year.
now = datetime.now()
print(f"Current week number (ISO Callendar): {now.isocalendar().week}")
print(f"Current day number of the year: {now.timetuple().tm_yday}")

#todo Timezone Handling
# Display the current UTC time and convert it to your local timezone (using zoneinfo).
'''
1. get time now in utc
2. get my local timezone
3. sum up utc and my deltatime
'''
from datetime import datetime
import pytz

utc_now = datetime.now(pytz.utc)
local_time = utc_now.astimezone(pytz.timezone("Europe/Warsaw"))

print("UTC:", utc_now)
print("Local:", local_time)


# Next Monday Finder
# Write a function that, given any date, returns the date of the next Monday.
print(50 * '-')
def next_monday(g_date):
    formats = ["%Y-%m-%d", "%d/%m/%Y", "%B %d, %Y"]
    dateobj = None
    for f in formats:
        try:
            dateobj = datetime.strptime(g_date, f)
        except ValueError:
            continue
    days_until_monday = (7 - dateobj.weekday()) % 7
    if days_until_monday == 0:
        days_until_monday = 7

    next_mon = dateobj + timedelta(days=days_until_monday)
    return f"Next Monday will be on: {next_mon.date()}"
print(next_monday("2025-10-19"))
    

# Scheduling Simulation
# Given a list of event times, calculate how many minutes remain until the next event.
from datetime import datetime, timezone

# Given event times (UTC)
event_times = [
    "2025-10-19T10:30:00Z","2025-10-19T14:00:00Z","2025-10-19T18:45:00Z",
    "2025-10-20T09:15:00Z","2025-10-20T16:00:00Z","2025-10-21T08:30:00Z",
    "2025-10-21T12:00:00Z","2025-10-22T07:45:00Z","2025-10-22T18:00:00Z",
    "2025-10-23T10:00:00Z"
]

# Convert string times to datetime (UTC-aware)
date_converted = [datetime.strptime(i, "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=timezone.utc) for i in event_times]

# Get current UTC time
now = datetime.now(timezone.utc)

# Find the next event that’s still upcoming
upcoming = [t for t in date_converted if t > now]

if upcoming:
    next_event = min(upcoming)
    minutes_remaining = int((next_event - now).total_seconds() / 60)
    print(f"Next event: {next_event}")
    print(f"Minutes remaining: {minutes_remaining}")
else:
    print("No upcoming events.")


# Countdown Timer
# Create a live countdown in the terminal for 10 seconds using datetime and time.sleep().
import time
# i = 10
# while i != 0:
#     print(i)
#     i -= 1
#     time.sleep(1)
# print("Time's up!")


# Date Range Filtering
# You have a list of events with timestamps. Filter only those that happened in the past 7 days.
timestamps = ["2025-09-25T11:43:28Z","2025-09-28T05:10:12Z","2025-10-01T19:27:50Z","2025-10-02T08:02:33Z","2025-10-04T22:10:45Z","2025-10-05T14:56:19Z","2025-10-06T23:40:51Z","2025-10-08T09:17:03Z","2025-10-09T03:28:49Z","2025-10-10T18:22:30Z","2025-10-11T07:05:12Z","2025-10-12T20:49:27Z","2025-10-13T15:33:40Z","2025-10-14T09:56:18Z","2025-10-15T23:45:59Z","2025-10-16T10:18:26Z","2025-10-17T04:40:12Z","2025-10-17T22:15:08Z","2025-10-18T19:57:03Z","2025-10-19T06:28:54Z"]
validtimestmaps = []
for timestamp1 in timestamps:
    if datetime.fromisoformat(timestamp1.replace("Z","")) > datanow - timedelta(days=7):
        validtimestmaps.append(timestamp1)
print(validtimestmaps) 


# ⚫ Expert / Real-World Projects
# Employee Attendance Tracker
# Log check-in/check-out times using datetime.now() and calculate total hours worked per day.

# Time Zone Aware Logger
# Automatically tag log entries with the current local time and UTC offset.

# Flight Time Calculator
# Given a departure time in one timezone and an arrival time in another, calculate the total flight duration.

# Recurring Task Generator
# Generate all future occurrences of a weekly meeting for the next 3 months.