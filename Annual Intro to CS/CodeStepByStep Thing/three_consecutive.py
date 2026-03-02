def three_consecutive(a, b, c):
    return min(a,b,c) + 2 == max(a,b,c) and min(a,b,c) + 1 == (a+b+c-max(a,b,c)-min(a,b,c))

