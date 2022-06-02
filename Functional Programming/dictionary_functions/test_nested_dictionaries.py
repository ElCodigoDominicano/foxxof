"""
A completed test script for the weather reports

Author: AERivas
Date: 05-29-2022
"""
import unittest
from nested_dictionaries import reports_above_temp # from file import function

class Tester(unittest.TestCase):

    def test_reports_above_temp(self):
        """
        Test procedure for function reports_above_temp().
        """
        result = reports_above_temp(20)
        self.assertEqual(0,result)
        
        result = reports_above_temp(10)
        self.assertEqual(1,result)
        
        result = reports_above_temp(5)
        self.assertEqual(58,result)
        
        result = reports_above_temp(2)
        self.assertEqual(116,result)
        
        result = reports_above_temp(0)
        self.assertEqual(154,result)
        
        result = reports_above_temp(-2)
        self.assertEqual(258,result)
        
        result = reports_above_temp(-5)
        self.assertEqual(392,result)
        
        result = reports_above_temp(-10)
        self.assertEqual(505,result)
        
        result = reports_above_temp(-15)
        self.assertEqual(600,result)
        
        result = reports_above_temp(-20)
        self.assertEqual(646,result)

if __name__ == '__main__':
    unittest.main()