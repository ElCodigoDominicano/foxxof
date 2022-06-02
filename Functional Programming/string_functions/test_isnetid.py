"""  
A completed test script for isnetid.

Author: AERivas
Date: 5-16-2022 
"""
from isnetid import isnetid
import unittest

class Tester(unittest.TestCase):
        
    def test_isnetid(self):
        """
        Test procedure for isnetid
        """
        print('Testing isnetid()')
        
        test_cases = (
            'wmw2', #True
            'jrs1234', #True
            'ww9999', #True
            'Wmw2', #False
            'wMw2', #False
            'wmW2', #False
            'ww99a99', #False
            '#w999', #False
            'w#w999', #False
            'ww#999', #False
        )
        for string in test_cases:
            if string[0:len(string)].isupper():
                self.assertFalse(isnetid(string))
            if string.find('#') != -1:
                self.assertFalse(isnetid(string))
            if string[3].isnumeric() and (string.find('a') == 4):
                self.assertFalse(isnetid(string))
            
        print('Function isnetid() passed..')
# Script code
if __name__ == '__main__':
    unittest.main()