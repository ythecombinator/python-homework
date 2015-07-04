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


  def drawTree(self, n, length, x, y, prevAngle, sizeOfPen):

    if n == 0:
      return

    fun.setpos(x, y)

    fun.pensize(sizeOfPen)

    if sizeOfPen == 1:
      newPenSize = 1

    else:
      newPenSize = sizeOfPen - 1

    fun.pd()

    angle1 = prevAngle + random.randrange(20, 40)
    angle2 = prevAngle - random.randrange(20, 40)

    fun.setheading(angle1)
    fun.forward(length)

    x1 = fun.pos()[0]
    y1 = fun.pos()[1]

    if n == 1:
      fun.dot(4, "#27ae60")

    if n == 2:
      if random.random() <= 0.49:
        fun.dot(2, "#27ae60")
        fun.pu()
        return

    fun.backward(length)
    fun.setheading(angle2)

    fun.forward(length)
    x2 = fun.pos()[0]
    y2 = fun.pos()[1]

    if n == 1:
      fun.dot(2, "#c0392b")

    fun.pu()

    self.drawTree(n - 1, random.uniform(0.70, 0.95) * length, x1, y1, angle1, newPenSize)
    self.drawTree(n - 1, random.uniform(0.70, 0.95) * length, x2, y2, angle2, newPenSize)

window = turtle.Screen()

fun = turtle.Turtle()
