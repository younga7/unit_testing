# CS362 HW4
# Alex Young
# 2/2/2021
# Run this file using python3 HW4.py
# This program holds funtions to
# find the volume of a cube,
# find average of elements in a list,
# and to generate a full name give first/last names

def cube(x):
    try:
        n = pow(x, 3)
    except TypeError:
        return("Type Error")
    return n

def avg(x):
    try:
        n = sum(x) / len(x)
    except TypeError:
        return("Type Error")
    except ZeroDivisionError:
        return("Zero Division")
    return n

def name(x,y):
    try:
        z = x + " " + y
    except TypeError:
        return("Type Error")
    return z