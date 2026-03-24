import turtle as ts

ts.speed(0)

def create_ngon(n):
    for i in range(n):
        ts.fd(50)
        ts.rt(360 / n)

ts.pu()
ts.goto(-100, 100)
ts.pd()
create_ngon(4)
ts.pu()
ts.goto(100, 100)

ts.pd()
create_ngon(3)
ts.pu()

ts.goto(-100, -100)
ts.pd()
for i in range(5):
    ts.fd(70)
    ts.rt(144)

ts.pu()
ts.goto(100, -100)
ts.pd()
ts.color("blue")

x = 1
while True:
    ts.fd(x)
    ts.rt(144)
    x += 3

ts.done()