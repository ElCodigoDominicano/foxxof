"""  
A completed test script for the string functions which use string methods.

Author: AERivas
Date: 5-16-2022 
"""
from firstinparens import first_in_parens
import unittest


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
    
# Script code
if __name__ == '__main__':
    unittest.main()
