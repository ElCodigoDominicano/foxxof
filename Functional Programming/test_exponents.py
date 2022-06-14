"""
Test script for the exponential function

Author: AERivas
Date: 06/04/2022
"""
from exponents import exp
import unittest

class Tester(unittest.TestCase):
        
    def test_exp(self):
        """
        Test procedure for function exp().
        """
        print('Testing exp()')
        
        # Note that we round the result to ignore anything outside margin of error
        result = round(exp(1),5)
        self.assertEqual(2.71828, result)
        
        result = round(exp(1,1e-12),11)
        self.assertEqual(2.71828182846, result)
        
        result = round(exp(-2),5)
        self.assertEqual(0.13534, result)
        
        result = round(exp(-2,1e-12),11)
        self.assertEqual(0.13533528324, result)
        
        result = round(exp(8,1e-1),0)
        self.assertEqual(2981.0, result)
        
        result = round(exp(8),5)
        self.assertEqual(2980.95799, result)
        
        result = round(exp(8),11)
        self.assertEqual(2980.95798704173, result)
       
if __name__ == '__main__':
    unittest.main()