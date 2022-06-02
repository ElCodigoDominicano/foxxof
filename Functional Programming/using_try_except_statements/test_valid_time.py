"""  
A completed test script for the time functions.

This test script is more advanced than normal test scripts in that it uses try-except
statements to check that time_to_minutes enforces its preconditions.

Author: AERivas
Date: 06-02-2022
"""
from valid_time import valid_format, time_to_minutes, str_to_minutes
import unittest

class Tester(unittest.TestCase):

    def test_valid_format(self):
        """
        Test procedure for the function valid_format()
        """
        print('Testing valid_format()')

        result = valid_format('2:45 AM')
        self.assertEqual(True,result)
        
        result = valid_format('2:45 PM')
        self.assertEqual(True,result)
        
        result = valid_format('12:45 AM')
        self.assertEqual(True,result)
        
        result = valid_format('12:45 PM')
        self.assertEqual(True,result)
        
        result = valid_format('12:75 AM')
        self.assertEqual(False,result)
        
        result = valid_format('2:45PM')
        self.assertEqual(False,result)
        
        result = valid_format('14:45')
        self.assertEqual(False,result)
        
        result = valid_format('14:45 AM')
        self.assertEqual(False,result)
        
        result = valid_format('PM')
        self.assertEqual(False,result)
        
        result = valid_format(True)
        self.assertEqual(False,result)
        
        result = valid_format(245)
        self.assertEqual(False,result)


    def test_time_to_minutes(self):
        """
        Test procedure for the function time_to_minutes()
        """
        print('Testing time_to_minutes()')
        
        result = time_to_minutes('12:00 AM')
        self.assertEqual(0,result)
        
        result = time_to_minutes('12:00 PM')
        self.assertEqual(720,result)
        
        result = time_to_minutes('9:05 AM')
        self.assertEqual(545,result)
        
        result = time_to_minutes('11:15 AM')
        self.assertEqual(675,result)
        
        result = time_to_minutes('9:05 PM')
        self.assertEqual(1265,result)
        
        result = time_to_minutes('11:15 PM')
        self.assertEqual(1395,result)


    def test_str_to_minutes(self):
        """
        Test procedure for the function str_to_minutes()
        """
        print('Testing str_to_minutes()')
        
        result = str_to_minutes('12:00 AM')
        self.assertEqual(0,result)
        
        result = str_to_minutes('12:00 PM')
        self.assertEqual(720,result)
        
        result = str_to_minutes('9:05 AM')
        self.assertEqual(545,result)
        
        result = str_to_minutes('11:15 AM')
        self.assertEqual(675,result)
        
        result = str_to_minutes('9:05 PM')
        self.assertEqual(1265,result)
        
        result = str_to_minutes('11:15 PM')
        self.assertEqual(1395,result)
        
        result = str_to_minutes('12:75 AM')
        self.assertEqual(-1,result)
        
        result = str_to_minutes('2:45PM')
        self.assertEqual(-1,result)
        
        result = str_to_minutes('14:45')
        self.assertEqual(-1,result)
        
        result = str_to_minutes('14:45 AM')
        self.assertEqual(-1,result)
        
        result = str_to_minutes('PM')
        self.assertEqual(-1,result)
        
        result = str_to_minutes(True)
        self.assertEqual(-1,result)
        
        result = str_to_minutes(245)
        self.assertEqual(-1,result)

if __name__ == '__main__':
    unittest.main()
