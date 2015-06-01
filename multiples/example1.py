# This can be used to print "m" multiples of a "n" number
print "Which number do you want to know the multiples of?"
n = input("Type any value:")
# Since we want to know the fist 3 multiples, we make m = 3
m = 3
# Here we are using range() which is a cool function to create lists of arithmetic progressions.
# The arguments (start, stop[,step]) must be plain integers.
print range(n, (m+1)*n, n)
# It should return [5, 10, 15]
