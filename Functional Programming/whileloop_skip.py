"""
Function using a while loop to loop over positions.

Author: AERivas
Date: 06-04-2021
Updated: 06-02-2022
"""

def skip(string: str, position: int) -> str:
    """
    Returns a copy of the string, only including positions that are multiples of n
    
    A position is a multiple of n if pos % n == 0.
    
    Examples:
        skip('hello world',1) returns 'hello world'
        skip('hello world',2) returns 'hlowrd'
        skip('hello world',3) returns 'hlwl'
        skip('hello world',4) returns 'hor'
    
    Parameter s: the string to copy
    Precondition: s is a nonempty string
    
    Parameter n: the letter positions to accept
    Precondition: n is an int > 0
    """
    result: str = ''
    while position > 0:
        result += string[:len(string):position]
        position -= position
    return result
    
