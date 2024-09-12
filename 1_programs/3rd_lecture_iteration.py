from typing import List
"""
While Statement

The repeated execution of instructions in a loop is called an iteration
The syntax of while-loop is:
    while termination_condition:
       #body
The flow of execution of a while-loop is:

1. Determine whether the termination condition is true or false
2. If false, exit the while statement and continue with the next statement outside of the loop
3. If the condition is True, run the body and go back to step 1
"""

val: int = int(input("Give a positive value:"))

i: int = 0
print("initial value:", val)

while i < val:
    print("Hello World!")
    i += 1

#Container with given size, calculate how many smaller boxes, size given by the user per box, fit in the container

container_size: int = 50

nr_of_boxes: int = 0

while container_size > 0:
    box_size: int = int(input("Give size of box:"))
    if container_size-box_size >= 0:
        nr_of_boxes += 1
        container_size -= box_size
    else:
        print("box is too big")

print(nr_of_boxes)

'''
Loop Termination and Initialization
'''

'''

Break statement- the break statement stops the execution of the loop, it is a wsy to force the terminating an iteration

'''

#Example

values: List[int] = [12, 4, 36, 7, 25, 13, 17, 90]
n: int = 0

while n < len(values):
    if(values[n] % 5 == 0):
        print("Finished:" + str(values[n]))
        break
    n+=1

'''
Continue statement - the continue statement in a loop body stops the execution of specific iterations.
It stops the execution of a specific iteration of the loop, but continues with the next iteration.
'''

#Example

vowels: str = 'aeiou'
count: int = 0
string: str = 'Hello'

while count < len(string):
    letter: str = string[count]
    count+=1

    if letter not in vowels:
        continue

    print(letter)

