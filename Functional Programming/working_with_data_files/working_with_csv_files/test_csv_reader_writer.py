"""  
A completed test script for read_csv and write_csv function.

Author: AERivas
Date: 06-11-2022
"""
import unittest
import os.path

from csv_reader import read_csv
from csv_writer import write_csv

FILE1 = [
    ['STUDENT','AIRPLANE','INSTRUCTOR','TAKEOFF','LANDING','FILED','AREA'],
    ['S00309','738GG','I076','2015-01-12T09:00:00-05:00','2015-01-12T11:00:00-05:00','VFR','Pattern'],
    ['S00308','133CZ','I053','2015-01-13T09:00:00-05:00','2015-01-13T12:00:00-05:00','VFR','Practice Area'],
    ['S00324','426JQ','I053','2015-02-04T11:00:00-05:00','2015-02-04T14:00:00-05:00','VFR','Cross Country'],
    ['S00319','811AX','I072','2015-02-06T13:00:00-05:00','2015-02-06T15:00:00-05:00','VFR','Pattern'],
    ['S00321','738GG','I072','2015-02-08T10:00:00-05:00','2015-02-08T13:00:00-05:00','VFR','Practice Area'],
    ['S00308','811AX','I072','2015-02-23T09:00:00-05:00','2015-02-23T13:00:00-05:00','VFR','Cross Country']
]

FILE2 = [
    ['TAIL NO','TYPE','CAPABILITY','ADVANCED','MULTIENGINE','ANNUAL','HOURS'],
    ['133CZ','Cessna 152','VFR','No','No','2016-04-15','88'],
    ['811AX','Cessna 152','VFR','No','No','2016-01-22','39'],
    ['426JQ','Cessna 152','VFR','No','No','2016-07-30','31']
    ]

class Tester(unittest.TestCase):

        
    def test_read_csv(self):
        """
        Test procedure for the function read_csv()
        """
        # Access the file relative to this one, not the user's terminal
        parent = os.path.split(__name__)[0]
        
        # First test
        fpath  = os.path.join(parent,'files','readcsv1.csv')
        table = read_csv(fpath)
        
        self.assertEqual(type(table), list)
        self.assertTrue(len(table) > 0 and type(table[0]) == list)
        self.assertTrue(len(table[0]) > 0 and type(table[0][0]) == str)
        self.assertEqual(table, FILE1)
        
        # Second test
        fpath  = os.path.join(parent,'files','readcsv2.csv')
        table = read_csv(fpath)
        
        self.assertEqual(type(table), list)
        self.assertTrue(len(table) > 0 and type(table[0]) == list)
        self.assertTrue(len(table[0]) > 0 and type(table[0][0]) == str)
        self.assertEqual(table, FILE2)
        print("read_csv complete")

    def test_write_csv(self):
        """
        Test procedures for the function write_csv()
        """
        print('Testing write_csv()')
        
        # Access the file relative to this one, not the user's terminal
        parent = os.path.split(__name__)[0]
        
        # First test (erase any existing file)
        fpath = os.path.join(parent,'files','temp1.csv')

        with open(fpath) as file_object:
            actual = file_object.read()
        
        fpath = os.path.join(parent, 'files', 'writecsv1.csv')
        with open(fpath) as file_object:
            correct = file_object.read()

        # Check if file was created and check if files are the same 
        self.assertTrue(os.path.exists(fpath))
        self.assertEqual(correct,actual)
        
        # Second test (erase any existing files)
        fpath  = os.path.join(parent,'files','temp2.csv')

        with open(fpath, 'w') as file_object:
            write_csv(FILE2, fpath)
       
        with open(fpath) as file_object:
            actual = file_object.read()

        fpath = os.path.join(parent, 'files', 'writecsv2.csv')
        with open(fpath) as file_object:
            correct = file_object.read()
         
        # Check if file was created and if the creations are the same
        self.assertTrue(os.path.exists(fpath))
        self.assertEqual(correct,actual)
        print("write_csv complete")

if __name__ == '__main__':
    unittest.main()