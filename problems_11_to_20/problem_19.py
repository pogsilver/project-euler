

months = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
          7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}

start_year = 1900
end_year = 2001

sundays = 0
days_counter = 1
for year in range(start_year, end_year):
    # Leap year:
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        months[2] = 29

    for month in range(1, 13):
        days = months[month]
        for day in range(1, days + 1):
            # 1/1/1900 was a Monday, thus days_counter == 7 iff the day is Sunday
            if days_counter == 7 and day == 1 and year != 1900:
                # First day of the month
                sundays += 1
            days_counter = days_counter % 7 + 1

    months[2] = 28

print(sundays)