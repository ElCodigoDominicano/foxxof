"""
A simple test script for avg()
Makes use of pythons unittest framework using the TestCase class (inheiritance) for simple testing.
Author: AERivas
Date: 05-20-2022
"""
import unittest
from tuple_expansion import avg

class Tester(unittest.TestCase):

    def test_avg(self):
        """
        Test procedure for function avg().
        """
        print('Testing avg()')
        
        result = avg()
        self.assertEqual(0,result)
        
        result = avg(7, 1, 4, 3, 6, 8)
        self.assertEqual(4.833333333333333,result)
        
        result = avg(-1, 1, 3, 5)
        self.assertEqual(2.0,result)
        
        result = avg(2.5)
        self.assertEqual(2.5,result)
        
        result = avg(1.0, 1.0, 1.0)
        self.assertEqual(1.0,result)
        
        # Test range(10,20) here
        tup = tuple(range(10,20))
        result = avg(*tup)
        self.assertEqual(14.5,result)

if __name__ == '__main__':
    unittest.main()
    print('Module func passed all tests.')