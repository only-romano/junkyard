"""
Sorting Arrays

Usage:
    insertion(array)  # Insertion sort

"""

# Insertion sort
def insertion(array):
    newArr = []
    for el in array:
        past = None
        for i in range(len(newArr)):
            if newArr[i] > el:
                past = i
                break
        if past == None:
            newArr.append(el)
        else:
            newArr.insert(past, el)
    return newArr


if __name__ == '__main__':
    from random import randint
    array = []
    for i in range(10000):
        array.append(randint(-100000, 100000))
    print(insertion(array)[999])
