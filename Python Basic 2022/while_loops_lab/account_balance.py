command_word = input()
balance_total = 0.00

while command_word != 'NoMoreMoney':
    if float(command_word) >= 0:
        balance_total += float(command_word)
        print(f"Increase: {float(command_word):.2f}")
        command_word = input()
    else:
        print("Invalid operation!")
        print(f"Total: {balance_total:.2f}")
        break
else:
    print(f"Total: {balance_total:.2f}")