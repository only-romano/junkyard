# Fibonacci numbers
def fibs(_to, _from=0):
    '''
    Returns a given range of fibonacci sequence. Both indexes are included.
    fibonacci_sequence[_from:_to]

    param _to:   int [required] - upper index of requested range
    param _from: int [optional] - lower index of requested range

    returns: list - requested range of fibonacci sequence
    '''
    rev_ord = _from > _to
    if rev_ord: neg_end, pos_end = _to, _from
    else: neg_end, pos_end = _from, _to
    neg = neg_end < 0
    pos = pos_end > 0
    if pos_end < 0: rev_ord = not rev_ord


    def fib_a(end, neg=0):
        seq.append(0)
        if end > 1:
            seq.append(neg or 1)
            if end > 2:
                fib_b(end-2)
        neg and seq.reverse()

    def fib_b(reps):
        for i in range(reps):
            seq.append(seq[-2] + seq[-1])

    seq = [];
    if neg: fib_a(-neg_end, -1)
    if pos: fib_a(pos_end)
    if pos_end < 0: seq.reverse()
    seq = seq[-(pos_end-neg_end+1):]
    if rev_ord: seq.reverse()

    return seq


def fib(num):
    '''
    Runs a fibs function with given num param as fibs(end=num), and returns
    last element from fibs run result.

    param num:   int, required; requested number of fibonacci sequence
    returns:     int; number from fibonacci sequence
    '''
    if num == 0:
        return None
    return fibs(num)[-1]


if __name__ == '__main__':
    print(fibs(255, -255))
