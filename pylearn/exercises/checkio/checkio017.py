def checkio(text):
    ...
    newtext = map(text.lower().count(), filter(ord() in range(97, 123), [i for i in text.lower()]))
    repeats = 0
    frequency = newtext[0]
    for letter in newtext:
        #elif newtext.count(letter) > repeats:
            repeats = newtext.count(letter)
            #frequency = letter
        #if newtext.count(letter) == repeats:
            if ord(letter) < ord(frequency):
                frequency = letter
    return frequency

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio("Hello World!") == "l", "Hello test"
    assert checkio("How do you do?") == "o", "O is most wanted"
    assert checkio("One") == "e", "All letter only once."
    assert checkio("Oops!") == "o", "Don't forget about lower case."
    assert checkio("AAaooo!!!!") == "a", "Only letters."
    assert checkio("abe") == "a", "The First."
    print("Start the long test")
    assert checkio("a" * 9000 + "b" * 1000) == "a", "Long."
    print("The local tests are done.")
