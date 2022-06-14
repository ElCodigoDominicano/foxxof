"""
A simple function computing time elapsed

Author: AERivas
Date: 06-13-2022
"""
import datetime

first_hint = datetime.date or datetime.datetime
second_hint = datetime.date or datetime.datetime
def past_a_week(first_event: first_hint, second_event: second_hint) -> bool:
    """
    Returns True if event second_event happens at least a week (7 days) after d1.
    
    If first_event is after second_event, or less than a week has passed, this function returns False.
    Values first_event and second_event can EITHER be date objects or datetime objects.If a date object,
    assume that it happens at midnight of that day. 
    
    Parameter first_event: The first event
    Precondition: first_event is EITHER a date objects or a datetime object
    
    Parameter second_event: The first event
    Precondition: second_event is EITHER a date objects or a datetime object
    """
    assert isinstance(first_event, first_hint), f'The parameter must be a date or datetime object not {type(first_event)}.'
    assert isinstance(second_event, second_hint), f'The parameter must be a date or datetime object not {type(second_event)}.'

    seventh = first_event.day - second_event.day
    return False if first_event.day > second_event.day or seventh >= 7 else True