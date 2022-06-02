"""
Test script for the uniques function

Author: AERivas
Date: 05-31-2022
"""
from uniques import uniques
import unittest

class Tester(unittest.TestCase):


   def test_uniques(self):
        """
        Test procedure for function uniques().
        """
        print('Testing uniques()')
        
        result = uniques((5, 9, 5, 7))
        self.assertEqual(3,result)
        
        result = uniques((5, 5, 1, 'a', 5, 'a'))
        self.assertEqual(3,result)
        
        result = uniques((1, 2, 3, 4, 5))
        self.assertEqual(5,result)
        
        result = uniques((1,))
        self.assertEqual(1,result)
        
        result = uniques(())
        self.assertEqual(0,result)

if __name__ == '__main__':
    unittest.main()