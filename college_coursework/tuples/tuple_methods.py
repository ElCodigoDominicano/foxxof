"""
Module to show off tuple methods.

Neither this module nor the function should import the introcs module.  In addition,
the function should not use a loop or recursion.

Author: Alfredo Elias Rivas
Date: 09-15-2021 -> 05-17-2022 [updated to use type annotation and assert statements]
"""


def replace_first_val(tup: tuple[int, ...], a: int, b: int) -> tuple[int, ...]:
    """
    Returns a copy of tup with the first value of a replaced by b
    
    Examples:
        replace_first((1,2,1),1,3) returns (3,2,1)
        replace_first((1,2,1),4,3) returns (1,2,1)
    
    Parameter tup: The tuple to copy
    Precondition: tup is a tuple of integers
    
    Parameter a: The value to replace
    Precondition: a is an int
    
    Parameter b: The value to replace with
    Precondition: b is an int
    """
    assert type(a) == int and type(b) == int, f'This function parameters uses the int data type not {type(a)} and {type(b)}'
    assert type(tup) == tuple, f'This function only uses the tuple datatype.. not {type(tup)}'
    
    bee = list(tup)
    if a in tup:
      bee[bee.index(a)] = b
      result = tuple(bee)
    if a not in tup:
      result = tup
    return result

# Uncomment lines below to run within an IDE or output to a command line
if __name__ == '__main__':
  test1 =  replace_first_val((1,2,1),1,3)
  test2 =  replace_first_val((2,1,3),1,3)
  print(test1)
  print(test2)