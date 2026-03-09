def sum67(nums):
    c = 0
    count = True
    for i in nums:
        if i == 6:
            count = False
        elif count == False and i == 7:
            count = True
        else:
            c += i if count == True else 0

    return c
