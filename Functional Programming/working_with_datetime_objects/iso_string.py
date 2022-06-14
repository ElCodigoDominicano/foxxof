"""
A simple function using datetimes isoformat

Author: AERivas
Date: 06-13-2022
"""
import datetime

def iso_str(d: datetime.date,t: datetime.time) -> str:
    """
    Returns the ISO formatted string of data and time together.
    
    When combining, the time must be accurate to the microsecond.
    
    Parameter d: The month-day-year
    Precondition: d is a date object
    
    Parameter t: The time of day
    Precondition: t is a time object
    """
    assert isinstance(d, datetime.date), f'The paramater d must be a date object not {type(d)}.'
    assert isinstance(t, datetime.time),f'The parameter t must be a time object not {type(t)}.'
    return d.isoformat()+'T'+t.isoformat()
