from xml.sax.handler import ContentHandler
from xml.sax import parse
import os
from handler_dispatcher import Dispatcher


def make_page(xml_path, dir_name="my_site"):
    """Makes webpage from given xml file in selected directory"""
    parse(xml_path, WebsiteXMLConstructor(dir_name))


class WebsiteXMLConstructor(Dispatcher, ContentHandler):
    """
    Build website files from XML file
    """

    passthrough = False

    def __init__(self, directory):
        self.directory = [directory]
        self.ensureDirectory()

    def ensureDirectory(self):
        path = os.path.join(*self.directory)
        if not os.path.isdir(path):
            os.makedirs(path)

    def characters(self, chars):
        if self.passthrough:
            self.out.write(chars)

    def defaultStart(self, name, attrs):
        if self.passthrough:
            self.out.write('<' + name)
            for key, val in attrs.items():
                self.out.write(' %s="%s"' % (key, val))
            self.out.write('>')

    def defaultEnd(self, name):
        if self.passthrough:
            self.out.write('</%s>' % name)

    def startDirectory(self, attrs):
        self.directory.append(attrs['name'])
        self.ensureDirectory()

    def endDirectory(self):
        self.directory.pop()

    def startPage(self, attrs):
        filename = os.path.join(*self.directory + [attrs['name'] + '.html'])
        self.out = open(filename, 'w')
        self.writeHeader(attrs['title'])
        self.passthrough = True

    def endPage(self):
        self.passthrough = False
        self.writeFooter()
        self.out.close()

    def writeHeader(self, title):
        self.out.write('<html>\n  <head>\n    <title>')
        self.out.write(title)
        self.out.write('</title>\n  </head>\n  <body>')

    def writeFooter(self):
        self.out.write('\n  <body>\n</html>\n')


def main():
    make_page('src/example.xml', 'src/example')

if __name__ == '__main__':
    main()
