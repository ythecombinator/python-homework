# -*- coding: utf-8 -*-

# Here, we're going to implement the famous Fibonacci sequence, which can be mathematically defined by: Fn = F{n-1} + F{n-2}, onde
# F1 = 1 e F2 = 1.

'''
Implementing an iterations-based approach, which is more performatic, we have something like this:

function fib(n)
    i gets 1
    j gets 0
    for k from 1 to n do

        t gets i+j
        i gets j
        j gets t

    return j
'''

def fibonacci(n):
    a,b = 0,1
    for i in range(n):
        a,b = b,a+b
    return a

for x in range(10):
    fibonacci(x)
    print (fibonacci(x))
