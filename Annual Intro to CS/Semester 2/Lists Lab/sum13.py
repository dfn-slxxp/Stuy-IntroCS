def sum13(nums):
    if len(nums) == 0:
        return 0
    if len(nums) == 1:
        return 0 if 13 in nums else nums[0]

    cnt = nums[0] if nums[0] != 13 else 0
    for i in range(1, len(nums)):
        if nums[i] == 13 or nums[i - 1] == 13:
            continue
        else:
            cnt += nums[i]

    return cnt
