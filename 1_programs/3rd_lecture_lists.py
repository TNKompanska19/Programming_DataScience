#Lists

#Declaration and initiliazation of a list
rainbow_colors: list = ['yellow', 'blue', 'red', 'orange', 'green', 'violet', 'indigo']
print(rainbow_colors)
"""
The data structure to store the colors is a list, which is a sequence to store values (elements or items) of any type.

A string is also a sequence, but of characters.

You write the items of the list within square brackets ([]).
    [ value1, value2, value3,...]
In orfer to be able to use the type hints for a list, you need to import the List type from typing.
"""
from typing import List
rainbow_colors: List[str] = ['yellow', 'blue', 'red', 'orange', 'green', 'violet', 'indigo']

#A list can contain items of different types, but avoid doing so
from typing import Any
messy_list: List[Any] = ['color', 1, True, 3.14]

'''
Mutability
    A list is mutable, in contrast to a string. The value can be modified.
'''
rainbow_colors[0] = 'Yellow'
print(rainbow_colors)
"""
You do not need to create a new list to change it (contrary to strings).
"""

"""
Indexing and Slicing
"""
#Get the last element
print(rainbow_colors[len(rainbow_colors)-1])
#or
print(rainbow_colors[-1])

#Get all items of the rainbow_colors except for the first and last ones
print(rainbow_colors[1:6])
#or
print(rainbow_colors[1:len(rainbow_colors)-1])

print(rainbow_colors[1:len(rainbow_colors)//2])
'''
When u use the double slash // for division, you get an integer, with single, you get float/double
'''

'''
List Operations & Methods
The concatenation (+) and multiplication (*): work the same as for strings.

The method append() adds a new item at the end of the list.
It does not return anything (Node)

The method extend() merges two lists.
It does not return anything(Node)

Both methods are type void function - this func does not have a return type.

The pop() method requires an index as input to remove the item at that location. It returns the deleted item.

The remove() method is useful when you know the item you want to remove but not necessarily its index.
 It does not return anything(None).
 
 The del statement can remove a slice of the list. Because del is a statement it does not return anything.
'''

#Suppose you want to append a new color to the rainbow_colors
rainbow_colors.append('white')
print(rainbow_colors)

#Suppose you want to append a new list with colors to the rainbow_colors
bw_colors: List[str] = ['black', 'white']
rainbow_colors.extend(bw_colors)
#or
rainbow_colors = rainbow_colors + bw_colors
print(rainbow_colors)

#Suppose you want to sort the list
rainbow_colors.sort()
print(rainbow_colors)

print("Return", rainbow_colors.pop(0))
print("Colors", rainbow_colors)

rainbow_colors.remove('blue')
print(rainbow_colors)

del rainbow_colors[1:len(rainbow_colors)-1]
print("Colors: ", rainbow_colors)

