def bruteforceGCD(a, b):
    hero.say("The naive algorithm.")
    cycles = 0
    counter = b
    while True:
        cycles += 1
        if cycles > 100:
            hero.say("Calculating is hard. I'm tired.")
            break
        if a % counter == 0 and b % counter == 0:
            break
        counter -= 1
    hero.say("I used " + cycles + " cycles")
    return counter


def euclidianGCD (a, b):
    cycles = 0
    while b:
        cycles += 1
        b, a = a % b, b
    hero.say("I used " + cycles + " cycles")
    return a


friends = hero.findFriends()
num1 = friends[0].secretNumber
num2 = friends[1].secretNumber

if num2 > num1:
    num1, num2 = num2, num1

secretNumber = euclidianGCD(num1, num2)
hero.moveXY(48, 34)
hero.say(secretNumber)
hero.moveXY(68, 34)
