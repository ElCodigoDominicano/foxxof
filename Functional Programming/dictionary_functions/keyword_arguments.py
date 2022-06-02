"""
Module to demonstrate keyword expansion (**kwargs; keyword arguments).

Author: AERivas
Date: 09-17-2021
Updated: 05-29-2022 [Updated code; added typehints and preconditions enforced. ]
"""
import math
from typing import Dict, Tuple

def circ_area(**kwd: Dict[str,int]) -> [float]: 
    """
    Returns the area of the specified circle, defined by the keywords in kwd
    
    The area of a circle is PI r*r where r is the radius
    
    The circle may be specified by 'radius' or 'diameter', but not both.  This function
    should intentionally crash (with an AssertionError) if neither 'radius' nor 'diameter' 
    are specified, or if they both are.
    
    Any keyword arguments other than 'radius' or 'diameter' are ignored.
    
    Examples: 
        circ_area(radius=3) returns approx 28.27433
        circ_area(diameter=4) returns approx 12.56637
        circ_area(radius=3,foo=20) returns approx 28.27433
        circ_area() crashes with AssertionError
        circ_area(radius=2,diameter=4) crashes with AssertionError
    
    Parameter kwd: the function keyword arguments
    Precondition: the arguments are all numbers (int or float)
    """
    assert isinstance(kwd, Dict), 'This program requests the usage of dictionary. its keys are keyword arguments.'
    result = 0
    
    if len(kwd) > 1 and 'radius' and 'diameter' in kwd.keys():
        assert '', 'Either or Not Both.'
      
    elif 'radius' in kwd.keys():
        result += (kwd['radius'] * kwd['radius']) * math.pi
    
    elif 'diameter' in kwd.keys():
        result += kwd['diameter'] * math.pi

    elif 'foo' in kwd.keys():
        result += kwd['foo'] * 2 * math.pi
    
    elif 'bar' in kwd.keys():
        result += kwd['bar'] * 2 * math.pi
    
    else:
        assert '', 'Must not be empty'

    return round(result, 5)
    
# if __name__ == '__main__':
    # example1 = circ_area(radius=3) #returns approx 28.27433
    # example2 = circ_area(diameter=4) #returns approx 12.56637
    # example3 = circ_area(radius=3,foo=20) #returns approx 28.27433
    # example4 = circ_area() #crashes with AssertionError
    # example5 = circ_area(radius=2,diameter=4) #crashes with AssertionError
    # print(example1)
    # print(example3)
    # print(example2)