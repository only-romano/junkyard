highlanderName = "mac"


def wordInString(string, word):
    lenString = len(string)
    lenWord = len(word)
    for i in range(lenString - lenWord + 1):
        for j in range(lenWord):
            if string[i + j] != word[j]:
                break
            if j == lenWord - 1:
                return True
    return False


soldiers = hero.findFriends()
for soldier in soldiers:
    if wordInString(soldier.id, highlanderName):
        hero.say(soldier.id + " be ready.")

hero.say("ATTACK!!!");
