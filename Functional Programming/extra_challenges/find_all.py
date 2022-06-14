"""
A function to find all instances of a substring.

This function is not unlike a 'find-all' option that you might see in a text editor.

Author: AERivas
Date: 06-03-2021
Updated: 06-05-2022
"""
from typing import Tuple

def findall(text: str, sub: str) -> Tuple[str, ...]:
    """
    Returns the tuple of all positions of substring sub in text.
    
    If sub does not appears anywhere in text, this function returns the empty tuple ().
    
    Examples:
        findall('how now brown cow','ow') returns (1, 5, 10, 15)
        findall('how now brown cow','cat') returns ()
        findall('jeeepeeer','ee') returns (1,2,5,6)
    
    Parameter text: The text to search
    Precondition: text is a string
    
    Parameter sub: The substring to search for
    Precondition: sub is a nonempty string
    """
    assert isinstance(text, str), f'Parameter text: must be a string not -> {type(text)}.'
    assert isinstance(sub, str), f'Parameter sub: must be a string not -> {type(sub)}.'
    assert len(sub) != 0, 'Parameter sub: must not be empty for this program to work properly'

    result: Tuple = ()
    count: int = 0
    while count < len(text):
        count = text.find(sub,count)
        if count == -1:
            return result
        else:
            result = list(result)
            result.append(count)
            result = tuple(result)
            count += 1
    return result

