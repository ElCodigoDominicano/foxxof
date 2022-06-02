"""
Module with for-loops that loop over positions.

Author: AERivas
Date: 06-04-2021
Updated: 06-01-2022 [code updated; added type hints and enforced preconditions]
"""
from typing import Tuple

def skip(string: str, number: int) -> str:
    """
    Returns a copy of string, only including positions that are multiples of n
    
    A position is a multiple of number if pos % number == 0.
    
    Examples:
        skip('hello world',1) returns 'hello world'
        skip('hello world',2) returns 'hlowrd'
        skip('hello world',3) returns 'hlwl'
        skip('hello world',4) returns 'hor'
    
    Parameter string: the string to copy
    Precondition: string is a nonempty string
    
    Parameter number: the letter positions to accept
    Precondition: number is an int > 0
    """
    assert len(string) >= 1, "Precondition violated: 'string' must contain a non-empty string."
    assert isinstance(string, str), "Precondition violated: 'string' must be a str type."
    assert isinstance(number, int), "Precondition violated: 'number' must be a int type."
    assert number > 0, "Precondition violated: 'number' must be > 0."
    return ''.join([string[pos] for pos in range(len(string)) if pos % number == 0])

# if __name__ == '__main__':
#     example_1 = skip('hello world',1) # returns 'hello world'
#     example_2 = skip('hello world',2) # returns 'hlowrd'
#     example_3 = skip('hello world',3) # returns 'hlwl'
#     example_4 = skip('hello world',4) # returns 'hor'
#     print(example_1)
#     print(example_2)
#     print(example_3)
#     print(example_4)
