def count_evens(nums):
    count = 0
    for val in nums:
        count += 1 if val % 2 == 0 else 0
    return count
