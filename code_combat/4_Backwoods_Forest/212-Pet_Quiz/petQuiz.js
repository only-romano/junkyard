// Write an event handler function called onHear

// Complete the onHear function
function onHear(event) {
    // The pet should say something in onHear.
    pet.say("Yes.");
}

pet.on("hear", onHear);

hero.say("Do you understand me?");
hero.say("Are you a cougar?");
hero.say("How old are you?");
// Ask two more questions.
hero.say("Did you know all the words?");
hero.say("Well, ok. Cool.");
