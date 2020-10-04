import turtle
import time as t


def pythonturtle_work():
    turtle.Screen()
    turtle.bgcolor("blue")
    turtle.penup()
    turtle.goto(0, -363)
    turtle.pendown()
    n = 10
    while True:
        n += 5
        if n == 100:
            t.sleep(5)
        else:
            turtle.circle(n)


pythonturtle_work()
