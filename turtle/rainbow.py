# Here we intend to create a simple color effect that gradually change between colors.
# It's named "She's A Rainbow" because it raminds me the song from Rolling Stones

# It should use the turtle module
import turtle

# Here we import the Python's colorsys module which will help us convert HSV values into RGB.

# We could do this in another way by creating a list containing many different colors - reddish,
# orangey, yellowy, greenish, blueish... - each color in a RGB tuple and then, within a loop, choose
# a color from the list.

import colorsys

# Since he's one of the songwriters, he deserves.
jagger = turtle.Turtle()

# We'll use this to exitonclick().
window = turtle.Screen()

# Set a dark color for the background.
turtle.bgcolor("#2c3e50")

# Set the fastest speed
jagger.speed(0)

# The song which inspirates this.
turtle.title("She's A Rainbow")

# The main function
def drawRainbow():

  for i in range(1000):

      # Let's get some cool colors by moving around the upper edge of the HSV cylinder.
      color = colorsys.hsv_to_rgb(i/1000.0, 1.0, 1.0)
      jagger.color(color)
      jagger.forward(i)
      jagger.right(98)

  # After it draws the main part then sets a color and font to write a verse of the song.
  jagger.color("#ecf0f1")
  jagger.hideturtle()
  jagger.penup()
  jagger.setpos((20,0))
  jagger.write("Have you seen her dressed in blue?",True, align="center", font=("Sans", 26, "normal"))

# Execute the main function.
drawRainbow()

# Exit on user click.
window.exitonclick()
