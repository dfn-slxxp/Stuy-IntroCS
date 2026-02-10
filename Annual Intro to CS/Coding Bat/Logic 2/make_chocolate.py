def make_chocolate(small, big, goal):
    if (5 * big + small < goal or goal % 5 > small):
        return -1
    
    if (goal // 5 > big):
        return goal - 5 * big

    return goal % 5