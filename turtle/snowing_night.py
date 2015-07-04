# Here we intend to draw a simple night scene, with a tree and some snowing effect
# It's named "Some Nights" because it raminds me the song from Fun.

# It should use the turtle module
import turtle

# Here we import the randon module because it will be used for generating values in the branches
import random

class someNights():

  def __init__(self, n):

    # The song which inspirates this.
    turtle.title("Some Nights")
    # Mode logo makes positive angles clockwise.
    turtle.mode("logo")
    # Set a dark color for the background.
    turtle.bgcolor("#2c3e50")
    fun.speed(10)
    # Set a the branches' color.
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
            # Set the color of the snowflakes
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

  # The function to draw the tree
  def drawTree(self, n, length, x, y, prevAngle, sizeOfPen):

    # If the counter is now zero, terminate the branch
    if n == 0:
      return

    # Put at x,y
    fun.setpos(x, y)

    # Set the pensize to the new pensize specified by previous recursive call
    fun.pensize(sizeOfPen)

    if sizeOfPen == 1:
      newPenSize = 1

    # If pensize isn't 1 decrease the pensize
    else:
      newPenSize = sizeOfPen - 1

    fun.pd()

    # Left branch
    angle1 = prevAngle + random.randrange(20, 40)

    # Right branch
    angle2 = prevAngle - random.randrange(20, 40)

    fun.setheading(angle1)

    fun.forward(length)
    # x1 is the current x coordinate
    x1 = fun.pos()[0]
    # y1 is the current y coordinate
    y1 = fun.pos()[1]

    # Each leaf has a green dot as a leaf on the tree
    if n == 1:
      fun.dot(4, "#27ae60")

    # 50% of chance that the branch will finish when n = 2
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

    #The recursive calls, which also set the new length of the branch randomly
    self.drawTree(n - 1, random.uniform(0.70, 0.95) * length, x1, y1, angle1, newPenSize)
    self.drawTree(n - 1, random.uniform(0.70, 0.95) * length, x2, y2, angle2, newPenSize)

  # The function used in the function below
  def drawFractal(self, length, depth):
      if depth == 1:
          fun.forward(length)
      else:
          drawFractal(length, depth-1)
      fun.right(60)
      if depth == 1:
          fun.forward(length)
      else:
          drawFractal(length, depth-1)
      fun.left(120)
      if depth == 1:
          fun.forward(length)
      else:
          drawFractal(length, depth-1)
      fun.right(60)
      if depth == 1:
          fun.forward(length)
      else:
          drawFractal(length, depth-1)

  # The function to draw each snowflake
  def drawSnowflake(self, length, depth):
    self.drawFractal(length, depth-1)
    fun.left(120)
    self.drawFractal(length, depth-1)
    fun.left(120)
    self.drawFractal(length, depth-1)

window = turtle.Screen()

fun = turtle.Turtle()

# Define the number of iterations
n = 13

thisNight = someNights(n)
