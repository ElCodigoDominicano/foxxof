"""
* FOR DEMONSTRATIONAL PURPOSES ONLY *
A simple directory and filename mapper that come in a standard wordpress distribution

- Specifically this program targets HTML or text files which are more likely contain useful information
- Fingerprints a wordpress website.
-AERivas
"""

import contextlib
import os
import queue
import requests
import sys
import threading
import time

FILTERED = [".jpg",".gif",".png",".css"]
TARGET = "http://testphp.vulnweb.com/"
THREADS = 10

answers = queue.Queue()
web_paths = queue.Queue()

def gather_paths():
    """ 
    loops through all the files and directories in the local web application 
    while building the full paths to the target files while testing them against FILTERED
    to loop through files that are NOT being filtered out and adds the valid file to the web_paths queue object.
    """
    for root, _, files in os.walk('.'):
        for fname in files:
            if os.path.splitext(fname)[1] in FILTERED:
                continue
            path = os.path.join(root, fname)
            if path.startswith('.'):
                path = path[1:]
            print(path)
            web_paths.put(path)

def test_remote():
    """
    Loops until the web_paths queue is empty.
    gives us a success with a status code of 200
    the successful attemps are then saved into the answers queue object.        
    """
    while not web_paths.empty():
        path = web_paths.get()
        url = f'{TARGET}{path}'
        time.sleep(2)
        r = requests.get(url)
        if r.status_code == 200:
            answers.put(url)
            sys.stdout.write('+')
        else:
            sys.stdout.write('x')
        sys.stdout.flush()

def run():
    """
    starts amount supplied to THREADS and waits till all are complete using thread.join before stopping.
    """
    mythreads = list()
    for i in range(THREADS):
        print(f'Spawning thread {i}')
        t = threading.Thread(target=test_remote)
        mythreads.append(t)
        t.start()
    
    for thread in mythreads:
        thread.join()

@contextlib.contextmanager
def chdir(path):
    """
    navigates to the correct directory before the a call is made to the gather_paths function
   
    On enter, change directory to specified path.
    On exit, change directory back to original.
    """
    this_dir = os.getcwd()
    os.chdir(path)
    try:
        yield
    finally:
        os.chdir(this_dir)



if __name__ == '__main__':
    with chdir("/home/foxhound/BH_Python (current)/wordpress_tests"):
        gather_paths() 
    input('Press return to continue.')

    run()
    with open('myanswers.txt', 'w') as f:
        while not answers.empty():
            f.write(f'{answers.get()}\n')
    print('done')


    