points = int(input())
bonus_points = 0.00

if points <= 100:
    bonus_points = 5
elif 101 <= points <= 999:
    bonus_points = points * 0.20
elif points >= 1000:
    bonus_points = points * 0.10

if points % 2 == 0:
    bonus_points += 1
elif points % 10 == 5:
    bonus_points += 2

print(bonus_points)
print(points + bonus_points)
