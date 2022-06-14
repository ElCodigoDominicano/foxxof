"""
Module with a function to write CSV files (using data in a 2D list)

* The file may or may not exist
* data is a  2-dimensional list
* To be a proper CSV file, data must be a 2-dimensional list with the first row containing only strings.
* All other rows may be any Python value.
* Dates are converted using ISO formatting.
* all other objects are converted to their string representation.

Author: AERivas
Date: 06/12/2022
"""
import csv
from typing import List, Any

def write_csv(data: List[list[Any]], filename: str) -> None:
    """
    Writes the given data out as a CSV file filename.
    
    To be a proper CSV file, data must be a 2-dimensional list with the first row 
    containing only strings.  All other rows may be any Python value.  Dates are
    converted using ISO formatting. All other objects are converted to their string
    representation.
    
    Parameter data: The Python value to encode as a CSV file
    Precondition: data is a 2-dimensional list
    
    Parameter filename: The file to read
    Precondition: filename is a string representing a path to a file with extension
    .csv or .CSV.  The file may or may not exist.
    """
    assert isinstance(data, List), f'This function requires that data parameter is a list not {type(data)}.'
    assert isinstance(filename, str), f'filenames are usually strings not {type(filename)}.'
    
    table: List[list[Any]] = []
    with open(filename, 'w', newline='') as file_object:
        file_object_csv_writer = csv.writer(file_object)
        for row in data:
            table.append(row) 
        file_object_csv_writer.writerows(table)