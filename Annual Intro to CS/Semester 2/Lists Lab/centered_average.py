def centered_average(nums):
    maximum = nums[0]
    minimum = nums[0]
    s = 0
    for v in nums:
        minimum = min(v, minimum)
        maximum = max(v, maximum)
        s += v

    return (s - maximum - minimum) / (len(nums) - 2)
