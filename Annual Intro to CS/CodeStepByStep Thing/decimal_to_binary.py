def decimal_to_binary(num):
    if num == 0:
        return 0
    binary_num = ""
    while num > 0:
        remainder = num % 2
        binary_num = str(remainder) + binary_num
        num = num // 2
    return int(binary_num)