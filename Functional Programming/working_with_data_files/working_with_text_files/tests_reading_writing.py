"""  
A completed test script for the functions count_lines and_write lines

Author: AERivas
Date: 06-10-2022
"""
import unittest
import os.path

from reading_text import count_lines
from writing_text import write_numbers

class Tester(unittest.TestCase):
        
    def test_count_lines(self):
        """
        Test procedure for the function count_lines()
        """
        
        # Find the directory with this file in it
        parent = os.path.split(__name__)[0]
        
        filepath = os.path.join(parent,'files','readfile1.txt')
        result = count_lines(filepath)
        self.assertEqual(6,result)
        
        filepath = os.path.join(parent,'files','readfile2.txt')
        result = count_lines(filepath)
        self.assertEqual(23,result)
        
        filepath = os.path.join(parent,'files','readfile3.txt')
        result = count_lines(filepath)
        self.assertEqual(10,result)
    
    def test_write_numbers(self):
        """
        Test procedure for the function write_numbers()
        """
        print('Testing write_numbers()')
        
        # Find the directory with this file in it
        parent = os.path.split(__name__)[0]
    
        # TEST 1
        filepath = os.path.join(parent,'files','tempfile.txt')
        write_numbers(filepath,5)
        
        with open(filepath) as file_object:
            actual = file_object.read()
        
        filepath = os.path.join(parent,'files','writefile1.txt')
        with open(filepath) as file_object:
            correct = file_object.read()
         
        # Check file was created and are the same
        self.assertTrue(os.path.exists(filepath))
        self.assertEqual(correct,actual)
        
        # TEST 2
        filepath = os.path.join(parent,'files','tempfile.txt')
        write_numbers(filepath,16)
    
        with open(filepath) as file_object:
            actual = file_object.read()
    
        filepath = os.path.join(parent,'files','writefile2.txt')
        with open(filepath) as file_object:
            correct = file_object.read()
        
        # Check file was created and to check if its the same
        self.assertTrue(os.path.exists(filepath))
        self.assertEqual(correct,actual)
        
        # TEST 3
        filepath = os.path.join(parent,'files','tempfile.txt')
        write_numbers(filepath,26)

        with open(filepath) as file_object:
            actual = file_object.read()
        
        filepath = os.path.join(parent,'files','writefile3.txt')
        with open(filepath) as file_object:
            correct = file_object.read()        
        
        # Check file was created and to check if they are the same.
        self.assertTrue(os.path.exists(filepath))
        self.assertEqual(correct,actual)

if __name__ == '__main__':
    unittest.main()