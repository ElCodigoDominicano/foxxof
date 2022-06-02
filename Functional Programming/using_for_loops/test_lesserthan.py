"""
Test script for the lesser function

Author: AERivas
Date: 05-31-2022
"""
from lesserthan import lesser
import unittest

class Tester(unittest.TestCase):

    def test_lesser(self):
        """
        Test procedure for function lesser().
        """
        print('Testing lesser()')
        tup = (5, 9, 5, 7, 3, 10, 4)

        result = lesser(tup,5)
        self.assertEqual(2,result)

        result = lesser(tup,4)
        self.assertEqual(1,result)

        result = lesser(tup,3)
        self.assertEqual(0,result)

        result = lesser(tup,6)
        self.assertEqual(4,result)

        result = lesser(tup,10)
        self.assertEqual(6,result)

        result = lesser(tup,20)
        self.assertEqual(7,result)

if __name__ == '__main__':
    unittest.main()
