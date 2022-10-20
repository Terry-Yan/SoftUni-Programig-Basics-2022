bad_grades = int(input())
bad_grades_counter = 0
task_name = input()
task_grade = int(input())
task_counter = 0
last_task = ''
grades_total = 0

while task_name != 'Enough':
    task_counter += 1
    grades_total += task_grade
    last_task = task_name

    if task_grade <= 4:
        bad_grades_counter += 1

    if bad_grades == bad_grades_counter:
        print(f"You need a break, {bad_grades_counter} poor grades.")
        break

    task_name = input()

    if task_name == "Enough":
        break
    else:
        task_grade = int(input())

if bad_grades != bad_grades_counter:
    average_score = grades_total / task_counter
    print(f"Average score: {average_score:.2f}")
    print(f"Number of problems: {task_counter}")
    print(f"Last problem: {last_task}")
