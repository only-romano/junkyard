active = True
dictionary = {"roma": "Godlike innocent eternal grace"}

while active:
	answer = input("Would you like to find (f) or set (s) description in " +
		"dictionary? Or do you want to quit (q)?\n\t").lower()
	if answer not in ["f", "s", "q"]:
		print("Well, I don't know that command...")
		continue
	elif answer == "q":
		print("Goodbye!")
		break
	elif answer == "f":
		answer = input("What word you like to find?\n\t").lower()
		if answer in dictionary.keys():
			print(dictionary[answer])
		elif len(answer):
			edit = input("Where still not this word in dictionary.. Whould you like" +
				" to add description (y)?\n").lower()
			if edit == "y":
				dictionary[answer] = input("Input your description for \"" + answer + "\":\n\t")
				print("Thank you!")
			else:
				print("Well, ok")
			continue
		else:
			print("You don't input any word...")
			continue
	else:
		answer = input("What word you like to set?\n\t").lower()
		if answer in dictionary.keys():
			edit = input("Where is a description for that word. Are you sure you" +
				"want to change it (y)?\n\t").lower()
			if edit == 'y':
				dictionary[answer] = input("Input your description for \"" + answer + "\":\n\t")
				print("Thank you!")
			else:
				print("Well, ok")
			continue
		elif len(answer):
			dictionary[answer] = input("Input your description for \"" + answer + "\":\n\t")
			print("Thank you!")
		continue

