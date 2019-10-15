def startsWith(phrase, word):
    if len(word) > len(phrase):
        return False
    for i in range(len(word)):
        if phrase[i] != word[i]:
            return False
    return True


guides = hero.findFriends()
for guide in guides:
    if startsWith(guide.id, "Mac"):
        while True:
            hero.move(guide.pos)
