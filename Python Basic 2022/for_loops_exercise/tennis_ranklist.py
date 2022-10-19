import math

number_of_tournaments = int(input())
starting_points = int(input())
tournament_points = 0
win_counter = 0

for _ in range(number_of_tournaments):
    tournament_result = input()

    if tournament_result == 'W':
        tournament_points += 2000
        win_counter += 1

    elif tournament_result == 'F':
        tournament_points += 1200

    elif tournament_result == 'SF':
        tournament_points += 720

final_points = starting_points + tournament_points
average_points = math.floor(tournament_points / number_of_tournaments)
win_percentage = (win_counter / number_of_tournaments) * 100

print(f"Final points: {final_points}")
print(f"Average points: {average_points:.0f}")
print(f"{round(win_percentage, 2):.2f}%")
