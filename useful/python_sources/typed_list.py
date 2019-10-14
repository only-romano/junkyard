"""Typed List class"""
class TypedList(list):
    def __init__(self, example_element, initial_list=[]):
        self.type = type(example_element)
        if not isinstance(initial_list, list):
            raise TypeError("Second argument of TypedList must be a list.")
        for element in initial_list:
            self.__check(element)
        super().__init__(initial_list)

    def __check(self, element):
        if type(element) != self.type:
            raise TypeError("Attepted to add an element of incorrect type to \
                    a tiped list.")

    def __setitem__(self, i, element):
        self.__check(element)
        super().__setitem__(i, element)


if __name__ == '__main__':
    t = TypedList(1, [1,2,3])
    t.append("1")
    print(t)
