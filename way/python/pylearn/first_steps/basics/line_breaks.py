#! Line breaks in 'print' function.

print(
    """1 line
    2 line
    3 line"""
)

print(
    '1 line\n'
    '2 line\n'
    '3 line')

# Separator parameter.
print(
    '1 line\n',
    '2 line\n',
    '3 line',
    sep='______\n')

# End paramerer.
print('hello', 'kato', sep=' ', end="!")
