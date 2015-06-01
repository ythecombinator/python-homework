# -*- coding: utf-8 -*-

# Let's find the area of a circle based on its radius.

# Let's use the "math" lib
import math

def area(r):
    pi = math.pi
    area = ( r ** 2 ) * pi
    return area

def main():
    # User should provide the radius of the circle
    r = int(input('Enter the radius of your circle: '))
    # We print it :)
    print "Your circle's area is:", area
