def most_frequent(data):
    """
        determines the most frequently occurring string in the sequence.
    """
    return max({i: data.count(i) for i in data}.items(), key=lambda item: item[1])[0]


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert most_frequent([
        'a', 'b', 'c',
        'a', 'b',
        'a'
    ]) == 'a'

    assert most_frequent(['a', 'a', 'bi', 'bi', 'bi']) == 'bi'
    print('Done')
