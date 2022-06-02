"""
Function factorial with range-based for-loop.

Author: AERivas
Updated: 06-01-2022 [Updated Code; type hints added preconditions enforced]
"""

def factorial(number):
    """
    Returns number! = number * (number-1) * (number-2) ... * 1

    0! is 1.  Factorial is undefined for integers < 0.

    Examples:
        factorial(0) returns 1
        factorial(2) returns 2
        factorial(3) returns 6
        factorial(5) returns 120

    Parameter n: The integer for the factorial
    Precondition: n is an int >= 0
    """
    assert isinstance(number, int), f"The function parameter 'n' must be of integer type not {type(number)}."
    assert number >= 0, f'Factorial is undefined for integers < 0'
    result = 1
    # The walrus operator -> := <- released in python 3.8(3.8+ is required) 
    # allows for data to be assigned to a variable whilst in an expression
    # its a list comprehension which creates the range of numbers, multiplies 
    # the range of numbers; ex. 5*4*3*2*1. While the values are being accumulated.
    [result := result * element for element in range(1, number+1)]
    return result

if __name__ == '__main__':    
    example_1 = factorial(0)
    example_2 = factorial(2)
    example_3 = factorial(3)
    example_4 = factorial(5)
    print(example_1) # returns 1
    print(example_2) # returns 2
    print(example_3) # returns 6
    print(example_4) # returns 120
    print()
