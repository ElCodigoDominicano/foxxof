"""
Test script for the findall function

Author: AERivas
Date: 06-05-2022
"""
from find_all import findall
import unittest

class Tester(unittest.TestCase):
        
    def test_findall(self):
        """
        Tests procedure for function findall().
        """
        print('Testing findall()')
        
        text = 'how now brown cow'
        result = findall(text,'ow')
        self.assertEqual((1, 5, 10, 15),result)
        
        result = findall(text,'brown')
        self.assertEqual((8,),result)
        
        result = findall(text,'cat')
        self.assertEqual((),result)
        
        result = findall('jeeepeeer','ee')
        self.assertEqual((1, 2, 5, 6),result)
        
        result = findall('','a')
        self.assertEqual((),result)
        
        result = findall('the cat in the hat had a sad','a')
        self.assertEqual((5, 16, 20, 23, 26),result)

if __name__ == '__main__':
    unittest.main()