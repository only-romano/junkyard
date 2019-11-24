class Processor:
    def __init__(self, reader, writer):
        self.reader = reader
        self.writer = writer
    def process(self):
        while True:
            data = self.reader.readline()
            if not data: break
            data = self.converter(data)
            self.writer.write(data)
    def converter(self, data):
        assert(0, 'Converter must be defined')


class Uppercase(Processor):
    def converter(self, data):
        return data.upper()


if __name__ == '__main__':
    import sys
    Uppercase(open('str_test.py'), sys.stdout).process()
