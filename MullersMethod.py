"""
Implementation of Muller's method
Approximates the root or at least one of the roots for an equation of the form f(x) = 0

Contributors:
Archana (most of the code)
Arun (to a lesser extent)
"""

from math import *

expr = input("Enter the function: ")
expr = expr.replace("^", "**") #** is used for pow in Python

#TODO Support for natural mathematic notation
#TODO Input validation

x0 = float(input("Initial guess 1: "))
x1 = float(input("Initial guess 2: "))
x2 = float(input("Initial guess 3: "))
#TODO If x0 = x1 or x1 = x2, ZeroDivisionError is raised.

func = lambda x: eval(expr) # Assuming "x" is the independent var

while True: #TODO Please limit noof iterations
    e = func(x0)
    f = func(x1)
    g = func(x2)

    h0 = x1-x0
    h1 = x2-x1
    delta0 = (f-e) / h0
    delta1 = (g-f) / h1

    a = (delta1-delta0)/(h1+h0)
    b = (a*h1)+delta1
    c = g
    d = sqrt((b*b)-(4*a*c)) # Square root of discriminant
    #TODO Support for complex numbers; Keeps throwing ValueError - math domain error

    if b < 0:
        x3 = x2-((2*c)/(b-d))
    else:
        x3 = x2-((2*c)/(b+d))

    rel_percentage_error = abs(((x3-x2)/x3)*100) # Is it really necessary to calculate this when a simple x3 == x2 comparison is all is required? Plus TODO ZeroDivisionError for x3

    if rel_percentage_error == 0:
        print("One of the roots is: ", x3) #TODO Maybe set precision unless that defeats the point
        break
        
    else:
        x0, x1, x2 = x1, x2, x3

"""
TEST CASES

#1
stdin:
x^3 - 13*x - 12
4.5
5.5
5.0

stdout:
4.0

#2
stdin:
x^4 - 3*x^2 + x - 10
2
2.5
3

stdout:
2.1624

We need test cases for non-polynomial functions too.
"""      