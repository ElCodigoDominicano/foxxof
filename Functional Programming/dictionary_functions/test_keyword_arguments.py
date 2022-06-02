"""
Completed test script for keyword expansion

Author: AERivas
Date: 05-29-2022
"""
import unittest
from keyword_arguments import circ_area

class Tester(unittest.TestCase):

    def test_circ_area(self):
        """
        Test procedure for function circ_area().
        """
        print('Testing circ_area()')
        
        result = circ_area(radius=3)
        self.assertEqual(28.27433,result)
        
        result = circ_area(radius=2)
        self.assertEqual(12.56637,result)
        
        result = circ_area(diameter=4)
        self.assertEqual(12.56637,result)
        
        # Test for crashes
        try:
            circ_area()
            self.assertTrue(False) # We should never reach this line!
        except:
            pass
        
        try:
            circ_area(radius=3,diameter=6)
            self.assertTrue(False) # We should never reach this line!
        except:
            pass
        
        # extra test_case
        args = {'radius': 3,'bob': 2}
        result = circ_area(**args)
        self.assertEqual(28.27433,result)
 
if __name__ == '__main__':
    unittest.main()