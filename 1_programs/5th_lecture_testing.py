"""
Testing is a way of convincing yourself that the implementation of the function is correct.
Testing cannot proof the correctness of a program. It cannot proof the absence of errors, it can only find
errors within the cases you have tested.

Checking type & value of a variable
Of a variable you can test its type and value
"""

#Example
pi: float = 3.14

print(type(pi) == float)
print(pi == 3.14)

"""
Checking Arguments & the assert statement

Of a function you can test its return value when passing different arguments.

We have many assumptions about the nature of the arguments of a function. If the user does not comply with such 
assumptions, the function can exhibit an unwanted behaviour.

You check the arguments of a function via auxiliary code in the form of conditionals, or via assert statements.

An assert sta,enet is a debugging tool that checks if certain preconditions are being met.

Debugging is the process of finding errors in the code of a program.

The syntax of the assert statement is as follows:

assert<boolean_condition>
or
assert<boolean_condition>, <error_message>
"""

# Convert from binary to decimal

def is_binary(binary_num: str) -> bool:
    """
    Checks whether a string is binary or not.
    :param binary_num: binary number to check of type string
    :return: boolean
    """

    for digit in binary_num:
        if digit not in '01':
            return False
        return True
def binary_to_decimal (binary_num: str)->int:
    """
    Convert a binary number represented as a string to a decimal number.
    :param binary_num: binary number to convert of type string.
    :return: integer with the decimal representation of the binary number.
    """
    assert not isinstance(binary_num, str), print('The type of the argument should be string')
    assert binary_num != '', print('The string should not be empty')
    assert not is_binary(binary_num), print('Argument contains strange characters')
    decimal_num: int = 0
    binary_num = binary_num[::-1]
    for index in range(len(binary_num)):
        digit: str = binary_num[index]
        if digit == '1':
            decimal_num += 1 * (2 ** index)

    return decimal_num


# print(binary_to_decimal('101'))


"""
Testing with doctest

dovtest.run_docstring_examples(roll_dice, globals(), verbose=True, name='roll_dice')
"""