"""  
A completed test script for the list functions.

Author: AERivas
Date: May, 19 2022
"""
from list_examples2 import clamp, removeall
import unittest


class Tester(unittest.TestCase):
    def test_clamp(self):
        """
        Test procedure for function clamp().
        """
        print('Testing clamp()')
        
        alist = [-1, 1, 3, 5]
        result = clamp(alist,0,4)
        self.assertEqual([ 0, 1, 3, 4],result)
        self.assertEqual([-1, 1, 3, 5],alist)
        
        result = clamp(alist,-2,8)
        self.assertEqual([-1, 1, 3, 5],result)
        self.assertEqual([-1, 1, 3, 5],alist)
        
        result = clamp(alist,-2,-1)
        self.assertEqual([-1,-1,-1,-1],result)
        self.assertEqual([-1, 1, 3, 5],alist)
        
        result = clamp(alist,1,1)
        self.assertEqual([ 1, 1, 1, 1],result)
        self.assertEqual([-1, 1, 3, 5],alist)
        
        alist = [-1, 4, -1, 4, 2]
        result = clamp(alist,0,4)
        self.assertEqual([ 0, 4, 0, 4, 2],result)
        self.assertEqual([-1, 4,-1, 4, 2],alist)
        
        alist = [ 1, 3]
        result = clamp(alist,0,4)
        self.assertEqual([ 1, 3],result)
        self.assertEqual([ 1, 3],alist)
        
        alist = []
        result = clamp(alist,0,4)
        self.assertEqual([],result)
        self.assertEqual([],alist)


    def test_removeall(self):
        """
        Test procedure for removeall
        """
        print('Testing removeall()')
        
        alist = [1,2,2,3,1]
        result = removeall(alist,1)
        self.assertEqual([2,2,3],result)
        self.assertEqual([1,2,2,3,1],alist)
        
        result = removeall(alist,2)
        self.assertEqual([1,3,1],result)
        self.assertEqual([1,2,2,3,1],alist)
        
        result = removeall(alist,5)
        self.assertEqual([1,2,2,3,1],result)
        self.assertEqual([1,2,2,3,1],alist)
        
        alist = [3,3,3]
        result = removeall(alist,3)
        self.assertEqual([],result)
        self.assertEqual([3,3,3],alist)
        
        alist = [3,3,3]
        result = removeall(alist,1)
        self.assertEqual([3,3,3],result)
        self.assertEqual([3,3,3],alist)
        
        alist = [7]
        result = removeall(alist,7)
        self.assertEqual([],result)
        self.assertEqual([7],alist)
        
        alist = []
        result = removeall(alist,7)
        self.assertEqual([],result)
        self.assertEqual([],alist)


# Script code
if __name__ == '__main__':
    unittest.main()
    print('Module funcs is working correctly')