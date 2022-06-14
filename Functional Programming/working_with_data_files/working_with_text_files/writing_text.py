"""
A simple function that writes numbers to a file.

* the number parameter are converted to strings first before written to a file
Author: AERivas
Date: 06-10-2022
"""

def write_numbers(filepath: str, number: int) -> None:
    """
    Writes the numbers 0..n-1 to a file.
    
    Each number is on a line by itself.  So the first line of the file is 0,
    the second line is 1, and so on. Lines are separated by the '\n' character, 
    which is standard for Unix files.  The last line (the one with the number
    n-1) should NOT end in '\n'
    
    Parameter filepath: The file to be written
    Precondition: filepath is a string with the FULL PATH to a text file
    
    Parameter number: The number of lines to write
    Precondition: number is an int > 0.
    """
    assert isinstance(filepath, str), f'Filepaths are usually of a string type not {type(filepath)}.'
    assert isinstance(number, int), f'Numbers are are usually of a integer type not {type(number)}.'

    numbers: list = []
    for lines in range(number):
        numbers.append(str(lines)+"\n")
    
    list_to_str: str = ''.join(numbers)
    with open(filepath, 'w') as file_object:
        file_object.write(list_to_str[:-1])
        

