"""Simple Markup Program"""
import sys, re
from utils import *
from rules import *
from handlers import *


class Parser:
    """
    A Parser reads a text file, applying rules and controlling a handler.
    """
    def __init__(self, handler):
        self.handler = handler
        self.rules = []
        self.filters = []

    def addRule(self, rule):
        self.rules.append(rule)

    def addFilter(self, pattern, name):
        def filter(block, handler):
            return re.sub(pattern, handler.sub(name), block)
        self.filters.append(filter)

    def parse(self, file):
        page = []
        page.append(self.handler.start('document'))

        for block in blocks(file):
            for filter in self.filters:
                block = filter(block, self.handler)
            for rule in self.rules:
                if rule.condition(block):
                    last = rule.action(block, self.handler, page)
                    if last: break
        
        page.append(self.handler.end('document'))
        page_plain = "".join([s for s in page if isinstance(s, str)])

        return page_plain


class BasicTextParser(Parser):
    """
    A specific Parser that adds rules and filters in its
    constructor.
    """
    def __init__(self, handler):
        Parser.__init__(self, handler)
        self.addRule(ListRule())
        self.addRule(ListItemRule())
        self.addRule(TableRule())
        self.addRule(TableRowRule())
        self.addRule(TitleRule())
        self.addRule(HeadingRule())
        self.addRule(ParagraphRule())
        self.addFilter(r'\*(.+?)\*', 'emphasis')
        self.addFilter(r'(http://[\.a-zA-Z/]+)', 'url')
        self.addFilter(r'([\.a-zA-Z]+@[\.a-zA-Z]+[a-zA-Z]+)', 'mail')
        self.addFilter(r' \| ', 'td')


def main():
    handler = HTMLRenderer()
    parser = BasicTextParser(handler)
    print(parser.parse(sys.stdin))

if __name__ == '__main__':
    main()
