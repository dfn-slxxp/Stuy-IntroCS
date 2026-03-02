def sum_of_range(mi, ma):
    if mi > ma:
        return 0

    s = 0
    for i in range(mi, ma+1):
        s += i

    return s