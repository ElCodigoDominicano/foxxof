"""
Test script for the clamp function

Author: AERivas
Date: 05-31-2022
"""
from clamp import clamp
import unittest

class Tester(unittest.TestCase):

    def test_clamp(self):
        """
        Test procedure for function clamp().
        """
        print('Testing clamp()')
        
        result = clamp((-1, 1, 3, 5),0,4)
        self.assertEqual((0,1,3,4),result)
        
        result = clamp((-1, 1, 3, 5),-2,8)
        self.assertEqual((-1,1,3,5),result)
        
        result = clamp((-1, 1, 3, 5),-2,-1)
        self.assertEqual((-1,-1,-1,-1),result)
        
        result = clamp((-1, 1, 3, 5),1,1)
        self.assertEqual((1,1,1,1),result)
        
        result = clamp((1, 3),0,4)
        self.assertEqual((1,3),result)
        
        result = clamp((),0,4)
        self.assertEqual((),result)

if __name__ == '__main__':
    unittest.main()