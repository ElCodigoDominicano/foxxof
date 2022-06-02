"""  
A completed test script for the nested list functions.

Author: AERivas
Date: May 21, 2022
"""
from nested_lists import row_sums, crossout
import unittest
import copy

class Tester(unittest.TestCase):
    def test_row_sums(self):
        """
        Test procedure for function row_sums().
        """
        print('Testing row_sums()')
        
        table = [[0.7, 0.0, -0.7, 1.0, -0.9]]
        # Snapshot table to make sure we do not modify
        orig = copy.deepcopy(table)
        result = row_sums(table)
        self.assertEqual([0.1],result)
        self.assertEqual(orig,table)
        
        table = [[0.7], [0.1], [0.4], [-0.2], [0.6]]
        # Snapshot table to make sure we do not modify
        orig = copy.deepcopy(table)
        result = row_sums(table)
        self.assertEqual([0.7, 0.1, 0.4, -0.2, 0.6],result)
        self.assertEqual(orig,table)
    
        table = [[0.7, 0.0, -0.7], [0.1, 0.4, -0.6]]    
        # Snapshot table to make sure we do not modify
        orig = copy.deepcopy(table)
        result = row_sums(table)
        self.assertEqual([0.0, -0.1],result)
        self.assertEqual(orig,table)
        
        table = [[0.7, 0.0, -0.7, 1.0, -0.9], 
                [0.1, 0.4, -0.6, 0.9, 0.2],
                [0.4, -0.1, -0.2, 0.1, -0.6], 
                [-0.2, 0.2, 0.2, -0.3, -0.2],
                [0.6, -0.1, -0.0, 0.8, 0.9]]
        # Snapshot table to make sure we do not modify
        orig = copy.deepcopy(table)
        result = row_sums(table)
        self.assertEqual([0.1, 1.0, -0.4, -0.3, 2.2],result)
        self.assertEqual(orig,table)


    def test_crossout(self):
        """
        Test procedure for function crossout().
        """
        print('Testing crossout()')
        
        table = [[0.1,0.3,0.5],[0.6,0.2,0.7],[1.5,2.3,0.4]]
        orig = copy.deepcopy(table)
        
        result = crossout(table,1,2)
        self.assertEqual([[0.1,0.3],[1.5,2.3]],result)
        self.assertEqual(orig,table)
      
        result = crossout(table,0,0)
        self.assertEqual([[0.2,0.7],[2.3,0.4]],result)
        self.assertEqual(orig,table)
    
        result = crossout(table,2,1)
        self.assertEqual([[0.1,0.5],[0.6,0.7]],result)
        self.assertEqual(orig,table)
        
        table = [[0.1,0.3,0.5],[0.6,0.2,0.7],[1.5,2.3,0.4],[0.1,0.2,0.3]]
        orig = copy.deepcopy(table)
        result = crossout(table,1,2)
        self.assertEqual([[0.1,0.3],[1.5,2.3],[0.1,0.2]],result)
        self.assertEqual(orig,table)
        
        table = [[0.1,0.3,0.5,1.0],[0.6,0.2,0.7,2.0],[1.5,2.3,0.4,3.0]]
        orig = copy.deepcopy(table)
        result = crossout(table,1,2)
        self.assertEqual([[0.1,0.3,1.0],[1.5,2.3,3.0]],result)
        self.assertEqual(orig,table)
        
        table = [[1,2],[3,4]]
        orig = copy.deepcopy(table)
        result = crossout(table,1,0)
        self.assertEqual([[2]],result)
        self.assertEqual(orig,table)
        
        result = crossout(table,0,1)
        self.assertEqual([[3]],result)
        self.assertEqual(orig,table)
        
        table = [[5]]
        orig = copy.deepcopy(table)
        result = crossout(table,0,0)
        self.assertEqual([],result)
        self.assertEqual(orig,table)


# Script code
if __name__ == '__main__':
    unittest.main()