city = input()
sales = float(input())
commissions = 0.00
flag = True

if city == 'Sofia':
    if 0 <= sales <= 500:
        commissions = sales * 0.05
    elif 500 < sales <= 1000:
        commissions = sales * 0.07
    elif 1000 < sales <= 10000:
        commissions = sales * 0.08
    elif sales > 10000:
        commissions = sales * 0.12
    else:
        flag = False

elif city == 'Varna':
    if 0 <= sales <= 500:
        commissions = sales * 0.045
    elif 500 < sales <= 1000:
        commissions = sales * 0.075
    elif 1000 < sales <= 10000:
        commissions = sales * 0.10
    elif sales > 10000:
        commissions = sales * 0.13
    else:
        flag = False

elif city == 'Plovdiv':
    if 0 <= sales <= 500:
        commissions = sales * 0.055
    elif 500 < sales <= 1000:
        commissions = sales * 0.08
    elif 1000 < sales <= 10000:
        commissions = sales * 0.12
    elif sales > 10000:
        commissions = sales * 0.145
    else:
        flag = False
else:
    flag = False

if flag:
    print(f'{round(commissions,2):.2f}')
else:
    print('error')
