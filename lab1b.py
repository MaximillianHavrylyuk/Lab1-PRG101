#Author:Maximillian Havrylyuk
#Lab1b.py
#changing data types of variable user inputs and applying all basic arithmetic operations and printing
#the results of the operations

#creating a variable called "num1" that takes a user input.
num1 = input()

#creating a variable called "num2" that takes a user input.
num2 = input()

#converting the user's input of a string from the variable "num1" into an integer.
num1 = int(num1)

#converting the user's input of a string from the variable "num2" into an integer.
num2 = int(num2)

#using basic arithemtic operations based on user's input for the variables "num1" and "num2".
operation1 = num1 + num2
operation2 = num1 - num2
operation3 = num1 * num2
operation4 = num1 ** num2
operation5 = num1 / num2
operation6 = num1 // num2
operation7 = num1 % num2

#printing the result of the basic operators based on the user's input and converting the int of both
# of the user's inputs back into a string in order to concantenate and print the result.
print("num1 + num2 = " + str(operation1))
print("num1 - num2 = " + str(operation2))
print("num1 * num2 = " + str(operation3))
print("num1 ** num2 = " + str(operation4))
print("num1 / num2 = " + str(operation5))
print("num1 // num2 = " + str(operation6))
print("num1 % num2 = " + str(operation7))
