def hello_name(name):
    return "Hello " + name + "!"

def make_abba(a, b):
    return a + b + b + a

def make_out_word(out, word):
    return out[:len(out)/2] + word + out[len(out)/2:]

def extra_end(str):
    return str[-2:] + str[-2:] + str[-2:]

def first_two(str):
    return str if len(str) <= 2 else str[0:2]

def without_end(str):
    return str[1:-1]

def left2(str):
    return str[2:] + str[:2]

def countLetter(str, l):
    count = 0
    for char in str:
        count += 1 if char == l else 0

    return count

def findLetter(str, l):
    for i in range(len(str)):
        if str[i] == l:
            return i
        
    return -1

def findWord(str, n):
    for i in range(len(str) - len(n) + 1):
        ts = True
        for j in range(len(n)):
            if (str[i + j] == n[j]):
                continue
            else:
                ts = False
                break
        if ts:
            return i
        
    return -1

def countWord(str, n):
    count = 0
    for i in range(len(str) - len(n) + 1):
        ts = True
        for j in range(len(n)):
            if (str[i + j] == n[j]):
                continue
            else:
                ts = False
                break
        if ts:
            count += 1
        
    return count

def isVowel(c):
    return c.lower() in ["a", "e", "i", "o", "u"]

def countVowels(s):
    count = 0
    for char in s:
        count += 1 if char.lower() in ["a", "e", "i", "o", "u"] else 0
    return count

def noVowels(s):
    st = ""
    for char in s:
        if not char.lower() in ["a", "e", "i", "o", "u"]:
            st = st + char

    return st
