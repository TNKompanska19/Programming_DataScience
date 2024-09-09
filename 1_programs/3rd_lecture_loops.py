from typing import List
rainbow_colors: List[str] = ['yellow', 'blue', 'red', 'orange', 'green', 'violet', 'indigo']

#Suppose you need to print every individual color of the rainbow (USE FOR LOOPS)
i: int = 0
for color in rainbow_colors:
    i += 1
    print(color)
print(i)

'''
The for-loop is a statement that helps us traverse any sort of sequence (e.g. strings, lists)
'''

for index in range(len(rainbow_colors)):
    print(index)

#Take all items in the rainbow_colors variable and change all their characters into uppercase
for index in range(len(rainbow_colors)):
    rainbow_colors[index] = rainbow_colors[index].upper()

print(rainbow_colors)

#Only first letter is capital
for color in rainbow_colors:
    print(color.capitalize())

'''
Map, Filter, and Reduce

When you want to apply an operation to all elements of a list, see previous cells with upper, it is called a map
operation on a list.
'''

#Given a list with arbitrary integers, create a new list with only the even integers
numbers: List[int] = [4, 5, 7, 9, 12, 27]
evens: List[int] = []

for number in numbers:
    if number % 2 == 0:
        evens.append(number)

print(evens)

'''
When you want to obtain a sublist for specific elements of a list, it is called a filter operation on a list
'''

#Given the list with numbers, sum the list elements in total variable
numbers: List[int] = [4, 5, 7, 9, 12, 27]

total: int = 0
for number in numbers:
    total += number

print(total)

'''
If you want to transform the list into a single value, it is called a reduce
'''



