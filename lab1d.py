#Author:Maximillian Havrylyuk
#Lab1d.py
#using indexing to return certain characters from a string and use formating to format a sentence with
#my name and age

#assigning the variable called "name" my personal name.
name = "Maximillian Havrylyuk"

#using the .upper function to make every character in the str of the variable "name" a uppercase letter
#and checking and printing the result
name = name.upper()
print(name)

#creating the variable called age and assigning it my age.
age = 18

#using the .format function to format the variables with my name and age in the appropiate spaces within
#the print statement
print("How are you {}? Happy {}th Birthday!".format(name,age))

#creating the variable words and assigning the string below and then printing the 1st and 17th character
#using indexing
words = "The quick brown fox jumps over the lazy dog."
print(words[0] + words[16])

#using nexgative indexing I extract certain characters to create the strings "jumps " and "quick" and
#then I print the result
print(words[-24:-18] + words[-40:-35])

#I print the 3rd-16th characters from the variable "words" using indexing
print(words[2:15])

#using indexing and print() function I return the string "uick brown fox ju"
print(words[5:22])
