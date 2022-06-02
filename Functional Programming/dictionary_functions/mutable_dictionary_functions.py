"""
Module demonstrating mutable functions on dictionaries.

All of these functions modify their dictionary arguments.

Author: AERivas
Date: 09-17-2021
Updated: 05-28-2022 [Updated code; type hints added and preconditions enforced.]
"""
from typing import Dict

def letter_grades(adict: Dict) -> None:
    """
    Modifies the new dictionary to replace numerical grades with letter grades.
    
    The dictionary adict has netids for keys and numbers 0-100 for values. These
    represent the grades that the students got on the exam. This function replaces
    all of the numerical grades with letter grades (strings) for values.
    
    Our cut-off is 90 for an A, 80 for a B, 70 for a C, 60 for a D. Anything below 60 
    is an F.
    
    Examples:
        If a = {'wmw2' : 55, 'abc3' : 90, 'jms45': 86}, letter_grades(a) changes
            a to {'wmw2' : 'F, 'abc3' : 'A', 'jms45': 'B'}.
        If a = {} letter_grades(a) changes a to {}
    
    Parameter adict: the dictionary of grades
    Precondition: adict is dictionary mapping strings to ints
    """
    assert isinstance(adict, Dict), 'The Parameter: adict must be a dictionary'
    
    for k,v in adict.items():
        if v in list(range(90,101)):
            v = 'A'
            adict.update({k:v})

        if v in list(range(80,90)):
            v = 'B'
            adict.update({k:v})

        if v in list(range(70,80)):
            v = 'C'
            adict.update({k:v})    
        
        if v in list(range(60,70)):
            v = 'D'
            adict.update({k:v})
        
        if v in list(range(0,60)):
            v = 'F'
            adict.update({k:v})

def drop_below(adict: Dict[str, int], limit: int) -> None:
    """
    Modifies a dictionary omitting the students whose grades are below limit.
    
    The dictionary adict has netids for keys and numbers 0-100 for values. These
    represent the grades that the students got on the exam.
    
    Examples: Suppose a = {'wmw2' : 55, 'abc3' : 90, 'jms45': 86}
        drop_below(a,60) changes a to {'abc3' : 90, 'jms45': 86}
        drop_below(a,90) changes a to {'abc3' : 90}
        drop_below(a,95) changes a to {}
        drop_below(a,50) leaves a unchanged as {'wmw2' : 55, 'abc3' : 90, 'jms45': 86}
    
    Parameter adict: the dictionary of grades
    Precondition: adict is dictionary mapping strings to ints
    
    Paramater limit: the cut-off boundary
    Precondition: limit is a number (int or float)
    """
    assert isinstance(adict, Dict), 'The Parameter: adict, must be a dictionary' 
    assert isinstance(limit, (int, float)), 'The Parameter: limit, must be an integer or a float'
    # This also works.. but this function is procedural, doesn't return-a-value.
    # This dictionary comprehension omits the student whose grade is less than the limit.
    # adict: Dict = {k: v for k, v in adict.items() if adict[k] < limit}
    # return above_limit
    for k in list(adict.keys()):
        if adict[k] < limit:
            adict.pop(k, None)
            
