# Here we intend to create a simple spiral.

# It should use the turtle module
import turtle

# Let's give it a name.
spiral = turtle.Turtle()

# We'll use this to exitonclick().
window = turtle.Screen()

# A random  name.
turtle.title("A pointless spiral")

# Set a dark color for the background and a green color for the pen
turtle.bgcolor("#2c3e50")
spiral.pencolor('#16a085')

# Set the fastest speed
spiral.speed(0)

# Define the number of iterations
n = 120

# Create a counter variable x with value 0
x = 0

def drawSpiral (n,x):
  # Lift the pen up, so no lines are drawn
  turtle.up()

  # Initial positions
  spiral.rt(45)
  spiral.fd(90)
  spiral.rt(135)

  # Sets the pen down, so that turtle can draw
  spiral.down()

  # While the value of x is lesser than n, continuously do this:
  for i in range(n):
      spiral.fd(200)
      spiral.rt(61)
      spiral.fd(200)
      spiral.rt(61)
      spiral.fd(200)
      spiral.rt(61)
      spiral.fd(200)
      spiral.rt(61)
      spiral.fd(200)
      spiral.rt(61)
      spiral.fd(200)
      spiral.rt(61)

      spiral.rt(11.1111)

      # Add 1 to the value of x so that it's closer to n after every iteration
      x = x + 1

# Perform the main fucntion
drawSpiral (n, x)

# Exit on user click.
window.exitonclick()
