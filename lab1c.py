#Author:Maximillian Havrylyuk
#Lab1c.py
#using the math module and creating basic mathematic functions

#importing the math module
import math

#creating a new variable, "r" which is assigned the value of a user input and assigning it the data type
#of an integer
r = int(input())

#assigning the answer to a new variable so it can be printed and
#creating the mathematic function for calculating the area of a circle using the radius and math module.
a = math.pi * r ** 2

#printing the result-area of the circle based off the user's input
print(a)
