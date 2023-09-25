# Easy way: using 3.14 as an approx. value of pi
radius = int(input("What is the radius? "))
print("The area of this circle is ", 3.14 * radius * radius)

# Hard way: utilise the value of pi from a library
import math
radius = int(input("What is the radius? "))
print("The area of this circle is ", math.pi * radius * radius)