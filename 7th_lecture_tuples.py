"""
Tuples

Lists are mutable, as we have seen this prevents us of using lists as keys in dictionaries.

An immutable alternative is tuple, which is a sequence of values similar to a list.

An important difference is that in case of lists the data elements are mainly of the same type,
whereas in case of tuples the data elements of different types, but related to each other.
"""

# Example

from typing import Tuple
from typing import List

balance: Tuple = ('123456789', 'Teodora', 2023, 9, 25, 468.50,)
print(balance)

# Tuple with one element
one_element_tuple: Tuple = 'data',
print(one_element_tuple)

# Different way
one_element_tuple: Tuple = ('data',)
print(type(one_element_tuple))

# Extract client id and name from a balance tuple
user_id: str = balance[0]
user_name: str = balance[1]
print(user_id)
print(user_name)

# Extract the date from a balance tuple
balance_date: Tuple = balance[2:5]
print(balance_date)

"""
Comparing tuples

Python performs a one-to-one comparison of each elements (located at the same index) within the tuples. It starts from 
left to right. If at some point the relation does not hold, it stops and returns False.
"""

#Example
client_karim: Tuple = ('4235820', 'Karim Zeller', 2024, 9, 25, 45.50)
client_amy: Tuple = ('123688520', 'Amy Zeller', 2024, 9, 25, 56320.50)
print(client_karim > client_amy)

print((2023,) == (2023, 9, 25))
print((2024, 9, 20) < (2023, 9, 25))

# Sort the words in a string from longest to shortest, so not alphabetically
poem: str = 'My tactic is to talk to you and listen to you have a good conversation'
poem_words: list[str] = poem.split()
sorted_words: list[str] = sorted(poem_words, key=len, reverse=True)
print(sorted_words)

# Sort a more complex structure, given the following list ot tuples

capital_cities: List = [('Paris', 503), ('Berlin', 657), ('Barcelona', 1575), ('Bern', 833)]
print(sorted(capital_cities, key=lambda t: t[1], reverse=True))

"""
lambda is an anonymous function (without a name). In this case, the lambda function takes a tuple and returns
either the first element of the tuple or the second element of a tuple.
"""

"""
Tuple assignment

If you want to assign individual values of a tuple to two or more variables you use a tuple assignment
"""

# Example
balance: Tuple = ('123456789', 'Teodora', 2023, 9, 25, 468.50,)
(user_id, user_name, year, month, day, amount) = balance

print(f'{user_id=}', f'{user_name=}', f'{year=}', )  # and so on

name: Tuple = ('Karim', 'Zeller')
print(sorted(name, reverse=True))
# or
(first_name, last_name) = name
print(last_name, first_name)

# Split an email address
user_name, domain_name = 'm.g.j.v.d.brand@tue.nl'.split('@')
print(user_name)
print(domain_name)

# Combine two sequences of the same length and return an iterator of tuples
# zip() function

capitals: List[str] = ['Sofia', 'Amsterdam', 'Lisboa', 'Belgrade']
countries: List[str] = ['Bulgaria', 'Netherlands', 'Portugal', 'Serbia']

zipper: zip = zip(capitals, countries)
print(zipper)

for pair in zipper:
    print(pair)  # You cannot index/slice nor repeat the iteration

# Change a zipper into a list of tuples
list(zipper)

zipper: zip = zip(capitals, countries)
for capital, country in zipper:
    print(capital)
    print(country)

"""
Sets

A set is a mutable data structure, which is unordered and has no duplicates
"""


from typing import Set

fruits: Set = {'apple', 'pear', 'orange', 'mango'}
fruits.add('banana')
print(fruits)

dutch_snacks: Set = set()
dutch_snacks.add('kroket')
print(dutch_snacks)


# There are three common operations you can perform on sets
fruits.union(dutch_snacks)
print(fruits | dutch_snacks)
print(fruits & dutch_snacks)


