"""
A module to demonstrate how to test precondition enforcement.

This module has a function (and a helper) that uses assert statements to enforce
the preconditions.

Author: Alfredo Elias Rivas
Date: 06-03-2021    Edited: 12/26/2021
Updated: 06-02-2022
"""

def valid_format(time_string: str) -> bool:
    """
    Returns True if s is a string in 12-format <hours>:<min> AM/PM

    Example:
        valid_format('2:45 PM') returns True
        valid_format('2:45PM') returns False
        valid_format('14:45') returns False
        valid_format('14:45 AM') returns False
        valid_format(245) returns False

    Parameter time_string: the candidate time to format
    Precondition: time_string is in 12-format <hours>:<min> AM/PM
    """
    result = bool()   
    try:
        colon = time_string.find(":")
        space = time_string.find(" ")
        if space < colon:
            result = False
  
        hours  = int(time_string[:colon])
        minutes = int(time_string[colon+1:colon+3])
        suffix = time_string[space+1:]
        if space > colon and (1 <= hours < 13) and (0 <= minutes < 60):
            result = True
        else:
            result = False
    
    except AttributeError:
        pass
    
    finally:
        return result
    
def time_to_minutes(time_string: str) -> int:
    """
    Returns the number of minutes since midnight

    Examples:
       time_to_minutes('2:45 PM') returns 885
       time_to_minutes('9:05 AM') returns 545
       time_to_minutes('12:00 AM') returns 0

    Parameter time_string: string representation of the time
    Precondition: time_string is a string in 12-format '<hours>:<min> AM/PM'
    """
    assert isinstance(time_string, str), f'Parameter time_string: must be of str type not -> {type(time_string)}'
    assert ':' and ' ' in time_string, f"Parameter time_string: must formatted properly '<hours>:<minutes> AM/PM' "

    pos1 = time_string.find(":")
    pos2 = time_string.find(" ")
    hour = int(time_string[:pos1])
    minutes = int(time_string[pos1+1:pos2])
    suffix = time_string[pos2+1:]
    assert 1 <= hour < 13
    assert 0 <= minutes < 60
    assert 'AM' or 'PM' in suffix
    
    if (hour == 12) and (minutes == 0) and (suffix == 'PM'):
        hour -= 12
    if (suffix == 'PM'):
        hour += 12
    if (suffix == 'PM') and (hour == 12) and (minutes == 0):
        hour = 12
    if (suffix == 'AM') and (hour == 12):
        hour = 0
    
    return hour * 60 + minutes

def str_to_minutes(time_string: str) -> int:
    """
    Returns the number of minutes since midnight.

    If s does not represent a time, this function returns -1.

    Examples:
       time_to_minutes('2:45 PM') returns 885
       time_to_minutes('9:05 AM') returns 545
       time_to_minutes('12:00 AM') returns 0
       time_to_minutes('12:75 AM') returns -1
       time_to_minutes('apple') returns -1

    Parameter s: a string potentially representating a time
    Precondition: s is non-empty
    """
    try:
        return time_to_minutes(time_string)

    except:
        return -1

if __name__ == '__main__':
    example_1 = time_to_minutes('2:45 PM') # returns 885
    example_2 = time_to_minutes('9:05 AM') # returns 545
    example_3 = time_to_minutes('12:00 AM') # returns 0
    print(example_1)
    print(example_2)
    print(example_3)
    print()
    example_4 = valid_format('2:45 PM') # returns True
    example_5 = valid_format('2:45PM') # returns False
    example_6 = valid_format('14:45') # returns False
    example_7 = valid_format('14:45 AM') # returns False
    example_8 = valid_format(245) # returns False
    example_9 = valid_format('0:12 AM') # returns False
    example_10 = valid_format('1:59 AM') # returns True
    example_11 = valid_format('1:60 PM') # returns False
    example_12 = valid_format('2:00 PM') # returns True
    print(example_4)
    print(example_5)
    print(example_6)
    print(example_7)
    print(example_8)
    print(example_9)
    print(example_10)
    print(example_11)
    print(example_12)

