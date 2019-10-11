from xml.sax.handler import ContentHandler
from xml.sax import parse

class Dispatcher:
    """Dispatcher for standart ContentHandler events to envoke"""
    def dispatch(self, prefix, name, attrs=None):
        mname = prefix + name.capitalize()
        dname = 'default' + prefix.capitalize()
        method = getattr(self, mname, None)

        if callable(method):
            args = ()
        else:
            method = getattr(self, dname, None)
            args = name,

        if prefix == 'start':
            args += attrs,
        if callable(method):
            method(*args)

    def startElement(self, name, attrs):
        self.dispatch('start', name, attrs)

    def endElement(self, name):
        self.dispatch('end', name)


"""Old test part"""

class HeadlineHandler(ContentHandler):
    in_headline = False

    def __init__(self, headlines):
        ContentHandler.__init__(self)
        self.headlines = headlines
        self.data = []

    def startElement(self, name, attrs):
        if name.lower() == 'h1':
            self.in_headline = True

    def endElement(self, name):
        if name.lower() == 'h1':
            text = ''.join(self.data)
            self.data = []
            self.headlines.append(text)
            self.in_headline = False

    def characters(self, string):
        if self.in_headline:
            self.data.append(string)


def main():
    headlines = []
    parse('src/site.xml', HeadlineHandler(headlines))
    print('The folowing <h1> elements were found:')
    for h in headlines:
        print(h)

if __name__ == '__main__':
    main()
