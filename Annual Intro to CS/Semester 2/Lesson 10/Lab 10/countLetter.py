def countLetter(str, l):
    count = 0
    for char in str:
        count += 1 if char == l else 0

    return count
