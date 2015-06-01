# Let's find the area of a rectangle.

def area(a, b):
    # And then we find out the area
    area = a * b
    return area

def main():
    # User should provide the two slides of the rectangle
    a = int(input('Enter first side: '))
    b = int(input('Enter second side: '))
    # We print it :)
    print "Your rectangle's area is:", area(a, b)
