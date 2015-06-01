# -*- coding: utf-8 -*-

# Let's find the area of a rectangle.

# Let's use the "math" lib
import math

def area(a, b):
    # First we define the area
    area = a * b
    return area

def main():
    # User should provide the two slides of the rectangle
    a = int(input('Enter first side: '))
    b = int(input('Enter second side: '))
    # We print it :)
    print "Your rectangle's area is:", area(a, b)
