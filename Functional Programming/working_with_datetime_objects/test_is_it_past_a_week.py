"""  
A completed test script for the past_a_week function

Author: AERivas
Date: 06-13-2022
"""
import unittest
import datetime

from is_it_past_a_week import past_a_week


class Tester(unittest.TestCase):

    def test_past_a_week(self):
        """
        Test procedure for the function past_a_week()
        """
        print('Testing past_a_week()')
        
        # Find the directory with this file in it
        d1 = datetime.date(2019,10,12)
        d2 = datetime.date(2019,10,25)
        d3 = datetime.date(2019,10,19)
        d4 = datetime.datetime(2019,10,12,9,45,15)
        d5 = datetime.datetime(2019,10,19,10,15)
        d6 = datetime.datetime(2019,10,19,8,30)
        
        result = past_a_week(d1,d2)
        self.assertEqual(True,result)
        
        result = past_a_week(d2,d1)
        self.assertEqual(False,result)
        
        result = past_a_week(d1,d3)
        self.assertEqual(True,result)
        
        result = past_a_week(d2,d3)
        self.assertEqual(False,result)
        
        result = past_a_week(d1,d5)
        self.assertEqual(True,result)
        
        result = past_a_week(d4,d5)
        self.assertEqual(True,result)
        
        result = past_a_week(d4,d6)
        self.assertEqual(True,result)
        print("Test Complete")

if __name__ == '__main__':
    unittest.main()