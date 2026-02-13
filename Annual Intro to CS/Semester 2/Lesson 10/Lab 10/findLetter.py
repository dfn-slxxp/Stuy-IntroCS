def findLetter(str, l):
    for i in range(len(str)):
        if str[i] == l:
            return i
        
    return -1