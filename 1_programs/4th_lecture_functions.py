
"""
Function calls
Funtion call: Language construct used to execute te body of a specific function definition. It provides a structured way
to facilitate re-use of functionality

The syntax of a function call is as follows:
function_name (arg1, arg2..., argn)


Built-in FUnctions and Packages
Built-in functions: There are functions provided by standard Python libraries

You can import library functions
"""
# Example
import math
print(math.log10(28))

# Example for importing specific function/method
from math import log10
log10(34)

# Check which functions the math library provides - use dir() method
import math
dir(math)

# Change the name of the package - example
import math as mt

# Example - use the random package
import random
random.random() # gives random number between 0 and 1

import random
random.randint(1, 10) #generate a random number between 1 and 10

"""
Function Call Composition

It is the ability to use a function call as an argument of a different function.
"""
math.exp(math.log(6+7))

"""
Function Definition

Definition that specifies and creates a new function with a given name, a sequence of parameters, and a sequence of instructions.
The syntax of a function definition is as follows:

def function_name(param1, param2, ...):
    #function_body: instructions
    
"""

def my_first_function():
    pass


"""
Doctring and Type Hints

Docstring: it is a string at the beginning of a function definition that explains the inputs, output, and purpose of a 
function--in other words, it interface\


The parameters and return value of a function should always be accompanied by type hints.
"""
#Example - void function (None function - just printing)
def print_word(word: str) -> None:
    """
    Prints a word, and it does not return a value
    :param word: word to be printed
    """
    print(word)

#Example - return-type function
def print_word(word: str) -> str:
    """
    Returns twice the input word.
    :param word: word to be returned twice
    :return:  twice the input word
    """
    return word * 2


"""
Arguments are concrete values that we give to the function
and parameters are the variables that the function needs
"""

"""
Local and Global Variables

Variable scope: it is the code context in which a variable is defined and can be used.

Local variable: A variable that is declared in a function and can only be used within it. (Not outside the function!)

Global variable: A variable is declared outside a function
"""


