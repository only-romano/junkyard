def vowel_indices(word):
    letters = []
    nums = []
    for letter in word:
        letters.append(letter)
        if letter in ('a', 'e', 'i', 'o', 'u'):
            nums.append(len(letters))
    return nums

print(vowel_indices("super"))