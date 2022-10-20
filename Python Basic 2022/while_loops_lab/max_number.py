import sys

entry = input()
max_number = -sys.maxsize

while entry != 'Stop':
    if max_number <= int(entry):
        max_number = int(entry)

    entry = input()

print(max_number)
