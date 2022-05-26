"""  
A completed test script for the string functions which use string methods.

Author: AERivas
Date: 5-16-2022 
"""
import unittest
from string_methods import first_in_parens, isnetid

class Tester(unittest.TestCase):
        
    def test_first_in_parens(self):
        """
        Test procedure for first_in_parens
        """
        print('Testing first_in_parens()')
        
        test_cases = (
            'A (B) C',
            'A (B) (C) D',
            'A (B (C) D) E',
            'A ) B (C) D',
            'A () D',
            '(A D)'
        )
        self.assertEqual('B', first_in_parens(test_cases[0]))
        self.assertEqual('B', first_in_parens(test_cases[1]))
        self.assertEqual('B (C', first_in_parens(test_cases[2]))
        self.assertEqual('C', first_in_parens(test_cases[3]))
        self.assertEqual('', first_in_parens(test_cases[4]))
        self.assertEqual('A D', first_in_parens(test_cases[5]))
        
        print('Function first_in_parens() passed..')
    
    def test_isnetid(self):
        """
        Test procedure for isnetid
        """
        print('Testing isnetid()')
        
        test_cases = (
            'wmw2', #True
            'jrs1234', #True
            'ww9999', #True
            'Wmw2', #False
            'wMw2', #False
            'wmW2', #False
            'ww99a99', #False
            '#w999', #False
            'w#w999', #False
            'ww#999', #False
        )
        for string in test_cases:
            if string[0:len(string)].isupper():
                self.assertFalse(isnetid(string))
            if string.find('#') != -1:
                self.assertFalse(isnetid(string))
            if string[3].isnumeric() and (string.find('a') == 4):
                self.assertFalse(isnetid(string))
            
        print('Function isnetid() passed..')
# Script code
if __name__ == '__main__':
    unittest.main()
    print('Module first_parenthesis_isnetid is working correctly')