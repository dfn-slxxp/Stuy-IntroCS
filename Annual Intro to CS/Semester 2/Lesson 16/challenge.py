import turtle, math, random

def random_rgb():
    return (random.randint(0, 150), random.randint(0, 150), random.randint(0, 150))

def draw_hex():
    t.pd()
    turtle.colormode(255)
    t.fillcolor(random_rgb())
    t.begin_fill()
    for i in range(6):
        t.fd(30)
        t.rt(60)
    t.pu()
    t.end_fill()

def hex_with_number(n):
    draw_hex()
    t.pu()
    t.fd(5)
    t.rt(90)
    t.fd(15 * math.sqrt(3))
    t.write(n, align="center", font=("Arial", 12, "normal"))
    t.bk(15 * math.sqrt(3))
    t.lt(90)
    t.bk(5)

def next_hex():
    t.pu()
    t.lt(60)
    t.bk(30)
    t.lt(60)
    t.bk(30)
    t.rt(120)
    t.pd()

def next_row(num_in_row):
    t.pu()
    for i in range(num_in_row):
        t.lt(120)
        t.fd(30)
        t.rt(60)
        t.fd(30)
        t.rt(60)

    t.rt(60)
    t.bk(30)
    t.lt(60)
    t.bk(30)
    t.pd()
    

t = turtle.Turtle()
t.speed(0)
t.pu()
t.bk(15)
t.lt(90)
t.fd(300)

t.pd()


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
        len_row = len(row)
        for value in row:
            hex_with_number(value)
            next_hex()
        next_row(len_row)

print_pascals_triangle(11)

turtle.done()