
def popular_words(text, words):
    a = text.lower().replace('\n', ' ').replace(',', ' ').replace('.', ' ').replace('!', ' ').split()
    lib = {}
    for word in words:
        if word.lower() in a:
            lib[word] = a.count(word)
        else:
            lib[word] = 0
    return lib


if __name__ == '__main__':
    print("Example:")
    print(popular_words('''
When I was One,
I had just begun.
When I was Two,
I was nearly new.
''', ['i', 'was', 'three']))

