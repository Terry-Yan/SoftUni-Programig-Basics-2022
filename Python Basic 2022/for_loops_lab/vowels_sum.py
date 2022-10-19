word = input()
value = 0

for i in word:
    if i == 'a':
        value += 1
    if i == 'e':
        value += 2
    if i == 'i':
        value += 3
    if i == 'o':
        value += 4
    if i == 'u':
        value += 5

print(value)
