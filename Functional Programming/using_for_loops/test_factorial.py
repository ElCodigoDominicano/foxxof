"""
Test script for the function factorial

Author: AERivas
Date: 06-02-2022
"""

from factorial import factorial
import unittest

class Tester(unittest.TestCase):


    def test_factorial(self):
        """
        Test procedure for function factorial().
        """
        print('Testing factorial()')
        
        result = factorial(0)
        self.assertEqual(1,result)
        
        result = factorial(1)
        self.assertEqual(1,result)
        
        result = factorial(2)
        self.assertEqual(2,result)
        
        result = factorial(3)
        self.assertEqual(6,result)
        
        result = factorial(5)
        self.assertEqual(120,result)
        
        result = factorial(8)
        self.assertEqual(40320,result)

if __name__ == '__main__':
    unittest.main()