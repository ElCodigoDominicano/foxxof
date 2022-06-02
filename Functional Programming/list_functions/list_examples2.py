"""
Module with non-mutable functions on lists.

All of these functions make use of accumulators that make new lists.

Author: Alfredo Elias Rivas
Date: 09-15-2021
Updated: 05/18/2022 [revised code, added type hints, enforced preconditions.]
"""


def clamp(alist: list[int,float], min_value: int, max_value: int) -> list:
    """
    Returns a copy of alist where every element is between min_value and max_value.
    
    Any number in the list less than min_value is replaced with min_value.  Any number
    in the tuple greater than max_value is replaced with max_value. Any number between
    min_value and max_value is left unchanged.
    
    Examples:
        clamp([-1, 1, 3, 5],0,4) returns [0,1,3,4]
        clamp([-1, 1, 3, 5],-2,8) returns [-1,1,3,-5]
        clamp([-1, 1, 3, 5],-2,-1) returns [-1,-1,-1,-1]
        clamp([],0,4) returns []
    
    Parameter alist: the list to copy
    Precondition: alist is a list of numbers (float or int)
    
    Parameter min_value: the minimum value for the list
    Precondition: min_value is a number
    
    Parameter max_value: the maximum value for the list
    Precondition: max_value is a number
    """
    assert type(alist) == list, f'alist must be a list containing either. not {type(alist)}'
    assert type(min_value) == int, f'The min_value value must be an integer not {type(min_value)}'  
    assert type(max_value) == int, f'The max_value value Must be an integer not {type(max_value)}'

    result = alist.copy()
    for index, value in enumerate(result):
        if value < min_value:
            result[index] = min_value
        if value > max_value:    
            result[index] = max_value
    
    return result

def removeall(alist: list, n: int) -> list:
    """
    Returns a copy of alist, removing all instances of n
    
    Examples:
        removeall([1,2,2,3,1],1) returns [2,2,3]
        removeall([1,2,2,3,1],2) returns [1,3,1]
        removeall([1,2,2,3,1],4) returns [1,2,2,3,1]
        removeall([1,1,1],1) returns []
        removeall([],1) returns []
    
    Parameter alist: the list to copy
    Precondition: alist is a list of numbers (float or int)
    
    Parameter n: the number to remove
    Precondition: n is a number
    """
    assert type(alist) == list, f'This function uses lists not -> {type(alist)}'
    assert type(n) == int, f'This functions paramater must be an int not -> {type(n)}'
    
    result = []
    for ind, value in enumerate(alist):
        if value != n:
            del ind
            result.append(value)
    return result

if __name__ == '__main__':
    test_1 = clamp([-1, 1, 3, 5],0,4) # returns [0,1,3,4]
    test_2 = clamp([-1, 1, 3, 5],-2,8) # returns [-1,1,3,-5]
    test_3 = clamp([-1, 1, 3, 5],-2,-1) # returns [-1,-1,-1,-1]
    test_4 = clamp([],0,4) # returns []
    print(f'function clamp first test -> {test_1}')
    print(f'function clamp second test -> {test_2}')
    print(f'function clamp third test -> {test_3}')
    print(f'function clamp fourth test -> {test_4}')
    print()
    test_5 = removeall([1,2,2,3,1],1) # returns [2,2,3]
    test_6 = removeall([1,2,2,3,1],2) # returns [1,3,1]
    test_7 = removeall([1,2,2,3,1],4) # returns [1,2,2,3,1]
    test_8 = removeall([1,1,1],1) # returns []
    test_9 = removeall([],1) # returns []
    print(f'function removall first test -> {test_5}')
    print(f'function removall second test -> {test_6}')
    print(f'function removeall fourth test -> {test_7}')
    print(f'function removeall fifth test -> {test_8}')
    print(f'function removeall sixth test -> {test_9}')