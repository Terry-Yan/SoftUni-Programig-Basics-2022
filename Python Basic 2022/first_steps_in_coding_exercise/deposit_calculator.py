deposit = float(input())
duration = int(input())
interest = float(input())/100

final_deposit = deposit + duration * ((deposit*interest)/12)

print(final_deposit)
