"""
Test script for the fixed_points functions

Author: AERivas
Date: 06-01-2022
"""
from fixedpoints import fixed_points
import unittest

class Tester(unittest.TestCase):
   
    def test_fixed_points(self):
        """
        Test procedure for function fixed_points().
        """
        print('Testing fixed_points()')
        
        result = fixed_points((0,3,2)) 
        self.assertEqual((0,2),result)
        
        result = fixed_points((0,1,2,3))
        self.assertEqual((0,1,2,3),result)
        
        result = fixed_points((2,1,2,1))
        self.assertEqual((1,2),result)
        
        result = fixed_points((2,2,2,2))
        self.assertEqual((2,),result)
        
        result = fixed_points((3,2,1,0))
        self.assertEqual((),result)


if __name__ == '__main__':
    unittest.main()