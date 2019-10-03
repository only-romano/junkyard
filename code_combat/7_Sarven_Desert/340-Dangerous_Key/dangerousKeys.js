// Listen to the paladin and fetch the right key.

function onHear(event) {
    // The pet can find the paladin and keys.
    var paladinUnit = pet.findNearestByType("paladin");
    var goldKey = pet.findNearestByType("gold-key");
    var silverKey = pet.findNearestByType("silver-key");
    var bronzeKey = pet.findNearestByType("bronze-key");
    var message = event.message;
    // If event.speaker is paladinUnit:
    if (event.speaker == paladinUnit) {
        // If event.message is "Gold":
        if (message == "Gold")
            // The pet should fetch the gold key.
            pet.fetch(goldKey);
        // If event.message is "Silver":
        else if (message == "Silver")
            // The pet should fetch the silver key.
            pet.fetch(silverKey);
        // If event.message is "Bronze":
        else if (message == "Bronze")
            // The pet should fetch the bronze key.
            pet.fetch(bronzeKey);
    }
}

pet.on("hear", onHear);
