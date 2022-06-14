"""
A simple function comparing datetime objects.

Author: AERivas
Date: 06-13-2022
"""
import datetime
d1_hint = datetime.date or datetime.datetime
d2_hint = datetime.date or datetime.datetime

def is_before(d1: d1_hint, d2: d2_hint) -> bool:
    """
    Returns True if event d1 happens before d2.
    
    Values d1 and d2 can EITHER be date objects or datetime objects.If a date object,
    assume that it happens at midnight of that day. 
    
    Parameter d1: The first event
    Precondition: d1 is EITHER a date object or a datetime object
    
    Parameter d2: The first event
    Precondition: d2 is EITHER a date object or a datetime object
    """
    assert isinstance(d1, d1_hint), f'The parameters d1 must be date or datetime objects not {type(d1)}.'
    assert isinstance(d2, d2_hint), f'The parameters d2 must be a date or datetime objects not {type(d2)}.'
    return True if str(d1) < str(d2) else False
