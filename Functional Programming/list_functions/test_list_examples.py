"""  
A completed test script for the list functions.

Author: AERivas
Date: May 18, 2022
"""
from list_examples import put_in, rotate
import unittest


class Tester(unittest.TestCase):
    def test_put_in(self):
        """
        Test procedure for put_in
        """
        print('Testing put_in()')
        
        alist = [0,1,2,4]
        result = put_in(alist,3)
        self.assertEqual(None,result)
        self.assertEqual([0,1,2,3,4],alist)
        
        result = put_in(alist,-1)
        self.assertEqual(None,result)
        self.assertEqual([-1,0,1,2,3,4],alist)
        
        result = put_in(alist,2)
        self.assertEqual(None,result)
        self.assertEqual([-1,0,1,2,2,3,4],alist)
        
        result = put_in(alist,0)
        self.assertEqual(None,result)
        self.assertEqual([-1,0,0,1,2,2,3,4],alist)
        
        alist = []
        result = put_in(alist,0)
        self.assertEqual(None,result)
        self.assertEqual([0],alist)
        
        result = put_in(alist,1)
        self.assertEqual(None,result)
        self.assertEqual([0,1],alist)
        
        alist = ['a','aa','ab','b','ce']
        result = put_in(alist,'aab')
        self.assertEqual(None,result)
        self.assertEqual(['a','aa','aab','ab','b','ce'],alist)


    def test_rotate(self):
        """
        Test procedure for rotate
        """
        print('Testing rotate()')
        
        alist = [0,1,3,5]
        result = rotate(alist)
        self.assertEqual(None,result)
        self.assertEqual([5,0,1,3],alist)
        
        result = rotate(alist)
        self.assertEqual(None,result)
        self.assertEqual([3,5,0,1],alist)
        
        result = rotate(alist)
        self.assertEqual(None,result)
        self.assertEqual([1,3,5,0],alist)
        
        result = rotate(alist)
        self.assertEqual(None,result)
        self.assertEqual([0,1,3,5],alist)
        
        alist = [9]
        result = rotate(alist)
        self.assertEqual(None,result)
        self.assertEqual([9],alist)


# Script code
if __name__ == '__main__':
    unittest.main()
    print('Module funcs is working correctly')