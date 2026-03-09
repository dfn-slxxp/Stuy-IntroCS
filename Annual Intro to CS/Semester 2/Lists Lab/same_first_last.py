def same_first_last(nums):
    return False if len(nums) < 1 else  True if nums[0] == nums[-1] else False
