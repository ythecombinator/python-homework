# -*- coding: utf-8 -*-

# Using Python 3.4+ "statistics" module (also know as "stats" for 3.1-3.3)
import statistics
# Let's get a array of three numbers, for example
a = [2, 3, 4]
# If you want calculate from an user input:
# a = input("Write here the values that you want calculate the average")

# Using "statistics.mean" which computes the arithmetic mean
print(statistics.mean(a))
# It should return "3"
