"""  
A completed test script for christmas_day function

Author: AERivas
Date: 06-13-2022
"""
import unittest
import datetime

from when_was_christmas import christmas_day


class Tester(unittest.TestCase):

    def test_christmas_day(self):
        """
        Test procedure for the function christmas_day()
        """
        print('Testing christmas_day()')
        
        year = (
            2023,
            2022,
            2018,
            2017,
            2016,
            1984,
            2100
        )
        self.assertEqual(1, christmas_day(year[0]))
        self.assertEqual(7, christmas_day(year[1]))
        self.assertEqual(2, christmas_day(year[2]))
        self.assertEqual(1, christmas_day(year[3]))
        self.assertEqual(7, christmas_day(year[4]))
        self.assertEqual(2, christmas_day(year[5]))
        self.assertEqual(6, christmas_day(year[6]))

if __name__ == '__main__':
    unittest.main()