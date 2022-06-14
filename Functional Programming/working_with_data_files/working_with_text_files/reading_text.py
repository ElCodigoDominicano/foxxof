"""
a simple function that reads from a file.

Author: AERivas
Date: 06-10-2022
"""
def count_lines(filepath: str) -> int:
    """
    Returns the number of lines in the given file.
    
    Lines are separated by the '\n' character, which is standard for Unix files.
    
    Parameter filepath: The file to be read
    Precondition: filepath is a string with the FULL PATH to a text file
    """
    assert isinstance(filepath, str), f'Filepaths are usually a string type not {type(filepath)}.'
    
    count: int = 0
    with open(filepath) as f:
        for lines in f:
            count += 1
    return count