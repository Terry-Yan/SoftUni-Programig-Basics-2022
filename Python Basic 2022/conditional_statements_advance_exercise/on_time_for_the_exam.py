start_hour = int(input())
start_minutes = int(input())
arrival_hour = int(input())
arrival_minutes = int(input())
status = ''

start_time = start_hour * 60 + start_minutes
arrival_time = arrival_hour * 60 + arrival_minutes
difference_hours = 0
difference_minutes = arrival_time - start_time
window_time = start_time - 30
# print(start_time)
# print(arrival_time)

if arrival_time > start_time:
    status = 'Late'
    if difference_minutes >= 60:
        difference_hours = difference_minutes // 60
        difference_minutes = difference_minutes % 60
        print(status)
        if 0 <= difference_minutes < 10:
            print(f"{abs(difference_hours)}:0{abs(difference_minutes)} hours after the start")
        else:
            print(f"{abs(difference_hours)}:{abs(difference_minutes)} hours after the start")
    else:
        print(status)
        print(f"{difference_minutes} minutes after the start")
elif arrival_time == start_time:
    status = 'On time'
    print(status)
elif start_time > arrival_time >= window_time:
    status = 'On time'
    print(status)
    print(f"{abs(difference_minutes)} minutes before the start")
elif window_time > arrival_time:
    status = 'Early'
    if abs(difference_minutes) >= 60:
        difference_minutes = abs(difference_minutes)
        difference_hours = difference_minutes // 60
        difference_minutes = difference_minutes % 60
        print(status)
        if 0 <= difference_minutes < 10:
            print(f"{abs(difference_hours)}:0{abs(difference_minutes)} hours before the start")
        else:
            print(f"{abs(difference_hours)}:{abs(difference_minutes)} hours before the start")
    else:
        print(status)
        print(f"{abs(difference_minutes)} minutes before the start")
