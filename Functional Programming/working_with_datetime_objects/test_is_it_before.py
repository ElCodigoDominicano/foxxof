"""  
A completed test script for the module func

Author: AERivas
Date: 06-13-2022
"""
import unittest
import datetime
from is_it_before import is_before

class Tester(unittest.TestCase):
        
    def test_is_before(self):
        """
        Test procedure for the function is_before()
        """
        print('Testing is_before()')
        d1 = datetime.date(2019,10,12)
        d2 = datetime.date(2019,10,15)
        d3 = datetime.datetime(2019,10,12,9,45,15)
        d4 = datetime.datetime(2019,10,12,10,15)
        
        result = is_before(d1,d2)
        self.assertEqual(True,result)
        
        result = is_before(d2,d1)
        self.assertEqual(False,result)
        
        result = is_before(d3,d4)
        self.assertEqual(True,result)
        
        result = is_before(d4,d3)
        self.assertEqual(False,result)
        
        result = is_before(d1,d3)
        self.assertEqual(True,result)
        
        result = is_before(d3,d1)
        self.assertEqual(False,result)
        
        result = is_before(d3,d3)
        self.assertEqual(False,result)
        
        result = is_before(d3,d3)
        self.assertEqual(False,result)
    

if __name__ == '__main__':
    unittest.main()