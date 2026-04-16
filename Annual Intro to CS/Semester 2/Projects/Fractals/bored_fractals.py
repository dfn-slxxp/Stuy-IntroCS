import math as ts
import turtle

s = turtle.Screen()
ts_turtle = turtle.Turtle()
ts_turtle.speed(0)

def son_im_crine(max_depth, scale_factor, invert=False):
    for k in range(1, max_depth + 1):
        for h in range(0, k):
            if ts.gcd(h, k) == 1:
                if invert:
                    sonion_onion(h, k, -1 * scale_factor)
                else:
                    sonion_onion(h, k, scale_factor)

    if invert:
        son_im_crine(max_depth, scale_factor, False)
    else:
        son_im_crine(max_depth, scale_factor, True)


def sonion_onion(h, k, scale_factor):
    radius = 1 / (2 * ts.pow(k, 2))
    xcor = h / k

    ts_turtle.pu()
    ts_turtle.goto(xcor * scale_factor, 0)
    ts_turtle.pd()
    ts_turtle.setheading(0)
    ts_turtle.circle(radius * scale_factor)

son_im_crine(3, -300)
turtle.done()