hours = int(input())
minutes = int(input())

future_minutes = minutes + 15

if future_minutes > 59:
    minutes = future_minutes % 60
    hours += 1
else:
    minutes = future_minutes

if hours > 23:
    hours = hours % 24

if minutes < 10:
    print(f'{hours}:0{minutes}')
else:
    print(f'{hours}:{minutes}')
