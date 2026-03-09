def ReplaceNegative(nums):
    for i in range(len(nums)):
        if nums[i] < 0:
            nums[i] = nums[i] * -2

    return nums
