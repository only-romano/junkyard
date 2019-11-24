"""
Lister readme, long and uninteresting at all
"""

class Lister:
    def __repr__(self):
        return ("<Instance of %s, adress %s: \n%s") % \
            (self.__class__.__name__, id(self), self.attrnames())

    def attrnames(self):
        result = ''
        for attr in self.__dict__.keys():
            if attr[:2] == '__':
                result += '\tname %s=<built-in>\n' % attr
            else:
                result += '\tname %s=%s\n' % (attr, self.__dict__[attr])
        return result


if __name__ == '__main__':
    class Spam(Lister):
        def __init__(self):
            self.data_1 = 'food'

    x = Spam()
    print(x)

    class Super:
        def __init__(self):
            self.data_1 = 'spam'

    class Sub(Super, Lister):
        def __init__(self):
            Super.__init__(self)
            self.data_2 = "eggs"
            self.data_3 = 42

    x = Sub()
    print(x)
