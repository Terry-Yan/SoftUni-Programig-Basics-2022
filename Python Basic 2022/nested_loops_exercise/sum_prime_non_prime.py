prime_sum = 0
non_prime_sum = 0
command = input()

while command != 'stop':
    number = int(command)

    if int(number) < 0:
        print("Number is negative.")
        command = input()
        continue

    count = 0

    for i in range(2, number + 1):
        if number % i == 0:
            count += 1

    if count > 1:
        non_prime_sum += number
    else:
        prime_sum += number

    command = input()

print(f"Sum of all prime numbers is: {prime_sum}")
print(f"Sum of all non prime numbers is: {non_prime_sum}")
