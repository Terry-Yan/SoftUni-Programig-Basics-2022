name_of_actor = input()
actor_academy_points = float(input())
number_of_judges = int(input())

for i in range(number_of_judges):
    judge_name = input()
    judge_points = float(input())
    actor_academy_points += (len(judge_name) * judge_points) / 2

    if actor_academy_points > 1250.5:
        print(f"Congratulations, {name_of_actor} got a nominee for leading role with {round(actor_academy_points, 1)}!")
        break

if actor_academy_points <= 1250.5:
    diff = round(1250.5 - actor_academy_points, 1)
    print(f"Sorry, {name_of_actor} you need {diff} more!")
