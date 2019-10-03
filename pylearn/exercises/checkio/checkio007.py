
def bigger_price(limit, data):
    """
        TOP most expensive goods
    """
    new_list = []
    while limit > 0:
        max_price = 0
        max_product = {}
        for value in data:
            if value['price'] > max_price:
                max_price = value['price']
                max_product = value
            else:
                pass
        new_list.append(max_product)
        data.remove(max_product)
        limit -= 1
    return new_list


if __name__ == '__main__':
    from pprint import pprint
    print('Example:')
    pprint(bigger_price(2, [
        {"name": "bread", "price": 100},
        {"name": "wine", "price": 138},
        {"name": "meat", "price": 15},
        {"name": "water", "price": 1}]))
    assert bigger_price(2, [
        {"name": "bread", "price": 100},
        {"name": "wine", "price": 138},
        {"name": "meat", "price": 15},
        {"name": "water", "price": 1}
    ]) == [
        {"name": "wine", "price": 138},
        {"name": "bread", "price": 100}
    ], "First"

    assert bigger_price(1, [
        {"name": "pen", "price": 5},
        {"name": "whiteboard", "price": 170}
    ]) == [{"name": "whiteboard", "price": 170}], "Second"