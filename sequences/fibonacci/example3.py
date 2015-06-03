# -*- coding: utf-8 -*-

# Here, we're going to implement the famous Fibonacci sequence, which can be mathematically defined by: Fn = F{n-1} + F{n-2}, where
# F1 = 1 e F2 = 1.

# Implemented using a functional approach, where we can write less and be more performatic :)

fibonacci = lambda n,a=1,b=1:[b,0][n>0] or fibonacci(n-1,b,a+b)

for x in range(10):
    fibonacci(x)
    print (fibonacci(x))
