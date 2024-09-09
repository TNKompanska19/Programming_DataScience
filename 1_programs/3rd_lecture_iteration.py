
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



