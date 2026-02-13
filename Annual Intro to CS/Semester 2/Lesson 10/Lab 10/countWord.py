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
