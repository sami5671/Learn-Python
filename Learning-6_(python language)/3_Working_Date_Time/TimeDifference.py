import datetime

date1 = datetime.datetime(2024, 9 , 1)
date2 = datetime.datetime(2023, 9 , 2)

difference = date1 - date2
print(difference)

new_date = date1 + datetime.timedelta(days=10)

print(new_date)