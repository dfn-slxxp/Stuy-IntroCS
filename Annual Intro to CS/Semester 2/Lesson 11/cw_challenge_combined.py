# Classwork

def shiftLetterBy1 (c):
    return chr(ord(c) + 1)

def shiftLetterByN(c, n):
    return chr(ord(c) + n)

def isLowerCase(c):
    return ord(c) >= 97 and ord(c) <= 122

def isDigit(c):
    return ord(c) >= 48 and ord(c) <= 57

def uppercaseLetter(c):
    return chr(ord(c) - 32) if isLowerCase(c) else c

def myUpper(str):
    s = ""

    for c in str:
        s = s + uppercaseLetter(c)

    return s



# Challenge

