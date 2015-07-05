# Here we intend to create a simple different star which have two colors.

# It should use the turtle module
import turtle

# Since he's one of the songwriters, he deserves.
star = turtle.Turtle()

# We'll use this to exitonclick().
window = turtle.Screen()

# A random  name.
turtle.title("A pointless star")

# Set a dark color for the background.
turtle.bgcolor("#2c3e50")

# Define the number of iterations
n = 100

# Define how much turtle walks forward
size = 90

# The main function
def drawStar(n, size):

  for i in range(n):
      star.forward (size)
      star.backward (50)
      star.right (90)
      star.pencolor("#8e44ad")
      star.forward (50)
      star.right (90)
      star.forward (50)
      star.right (90)
      star.forward (40)
      star.pencolor("#27ae60")
      star.left (1)
      size = size + 10

# Perform the main fucntion
drawStar(n, size)

# Exit on user click.
window.exitonclick()
