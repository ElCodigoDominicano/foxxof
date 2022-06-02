"""  
A completed test script for the function replace_first

Author: AERivas
Date: May 17, 2022
"""
import unittest
from replacefirst import replace_first_val

class Tester(unittest.TestCase):

    def test_replace_first(self):
        """
        Test procedure for replace_first
        """
        print('Testing replace_first()')
        
        test_cases = [
            ((1,2,3),1,4),
            ((1,2,3),2,4),
            ((1,2,3),3,4),
            ((1,2,3),5,4),
            ((1,2,1),1,4),
            ((1,2,1,2),2,4),
            ((2,),2,4),
            ((),2,4)
        ]

        self.assertEqual((4,2,3), replace_first_val(test_cases[0][0], test_cases[0][1], test_cases[0][2]))
        self.assertEqual((1,4,3), replace_first_val(test_cases[1][0], test_cases[1][1], test_cases[1][2]))
        self.assertEqual((1,2,4), replace_first_val(test_cases[2][0], test_cases[2][1], test_cases[2][2]))
        self.assertEqual((1,2,3), replace_first_val(test_cases[3][0], test_cases[3][1], test_cases[3][2]))
        self.assertEqual((4,2,1), replace_first_val(test_cases[4][0], test_cases[4][1], test_cases[4][2]))
        self.assertEqual((1,4,1,2), replace_first_val(test_cases[5][0], test_cases[5][1], test_cases[5][2]))
        self.assertEqual((4,), replace_first_val(test_cases[6][0], test_cases[6][1], test_cases[6][2]))
        self.assertEqual((), replace_first_val(test_cases[7][0], test_cases[7][1], test_cases[7][2]))

# Script code
if __name__ == '__main__':
    unittest.main()