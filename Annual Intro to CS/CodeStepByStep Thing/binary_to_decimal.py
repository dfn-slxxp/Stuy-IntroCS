def binary_to_decimal(binary_string):
    binary_string = str(binary_string)
    decimal_value = 0
    power = 0
    for digit in reversed(binary_string):
        if digit == '1':
            decimal_value += int(digit) * (2 ** power)
        power += 1
    return decimal_value