import turtle

import colorsys

jagger = turtle.Turtle()

window = turtle.Screen()

turtle.title("She's A Rainbow")

def drawRainbow():

  for i in range(1000):

      color = colorsys.hsv_to_rgb(i/1000.0, 1.0, 1.0)
      jagger.color(color)
      jagger.forward(i)
      jagger.right(98)

  jagger.color("black")
  jagger.hideturtle()
  jagger.penup()
  jagger.setpos((20,5))
  jagger.write("Have you seen her dressed in blue?",True, align="center", font=("Arial", 20, "normal"))

drawRainbow()

window.exitonclick()
