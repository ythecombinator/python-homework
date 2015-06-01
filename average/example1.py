# Let's calculate using "NumPy" which is package for working with scientific computing
import numpy
# Let's get a array of three numbers, for example
a = [2, 3, 4]
# If you want calculate from an user input:
# a = input("Write here the values that you want calculate the average")

# Using "numpy.nanmean" which computes the arithmetic mean ignoring NaNs
# In this case "a" is a parameter which means array_like and represents an array
# containing numbers whose mean is desired. If a is not an array, a conversion is attempted.
print(numpy.nanmean(a))
# It should return "3"
