"""  
A completed test script for the function iseurofloat.

Author: AERivas
Date: 06-02-2022

"""
from eurofloat import iseurofloat
import unittest
class Tester(unittest.TestCase):
    
    def test_iseurofloat(self):
        """
        Test procedure for the function iseurofloat()
        """
        print('Testing iseurofloat()')
        
        result = iseurofloat('12,5')
        self.assertEqual(True,result)
        
        result = iseurofloat('12,0')
        self.assertEqual(True,result)
        
        result = iseurofloat('0,5')
        self.assertEqual(True,result)
        
        result = iseurofloat('00,5')       # This is consistent with traditional float
        self.assertEqual(True,result)

        result = iseurofloat('-12,5')
        self.assertEqual(True,result)

        result = iseurofloat('12')
        self.assertEqual(False,result)

        result = iseurofloat('12,-5')
        self.assertEqual(False,result)

        result = iseurofloat(',5')
        self.assertEqual(False,result)
        
        result = iseurofloat('12,')
        self.assertEqual(False,result)
        
        result = iseurofloat('apple')
        self.assertEqual(False,result)
        
        result = iseurofloat('12,5.3')
        self.assertEqual(False,result)
        
        result = iseurofloat('12.5,3')
        self.assertEqual(False,result)
        
        result = iseurofloat('12,5,3')
        self.assertEqual(False,result)


if __name__ == '__main__':
    unittest.main()