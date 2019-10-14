#! /usr/bin/env python3
"""
num_to_words: number to words convrsion module: contains function num2words.
"""
import sys, string, optparse

_1to9dict = {'0': '', '1': 'one', '2': 'two', '3': 'three', '4': 'four',
        '5': 'five', '6': 'six', '7': 'seven', '8': 'eight','9': 'nine'}
_10to19dict = {'0': 'ten', '1': 'eleven', '2': 'twelve', '3': 'thirteen',
        '4': 'fourteen', '5': 'fifteen', '6': 'sixteen', '7': 'seventeen',
        '8': 'eighteen', '9': 'nineteen'}
_20to90dict = {'2': 'twenty', '3': 'thirty', '4': 'forty', '5': 'fifty',
        '6': 'sixty', '7': 'seventy', '8': 'eighty', '9': 'ninety'}
_magnitude_list = [(0, ''), (3, ' thousand '), (6, ' million '),
        (9, ' billion '), (12, ' trillion '),(15, '')]


def num2words(num):
    """num2words(num): convert number to english words"""
    num = str(num)
    if num == '0':
        return 'zero'
    length = len(num)
    max_length = _magnitude_list[-1][0]
    if length > max_length:
        return "Sorry, can't handle numbers with more than {0} digits".format \
                (max_length)
    num = '00' + num
    num_word = ''
    for mag, name in _magnitude_list:
        if mag >= length:
            return num_word
        else:
            hundreds, tens, ones = num[-mag-3], num[-mag-2], num[-mag-1]
            if not (hundreds == tens == ones == '0'):
                num_word = _handle1to999(hundreds, tens, ones) + name + num_word

def _handle1to999(hundreds, tens, ones):
    if hundreds == '0':
        return _handle1to99(tens, ones)
    else:
        return _1to9dict[hundreds] + ' hundred ' + _handle1to99(tens, ones)

def _handle1to99(tens, ones):
    if tens == '0':
        return _1to9dict[ones]
    elif tens == '1':
        return _10to19dict[ones]
    else:
        return _20to90dict[tens] + ' ' + _1to9dict[ones]

def test():
    values = sys.stdin.read().split()
    for val in values:
        num = val.replace(',', '')
        print("{0} = {1}".format(val, num2words(num)))

def main():
    parser = optparse.OptionParser(usage=__doc__)
    parser.add_option("-t", "--test", dest="test", action='store_true',
            default=False, help="Test mode: reads from stdin")
    (options, args) = parser.parse_args()
    if options.test:
        test()
    else:
        if len(args) < 1:
            parser.error("incorrect number of arguments")
        num = sys.argv[1].replace(',', '')
        try:
            result = num2words(num)
        except KeyError:
            parser.error('argument contains non-digits')
        else:
            print("For {0}, say: {1}".format(sys.argv[1], result))


if __name__ == '__main__':
    main()
else:
    print("n2w loaded as module")
