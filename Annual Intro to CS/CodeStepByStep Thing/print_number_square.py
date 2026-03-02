def print_number_square(mi, ma):
    nums = [i for i in range(mi, ma + 1)]

    if ma < mi:
        return
    
    for i in range(ma - mi + 1):
        for j in range(ma - mi + 1):
            print(nums[(j + i) % len(nums)], end="")
        print("")