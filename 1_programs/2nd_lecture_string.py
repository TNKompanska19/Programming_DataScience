# Note: !!!We should define the type of the variable in this course!!!
#ex
my_num: int = 10
print(my_num)
#not this
my_num = 10

#an empty strings - it also have a value, it just doesn't print anything
#ex
empty_str: str = ''
print(empty_str)

'''
Indexing
    Indexing is an operation to select a value from a sequence given its position (or index)
    The syntax for indexing is:
        sequence[index]
            where
                sequence: any variable of valur representing a sequence (e.g. string)
                index: positive integer value, small than the length of the string
Indexing starts from 0 - the first element is a zero
The empty spaces also have positions!!!
ex:'''

country: str = 'The Netherlands'
print(country[0])
#print the empty space
print(country[3])

#Compute length of a string
print(len(country))

#Get the last element of a string - you can start to count from the end of the string in Python
print(country[-1])
#You can get the last element with the method 'len'
print(country[len(country) - 1])

'''
Slicing
    Substring of the string - obtaining more than one character from string
    
    Definition:
        sequence[start_index : end_index : step] or 
        sequence[start_index : end_index]
            start_index: Start index of the slice
            end_index: End index of the slice
            step: Steps to take between the start and end index (it skips the characters)
'''
#Get a substring from string in Python
print(country[4:10])

#Get a substring from string with step
print(country[4:10:2])

'''You do not need to specigy all parameters. If you take a prefix, 
you can leave the start_index empty and in case of a suffix you leave the end_index empty'''
print(country[:9])

#Slice the whole string
print(country[:])

#Obtain a suffix from word
print(country[-5:])
print(country[10:])
print(country[10:len(country)])

'''
Immutability
    Strings are immutable this means that the string cannot be modified.
    If you want to change a string you must create a new string.
    
    + - concatenation 
'''
#ex
greeting: str = 'hello people!'
greeting2: str = 'H' + greeting[1:]
print(greeting2)

#Check if string contains another string
gazelle: str = 'gazelle'
zel: str = 'zel'
print(zel in gazelle) #The in operator checks if the first string is a substring of the second one

'''
    The '+' concatenate operator concatenates or glues two different strings.
    The '==' operator checks the equality of two strings
        Other relational operator such as <,> can be used to compare the lexicograpical order between two strings
    Bear in mind:
        Digits precedes letters
        Upper letters precede lowercase letters
    Overview: digits > upper case > lower case'''
#ex
print('1' < 'one')  # False
print('0' < 'o')

'''
  Methods
  When we use method, we use . (dot) operator
  - find() - finds substrings in a string and returns the index where the substring starts
  - lower() and upper() - transforms a string into uppercase and lowercase letters
'''
#ex - find()
index: int = 'holidays'.find('days')

#ex - upper()
lowercase_name: str = 'muhammad'
print(lowercase_name.upper())

#ex - lower()
uppercase_name: str = 'XIAYO'
print(uppercase_name.lower())

'''
String Formatting
    You have several alternatives:
        - F-strings
        - Format method (format())
        - Format operator (%)
    Formatting is used when u want to show that the string need to get another variable
    
    If we format different variables, they can be of different types
    
    You need to add slash if you want to add quotation, if u need double quotation u can define the string with single 
    and the other way goes the same.
'''

#ex - F-strings
f_string: str = f'The magic number is {42}'
print(f_string)

#ex - Format method
format_method: str = 'The magic number is {}'.format(42)
print(format_method)

#ex - Format operator
format_operator: str = 'The magic number is %d' % 42
print(format_operator)



