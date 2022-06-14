"""
Module with a function for writing JSON files (using dictionaries)

Author: AERivas
Date: 06-12-2022
"""
import json
from typing import List, Any

def write_json(data: dict[str, dict[str, List]] or List[dict[str, Any]], filename: str) -> None:
    """
    Writes the given data out as a JSON file filename.
    
    To be a proper JSON file, data must be a a JSON valid type.  That is, it must be
    one of the following:
        (1) a number
        (2) a boolean
        (3) a string
        (4) the value None
        (5) a list
        (6) a dictionary
    The contents of lists or dictionaries must be JSON valid type.
    
    When written, the JSON data should be nicely indented four spaces for readability.
    
    Parameter data: The Python value to encode as a JSON file
    Precondition: data is a JSON valid type
    
    Parameter filename: The file to read
    Precondition: filename is a string representing a path to a file with extension
    .json or .JSON.  The file may or may not exist.
    """
    json_data = json.dumps(data,indent=4)
    with open(filename, 'w') as file_object:
        file_object.write(json_data)
