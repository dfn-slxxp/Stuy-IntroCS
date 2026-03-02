import random

def random_over(n, m):
    while True:
        rand = random.randint(0, m)
        print(f"Random number: {rand}")
        if rand >= n:
            break