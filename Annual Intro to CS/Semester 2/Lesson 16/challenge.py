import turtle, math, random

def random_rgb():
    return (random.randint(100, 255), random.randint(100, 255), random.randint(100, 255))

def draw_hex():
    rose.pd()
    turtle.colormode(255)
    rose.fillcolor(random_rgb())
    rose.begin_fill()
    for i in range(6):
        rose.fd(30)
        rose.rt(60)
    rose.pu()
    rose.end_fill()

def hex_with_number(n):
    draw_hex()
    rose.pu()
    rose.fd(5)
    rose.rt(90)
    rose.fd(15 * math.sqrt(3))
    rose.write(n, align="center", font=("Arial", 12, "normal"))
    rose.bk(15 * math.sqrt(3))
    rose.lt(90)
    rose.bk(5)

def next_hex():
    rose.pu()
    rose.lt(60)
    rose.bk(30)
    rose.lt(60)
    rose.bk(30)
    rose.rt(120)
    rose.pd()

def next_row(num_in_row):
    rose.pu()
    for i in range(num_in_row):
        rose.lt(120)
        rose.fd(30)
        rose.rt(60)
        rose.fd(30)
        rose.rt(60)

    rose.rt(60)
    rose.bk(30)
    rose.lt(60)
    rose.bk(30)
    rose.pd()
    

rose = turtle.Turtle()
rose.speed(0)
rose.pu()
rose.bk(15)
rose.lt(90)
rose.fd(300)

rose.pd()


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

print_pascals_triangle(876)

turtle.done()