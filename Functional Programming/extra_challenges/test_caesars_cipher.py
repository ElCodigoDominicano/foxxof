"""
Test script for the encode function

Author: AERivas
Date: 06-05-2022
"""
from caesars_cipher import encode
import unittest

class Tester(unittest.TestCase):
        
    def test_encode(self):
        """
        Tests procedure for function encode().
        """
        print('Testing encode()')
        
        # Start with the original Caesar example
        result = encode('attackatdawn',3)
        self.assertEqual('dwwdfndwgdzq',result)
        
        # Decode with 26-3
        result = encode(result,23)
        self.assertEqual('attackatdawn',result)
        
        # Rot 13
        result = encode('attackatdawn',13) 
        self.assertEqual('nggnpxngqnja',result)
        
        result = encode(result,13)
        self.assertEqual('attackatdawn',result)
        
        result = encode('ordertheretreat',13)
        self.assertEqual('beqregurergerng',result)
        
        result = encode(result,13)
        self.assertEqual('ordertheretreat',result)
        
        # Once more test
        result = encode('letsmeetforlunch',10)
        self.assertEqual('vodcwoodpybvexmr',result)
        
        result = encode(result,16)
        self.assertEqual('letsmeetforlunch',result)
        
        # Empty string
        result = encode('',25)
        self.assertEqual('',result)



if __name__ == '__main__':
    unittest.main()