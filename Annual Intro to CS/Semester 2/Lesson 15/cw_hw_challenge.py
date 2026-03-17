# Classwork

def fib(n):
    if n <= 2:
        return 1
    return fib(n-1) + fib(n-2)


# Homework

def n_minus_two_sum(n):
    if n <= 0:
        return n
    return n + n_minus_two_sum(n - 2)

def harmonic_sum(n):
    if n == 1:
        return n
    return (1 / n) + harmonic_sum(n - 1)

def approxRad2(n):
    if n == 1:
        return 1
    
    n_minus_one = approxRad2(n - 1)

    return (1 / n_minus_one) + (n_minus_one / 2)

# Challenge

def pascals_triangle(n):
    if n == 1:
        return [[1]]
    
    triangle = pascals_triangle(n - 1)
    last_row = triangle[-1]

    row = [1]
    for i in range(len(last_row) - 1):
        row.append(last_row[i] + last_row[i + 1])
    row.append(1)

    triangle.append(row)
    return triangle

def print_pascals_triangle(rows):
    triangle = pascals_triangle(rows)

    for row in triangle:
        print(*row)

print_pascals_triangle(6)