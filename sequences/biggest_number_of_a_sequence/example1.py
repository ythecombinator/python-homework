# -*- coding: utf-8 -*-

# Let's calculate the biggest number of a sequence of three numbers.

# Receive three numbers from user input
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))

# Using the if...elif...else to find the largest among the three
if (a > b) and (a > c):
   biggest = a
elif (b > a) and (b > c):
   biggest = b
else:
   biggest = c
# Print the result
print("The biggest number is",biggest)
