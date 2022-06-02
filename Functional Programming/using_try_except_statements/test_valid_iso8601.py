"""
A test script for the function iso_8601.

Author: AERivas
Date: 06-03-2021
Updated: 06-02-2022
"""
from valid_iso8601 import iso_8601
import unittest

class Tester(unittest.TestCase):
        
    def test_iso_8601(self):
        """
        Test procedure for the function iso_8601()
        """
        print('Testing iso_8601()')

        result = iso_8601('00:00:00')
        self.assertTrue(result)

        result = iso_8601('12:35:15')
        self.assertTrue(result)

        result = iso_8601('3:302:05')
        self.assertFalse(result)

        result = iso_8601('33:00:205')
        self.assertFalse(result)

        result = iso_8601('aa:59:59')
        self.assertFalse(result)

        result = iso_8601('23:aa:59')
        self.assertFalse(result)

        result = iso_8601('')
        self.assertFalse(result)

        result = iso_8601('23:#9:00')
        self.assertFalse(result)

        result = iso_8601('@3:59:23')
        self.assertFalse(result)

        result = iso_8601(' :59:01')
        self.assertFalse(result)

        result = iso_8601('23:59:00')
        self.assertTrue(result)

        result = iso_8601('23:59:59')
        self.assertTrue(result)

        result = iso_8601('23:59:60')
        self.assertFalse(result)

        result = iso_8601('250000')
        self.assertFalse(result)

        result = iso_8601('23:59:4.')
        self.assertFalse(result)

        result = iso_8601('23:09:4')
        self.assertFalse(result)

        result = iso_8601('0:59:a59')
        self.assertFalse(result)
        
        print("Finished Performing Tests")
        
if __name__ == '__main__':
    unittest.main()
