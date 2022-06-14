"""  
A completed test script for both reading and writing json functions.

Author: AERivas
Date: 06-12-2022
"""
import os.path
import unittest

from writing_json import write_json
from reading_json import read_json


FILE1 = {
    "2018-01-01T00:00:00-05:00": {
        "visibility": {
            "prevailing": 1.75,
            "units": "SM"
        },
        "wind": {
            "speed": 13.0,
            "crosswind": 5.0,
            "units": "KT"
        },
        "temperature": {
            "value": -15.0,
            "units": "C"
        },
        "sky": [
            {
                "cover": "clouds",
                "type": "broken",
                "height": 1200.0,
                "units": "FT"
            },
            {
                "type": "overcast",
                "height": 1800.0,
                "units": "FT"
            }
        ],
        "weather": [
            "light snow",
            "mist"
        ],
        "code": "201801010456Z"
    },
    "2017-12-31T23:00:00-05:00": {
        "visibility": {
            "prevailing": 1.75,
            "units": "SM"
        },
        "wind": {
            "speed": 13.0,
            "crosswind": 5.0,
            "units": "KT"
        },
        "temperature": {
            "value": -15.0,
            "units": "C"
        },
        "sky": [
            {
                "cover": "clouds",
                "type": "broken",
                "height": 1300.0,
                "units": "FT"
            },
            {
                "type": "overcast",
                "height": 2200.0,
                "units": "FT"
            }
        ],
        "weather": [
            "light snow",
            "mist"
        ],
        "code": "201801010356Z"
    },
    "2017-12-31T22:00:00-05:00": {
        "visibility": {
            "prevailing": 3.0,
            "units": "SM"
        },
        "wind": {
            "speed": 11.0,
            "crosswind": 7.0,
            "units": "KT"
        },
        "temperature": {
            "value": -15.0,
            "units": "C"
        },
        "sky": [
            {
                "type": "overcast",
                "height": 1300.0,
                "units": "FT"
            }
        ],
        "weather": [
            "light snow",
            "mist"
        ],
        "code": "201801010317Z"
    },
    "2017-12-31T21:00:00-05:00": {
        "visibility": {
            "prevailing": 10.0,
            "units": "SM"
        },
        "wind": {
            "speed": 10.0,
            "crosswind": 7.0,
            "units": "KT"
        },
        "temperature": {
            "value": -16.1,
            "units": "C"
        },
        "sky": [
            {
                "type": "overcast",
                "height": 1700.0,
                "units": "FT"
            }
        ],
        "code": "201801010156Z"
    }
}

FILE2 = [
    {
        "cover": "clouds",
        "type": "broken",
        "height": 1200.0,
        "units": "FT"
    },
    {
        "type": "overcast",
        "height": 1800.0,
        "units": "FT"
    }
]

class Tester(unittest.TestCase):


    def test_read_json(self):
        """
        Test procedure for the function read_json()
        """
        print('Testing read_json()')
        
        # Access the file relative to this one, not the user's terminal
        parent = os.path.split(__name__)[0]
        
        # First test
        fpath = os.path.join(parent,'files','readjson1.json')
        data  = read_json(fpath)
        
        self.assertEqual(type(data), dict)
        self.assertEqual(data, FILE1)
        
        # Second test
        fpath  = os.path.join(parent,'files','readjson2.json')
        data  = read_json(fpath)
        
        self.assertEqual(type(data), list)
        self.assertEqual(data, FILE2)

    def test_write_json(self):
        """
        Test procedure for the function write_json()
        """
        print('Testing write_json()')
        
        # Access the file relative to this one, not the user's terminal
        parent = os.path.split(__name__)[0]
        
        # First test (erase any existing file)
        fpath  = os.path.join(parent,'files','temp1.json')
        with open(fpath, 'w') as file_object:
            write_json(FILE1,fpath)
        
        # Check file was created
        self.assertTrue(os.path.exists(fpath))
        
        with open(fpath) as file_object:
            actual = file_object.read()
        
        fpath = os.path.join(parent,'files','readjson1.json')
        with open(fpath) as file_object:
            correct = file_object.read()
        
        # Check to see if they are the same with and without indentation
        self.assertEqual(unindent_json(correct),unindent_json(actual))
        self.assertEqual(correct,actual)
        
        # Second test (erase any existing file)
        fpath  = os.path.join(parent,'files','temp2.json')
        with open(fpath,'w') as file_object:
            write_json(FILE2,fpath)
        
        # Check file was created
        self.assertTrue(os.path.exists(fpath))
        
        with open(fpath) as file_object:
            actual = file_object.read()
        
        fpath = os.path.join(parent,'files','readjson2.json')
        with open(fpath) as file_object:
            correct = file_object.read()

        # Check to see if they are the same WITHOUT indentation
        self.assertEqual(unindent_json(correct),unindent_json(actual))
        # Check to see if they are the same WITH indentation
        self.assertEqual(correct,actual)

def unindent_json(text):
    """
    Returns an unindented version of a JSON string.
    
    This function is used for comparisons.  It allows us to check if the only
    thing wrong was indentation.
    """
    import json
    return json.dumps(json.loads(text))

if __name__ == '__main__':
    unittest.main()