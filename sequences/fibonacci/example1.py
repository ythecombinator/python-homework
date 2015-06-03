# -*- coding: utf-8 -*-

# Here, we're going to implement the famous Fibonacci sequence, which can be mathematically defined by: Fn = F{n-1} + F{n-2}, onde
# F1 = 1 e F2 = 1.

'''
Implementing a recursive approach, which is the least performatic, we have something like this:

function fib(n)
    if n<2 then
        return n
    else
        return fib(n-1) + fib(n-2)
'''

def fibonacci(n):
    if n < 2:
        return n
    else:
        return fibonacci(n-1)+fibonacci(n-2)

for x in range(10):
    fibonacci(x)
    print (fibonacci(x))
