"""
Function demonstrating string methods.

Neither this module nor any of these functions should import the introcs module.
In addition, you are not allowed to use loops or recursion in either function.

Author: AERivas
Date: 09-15-2021 -> 05/16/2022 [updated code added type hints and enforced preconditions.]
"""

def first_in_parens(s: str) -> str:
    """
    Returns: The substring of s that is inside the first pair of parentheses.
    
    The first pair of parenthesis consist of the first instance of character
    '(' and the first instance of ')' that follows it.
    
    Examples: 
        first_in_parens('A (B) C') returns 'B'
        first_in_parens('A (B) (C)') returns 'B'
        first_in_parens('A ((B) (C))') returns '(B'
    
    Parameter s: a string to check
    Precondition: s is a string with a matching pair of parens '()'.
    """
    assert type(s) == str, f'The methods used in this function are not meant for {type(s)} datatypes'
    open_paren = s.find('(')
    close_paren = s.find(')',open_paren)
    return s[open_paren+1:close_paren]