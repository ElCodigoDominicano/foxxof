"""
Module with a function for reading JSON files (using dictionaries)

Author: AERivas
Date: 06-12-2022
"""
import json

def read_json(filename: str) -> dict:
    """
    Returns the contents read from the JSON file filename.
    
    This function reads the contents of the file filename, and will use the json module
    to covert these contents into a Python data value.  This value will either be a
    a dictionary or a list. 
    
    Parameter filename: The file to read
    Precondition: filename is a string, referring to a file that exists, and that file 
    is a valid JSON file
    """
    with open(filename) as file_object:
        text = file_object.read()
    data = json.loads(text)

    return data