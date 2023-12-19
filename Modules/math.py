import math

# value = dir(math)  // shows the functions that the module holds within
# value = help(math) // "help" displays what can be done with this functions
# value = help(math.factorial) // Shows the instrcutions for the specific function
squareRoot = math.sqrt(49)
factorial = math.factorial(5)
floor = math.floor(5.9)
ceil = math.ceil(5.9)
print(squareRoot)
print(factorial)
print(floor)
print(ceil)


# Module aliasing
import math as opr
print("--------------------")
alias = opr.factorial(4)
print(alias)

#Import all(*)
#Enables functions to be called without the module name
from math import *
print("--------------------")
val = factorial(6)
val2 = sqrt(9) 
print(val)
print(val2)

#Import certain functions from the module
from math import factorial,sqrt,ceil
print("--------------------")
a = factorial(5)
b = sqrt(25)
c = ceil(9.8)
print(a)
print(b)
print(c)

#If there is a user defined function that holds the same name as the one in the module, 
#the program will use the latest defined function. Which means the previous function will be overridden