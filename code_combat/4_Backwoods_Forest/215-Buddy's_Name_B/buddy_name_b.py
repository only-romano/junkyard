def sayHello(event):
    pet.say("Salutations.")

pet.on("hear", sayHello)
hero.say("Hello, my friend!")
