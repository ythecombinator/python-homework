#coding:utf8

# Let's get an interval from user to display all the primes in that.

# Let's get user input to know which interval to show
a = int(input("Enter first number in the interval: "))
b = int(input("Enter last number in the interval: "))

def list_primes(a, b):
  for num in range(a, b + 1):
     # Prime numbers are greater than 1
     if num > 1:
         for i in range(2,num):
             if (num % i) == 0:
                 break
         else:
             print(num)

print (list_primes(a, b))
