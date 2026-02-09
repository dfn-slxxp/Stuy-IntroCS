def sleep_in(w, v):
    return not w or v

def negate(n):
    return -n

def between(number,a,b):
    return number < b and number > a

def square(n):
    return n ** 2

def funkyCalc(x,y,z):
    return ( 3 * x + .5 * y ) / (2 * z)

def ftoc(f):
    return (f - 32) / 1.8

def isBig(n):
    return n > 10000

def isEven(n):
    return n % 2 == 0

def monkey_trouble(a, b):
    return (a and b) or not (a or b)

def sumDigits(n):
    n = abs(n)
    if n < 10:
        return n
    else:
        return n % 10 + sumDigits(n // 10)
    
def countDigits(n):
    n = abs(n)
    if (n < 10):
        return 1
    else:
        return 1 + countDigits(n // 10)

def countOddDigits(n):
    n = abs(n)
    if (n < 10):
        return (1 if n % 2 != 0 else 0)
    else:
        return (1 if n % 2 != 0 else 0) + countOddDigits(n // 10)

def isPrime(n):
    return n in [1, 3, 5, 7]

def countPrimeDigits(n):
    n = abs(n)
    if (n < 10):
        return (1 if isPrime(n) else 0)
    else:
        return (1 if isPrime(n % 10) else 0) + countPrimeDigits(n // 10)