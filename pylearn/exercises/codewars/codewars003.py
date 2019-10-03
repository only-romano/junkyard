#! Replace With Alphabet Position


def alphabet_position(text):
    string = ''
    for i in text:
        if 96 < ord(i.lower()) < 123:
            string += str(ord(i.lower()) - 96) + ' '
        else:
            pass
    return string.rstrip()


print(alphabet_position("The sunset sets at twelve o' clock."))
print(alphabet_position("The narwhal bacons at midnight."))
