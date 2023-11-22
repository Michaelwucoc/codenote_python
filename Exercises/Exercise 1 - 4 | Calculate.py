"""
    Write a Python program that calculates the area of a circle based on the radius entered by the user.

Python: Area of a Circle


"""
from math import pi #Import the pi module from math

r = float(input("Input the R of the circle")) #Ask user to enter the value

area = pi * r ** 2 # Calculate the value

print(
    f"The area of the circle is{str(area)}, and you have input the R with the value of{r}" # Print the value and show in console.
)