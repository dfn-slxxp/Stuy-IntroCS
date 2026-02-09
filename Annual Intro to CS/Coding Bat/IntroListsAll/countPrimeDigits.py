def isPrime(n):
    return n in [1, 3, 5, 7]

def countPrimeDigits(n):
    n = abs(n)
    count = 0
    while n > 0:
        count += (1 if isPrime(n % 10) else 0)
        n = n // 10
    return count