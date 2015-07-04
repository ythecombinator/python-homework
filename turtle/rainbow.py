import turtle

import colorsys

def drawRainbow():

  for i in range(1000):

      color = colorsys.hsv_to_rgb(i/1000.0, 1.0, 1.0)
      turtle.color(color)
      turtle.forward(i)
      turtle.right(98)

drawRainbow()

