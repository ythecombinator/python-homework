# -*- coding: utf-8 -*-

# This program should solve the quadratic equation ax^2 + bx + c = 0
import math

# Each coeffient
a = float(input('Enter a: '))
b = float(input('Enter b: '))
c = float(input('Enter c: '))

# Discriminant
d = b**2-4*a*c

# If Delta < 0
if d < 0:
    print "This equation has no real solution"
# If Delta == 0
elif d == 0:
    x = (-b + math.sqrt(d)) / (2 * a)
    print "This equation has one solutions: ", x
# If Delta > 0
else:
    x1 = (-b + math.sqrt(d)) / (2 * a)
    x2 = (-b - math.sqrt(d)) / (2 * a)
    print "This equation has two solutions: ", x1, " and", x2

""" Example:
Enter a: 1
Enter b: -1
Enter c: -20
This equation has two solutions: 5 and -4
"""
