
def best_stock(data):
    max, best = 0, ''
    for k, v in data.items():
        if v > max:
            max = v
            best = k
        else:
            pass
    return best


if __name__ == '__main__':
    print("Example:")
    print(best_stock({
        'CAC': 10.0,
        'ATX': 390.2,
        'WIG': 1.2
    }))

