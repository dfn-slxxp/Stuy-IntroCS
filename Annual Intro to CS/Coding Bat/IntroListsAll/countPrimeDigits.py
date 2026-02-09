def isPrime(n):
    return n in [1, 3, 5, 7]

def countPrimeDigits(n):
    n = abs(n)
    if (n < 10):
        return (1 if isPrime(n) else 0)
    else:
        return (1 if isPrime(n % 10) else 0) + countPrimeDigits(n // 10)