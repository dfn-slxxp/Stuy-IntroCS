def readFile(fileName):
    file = open(f'{fileName}.txt')
    text = file.read().split("\n")

    students = [student.split() for student in text]
    for i in range(len(students)):
        for j in range(1, len(students[i])):
            students[i][j] = int(students[i][j])

    return students

# 2
def studentAverageDropLowest():
    grades = readFile("data")

    for student in grades:
        min_grade = 1
        for i in range(1, len(student)):
            min_grade = min_grade if student[min_grade] < student[i] else i

        student.pop(min_grade)

        sum = 0
        for grade in student[1:]:
            sum += grade
        average = sum / (len(student) - 1)

        print(f"{student[0]} has an average of {average} after drop")

studentAverageDropLowest()

# 3
def compareAverages():
    grades = readFile("data")

    averages = []
    for student in grades:
        sum = 0
        for grade in student[1:]:
            sum += grade
        average = sum / (len(student) - 1)

        min_grade = 1
        for i in range(1, len(student)):
            min_grade = min_grade if student[min_grade] < student[i] else i

        student.pop(min_grade)

        sum = 0
        for grade in student[1:]:
            sum += grade
        average_after_drop = sum / (len(student) - 1)

        print(f"{student[0]} has an average of {average}. After drop, {student[0]} has an average of {average_after_drop}")

compareAverages()