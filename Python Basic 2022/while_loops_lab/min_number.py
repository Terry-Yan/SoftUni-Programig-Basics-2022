import sys

entry = input()
min_number = sys.maxsize

while entry != 'Stop':
    if min_number > int(entry):
        min_number = int(entry)

    entry = input()

print(min_number)
