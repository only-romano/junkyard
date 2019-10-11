def second_index(text: str, symbol: str):
    """
        returns the second index of a symbol in a given text
    """
    y = []
    if text.find(symbol) != -1:
        x = text.find(symbol)
        for i in text:
            y.append(i)
        if y[x] != ' ':
            y[x] = ' '
        else:
            y[x] = '1'
        if ''.join(y).find((symbol)) != -1:
            return ''.join(y).find((symbol))
        else:
            return None
    else:
        return None


if __name__ == '__main__':
    print('Example:')
    print(second_index("sims", "s"))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert second_index("sims", "s") == 3, "First"
    assert second_index("find the river", "e") == 12, "Second"
    assert second_index("hi", " ") is None, "Third"
    assert second_index("hi mayor", " ") is None, "Fourth"
    assert second_index("hi mr Mayor", " ") == 5, "Fifth"
    print('You are awesome! All tests are done! Go Check it!')
