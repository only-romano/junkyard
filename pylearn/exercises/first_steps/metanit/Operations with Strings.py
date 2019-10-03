#! Metanit.com - Python: Chapter 2, lesson 5 "Operations with Strings".

# Strings, type (str), - both single and double quotes are possible.
name = "jesus"
surname = 'christ'
print(name.title(), surname.title())

# Uniot of several strings.
fullname = name + " " + surname
print(fullname.title())

# Bringing a variable's type to str for print function.
age = 33
info = "Name: " + fullname.title() + "\nAge: " + str(age)
print("\n" + info)

# Multiset strings.
print("""
\nYes! It's settled! Now and for ever\nI have left my dear old plain.
\nAnd the winged leaves of poplars will never\nRing and rustle above me again..
\nOur house will sag in my absence,\nAnd my dog died a long time ago.
\nMe, I'm fated to die with compassions\nIn the crooked streets of Moscow, I know.
\nI admire this city of elm - trees,\nWith decrepit buildings and homes.
\nGolden somnolent Asian entities\nAre reposing on temple domes.
\nWhen the moonlight at night, dissipated,\nShines...like hell in the dark sky of blue!
\nI walk down the alley, dejected,\nTo the pub for a drink, maybe, two.
\nIt's a sinister den, harsh and roaring,\nBut in spite of it, all through the night
\nI read  poems for girls that go whoring\nAnd carouse with thieves with delight.
\nNow I speak but my words are quite pointless,\nAnd the beat of my heart is fast:
\n- Just like you, I am totally worthless,\nAnd I cannot re - enter the past.
\nOur house will sag in my absence,\nAnd my dog died a long time ago.
\nMe, I'm fated to die with compassions\nIn the crooked streets of Moscow, I know.
\n\t\tSergey Esenin.""")

print("\n\nКафе \"Central Perk\"")

# The digital alphabet is smaller than the alphabetic one.  The upper
# case is smaller than the lower one ^^ :
str1 = "1a"
str2 = "aa"
print(str1 > str2)

str3 = "Aa"
print(str2 > str3)
print(str2 == str3)

print(str2.lower() == str3.lower())
