"""
* FOR DEMONSTRATIONAL PURPOSES ONLY *
A simple webserver bruteforcer
- uses a wordlist from common brute forcers
- wordlist -> https://www.netsparker.com/blog/web-security/svn-digger-better-lists-for-forced-browsing/
- attempts to brute force directories and file locations on the target_server.
- run using "python bruter.py 2> /dev/null" to only see the successful requests.

- AERivas
"""
import queue
import requests
import threading
import sys

AGENT = "Mozilla/5.0 (X11; Linux x86_64; rv:19.0) Gecko/20100101 Firefox/19.0"
EXTENSIONS = ['.php', '.bak', '.orig', '.inc']
TARGET = "http://testphp.vulnweb.com/"
THREADS = 50
WORDLIST = "/home/foxhound/Downloads/all.txt"

def got_words(resume=None):
    """
    Returns found words from a supplied wordlist file after adding '/' before or after word.
    This function reads in a wordlist file, for every found word it attaches to the TARGET string
    words are placed in a queue while being found, incase of loss in connectivity
    it resumes from the last known word before the connection was severed.
    
    Parameter resume: A boolean -> True, False default: None
    Parameter word: A str -> 'admin.php' , "admin.html"
    """
    def extend_words(word):
        if '.' in word:
            words.put(f'/{word}')
        else:
            words.put(f'/{word}/')

        for extension in EXTENSIONS:
           words.put(f'/{word}{extension}')

    with open(WORDLIST) as f:
        raw_words = f.read()
    found_resume = False
    words = queue.Queue()
    for word in raw_words.split():
        if resume is not None:
            if found_resume:
                extend_words(word)
            elif word == resume:
                found_resume = True
                print(f'Resuming wordlist from: {resume}')    
        else:
            print(word)
            extend_words(word)
    return words

def dir_bruter(words):
    """
    This function accepts a queue object that is populated with words
    the words that are found within the got_words function with each 
    iterations of the word queue it creates a URL and attempts to 
    send the request to the target server and display if there was a success.

    Parameter words: str -> in this case from got_words function
    """
    headers = {'User-Agent': AGENT}
    while not words.empty():
        url = f'{TARGET}{words.get()}'
        try:
            r = requests.get(url, headers=headers)
        except requests.exceptions.ConnectionError:
            sys.stderr.write('x');sys.stderr.flush()
            continue

        if r.status_code == 200:
            print(f'\nSuccess ({r.status_code}): {url}')
        elif r.status_code == 404:
            sys.stderr.write('.');sys.stderr.flush()
        else:
            print(f'{r.status_code} => {url}')

if __name__ == '__main__':
    words = got_words()
    print('Press return to continue')
    sys.stdin.readline()
    for _ in range(THREADS):
        t = threading.Thread(target=dir_bruter, args=(words,))
        t.start()