import turtle as ts

ts.speed(0)

def create_ngon(n, color):
    ts.fillcolor(color)
    ts.color(color)
    ts.begin_fill()
    for i in range(n):
        ts.fd(50)
        ts.rt(360 / n)
    ts.end_fill()

ts.pu()
ts.goto(-150, 0)
ts.pd()
create_ngon(5, "blue")

ts.pu()
ts.goto(0, 0)
ts.pd()
create_ngon(6, "red")

ts.pu()
ts.goto(150, 0)
ts.pd()
create_ngon(8, "orange")

ts.done()