def make_pi():
    return [3,1,4]

def changeToSeven(nums):
    nums[1] = 7
    return nums

def same_first_last(nums):
    return False if len(nums) < 1 else  True if nums[0] == nums[-1] else False

def common_end(a, b):
    return True if a[0] == b[0] or a[-1] == b[-1] else False

def has23(nums):
  return True if 2 in nums or 3 in nums else False

def count_evens(nums):
    count = 0
    for val in nums:
        count += 1 if val % 2 == 0 else 0
    return count

def MinOddValue(nums):
    v = 999999999999999999999999999
    for value in nums:
        if value < v and value % 2 != 0:
            v = value

    return v

def ReplaceNegative(nums):
    for i in range(len(nums)):
        if nums[i] < 0:
            nums[i] = nums[i] * -2

    return nums

def big_diff(nums):
    minimum = nums[0]
    for v in nums:
        minimum = min(v, minimum)

        
    maximum = nums[0]
    for v in nums:
        maximum = max(v, maximum)

    return maximum - minimum

def centered_average(nums):
    maximum = nums[0]
    minimum = nums[0]
    s = 0
    for v in nums:
        minimum = min(v, minimum)
        maximum = max(v, maximum)
        s += v

    return (s - maximum - minimum) / (len(nums) - 2)

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

def has22(nums):
    if len(nums) < 2:
        return False
    for i in range(1, len(nums)):
        if nums[i] == 2 and nums[i - 1] == 2:
            return True
        
    return False

def makeSentence(words):
    if len(words) == 0:
        return ""
    if len(words) == 1:
        return words[0]

    w = words[0]
    for word in words[1:]:
        w = w + " " + word

    return w

def breakSentence(s):
    words = []
    w = ""
    for char in s:
        if char == " ":
            words.append(w)
            w = ""
        else:
            w = w + char
    if w != "":
        words.append(w)

    return words
    