def MinOddValue(nums):
    v = 999999999999999999999999999
    for value in nums:
        if value < v and value % 2 != 0:
            v = value

    return v
