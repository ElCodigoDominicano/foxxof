"""
Function demonstrating string methods.

Neither this module nor any of these functions should import the introcs module.
In addition, you are not allowed to use loops or recursion in either function.

Author: AERivas
Date: 09-15-2021 -> 05/16/2022 [updated code added type hints and enforced preconditions.]
"""

def isnetid(s: str) -> bool:
    """
    Returns True if s is a valid Cornell netid.
    
    Cornell network ids consist of 2 or 3 lower-case initials followed by a 
    sequence of digits.
    
    Examples:
        isnetid('wmw2') returns True
        isnetid('2wmw') returns False
        isnetid('ww2345') returns True
        isnetid('w2345') returns False
        isnetid('WW345') returns False
    
    Parameter s: the string to check
    Precondition: s is a string
    """
    assert type(s) == str, f'The methods used in this function are not meant for {type(s)} datatypes'
    
    result = bool()
    if s[:len(s)].islower():
        result = True
    if s[:1].isnumeric():
        result = False
    if s[:len(s)].isupper():
        result = False
    if s.find('#') != -1:
        result = False
    if s.find('a') > 3:
        result = False
    return result

#Uncomment lines below to run and test functions
# if __name__ == '__main__':
#     print(isnetid('wee'))
#     print(isnetid('wd33'))
#     print(isnetid('12e'))
#     print(isnetid('asAf'))
#     print(isnetid('teo#'))
#     print(isnetid(9)) # Testing assert statement