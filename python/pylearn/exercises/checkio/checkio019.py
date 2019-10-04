def checkio(game_result):
    a = game_result
    if 'XXX' in game_result:
        return 'X'
    if a[0][0] + a[1][0] + a[2][0] == 'XXX':
        return 'X'
    if a[0][1] + a[1][1] + a[2][1] == 'XXX':
        return 'X'
    if a[0][2] + a[1][2] + a[2][2] == 'XXX':
        return 'X'
    if a[0][0] + a[1][1] + a[2][2] == 'XXX':
        return 'X'
    if a[0][2] + a[1][1] + a[2][0] == 'XXX':
        return 'X'
    if 'OOO' in game_result:
        return 'O'
    if a[0][0] + a[1][0] + a[2][0] == 'OOO':
        return 'O'
    if a[0][1] + a[1][1] + a[2][1] == 'OOO':
        return 'O'
    if a[0][2] + a[1][2] + a[2][2] == 'OOO':
        return 'O'
    if a[0][0] + a[1][1] + a[2][2] == 'OOO':
        return 'O'
    if a[0][2] + a[1][1] + a[2][0] == 'OOO':
        return 'O'
    return "D"

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio([
        "X.O",
        "XX.",
        "XOO"]) == "X", "Xs wins"
    assert checkio([
        "OO.",
        "XOX",
        "XOX"]) == "O", "Os wins"
    assert checkio([
        "OOX",
        "XXO",
        "OXX"]) == "D", "Draw"
    assert checkio([
        "O.X",
        "XX.",
        "XOO"]) == "X", "Xs wins again"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")

