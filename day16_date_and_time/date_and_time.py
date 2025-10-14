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
print(date.timestamp)
today = date.today()
print(f"How much time passed between 1 January 1970 and now {today} - {differ}")
#Ex 6 Think, what can you use the datetime module for? Examples:
# 1 Time series analysis

# 2 To get a timestamp of any activities in an application

# 3 Adding posts on a blog
