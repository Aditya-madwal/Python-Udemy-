print("Date and Time module!")

import datetime as dt
# just to shorten the name

current_time = dt.datetime.now() 
# gets the exact year-month-date hrs:min:sec.milisec (accurately)
print(current_time)

current_year = current_time.year
current_month = current_time.month
current_date = current_time.date
current_day = current_time.weekday()

# for python
# monday = 0
# tuesday = 1
# wednesday = 2
# thursday = 3
# friday = 4
# saturday = 5
# sunday = 6


print(f"date = {current_date}, month = {current_month}, year = {current_year}, week day = {current_day}")

if current_day == 0 :
    current_day = "Monday"
elif current_day == 1 :
    current_day = "Tuesday"
elif current_day == 2:
    current_day = "Wednesday"

print(f"today is {current_day}")

