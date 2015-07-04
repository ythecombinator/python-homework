import turtle
import random

class FractalTree():

  def __init__(self, n):

    turtle.title("Some Nights")
    turtle.mode("logo")
    turtle.bgcolor("#2c3e50")
    fun.speed(10)
    fun.color("#825a2c")
    fun.pensize(10)
    fun.pu()
    fun.backward(300)
    fun.pd()
    fun.forward(100)
    fun.pu()
    fun.tracer(200)
    self.drawTree(n, 60, 0, -200, 0, 10)

    fun.width(1)
    fun.penup()
    fun.goto(-150, 100)
    for i in range(0, 10):
        for j in range(0,10):
            fun.color("#ecf0f1")
            fun.pendown()
            self.drawSnowflake((i+j)%3+1,2)
            fun.penup()
            fun.setheading(90)
            fun.forward(30)
        fun.setheading(270)
        fun.forward(300)
        fun.setheading(180)
        fun.forward(50)

    window.exitonclick()

window = turtle.Screen()

fun = turtle.Turtle()
