def factorial(n):
    b = 1 if n < 2 else n
    a = 1
    for i in range(1, b+1):
        a *= i

    print(f"{n} factorial = {a}")
