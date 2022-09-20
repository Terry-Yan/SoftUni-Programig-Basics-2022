speed = float(input())

if speed <= 10.00:
    print('slow')
elif 10.01 <= speed <= 50.00:
    print('average')
elif 50.01 <= speed <= 150.00:
    print('fast')
elif 150.01 <= speed <= 1000.00:
    print('ultra fast')
else:
    print('extremely fast')
