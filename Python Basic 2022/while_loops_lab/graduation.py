student_name = input()
total_score = 0.00
years_counter = 0
failed_years = 0

while True:
    year_score = float(input())
    years_counter += 1

    if year_score < 4.00:
        failed_years += 1
        if failed_years == 2:
            print(f"{student_name} has been excluded at {years_counter} grade")
            break

        years_counter -= 1

    else:
        total_score += year_score

    if years_counter == 12:
        average_score = total_score / 12
        print(f"{student_name} graduated. Average grade: {average_score:.2f}")
        break
