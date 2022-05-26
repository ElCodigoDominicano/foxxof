#Fox crawler -  Dec 5, 2017
import requests
from bs4 import BeautifulSoup

# Improve on this.. expand to other search engines
ulook = 'https://www.duckduckgo.com/html/?q='
ugrab = requests.get(ulook + input('What would you want me to query Sire? '))
soup = BeautifulSoup(ugrab.text, 'lxml')
results = soup.find_all("div", class_="web-result")
# Improve on this.. Give it a cleaner look, also research on capabilities of opening url (clickable links in terminal)
for meat in results[0:29]:
    print (" ".join(meat.text.splitlines()))


#Ultimately i want to create a 'search' bar on my desktop.. 
#Something similar to googles search bar on android devices..
