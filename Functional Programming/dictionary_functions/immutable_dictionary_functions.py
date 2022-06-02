"""
Module demonstrating immutable functions on dictionaries

All of these functions make use of accumulators.

Author: AERivas
Date: 09-17-2021
Updated: 05-27-2022 [updated code, added type hints, and preconditions enforced]
"""
from typing import Dict

def average_grade(adict: Dict[str, int]) -> int:
    """
    Returns the average grade among all students.

    The dictionary adict has netids for keys and numbers 0-100 for values.
    These represent the grades that the students got on the exam.  This function
    averages those grades and returns a value.

    Examples:
        average_grade({'wmw2' : 55, 'abc3' : 90, 'jms45': 86}) returns (55+90+86)/3 = 77
        average_grade({'wmw2' : 55}) returns 55
        average_grade({}) returns 0
    
    Parameter adict: the dictionary of grades
    Precondition: adict is dictionary mapping strings to ints
    """
    assert isinstance(adict, Dict), f'This program requires the use of a dictionary.'
    
    result: Dict = {k: v for k, v in adict.items()}
    if adict == {}:
        return 0
  
    return round(sum(result.values()) / len(result.values()), 3)

def letter_grades(adict: Dict[str, int]) -> Dict[str, str]:
    """
    Returns a new dictionary with the letter grades for each student.
    
    The dictionary adict has netids for keys and numbers 0-100 for values. These
    represent the grades that the students got on the exam. This function returns a 
    new dictionary with netids for keys and letter grades (strings) for values.
    
    Our cut-off is 90 for an A, 80 for a B, 70 for a C, 60 for a D. Anything below 60 
    is an F.
    
    Examples:  
        letter_grades({'wmw2' : 55, 'abc3' : 90, 'jms45': 86}) returns
            {'wmw2' : 'F, 'abc3' : 'A', 'jms45': 'B'}.
        letter_grades({}) returns {}
    
    Parameter adict: the dictionary of grades
    Precondition: adict is dictionary mapping strings to ints
    """
    assert isinstance(adict, Dict), f'This program requires the use of a dictionary.'
    
    result: Dict = {}
    for k,v in adict.items():
        if v in list(range(90,101)):
            v = 'A'
            result.update({k:v})
               
        if v in list(range(80,90)):
            v = 'B'
            result.update({k:v})

        if v in list(range(70,80)):
            v = 'C'
            result.update({k:v})    
        
        if v in list(range(60,70)):
            v = 'D'
            result.update({k:v})
        
        if v in list(range(0,60)):
            v = 'F'
            result.update({k:v})
    return result
# uncomment lines below to test within the terminal or an IDE that is equipped with pythons interpreter.
# if __name__ == '__main__':
    # example1 = average_grade({'wmw2' : 55, 'abc3' : 90, 'jms45': 86}) # returns (55+90+86)/3 = 77
    # example2 = average_grade({'wmw2' : 55}) # returns 55
    # example3 = average_grade({}) #returns 0
    # example4 = average_grade([1,2,3,4]) # to test assert statement
    # print(example1)
    # print(example2)
    # print(example3)
    # print(example4)
    # print()
    # example5 = letter_grades({'wmw2' : 55, 'abc3' : 90, 'jms45': 86}) # returns {'wmw2' : 'F, 'abc3' : 'A', 'jms45': 'B'}.
    # example6 = letter_grades({}) #returns {}
    # exmaple7 = letter_grades(['wmw2', 55, 'abc3', 90, 'jms45', 86]) # to test assert statement
    # print(example5)
    # print(example6)
    # print(example7)