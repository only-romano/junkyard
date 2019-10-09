# Usefull regex patterns
import re

words = '[a-zA-Z]+'
punctuation = r'[.?\-","]+'
web = r'www\.(.+)\.com$'
tag = (r'<\1>\2<\1>', r'(.+?)\*\*(.+?)\*\*')


if __name__ == '__main__':
    pat = '{name}'
    text = 'Dear {name}...'
    print(re.sub(pat, 'Roma', text))
    print(re.sub(tag[1], tag[0], 'div**This is inside** h2**This is inside too**'))
