"""
Test script for the function revrange

Author: AERivas
Date: 06-02-2022
"""

from revrange import revrange
import unittest

class Tester(unittest.TestCase):


    def test_revrange(self):
        """
        Test procedure for function revrange().
        """
        print('Testing revrange()')
        
        result = revrange(0,3)
        self.assertEqual((2,1,0),result)
        
        result = revrange(0,4)
        self.assertEqual((3,2,1,0),result)
        
        result = revrange(5,10)
        self.assertEqual((9,8,7,6,5),result)
        
        result = revrange(0,10)
        self.assertEqual((9,8,7,6,5,4,3,2,1,0),result)

if __name__ == '__main__':
    unittest.main()