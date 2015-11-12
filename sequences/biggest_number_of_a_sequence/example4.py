# Alternative "maximum number in list" version.

# This version uses a more functional approach based on Python anonymous functions
# + a very helpful list-operating function called reduce.

def maximum (list):

 return reduce(lambda a,b: a if (a > b) else b, list)

list = input("Diga a lista: ")
print (maximum(list))
