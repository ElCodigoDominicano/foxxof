"""
Module with for-loops that loop over positions.

Author: AERivas
Date: 06-04-2021
Updated: 06-01-2022 [code updated; added type hints and enforced preconditions]
"""
from typing import Tuple

def fixed_points(tuple_with_ints: Tuple) -> Tuple[int, ...]:
    """
    Returns a copy of tup, including only the "fixed points".
    
    A fixed point of a tuple is an element that is equal to its position in the tuple.
    For example 0 and 2 are fixed points of (0,3,2).  The fixed points are returned in
    the order that they appear in the tuple.
    
    Examples:
        fixed_points((0,3,2)) returns (0,2)
        fixed_points((0,1,2)) returns (0,1,2)
        fixed_points((2,1,0)) returns (1,)
    
    Parameter tup: the tuple to copy
    Precondition: tup is a tuple of ints
    """
    assert isinstance(tuple_with_ints, Tuple), 'tuple_with_ints must be a tuple with ints-> (0, 1, 2, 3)'
    for integers in tuple_with_ints:
        if isinstance(integers, str):
            raise AssertionError("The values inside the tuple must be integers.")
    return tuple([element for element in range(len(tuple_with_ints)) if element == tuple_with_ints[element]])
# if __name__ == '__main__':
#     example_1 = fixed_points((0,3,2)) # returns (0,2)
#     example_2 = fixed_points((0,1,2)) # returns (0,1,2)
#     example_3 = fixed_points((2,1,'a')) # returns (1,)
#     print(example_1)
#     print(example_2)
#     print(example_3)
