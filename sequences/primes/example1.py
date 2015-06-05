#coding: -*- utf8 -*-

# Let's check if a number given  by the user is prime or not.

import math

# Let's get user input to know which number to test
n = float(input('Is this number a prime? '))

# Let's make a function to find out if the number is prime by making divisions and analyzing their results
def is_prime(n):
    if n % 2 == 0 and n > 2:
        return False
    return all(n % i for i in range(3, int(math.sqrt(n)) + 1, 2))

# Let's print the result ("True" or "False")
print (is_prime(n))
