# Classwork/Homework

def idkWhatToCallThis(input_list):
    counter = 0
    for str in input_list:
        if len(str) > 2:
            counter += 1 if str[0] == str[-1] else 0

    return counter


# Challenge

def circularlyIdentical(list1, list2):
    if len(list1) != len(list2):
        return False
    
    for i in range(len(list1)):
        rot1 = list1[i:] + list1[:i]
        if rot1 == list2:
            return True
        
    return False