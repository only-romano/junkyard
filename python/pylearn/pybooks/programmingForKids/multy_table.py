for i in range(1, 11):
    for j in range(1, 11):
        a = i * j
        if a < 10:
            a = "  " + str(a)
        elif a < 100:
            a = " " + str(a)
        else:
            a = str(a)
        print(a, end=" ")
    print()
