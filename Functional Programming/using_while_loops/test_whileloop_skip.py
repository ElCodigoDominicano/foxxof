"""
Test script for the for-loop functions

Author: AERivas
Date: 06-04-2022
"""
import unittest
from whileloop_skip import skip

class Tester(unittest.TestCase):

    def test_skip(self):
        """
        Test procedure for function skip().
        """
        print('Testing skip()')

        result = skip('hello world',1)
        self.assertEqual('hello world',result)

        result = skip('hello world',2)
        self.assertEqual('hlowrd',result)

        result = skip('hello world',3)
        self.assertEqual('hlwl',result)

        result = skip('hello world',4)
        self.assertEqual('hor',result)

        result = skip('hello world',5)
        self.assertEqual('h d',result)

        result = skip('goodnight moon',4)
        self.assertEqual('gnto',result)

if __name__ == '__main__':
    unittest.main()