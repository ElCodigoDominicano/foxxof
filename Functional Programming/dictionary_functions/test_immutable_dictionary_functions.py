"""  
A completed test script for the immutable dictionary functions using 
deepcopy to prevent modifications happening to the original dictionary
as well as using the unittest framework to alongside some testcases for 
both functions.

Author: AERivas
Date: 05-29-2022
"""
import unittest
import copy
from immutable_dictionary_functions import average_grade, letter_grades

class Tester(unittest.TestCase):
    def test_average_grade(self):
        """
        Test procedure for function average_grade().
        """
        print('Testing average_grade()')
        
        grades = {'wmw2': 55, 'abc3': 90, 'jms45': 86}
        orignl = copy.deepcopy(grades)
        result = average_grade(grades)
        self.assertEqual(77.0,result)
        self.assertEqual(orignl,grades)
        
        grades = {'abc123': 0,'abc456':65,'jms457':50}
        orignl = copy.deepcopy(grades)
        result = average_grade(grades)
        self.assertEqual(38.333,result)
        self.assertEqual(orignl,grades)
        
        grades = {
            'abc123': 0,
            'abc456':65,
            'jms457':50,
            'jms123':60,
            'xyz123':70
            }
        orignl = copy.deepcopy(grades)
        result = average_grade(grades)
        self.assertEqual(49.0,result)
        self.assertEqual(orignl,grades)
        
        grades = {
            'abc123': 0,
            'abc456':65,
            'jms457':50,
            'jms123':60,
            'xyz123':70,
            'xyz456':80,
            'wmw4':90
            }
        orignl = copy.deepcopy(grades)
        result = average_grade(grades)
        self.assertEqual(59.286,result)
        self.assertEqual(orignl,grades)
        
        grades = {
            'abc123': 0,
            'abc456':65,
            'jms457':50,
            'jms123':60,
            'xyz123':70,
            'xyz456':80,
            'wmw4':90,
            'wmw5':100
            }
        orignl = copy.deepcopy(grades)
        result = average_grade(grades)
        self.assertEqual(64.375,result)
        self.assertEqual(orignl,grades)
        
        grades = {
            'abc123': 0,
            'abc456':65,
            'jms457':50,
            'jms123':60,
            'xyz123':70,
            'xyz456':80,
            'wmw4':90,
            'wmw5':100,
            'tor3':88
            }
        orignl = copy.deepcopy(grades)
        result = average_grade(grades)
        self.assertEqual(67.0,result)
        self.assertEqual(orignl,grades)
        
        grades = {'wmw2' : 55, 'abc3' : 90}
        orignl = copy.deepcopy(grades)
        result = average_grade(grades)
        self.assertEqual(72.5,result)
        self.assertEqual(orignl,grades)
        
        grades = {'abc3' : 90}
        orignl = copy.deepcopy(grades)
        result = average_grade(grades)
        self.assertEqual(90.0,result)
        self.assertEqual(orignl,grades)
        
        grades = {}
        orignl = copy.deepcopy(grades)
        result = average_grade(grades)
        self.assertEqual(0.0,result)
        self.assertEqual(orignl,grades)

    def test_letter_grades(self):
        """
        Test procedure for function letter_grades().
        """
        print('Testing letter_grades()')
        
        grades = {'wmw2': 55, 'abc3': 90, 'jms45': 86}
        answer = {'wmw2': 'F', 'abc3': 'A', 'jms45': 'B'}
        orignl = copy.deepcopy(grades)
        result = letter_grades(grades)
        self.assertEqual(answer,result)
        self.assertEqual(orignl,grades)
        
        grades = {'abc123': 0,'abc456':65,'jms457':50}
        answer = {'abc123': 'F','abc456':'D','jms457':'F'}
        orignl = copy.deepcopy(grades)
        result = letter_grades(grades)
        self.assertEqual(answer,result)
        self.assertEqual(orignl,grades)
        
        grades = {
            'abc123': 0,
            'abc456':65,
            'jms457':50,
            'jms123':60,
            'xyz123':70
            }
        answer = {
            'abc123': 'F',
            'abc456':'D',
            'jms457':'F',
            'jms123':'D',
            'xyz123':'C'
            }
        orignl = copy.deepcopy(grades)
        result = letter_grades(grades)
        self.assertEqual(answer,result)
        self.assertEqual(orignl,grades)
        
        grades = {
            'abc123': 0,
            'abc456':65,
            'jms457':50,
            'jms123':60,
            'xyz123':70,
            'xyz456':80,
            'wmw4':90
            }
        answer = {
            'abc123': 'F',
            'abc456':'D',
            'jms457':'F',
            'jms123':'D',
            'xyz123':'C',
            'xyz456':'B',
            'wmw4':'A'
            }
        orignl = copy.deepcopy(grades)
        result = letter_grades(grades)
        self.assertEqual(answer,result)
        self.assertEqual(orignl,grades)
        
        grades = {
            'abc123': 0,
            'abc456':65,
            'jms457':50,
            'jms123':60,
            'xyz123':70,
            'xyz456':80,
            'wmw4':90,
            'wmw5':100
            }
        answer = {
            'abc123': 'F',
            'abc456':'D',
            'jms457':'F',
            'jms123':'D',
            'xyz123':'C',
            'xyz456':'B',
            'wmw4':'A',
            'wmw5':'A'
            }
        orignl = copy.deepcopy(grades)
        result = letter_grades(grades)
        self.assertEqual(answer,result)
        self.assertEqual(orignl,grades)
        
        grades = {
            'abc123': 0,
            'abc456':65,
            'jms457':50,
            'jms123':60,
            'xyz123':70,
            'xyz456':80,
            'wmw4':90,
            'wmw5':100,
            'tor3':88
            }
        answer = {
            'abc123': 'F',
            'abc456':'D',
            'jms457':'F',
            'jms123':'D',
            'xyz123':'C',
            'xyz456':'B',
            'wmw4':'A',
            'wmw5':'A',
            'tor3':'B'
            }
        orignl = copy.deepcopy(grades)
        result = letter_grades(grades)
        self.assertEqual(answer,result)
        self.assertEqual(orignl,grades)
        
        grades = {'wmw2' : 55, 'abc3' : 90}
        answer = {'wmw2' : 'F', 'abc3' : 'A'}
        orignl = copy.deepcopy(grades)
        result = letter_grades(grades)
        self.assertEqual(answer,result)
        self.assertEqual(orignl,grades)
        
        grades = {'abc3' : 90}
        answer = {'abc3' : 'A'}
        orignl = copy.deepcopy(grades)
        result = letter_grades(grades)
        self.assertEqual(answer,result)
        self.assertEqual(orignl,grades)
        
        grades = {}
        answer = {}
        orignl = copy.deepcopy(grades)
        result = letter_grades(grades)
        self.assertEqual(answer,result)
        self.assertEqual(orignl,grades)

# Script code
if __name__ == '__main__':
   unittest.main()