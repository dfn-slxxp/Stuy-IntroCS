import turtle
import shapes

turtle.tracer(0, 0)
coffee = turtle.Turtle()
coffee.pensize(2)
coffee.speed(0)
coffee.pencolor('#ff69b4')

def ts():
    shapes.triangle(coffee, "sky blue")
    coffee.lt(90)
    shapes.square(coffee, "light blue")
    coffee.rt(150)
    shapes.square(coffee, "light blue")
    coffee.fd(50)
    coffee.lt(120)
    shapes.square(coffee, "light blue")
    coffee.rt(90)

    shapes.hexagon(coffee, "#bdc9ff")
    coffee.lt(90)
    coffee.fd(50)
    coffee.lt(30)
    shapes.hexagon(coffee, "#bdc9ff")
    coffee.lt(90)
    coffee.fd(50)
    coffee.lt(30)
    shapes.hexagon(coffee, "#bdc9ff")

    coffee.rt(120)
    coffee.fd(50)
    coffee.rt(30)

def ts2():
    for i in range(15):
        for j in range(6):
            for i in range(6):
                ts()
            coffee.fd(50)
            coffee.rt(30)
            coffee.fd(50)
            coffee.rt(30)
        coffee.fd(50)
        coffee.rt(30)
        coffee.fd(50)
        coffee.lt(60)
        coffee.fd(50)
        coffee.rt(30)


for i in range(5):      
    coffee.goto(-1000, 500 - (235 * i))
    ts2()

turtle.update()
turtle.done()