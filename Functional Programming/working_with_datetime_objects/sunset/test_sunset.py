"""  
A completed test script for the module funcs

Author: Walker M. White
Date: November 30, 2019
"""
import datetime
import os.path
import json
import unittest

from sunset import str_to_time, sunset

class Tester(unittest.TestCase):

    def test_str_to_time(self):
        """
        Test procedure for the function str_to_time()
        """
        print('Testing str_to_time()')
        
        d = datetime.datetime(2016,4,15)
        result = str_to_time('2016-04-15')
        self.assertEqual(datetime.datetime,type(result))
        self.assertEqual(d,result)
        
        d = datetime.datetime(2019,10,12)
        result = str_to_time('October 12, 2019')
        self.assertEqual(datetime.datetime,type(result))
        self.assertEqual(d,result)
        
        result = str_to_time('Octover 12, 2019')
        self.assertEqual(None,result)
        
        d = datetime.datetime(2016,4,15,10,15,45)
        result = str_to_time('2016-04-15T10:15:45')
        self.assertEqual(datetime.datetime,type(result))
        self.assertEqual(d,result)
        
        d = datetime.datetime(2017,8,2,13,0,15)
        result = str_to_time('2017-08-02 13:00:15')
        self.assertEqual(datetime.datetime,type(result))
        self.assertEqual(d,result)
        
        d = datetime.datetime(2019,10,12,22,15)
        result = str_to_time('10:15 pm, October 12, 2019')
        self.assertEqual(datetime.datetime,type(result))
        self.assertEqual(d,result)
        
        d = datetime.datetime(2019,10,12,22,15)
        result = str_to_time('22:15 pm, October 12, 2019')
        self.assertEqual(None,result)

    def test_sunset(self):
        """
        Test procedure for the function sunset()
        """
        print('Testing sunset()')
        
        # Find the directory with this file in it
        parent = os.path.split(__name__)[0]
        filepath = os.path.join(parent,'daycycle.json')
        
        with open(filepath) as file_object:
            daycycle = json.loads(file_object.read())
        
        # TEST 1
        d = datetime.date(2017,8,2)
        e = datetime.datetime(2017,8,2,19,24)
        result = sunset(d,daycycle)
        self.assertEqual(datetime.datetime,type(result))
        self.assertEqual(e,result)
        
        # TEST 2
        d = datetime.date(2019,12,25)
        e = datetime.datetime(2019,12,25,16,38)
        result = sunset(d,daycycle)
        self.assertEqual(datetime.datetime,type(result))
        self.assertEqual(e,result)
        
        # TEST 3
        d = datetime.date(2016,6,2)
        e = datetime.datetime(2016,6,2,19,38)
        result = sunset(d,daycycle)
        self.assertEqual(datetime.datetime,type(result))
        self.assertEqual(e,result)
        
        # TEST 3
        d = datetime.date(2016,12,25)
        e = datetime.datetime(2016,12,25,16,39)
        result = sunset(d,daycycle)
        self.assertEqual(datetime.datetime,type(result))
        self.assertEqual(e,result)
        
        # TEST 5
        d = datetime.date(2014,6,2)
        result = sunset(d,daycycle)
        self.assertEqual(None,result)
        
        # TEST 6
        d = datetime.date(2022,12,25)
        result = sunset(d,daycycle)
        self.assertEqual(None,result)


if __name__ == '__main__':
    unittest.main()