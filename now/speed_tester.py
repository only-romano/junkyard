"""Test speed of functions with given sets of *args"""
from time import time
from random import randint

class Tester:
    def __init__(self, *funcs, **kwargs):
        self._funcs = funcs if len(funcs) else None
        self._func = funcs[0] if self._funcs else None
        self._reps = kwargs['reps'] if 'reps' in kwargs else 1000
        self._size = kwargs['args'] if 'args' in kwargs else 1000
        self._type = kwargs['type'] if 'type' in kwargs else int
        self._args = self._create_args()
        pass
    def _create_args(self):
        if self._type == int:
            return [self._get_int(x) for x in range(self._size)]
    def _test_one(self):
        start_time = time()
        for i in range(self._reps):
            self._func(*self._args)
        elapsed = time() - start_time
        return elapsed
