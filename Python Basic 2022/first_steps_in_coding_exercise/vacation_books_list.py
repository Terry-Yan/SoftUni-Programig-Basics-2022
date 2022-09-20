from math import floor

number_of_pages = int(input())
pages_per_hour = int(input())
number_of_days = int(input())

number_of_hours_per_day = (number_of_pages / pages_per_hour) / number_of_days

print(floor(number_of_hours_per_day))
