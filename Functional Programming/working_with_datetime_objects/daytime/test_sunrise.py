"""  
A completed test script for the str_to_time and daytime functions

Author: AERivas
Date: 06-14-2022
"""
import unittest
import os.path
import json

from sunrise import str_to_time, daytime

TIMES = [
    ('2015-06-05T07:00:00',True,True),
    ('2015-06-05T17:00:00',True,True),
    ('2015-10-31T06:00:00',False,True),
    ('2015-10-31T17:00:00',True,False),
    ('2015-11-17T07:00:00',True,True),  
    ('2015-11-17T17:00:00',False,False),
    ('2015-12-11T07:00:00',False,True), 
    ('2015-06-05T17:00:00',True,True),
    ('2016-11-01T07:00:00',True,True),  
    ('2016-11-01T17:00:00',False,False),
    ('2017-11-17T07:00:00',False,True), 
    ('2017-11-17T17:00:00',False,False),
    ('2018-06-05T07:00:00',True,True),  
    ('2018-06-05T17:00:00',True,True),
    ('2018-11-15T07:00:00',True,True),  
    ('2018-11-15T17:00:00',False,False),
    ('2019-11-15T07:00:00',True,True),  
    ('2019-11-15T17:00:00',False,False)
]

STRINGS = [
    '2016-05-12',
    '16:23',
    '16:23-4:00',
    '2016-05-12T16:23-4:00',
    '2016-05-12T16:23',
    '2016-05-12T16:23',
    '2016-05-12T16:23',
    '2016-05-12T16:23'
]

class Tester(unittest.TestCase):
        
    def test_str_to_time(self):
        """
        Test procedure for the function str_to_time()
        """
        print('Testing str_to_time()')
        
        from dateutil.parser import parse
        from pytz import timezone
        
        for string in STRINGS:
            result = str_to_time(string)
            self.assertEqual(parse(string), result)

            if len(string) == 16:
                correct = parse(string+'-4:00')
                result = str_to_time(string, correct.tzinfo)
                self.assertEqual(correct,result)
                
                correct = parse(string+'-5:00')
                offset = parse(string+'-4:00')
                result = str_to_time(string+'-5:00', offset)
                self.assertEqual(correct, result)
                
                central = 'America/Chicago'
                correct = timezone(central).localize(parse(string))
                result = str_to_time(string, central)
                self.assertEqual(correct, result)

    def test_daytime(self):
        """
        Test procedure for the function daytime()
        """
        print('Testing daytime()')
       
        parent = os.path.split(__name__)[0]
        filepath = os.path.join(parent,'daycycle.json')
        with open(filepath) as file_object:
            daycycle = json.loads(file_object.read())
    
        for time in TIMES:
            act  = str_to_time(time[0],"America/New_York")
            day  = daytime(act,daycycle)
            self.assertEqual(time[1], day)
            
            act  = str_to_time(time[0],"America/Chicago")
            day  = daytime(act,daycycle)
            self.assertEqual(time[2], day)


if __name__ == '__main__':
    unittest.main()