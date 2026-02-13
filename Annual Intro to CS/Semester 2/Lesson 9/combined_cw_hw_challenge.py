# Classwork

def upperLower():
    s = input("Enter a string: ")
    print(s.upper(), s.lower(), sep="\n")



# Homework

def capFirstLast(s):
    return s[0].upper() + s[1:-1] + s[-1].upper()

def swaCase(s):
    return s.swapcase()


# Challenge

def upperIfUpper(s):
    count = 0
    for i in range(4):
        count += 1 if s[i].isupper() else 0
    return s.upper() if count >= 2 else s