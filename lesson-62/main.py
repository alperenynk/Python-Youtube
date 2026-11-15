# Python Dates & Times

import datetime

# date = datetime.date(2025, 1, 2)
# today = datetime.date.today()
# time = datetime.time(12, 30, 0)
# now = datetime.datetime.now()
# now = now.strftime("%H:%M:%S")

# print(date)
# print(today)
# print(time)
# print(now)

target_datetime = datetime.datetime(2025, 1, 2, 12, 30, 0)
current_datetime = datetime.datetime.now()
if current_datetime < target_datetime:
    print("The target date and time is in the future.")
else:
    print("The target date and time has already passed.")
