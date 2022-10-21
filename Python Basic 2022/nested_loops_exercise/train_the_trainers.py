number_of_judges = int(input())
command = input()
presentation_score = 0
total_score = 0
judging_counter = 0

while command != 'Finish':
    for i in range (0, number_of_judges):
        score = float(input())
        presentation_score += score
        judging_counter += 1

    presentation_score_final = presentation_score / number_of_judges
    print(f"{command} - {presentation_score_final:.2f}.")
    total_score += presentation_score
    presentation_score = 0
    command = input()

final_assessment = total_score / judging_counter
print(f"Student's final assessment is {final_assessment:.2f}.")
