import sys
hr = int(input('Enter Hour: '))

if hr > 12:
    print("INVALID TIME ENTERED")
    sys.exit()
am_pm = int(input('AM (1) or PM (2) :'))

if am_pm == 1:
    am_pm = 'AM'
else:
    am_pm = 'PM'

ahead = int(input('How many hours ahead? '))

time_ahead = hr + ahead

if time_ahead > 12 and am_pm == 'AM':
    print(f'New Hour: {time_ahead - 12} PM')
elif time_ahead > 12 and am_pm == 'PM':
    print(f'New Hour: {time_ahead - 12} AM')
elif time_ahead == 12 and am_pm == 'AM':
    print(f'Its Exactly 12 NOON')
elif time_ahead == 12 and am_pm == 'PM':
    print(f'Its Exactly 12 MID NIGHT')


