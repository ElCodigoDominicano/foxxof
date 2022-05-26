"""
Simple HTML Parser
- in order to use a byte string as a file object the function BytesIO is used.
- then use lxml htmls parser to parse the response
- used a simple query to find all <a> anchor tags using a for loop; these contain urls to other websites
"""
from io import BytesIO
from lxml import etree

import requests

url = 'https://nostarch.com'
r = requests.get(url)
content = r.content

parser = etree.HTMLParser()
content = etree.parse(BytesIO(content), parser=parser)

for link in content.findall('//a'):
    print(f"{link.get('href')} -> {link.text}")