"""
Module demonstrating immutable functions on nested lists.

All of these functions make use of accumulators that make new lists.

Author: AERivas
Date: 09-15-2021
Updated: 05-21-2022 [Updated code ; Type hinting and Preconditions enforced]
"""

def row_sums(table: list[list]) -> list[list]:
    """
    Returns a list that is the sum of each row in a table.
    
    This function assumes that table has no header, so each row has only numbers in it.
    
    Examples: 
        row_sums([[0.1,0.3,0.5],[0.6,0.2,0.7],[0.5,1.1,0.1]]) returns [0.8, 1.5, 1.7]
        row_sums([[0.2,0.1],[-0.2,0.1],[0.2,-0.1],[-0.2,-0.1]]) returns [0.3, -0.1, 0.1, -0.3]
    
    Parameter table: the nested list to process
    Precondition: table is a table of numbers.  In other words, 
        (1) table is a nested 2D list in row-major order, 
        (2) each row contains only numbers, and 
        (3) each row is the same length.
    """
    assert type(table) == list, f'This function uses list datatypes in this case a table ->[1,[2,]] not -> {type(table)} '

    result = []
    for row in table:
        result.append(round(sum(row), 2))
    return result
  
def crossout(table: list[list], row: int, col: int) -> list[list]:
    """
    Returns a copy of the table, missing the given row and column.
      
    Examples:
        crossout([[1,3,5],[6,2,7],[5,8,4]],1,2) returns [[1,3],[5,8]]
        crossout([[1,3,5],[6,2,7],[5,8,4]],0,0) returns [[2,7],[8,4]]
        crossout([[1,3],[6,2]],0,0) returns [[2]]
        crossout([[6]],0,0) returns []
    
    Parameter table: the nested list to process
    Precondition: table is a table of numbers.  In other words, 
        (1) table is a nested 2D list in row-major order, 
        (2) each row contains only numbers, and 
        (3) each row is the same length.
    
    Parameter row: the row to remove
    Precondition: row is an index (int) for a row of table
    
    Parameter col: the colummn to remove
    Precondition: col is an index (int) for a column of table
    """
    # Deep copy used to prevent program from crashing during unittest!
    # The 'table' in the unittest file gets modified outside of this script without it!
    assert type(table) == list, f'This function uses the list datatype (in this case nested) not -> {type(table)}'
    assert type(row) and type(col) == int, 'Parameters row  and col must be a integer for this function to work'
    from copy import deepcopy

    result = deepcopy(table)
    for index, value in enumerate(result):
        if row == index:
            del result[row]
            for col_index, col_value in enumerate(result[0:]):  
                del result[col_index][col]
    return result

# Uncomment lines below to run 
# if __name__ == '__main__':
#     example_1 = row_sums([[0.1,0.3,0.5],[0.6,0.2,0.7],[0.5,1.1,0.1]]) # returns [0.8, 1.5, 1.7]
#     example_2 = row_sums([[0.2,0.1],[-0.2,0.1],[0.2,-0.1],[-0.2,-0.1]]) # returns [0.3, -0.1, 0.1, -0.3]
#     print(example_1)
#     print(example_2)
#     print()
#     example_3 = crossout([[1,3,5],[6,2,7],[5,8,4]],1,2) # returns [[1,3],[5,8]]
#     example_4 = crossout([[1,3,5],[6,2,7],[5,8,4]],0,0) # returns [[2,7],[8,4]]
#     example_5 = crossout([[1,3],[6,2]],0,0) # returns [[2]]
#     example_6 = crossout([[6]],0,0) # returns []
#     example_7 = crossout([[0.1,0.3,0.5],[0.6,0.2,0.7],[1.5,2.3,0.4]],1,2)
#     print(example_3)
#     print(example_4)
#     print(example_5)
#     print(example_6)
#     print(example_7)
