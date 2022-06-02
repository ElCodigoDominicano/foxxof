"""
A function to test for floats in European format

Author: AERivas
Date: 06-03-2021
Updated: 06-02-2022
"""

def iseurofloat(string: str) -> bool:
    """
    Returns True if s is a float in European format.  Returns False otherwise.

    In European format, a comma is used in place of a decimal point.  So '12,5' stands
    for 12.5, '0,12' stands for 0.12 and so.  Formally, a string is in European format
    if it is of the form <d1>,<d2> where d1 and d2 are ints (and d2 >= 0).  See

        https://en.wikipedia.org/wiki/Decimal_separator

    for more information.

    This function does not recognize floats in scientific notation (e.g. '1e-2').

    Examples:
        iseurofloat('12,5') returns True
        iseurofloat('-12,5') returns True
        iseurofloat('12') returns False
        iseurofloat('12,-5') returns False
        iseurofloat(',5') returns False
        iseurofloat('apple') returns False
        iseurofloat('12,5.3') returns False
        iseurofloat('12,5,3') returns False
        iseurofloat('1e-2') returns False

    Parameter s: The string to check
    Precondition: s is a string
    """
    # You MAY NOT use conditionals anywhere in this function.
    try:
        comma = string.index(",")
        decimal = '.'
        pos1 = string[:comma].strip('-')
        pos2 = string[comma:].strip(',')
        result = pos1+pos2
        return bool(float(result)) and len(pos1) != 0 and len(pos2) != 0 and not decimal in string

    except ValueError:
        return False

if __name__ == '__main__':
        example_1 = iseurofloat('12,5') # returns True
        example_2 = iseurofloat('-12,5') # returns True
        example_3 = iseurofloat('12') # returns False
        example_4 = iseurofloat('12,-5') # returns False
        example_5 = iseurofloat(',5') # returns False
        example_6 = iseurofloat('apple') # returns False
        example_7 = iseurofloat('12,5.3') # returns False
        example_8 = iseurofloat('12,5,3') # returns False
        example_9 = iseurofloat('1e-2') # returns False
        print(example_1)
        print(example_2)
        print(example_3)
        print(example_4)
        print(example_5)
        print(example_6)
        print(example_7)
        print(example_8)
        print(example_9)
