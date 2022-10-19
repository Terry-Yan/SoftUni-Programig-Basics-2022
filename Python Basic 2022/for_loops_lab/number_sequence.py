import sys

n = int(input())
min_value = sys.maxsize
max_value = -sys.maxsize

for i in range(n):
    value = int(input())
    if value > max_value:
        max_value = value
    if value < min_value:
        min_value = value

print(f"Max number: {max_value}")
print(f"Min number: {min_value}")
