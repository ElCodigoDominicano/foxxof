"""
Module with a simple for-loop function.

Author: AERivas
Date: 06-04-2021
Updated: 05-31-2022 [code updated; type hints and precondition enforced]
"""
from typing import Tuple

def lesser(tup: Tuple, value: int) -> int:
    """
    Returns the number of elements in tup strictly less than value

    Examples:
        lesser((5, 9, 1, 7), 6) returns 2
        lesser((1, 2, 3), -1) returns 0

    Parameter tup: the tuple to check
    Precondition: tup is a non-empty tuple of ints

    Parameter value:  the value to compare to the tuple
    Precondition:  value is an int
    """
    assert isinstance(tup, Tuple), f'This program requires the parameter tup to use tuples -> () not {type(tup)}'
    assert isinstance(value, int), f'This program requires the parameter value to use integers not {type(int)}'
    return len([element for element in tup if element < value])

