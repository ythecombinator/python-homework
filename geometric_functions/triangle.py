# Let's find the area of a triangle using the Heron's Formula to calculate
# the semi-perimeter and then the area of the triangle.

def area(a, b, c):
    # We should then calculate the semi-perimeter
    s = (a + b + c) / 2
    # And then we find out the area
    area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
    return area

def main():
    # User should provide the three slides of the triangle
    a = int(input('Enter first side: '))
    b = int(input('Enter second side: '))
    c = int(input('Enter third side: '))
    # We print it :)
    print "Your triangle's area is:", area(a, b, c)
