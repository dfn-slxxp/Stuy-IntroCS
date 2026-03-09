def big_diff(nums):
    minimum = nums[0]
    for v in nums:
        minimum = min(v, minimum)

        
    maximum = nums[0]
    for v in nums:
        maximum = max(v, maximum)

    return maximum - minimum
