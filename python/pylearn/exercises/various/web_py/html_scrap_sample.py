#! usr/bin/python
# Python 2.7
# Simple scrapping using HTMLPArser
from urllib import urlopen
from HTMLParser import HTMLParser

class Scraper(HTMLParser):
    in_h4 = False
    in_link = False

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == 'h2':
            self.in_h4 = True
        if tag == 'a' and 'href' in attrs:
            self.in_link = True
            self.chunks = []
            self.url = attrs['href']

    def handle_data(self, data):
        if self.in_link:
            self.chunks.append(data)

    def handle_endtag(self, tag):
        if tag == 'h2':
            self.in_h4 = False
        if tag == 'a':
            if self.in_h4 and self.in_link:
                print '%s (%s)' % (''.join(self.chunks), self.url)
            self.in_link = False


text = urlopen('https://python.org').read()
parser = Scraper()
parser.feed(text)
parser.close()
