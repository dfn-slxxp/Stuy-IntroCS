def grades():
    print("This program reads your scores on homework")
    print("and exams and reports your course grade or")
    print("what score you need on the exam.")
    print("")

    weight1, weight2 = input("Exam weights? ").split()
    weight1, weight2 = int(weight1), int(weight2)

    print("")

    homework_weight = 100 - weight1 - weight2

    print(f"Homework (weight {homework_weight}):")

    num_hw = int(input("Number of assignments? "))
    homework_grades = []
    for i in range(num_hw):
        score_and_max_str = input(f"Assignment {i + 1} score and max? ").split()
        score_and_max = [int(score_and_max_str[i]) for i in range(2)]

        homework_grades.append(score_and_max)

    sections_attended = int(input("Sections attended? "))
    section_points = 3 * sections_attended
    if section_points > 20:
        section_points = 20

    print(f"Section points = {section_points} / 20")

    homework_score = section_points
    total_hw_score = 20
    for score_and_max in homework_grades:
        homework_score += score_and_max[0]
        total_hw_score += score_and_max[1]
    
    if homework_score > total_hw_score:
        homework_score = total_hw_score
    print(f"Total points = {homework_score} / {total_hw_score}")

    weighted_hw_score = round((homework_weight / 100) * (homework_score / total_hw_score) * 100, 1)
    print(f"Weighted score = {weighted_hw_score}")
    print("")


    print(f"Exam (weight {weight1}):")
    exam_1_score = int(input("Score? "))
    exam_1_curve = int(input("Curve? "))
    ex_1_total = exam_1_score + exam_1_curve
    if ex_1_total > 100:
        ex_1_total = 100
    print(f"Total points = {ex_1_total} / 100")

    weighted_ex1_score = round((ex_1_total / 100) * (weight1 / 100) * 100, 1)
    print(f"Weighted score = {weighted_ex1_score}")
    print("")


    taken_final = int(input("Have you taken the final? (1=yes, 2=no) "))
    if taken_final == 1:
        print(f"Exam (weight {weight2}):")
        exam_2_score = int(input("Score? "))
        exam_2_curve = int(input("Curve? "))
        ex_2_total = exam_2_score + exam_2_curve
        if ex_2_total > 100:
            ex_2_total = 100
        print(f"Total points = {ex_2_total} / 100")
        
        weighted_ex2_score = round((ex_2_total / 100) * (weight2 / 100) * 100, 1)
        print(f"Weighted score = {weighted_ex2_score}")
        print("")


        print(f"Course grade = {weighted_hw_score + weighted_ex1_score + weighted_ex2_score}")
    else:
        desired_percentage = int(input("Desired percentage? "))
        if (weighted_ex1_score + weighted_hw_score > desired_percentage):
            score_needed = 0.0
        else:
            weighted_hw_raw = (homework_weight / 100) * (homework_score / total_hw_score) * 100
            weighted_ex1_raw = (ex_1_total / 100) * weight1
            score_needed = round((desired_percentage - weighted_hw_raw - weighted_ex1_raw) / (weight2 / 100), 1)

    
        print(f"Score needed = {score_needed}")

        if score_needed > 100:
            print("Sorry, it is impossible to earn this score.")
            max_score = round(weight2 + weighted_ex1_score + weighted_hw_score, 2)
            print(f"The highest percentage you can get is {max_score}.")


def main3():
    grades()

def main2():
    main3()

def main():
    main2()

main()