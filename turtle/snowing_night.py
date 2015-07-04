import turtle
import random

class FractalTree():

  def __init__(self, n):

    turtle.mode("logo")
    turtle.bgcolor("")
    turtle.speed(10)
    turtle.color("")
    turtle.pensize(10)
    turtle.pu()
    turtle.backward(300)
    turtle.pd()
    turtle.forward(100)
    turtle.pu()
    turtle.tracer(200)
    self.drawTree(n, 60, 0, -200, 0, 10)

    turtle.width(1)
    turtle.penup()
    turtle.goto(-150, 100)
    for i in range(0, 10):
        for j in range(0,10):
            turtle.color("")
            turtle.pendown()
            self.drawSnowflake((i+j)%3+1,2)
            turtle.penup()
            turtle.setheading(90)
            turtle.forward(30)
        turtle.setheading(270)
        turtle.forward(300)
        turtle.setheading(180)
        turtle.forward(50)

    window.exitonclick()


window = turtle.Screen()
