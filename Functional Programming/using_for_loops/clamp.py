"""
Module with a more complex for-loop function.

All of these functions make use of accumulators that make new tuples.

Author: AERivas
Date: 06-04-2021    Edited: 12/30/2021
Updated: 05-31-2022 [code updated; type-hints and preconditions enforced]
"""
from typing import Tuple

def clamp(tup: Tuple, low: int, high: int) -> Tuple[int, float]:
    """
    Returns a copy of tup where every element is between low and high.

    Any number in the tuple less than low is replaced with low.  Any number
    in the tuple greater than high is replaced with high. Any number between
    low and high is left unchanged.

    Examples:
        clamp((-1, 1, 3, 5),0,4) returns (0,1,3,4)
        clamp((-1, 1, 3, 5),-2,8) returns (-1,1,3,5)
        clamp((-1, 1, 3, 5),-2,-1) returns (-1,-1,-1,-1)
        clamp((),0,4) returns ()

    Parameter tup: the tuple to copy
    Precondition: tup is a tuple of numbers (float or int)

    Parameter low: the lowest value for the tuple
    Precondition: low <= high is a number

    Parameter high: the highest value for the tuple
    Precondition: high >= low is a number
    """
    assert isinstance(tup, Tuple), f'This program requires the use of tuples -> () not {type(tup)}'
    assert isinstance(low, (int, float)), f'This parameter low must be an integer or a float {type(low)}'
    assert isinstance(high, (int, float)), f'The parameter high must be an integer or a float not {type(high)}'

    result = []
    for element in tup:
        result.append(element)
        for n in result:
            if n < low:
                result.pop()
                result.insert(n,low)
            if n > high:
                result.pop()
                result.insert(n,high)
    return tuple(result)