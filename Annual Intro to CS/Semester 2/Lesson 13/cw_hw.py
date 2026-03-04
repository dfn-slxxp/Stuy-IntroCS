# Classwork

def firstLast5Squares():
    lst = [i ** 2 for i in range(1,21)]
    print(*lst[0:5], *lst[-5:])


def removeDupes():
    print("Please enter values separated with a new line. Type \"done\" when complete.")
    usr_input = []
    while "done" not in usr_input and "Done" not in usr_input:
        usr_input.append(input())

    usr_input.pop(-1)

    result = []

    for i in range(len(usr_input)):
        if usr_input[i] not in result:
            result.append(usr_input[i])

    print(*result)



# Homework
def noEvens():
    print("Please enter numbers separated with a new line. Type \"done\" when complete.")
    usr_input = []
    while "done" not in usr_input and "Done" not in usr_input:
        usr_input.append(input())

    usr_input.pop(-1)

    numbers = [int(usr_input[i]) for i in range(len(usr_input))]

    result = []
    for num in numbers:
        if num % 2 != 0:
            result.append(num)

    print(*result)