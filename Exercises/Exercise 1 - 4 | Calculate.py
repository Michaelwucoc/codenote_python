"""
    Write a Python program that calculates the area of a circle based on the radius entered by the user.

Python: Area of a Circle


"""
from math import pi

r = float(input("Input the R of the circle"))

area = pi * r ** 2

print(
    f"The area of the circle is{str(area)}, and you have input the R with the value of{r}"
)