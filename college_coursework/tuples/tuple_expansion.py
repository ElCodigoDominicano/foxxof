"""
a simple demonstration of tuple expansion.

Author: AERivas
Date: 09-15-2021 
Updated: 05-19-2022 [Code updated; type hinting and preconditions enforced]
"""

def avg(* args: tuple) -> int or float:
    """
    Returns average of all of arguments (passed via tuple expansion)
    
    Remember that the average of a list of arguments is the sum of all of the elements 
    divided by the number of elements.
    
    Examples: 
        avg(1.0, 2.0, 3.0) returns 2.0
        avg(1.0, 1.0, 3.0, 5.0) returns 2.5
    
    Parameter args: the function arguments
    Precondition: args are all numbers (int or float)
    """
    assert type(args) == tuple, f'This function requires the arguments to be in tuple -> {type(args)}'
   
    result = 0
    if len(args) <= 0:
        pass # Do Nothing
    
    for x in args:
        result = sum(args) / len(args)
        
    return result

#Uncomment lines below to test function or run test_* file.
if __name__ == '__main__':
    example_1 = avg(1.0, 2.0, 3.0) # returns 2.0
    example_2 = avg(1.0, 1.0, 3.0, 5.0) # returns 2.5
   
    print(example_1)
    print(example_2)
    