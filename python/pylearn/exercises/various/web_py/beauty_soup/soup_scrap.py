#! usr/bin/python
# Python 2.7
# A screen scraping program using Beautiful Soup
from urllib import urlopen
from BeautifulSoup import BeautifulSoup

text = urlopen('https://python.org').read()
soup = BeautifulSoup(text)

jobs = set()
for header in soup('h2'):
    links = header('a', 'reference')
    if not links: continue
    link = links[0]
    jobs.add('%s (%s)' % (link.string, link['href']))

print '\n'.join(sorted(jobs, key=lambda s: s.lower()))
