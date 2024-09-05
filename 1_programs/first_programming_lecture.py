# This is a Python comment.
import string

print('Hello World')

# string sentence = 'Hello Software Developers'
print('Hello', 'World', sep='-')
print('Hello World'*3)
print(((40+25)*2)-5)

print(5**2) #** is power

#float pi = 3.141592653589793;
#float r = 10;

#print(pi*(r**2))

size: int = 5 # how we define variables
volume: int = size**3
print(volume)

# Print the sentence three times
sentence: string = 'Hello World'
size: int = 3
while(size > 0):
    print(sentence)
    size -= 1

# Calculate volume sphere and print it
pi: float = 3.141592653589793
radius: int = 3
volume_sphere: float = (4/3)*pi*radius
print(volume_sphere)

# How to ask for input !!! THE INPUT RETURNS A STRING
radius: int = int(input('Radius:'))
print((4/3)*pi*radius)

text: string = 'fio'
print(text)

text: string = string(pi)


