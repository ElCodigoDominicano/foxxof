"""
REDACTED
Author: REDACTED
Date: REDACTED
"""

import introcs
import funcs

def test_matching_parens():
    """
    Test procedure for matching_parens
    """
    print('Testing matching_parens')
    result = funcs.matching_parens('((A) B (C))')
    introcs.assert_equals(True,result)
    
    result = funcs.matching_parens('A)) (B)) ((C))')
    introcs.assert_equals(True,result)
    
    result = funcs.matching_parens('A B (C)')
    introcs.assert_equals(True,result)

    result = funcs.matching_parens('A (B)) C')
    introcs.assert_equals(True,result)

    result = funcs.matching_parens('A (B) C')
    introcs.assert_equals(True,result)

    result = funcs.matching_parens('A B C)')
    introcs.assert_equals(False,result)

    result = funcs.matching_parens('A )B( C')
    introcs.assert_equals(False,result)
    
    result = funcs.matching_parens(')A )((B (C(')
    introcs.assert_equals(False,result)
    print("matching_parens passed its tests")
def test_first_in_parens():
    """
    Test procedure for first_in_parens
    """
    print('Testing first_in_parens')
    result = funcs.first_in_parens('((A) B (C))')
    introcs.assert_equals('(A',result)
    
    result = funcs.first_in_parens('A)) (B)) ((C))')
    introcs.assert_equals('B',result)
    
    result = funcs.first_in_parens('A B (C)')
    introcs.assert_equals('C',result)

    result = funcs.first_in_parens('A (B)) C')
    introcs.assert_equals('B',result)

    result = funcs.first_in_parens('()A ((B (C))')
    introcs.assert_equals('',result)

    #result = funcs.first_in_parens('A )B( C')
    #introcs.assert_equals(' ',result)
    
    #result = funcs.first_in_parens('A)) (B)) ((C))')
    #introcs.assert_equals('(B)',result)
    
    #result = funcs.first_in_parens('A B (C)')
    #introcs.assert_equals('(C)',result)

    #result = funcs.first_in_parens('A (B)) C')
    #introcs.assert_equals('(B)',result)
# Script Code
test_matching_parens()
test_first_in_parens()
print('Module funcs is working correctly')
