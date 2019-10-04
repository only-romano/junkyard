true = True
false = False
print(type(true))

apple = input('How much apples do you have? ')
try:
    apple = int(apple)
except Exception:
    apple = 1
print("Roma gives you another one, now you've got - %s, hurray, comrads!" % (apple + 1))

a = "Run fool!"
b = "Incoming gooks."
c = b + ' Alas! ' + a
print(c, len(a), len(b), len(c))

flamingo = "CHIKENFRY"
print(flamingo[3], flamingo[1:7], flamingo[:3], flamingo[3:], '\nThi\'s is cloudy day for our city.')

name = input("Input your name: ")
if name:
    print("Output your name:", name)

a = name
b = "Am"
c = "Grut"
print(a, b, c, "\nBye-Bye,", a)
print(a, b, c, sep="-")
print("Yeah, we get it")
print(a, b, c, sep="\n", end=".")

print(" Finaly it's over?")
for n in range(3):
    print('Yeeey!', end=" ")
print()

ans = input("Is this your bd-bd-bd? (Ay/not Ay)\n")
if ans == 'Ay':
    print("Happy BD-bd-BD you,", name)

year = input('Is new year eve today? (y/n)\n')
if year == "y":
    print("Happy Hannuka!")
    print("Get a fuck outta here")
else:
    print("Not New Year's Eve.")

for i in range(10):
    print(i, end=' ')
print()

for i in range(2, 11, 2):
    print(i, end=' ')
print()

for i in range(10, 0, -1):
    print(i, end=" ")
print()

answer = 'y'
while answer == 'y':
    print("Stop, Don't move")
    answer = input('Does monster friendly? (y/n)\n')
print('Run Fool Run!')

table = 7
for i in range(1, 13):
    print('What\'s', i, 'x', table, '?')
    guess = input()
    ans = i * table

    if guess == 'stop':
        break
    if guess == 'skip':
        print("Skipping")
        continue
    try:
        if int(guess) == ans:
            print('Correct')
        else:
            print("No, it\'s',", ans)
    except Exception:
        print('No')
print("Finished")

listA = [1, 2, 3]
listB = listA
listC = listA.copy()
listB[0] = 13
print("listA == %s, listB(=) == %s, listC(.copy()) == %s" % (listA, listB, listC))

top_num = 5
total = 0
for n in range(1, top_num+1):
    total = total + n
print('Sum of numbers from 1 to', top_num, '=', total)

name = "Roma"
for c in name:
    print(c, ord(c), bin(ord(c)))

print('Zo\u00EB \u2602')
