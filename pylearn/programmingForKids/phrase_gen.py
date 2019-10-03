from random import randint

def pick_word(words):
    return words[randint(0, len(words) - 1)]


name = ["Roma", "Kate", "Sergio", "Ginger", "Piggy", "Smokie", "Snow"]
verb = ["bought", "walks with", "eats", "kick", "love", "hate", "hug"]
noun = ["lion", "bicycle", "airplane", "watermelon", "life", "exercises", "little girl"]

play = True

print("Input something to continue, leave empty to exit. Press enter.")

while play:
    print(pick_word(name), pick_word(verb), pick_word(noun), end='.\n')
    play = input()
