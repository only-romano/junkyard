def letterInWord(word, letter):
    for i in range(len(word)):
        if letter == word[i]:
            return True
    return False

spyLetter = "z"
friends = hero.findFriends()

for friend in friends:
    friendName = friend.id
    if letterInWord(friendName, spyLetter):
        hero.say(friendName + " is a spy!!!")
    else:
        hero.say(friendName + " is a friend.")
