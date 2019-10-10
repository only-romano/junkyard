#! usr/bin/python
"""
Simple urllib scrapper. python 2.7
"""
from urllib import urlopen
import re

p = re.compile('<h2>.*<a .* href="(.*?)".*>(.*?)</a>')
text = urlopen('https://python.org').read()

for url, name in p.findall(text):
    print '%s (%s)' % (name, url)
