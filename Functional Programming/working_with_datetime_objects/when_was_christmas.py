"""
Function for working with datetime objects.

Author: AERivas
Date:   06-13-2022
"""
import datetime

def christmas_day(year: int) -> int:
    """
    Returns ISO day of the week for Christmas in the given year.
    
    The ISO day is an integer between 1 and 7.  It is 1 for Monday, 7 for Sunday 
    and the appropriate number for any day in-between. 
    
    Parameter year: The year to check for Christmas
    Precondition: years is an int > 0 (and a year using the Gregorian calendar)
    """
    assert isinstance(year, int), f'The parameter year must be an integer not {type(year)}.'
    assert year >= 1582, f'Must be a year using the gregorian calender not {year}'
    return datetime.date.isoweekday((datetime.date(year,12,25)))

if __name__ == '__main__':
    print(christmas_day(1984))