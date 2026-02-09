def countOddDigits(n):
    n = abs(n)
    count = 0
    while n > 0:
        count += (1 if n % 2 != 0 else 0)
        n = n // 10
    return count