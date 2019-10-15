def sayName(event):
    pet.say("My name is Furious Beast.")
    pet.say("But my friends call me Fluffy.")

pet.on("hear", sayName)
