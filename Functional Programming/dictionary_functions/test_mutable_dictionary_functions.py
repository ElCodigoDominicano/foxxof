"""  
A completed test script for the mutable dictionary functions using 
deepcopy to prevent modifications happening to the original dictionary
as well as using the unittest framework to alongside some testcases for 
both functions.

Author: AERivas
Date: 05-28-2022
"""
import unittest
import copy
from mutable_dictionary_functions import letter_grades, drop_below

class Tester(unittest.TestCase):

    def test_letter_grades(self):
        """
        Test procedure for function letter_grades().
        """
        print('Testing letter_grades()')
        
        grades = {'wmw2': 55, 'abc3': 90, 'jms45': 86}
        answer = {'wmw2': 'F', 'abc3': 'A', 'jms45': 'B'}
        result = letter_grades(grades)
        self.assertEqual(None,result)
        self.assertEqual(answer,grades)
        
        grades = {'abc123': 0,'abc456':65,'jms457':50}
        answer = {'abc123': 'F','abc456':'D','jms457':'F'}
        result = letter_grades(grades)
        self.assertEqual(None,result)
        self.assertEqual(answer,grades)
        
        grades = {'abc123': 0,'abc456':65,'jms457':50,'jms123':60,'xyz123':70}
        answer = {'abc123': 'F','abc456':'D','jms457':'F','jms123':'D','xyz123':'C'}
        result = letter_grades(grades)
        self.assertEqual(None,result)
        self.assertEqual(answer,grades)
        
        grades = {'abc123': 0,'abc456':65,'jms457':50,'jms123':60,'xyz123':70,'xyz456':80,'wmw4':90}
        answer = {'abc123': 'F','abc456':'D','jms457':'F','jms123':'D','xyz123':'C','xyz456':'B','wmw4':'A'}
        result = letter_grades(grades)
        self.assertEqual(None,result)
        self.assertEqual(answer,grades)
        
        grades = {'abc123': 0,'abc456':65,'jms457':50,'jms123':60,'xyz123':70,
                'xyz456':80,'wmw4':90,'wmw5':100}
        answer = {'abc123': 'F','abc456':'D','jms457':'F','jms123':'D',
                'xyz123':'C','xyz456':'B','wmw4':'A','wmw5':'A'}
        result = letter_grades(grades)
        self.assertEqual(None,result)
        self.assertEqual(answer,grades)
        
        grades = {'abc123': 0,'abc456':65,'jms457':50,'jms123':60,'xyz123':70,
                'xyz456':80,'wmw4':90,'wmw5':100,'tor3':88}
        answer = {'abc123': 'F','abc456':'D','jms457':'F','jms123':'D',
                'xyz123':'C','xyz456':'B','wmw4':'A','wmw5':'A','tor3':'B'}
        result = letter_grades(grades)
        self.assertEqual(None,result)
        self.assertEqual(answer,grades)
        
        grades = {'wmw2' : 55, 'abc3' : 90}
        answer = {'wmw2' : 'F', 'abc3' : 'A'}
        result = letter_grades(grades)
        self.assertEqual(None,result)
        self.assertEqual(answer,grades)
        
        grades = {'abc3' : 90}
        answer = {'abc3' : 'A'}
        result = letter_grades(grades)
        self.assertEqual(None,result)
        self.assertEqual(answer,grades)
        
        grades = {}
        answer = {}
        result = letter_grades(grades)
        self.assertEqual(None,result)
        self.assertEqual(answer,grades)


    def test_drop_below(self):
        """
        Test procedure for function drop_below().
        """
        print('Testing drop_below()')
        orignl = {'wmw2': 55, 'abc3': 90, 'jms45': 86}
        grades = {'wmw2': 55, 'abc3': 90, 'jms45': 86}
        answer = {'abc3': 90, 'jms45': 86}
        result = drop_below(grades,20)
        self.assertEqual(None,result)
        self.assertEqual(orignl,grades)
        
        result = drop_below(grades,55)
        self.assertEqual(None,result)
        self.assertEqual(orignl,grades)
        
        result = drop_below(grades,60)
        self.assertEqual(None,result)
        self.assertEqual(answer,grades)
        
        grades = copy.deepcopy(orignl)
        result = drop_below(grades,86)
        self.assertEqual(None,result)
        self.assertEqual(answer,grades)
        
        grades = copy.deepcopy(orignl)
        result = drop_below(grades,95)
        self.assertEqual(None,result)
        self.assertEqual({},grades)
        
        orignl = {'abc123': 0,'abc456':65,'jms457':50,'jms123':60,'xyz123':70,
                'xyz456':80,'wmw4':90,'wmw5':100,'tor3':88}
        grades = copy.deepcopy(orignl)
        answer = {'xyz456':80,'wmw4':90,'wmw5':100,'tor3':88}
        
        result = drop_below(grades,0)
        self.assertEqual(None,result)
        self.assertEqual(orignl,grades)
        
        result = drop_below(grades,80)
        self.assertEqual(None,result)
        self.assertEqual(answer,grades)
        
        orignl = {'abc3' : 90}
        grades = {'abc3' : 90}
        result = drop_below(grades,90)
        self.assertEqual(None,result)
        self.assertEqual(orignl,grades)
        
        result = drop_below(grades,100)
        self.assertEqual(None,result)
        self.assertEqual({},grades)
        
        grades = {}
        result = drop_below(grades,0)
        self.assertEqual(None,result)
        self.assertEqual({},grades)



# Script code
if __name__ == '__main__':
    unittest.main()