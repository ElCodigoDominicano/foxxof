"""
Module demonstrating an input-driven while loop

There is no test script for this module.  Run this module as a script to test it.

Author: AERivas
Date: 06-04-2021
Updated: 06-02-2022
"""

def count_inputs() -> str:
    """
    Returns the number of times the user chose to continue.
    
    This function repeated asks the user
        
        Keep going [y/n]? 
    
    If the user answers 'y', the function adds one to a counter and keeps going.
    If the user answers 'n', the function quits and returns the number of times
    that the user answered 'y'.  If the user answers anything else, the function
    responds with
        
        Answer unclear. Use 'y' or 'n'.
    
    It will not quit in this case, but it will not add to the counter either.
    """
    result = 0
    choice = ''
    while choice != 'n':
        choice = input("Keep going [y/n]? ")
        if choice == 'y':
            result += 1
        else:
             print("Answer unclear. Use 'y' or 'n'")
    return result
    
if __name__ == '__main__':
    result = count_inputs()
    plural = ' time.' if result == 1 else ' times.'
    print(f"You answered 'y' {str(result)+plural}")
