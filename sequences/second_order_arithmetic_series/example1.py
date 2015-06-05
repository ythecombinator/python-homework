
# First term of the initial expression
a1 = input("Which is the first term of the initial expression? ")
a2 = input("Which is the second term of the initial expression? ")
# First term of the arithmetic series formed by differences between consecutive terms
b1 = a2 - a1
# Arithmetic series' ratio
r = input("Which is the ratio? ")
# The nth term of the initial expression
n = input("Which is the nth term of your expression? ")

while a1 <= n:
  print a1
  a1 = a1 + b1
  b1 = b1 + r
