""" 
Function revrange using range-based and for-loop

Author: AERivas
Date: 06-02-2022
"""
def revrange(start,end):
    """
    Returns the tuple (b-1, b-2, ..., a)

    Note that this tuple is the reverse of tuple(range(a,b))

    Parameter start: the "start" of the range
    Precondition: start is an int <= end

    Parameter end: the "end" of the range
    Precondition: end is an int >= start
    """
    assert isinstance(start, int), f'parameter start: must be an integer not -> {type(start)}'
    assert isinstance(end, int), f'parameter end: must be an integer not -> {type(end)}'
    assert start < end, f'parameter start needs to be less than the end start -> {start} end -> {end}'
    return () if start == end else tuple([i for i in range(end-1,start-1,-1)])
