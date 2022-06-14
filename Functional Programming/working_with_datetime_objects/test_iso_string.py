"""  
A completed test script for iso_str function

Author: AERivas
Date: 06-13-2022
"""
import unittest
import datetime

from iso_string import iso_str

class Tester(unittest.TestCase):
    
    def test_iso_str(self):
        """
        Test procedure for the function iso_str()
        """
        print('Testing iso_str()')
        
        d = datetime.date(2019,10,12)
        
        result = iso_str(d,datetime.time(12,35,15,205))
        self.assertEqual('2019-10-12T12:35:15.000205',result)
        
        result = iso_str(d,datetime.time(9,15))
        self.assertEqual('2019-10-12T09:15:00',result)
        
        result = iso_str(d,datetime.time(23,59,59))
        self.assertEqual('2019-10-12T23:59:59',result)
        
        d = datetime.date(1984,6,5)
        
        result = iso_str(d,datetime.time(12,35,15,205))
        self.assertEqual('1984-06-05T12:35:15.000205',result)
        
        result = iso_str(d,datetime.time(9,15))
        self.assertEqual('1984-06-05T09:15:00',result)
        
        result = iso_str(d,datetime.time(23,59,59))
        self.assertEqual('1984-06-05T23:59:59',result)
        print("Test Complete")

if __name__ == '__main__':
    unittest.main()