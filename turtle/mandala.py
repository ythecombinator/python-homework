# Here we intend to create a simple different star which have two colors.

# It should use the turtle module
import turtle

# Let's give it a name.
mandala = turtle.Turtle()

# We'll use this to exitonclick().
window = turtle.Screen()

# A random  name.
turtle.title("A pointless mandala")

# Set a dark color for the background.
turtle.bgcolor("#2c3e50")

# Set the fastest speed
mandala.speed(0)

# Define the number of iterations
n = 100

# The main function
def drawMandala(n):

  for i in range(n):

      turtle.penup()
      turtle.forward(100)
      turtle.left(90)
      turtle.penup()
      turtle.forward (30)
      turtle.left (90)
      turtle.pendown()
      turtle.pencolor ("#27ae60")
      turtle.forward (60)
      turtle.pencolor("#d35400")
      turtle.right (70)
      turtle.forward (70)
      turtle.right (40)
      turtle.forward (50)
      turtle.pencolor ("#c0392b")
      turtle.left (90)
      turtle.pensize(5)
      turtle.forward (100)
      turtle.pencolor("#2980b9")
      turtle.left(90)
      turtle.forward (100)
      turtle.right (50)
      turtle.forward (70)
      turtle.pensize(10)
      turtle.left (60)
      turtle.pensize(6)
      turtle.forward (65)
      turtle.left (45)
      turtle.forward (120)

# Perform the main fucntion
drawMandala(n)

# Exit on user click.
window.exitonclick()
