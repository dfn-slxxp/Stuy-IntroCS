def countOddDigits(n):
    n = abs(n)
    if (n < 10):
        return (1 if n % 2 != 0 else 0)
    else:
        return (1 if n % 2 != 0 else 0) + countOddDigits(n // 10)