"""
Reads a file and returns the number of lines, words, and characters - similar to
the UNIX wc utility
"""
from re import sub

class TextAnilize:

    def __init__(self, **qwargs):
        self._file = 'file' in qwargs and qwargs['file'] or 'file'
        self._text = 'text' in qwargs and qwargs['text'] or ''
        self._words = {'_len': 0}

    def load(self):
        try:
            lines = []
            words = []
            w_dict = {'_len': 0}
            with open(self._file, 'r') as file:
                for line in file:
                    lines.append(line)
                    print(line)
                    words.extend(line.split(' '))
            self._text = " ".join(lines)
            for word in words:
                word = word.strip()
                w_dict[word] = w_dict[word]+1 if word in w_dict else 1
                w_dict['_len'] += 1
            self._words = w_dict
        except Exception as e:
            raise e

    def set_file(self, file):
        self._file = file
        self._text = ''


def py_wc(file):
    infile = open(file) #open file
    lines = infile.read().split("\n")

    # init counters
    line_count = len(lines)
    word_count = 0
    char_count = 0

    for line in lines:
        words = line.split()
        word_count += len(words)
        char_count += len(line)

    return line_count, word_count, char_count

analizer = TextAnilize(file='prime_factors.py')
analizer.load()
