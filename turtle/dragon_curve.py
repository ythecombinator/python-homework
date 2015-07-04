# Here we intend to draw a simple Dragon Curve in its 14th iteration.
# A dragon curve is a recursive curve whose name derives from its resemblance to the known mythical creature.
# Here it's named "Imagine Dragons" because it raminds me the indie rock band.

# It should use the turtle module
import turtle

# The colorsys module will be used to get some colors from the HSV cylinder.
import colorsys

# Let's give the turtle a name - now it's a Dragon!
dragon = turtle.Turtle()

# The band which inspirates this.
turtle.title("Imagine Dragons")

# A dark background color.
turtle.bgcolor("#34495e")

# It will be useful
window = turtle.Screen()

# The number of iterations
# Actually an iteration of level 10 would be good enough
n = 13

# Some definitions
s = "F"
rep1 = "-F++G-"
rep2 = "+F--G+"

# The main loop behind the curve
for k in range(n):
    # Let's get z
    z = [(i,s[i]) for i in range(len(s)-1, -1, -1) if s[i]=='F' or s[i]=='G']
    # Let's get s
    for i in z:
        s = s[:i[0]]+(rep1 if i[1]=='F' else rep2)+s[i[0]+1:]

# The function whic will draw our dragon
def drawDragon():

  turtle.setworldcoordinates(-200, -500, 800, 500)
  turtle.setup(0.8, 0.8)
  window.delay(0)
  dragon.speed(0)
  dragon.pensize(2)
  dragon.ht()
  angle = 45
  speed = 6
  steps = s.count('F')+s.count('G')
  stepsSoFar = 0
  for i in s:
      if(i=='F' or i=='G'):
          stepsSoFar += 1
          n = (1.0*stepsSoFar)/steps;
          # Let's get some cool colors by moving around the upper edge of the HSV cylinder.
          dragon.pencolor(colorsys.hsv_to_rgb(n, 0.9,0.5))
          dragon.forward(speed)
      elif(i=='+'):
          dragon.left(angle)
      elif(i=='-'):
          dragon.right(angle)



# Perform the main function
drawDragon()

# Exit on user click.
window.exitonclick()
