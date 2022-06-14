"""
Function with while-loop that loop over positions.

Author: AERivas
Date: 06-04-2021
Updated: 06-02-2022
"""

def fixed_points(tup):
    """
    Returns a copy of tup, including only the "fixed points".
    
    A fixed point of a tuple is an element that is equal to its position in the tuple.
    For example 0 and 2 are fixed points of (0,3,2).  The fixed points are returned in
    the order that they appear in the tuple.
    
    Examples:
        fixed_points((0,3,2)) returns (0,2)
        fixed_points((0,1,2)) returns (0,1,2)
        fixed_points((2,1,0)) returns ()
    
    Parameter tup: the tuple to copy
    Precondition: tup is a tuple of ints
    """
    # You must use a while-loop, not a for-loop
    # Not done.
    result = ()
    position = 0

    while position < len(tup):  
        try:
            
            value = tup[position]
            index = tup.index(tup[position])
            # print(value, index)
            
            if value is index:
                result += (value,)
                position += 1
            if value is not index:
                # result += (value,)
                position += 1
            else:
                print('Que?')
                position += 1

        except ValueError:
            print('hi')
            position += 1
    # print(tup[position])

        #     if tup.index():
        #         #print(tup[position])
        #         result += (tup[position],)
        #         position += 1
        #     elif tup.index(position) != 0:
        #         position += 1
        # except ValueError:
        #     print(tup[position])
        #     position += 1
        # elif tup.index(tup[position]) not in tup:
        #     print(tup[position])
        #     
        #     position += 1
    return result

if __name__ == '__main__':
    print(fixed_points((0,3,2)))
    print(fixed_points((0,1,2)))
    print(fixed_points((2,1,0)))
    print(fixed_points((2,1,2,1)))
    print(fixed_points((2,2,2,2)))
