def create_ngon(n, turt, col):
    turt.pd()
    turt.fillcolor(col)
    turt.begin_fill()
    for i in range(n):
        turt.fd(50)
        turt.rt(360 / n)
    turt.end_fill()
    turt.pu()

def triangle(turt, col):
    create_ngon(3, turt, col)

def square(turt, col):
    create_ngon(4, turt, col)

def hexagon(turt, col):
    create_ngon(6, turt, col)