import math

def quadratic(a, b, c):
    r1 = (-b + math.sqrt((b ** 2) - (4 * a * c))) / (2 * a)
    r2 = (-b - math.sqrt((b ** 2) - (4 * a * c))) / (2 * a)

    print(f"First root = {r1}")
    print(f"Second root = {r2}")