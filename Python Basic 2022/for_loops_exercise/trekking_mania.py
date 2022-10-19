number_of_groups = int(input())
musala_people = 0
monblan_people = 0
kilimandjaro_people = 0
k2_people = 0
everest_people = 0

for i in range(number_of_groups):
    group_members = int(input())

    if 1 <= group_members <= 5:
        musala_people += group_members
    elif 6 <= group_members <= 12:
        monblan_people += group_members
    elif 13 <= group_members <= 25:
        kilimandjaro_people += group_members
    elif 26 <= group_members <= 40:
        k2_people += group_members
    elif 41 <= group_members:
        everest_people += group_members

total_people = musala_people + monblan_people + kilimandjaro_people + k2_people + everest_people

print(f"{(musala_people / total_people) * 100:.2f}%")
print(f"{(monblan_people / total_people) * 100:.2f}%")
print(f"{(kilimandjaro_people / total_people) * 100:.2f}%")
print(f"{(k2_people / total_people) * 100:.2f}%")
print(f"{(everest_people / total_people) * 100:.2f}%")
