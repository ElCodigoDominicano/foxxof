"""
Module with a more complex for-loop function.

All of these functions make use of accumulators that make new tuples.

Author: AERivas
Date: 06-04-2021    Edited: 12/30/2021
Updated: 05-31-2022 [code updated; type-hints and preconditions enforced]
"""
from typing import Tuple

def uniques(tup: Tuple) -> int:
    """
    Returns the number of unique elements in the tuple.

    Examplse:
        uniques((5, 9, 5, 7)) returns 3
        uniques((5, 5, 1, 'a', 5, 'a')) returns 3
        uniques(()) returns 0

    Parameter tup: the tuple to copy
    Precondition: tup is a tuple
    """
    assert isinstance(tup, Tuple), f'The parameter tup must be a tuple -> () not {type(tup)}'
    
    result: int = 0
    for element in tup:
        if isinstance(element, (str, int)):
            result = len(set(tup))
        elif tup.count(element) > 1:
            result = result + 1
    return result

