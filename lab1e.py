#Author:Maximillian Havrylyuk
#Lab1e.py
#creating a variable with a float and a user input which asks for a float then converting the input to
#a float and calculating the product and assigning it a variable in order to print it and then formating
#the product with the % function.

#created a variable thats a float of my choosing
quantity = 6.7

#created a variable that takes a user input and putting a string to tell the user to write a float only
stock = input('put a float only ')

#creating a variable with the arithemtic function to calculate the product of quantity * stock and
#converting the stock variable to a float data type
total = quantity * float(stock)

#printing the product with 4 spaces before the answer and using the % to format the product as a float
print("    %f" % (total))

#printing the product with 7 spaces before the answer and using the % to format the product as a float
#and to only show the decimals up to the hundredths place.
print("       %.2f" %(total))
