def has22(nums):
    if len(nums) < 2:
        return False
    for i in range(1, len(nums)):
        if nums[i] == 2 and nums[i - 1] == 2:
            return True
        
    return False
