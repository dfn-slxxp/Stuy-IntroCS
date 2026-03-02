import random

def print_random(n):
    for i in range(1, n+1):
        print(f"number {i} : {random.randint(1, 10)}")