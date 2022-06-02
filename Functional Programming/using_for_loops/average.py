"""
Module with a simple for-loop function.

Author: AERivas
Date: 06-04-2021
Updated: 05-31-2022 [code updated; type hints and precondition enforced]
"""
from typing import Tuple

def avg(tup: Tuple) -> int or float:
    """
    Returns average of all of the elements in the tuple.

    Remember that the average of a tuple is the sum of all of the elements in the
    tuple divided by the number of elements in the tuple.

    Examples:
        avg((1.0, 2.0, 3.0)) returns 2.0
        avg((1.0, 1.0, 3.0, 5.0)) returns 2.5

    Parameter tup: the tuple to check
    Precondition: tup is a tuple of numbers (int or float)
    """
    assert isinstance(tup, Tuple), f'This program requires the parameter tup to use tuples () not {type(tup)}'
    return sum([element / len(tup) for element in tup])
