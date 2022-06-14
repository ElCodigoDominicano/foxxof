"""
Module with a function to read CSV files (converting them into a 2D list)

Author: AERivas
Date: 06/10/2022
"""
import csv
from typing import List

def read_csv(filename: str) -> List[list]:
    """
    Returns the contents read from the CSV file filename.
    
    This function reads the contents of the file filename and returns the contents as
    a 2-dimensional list. Each element of the list is a row, with the first row being
    the header. Cells in each row are all interpreted as strings; it is up to the 
    programmer to interpret this data, since CSV files contain no type information.
    
    Parameter filename: The file to read
    Precondition: filename is a string, referring to a file that exists, and that file 
    is a valid CSV file
    """ 
    assert isinstance(filename, str), f'Filenames are usually string types not {type(filename)}.'
    
    table: List[list] = []
    with open(filename) as commma_separated_values:
        wrap_csv = csv.reader(commma_separated_values)
        for row in wrap_csv:
            table.append(row)   
    return table