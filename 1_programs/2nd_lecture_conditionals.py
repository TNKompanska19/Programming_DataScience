"""
Conditionals
Booleans: is a data type reprenting the value True or False

Using truth tables - Logic and Set Theory

Logical operators: Operators that combine boolean expressions

Precedence order: not > or > and. If in doubt, use brackets

operator % - remainder operator
"""

#ex - check if the value is smaller than min and bigger than max
min: int = 5
max: int = 25

user_value: int = int(input('Introduce int value:'))

flag: bool = user_value < min or user_value > max

flag_shorter: bool = not(min < user_value < max)

#ex - division byt 2 and 3 (using % operator)

value: int = int(input('Give an integer value: '))

# this % operator returns the remainder of the value assigned to the variable
print(value % 2 == 0 and value % 3 == 0)

"""
Conditionals

Syntax

if condition1:
    #if body
elif condition2:
    #elif body
else:
    #else body
"""

#ex - checking the smallest number
num1: int = int(input('num 1: '))
num2: int = int(input('num 2: '))
num3: int = int(input('num 3: '))

if num1 <= num2 <= num3:
    print(f'{num1} is the smallest')
elif num2 <= num1 and num2 <= num3:
    print(f'{num2} is the smallest')
else:
    print(f'{num3} is the smallest')

"""
Exceptions

Syntax:

try:
   #body
except:
    #body
"""



#Task 1: The Palaces of Persepolis and Task 2: Apadana Palace -> Homework




