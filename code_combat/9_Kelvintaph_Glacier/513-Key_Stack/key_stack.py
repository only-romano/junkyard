# Open doors and collect treasures.

peasant = hero.findByType("peasant")[0]

goldKey = peasant.findByType("gold-key")[0]
silverKey = peasant.findByType("silver-key")[0]
bronzeKey = peasant.findByType("bronze-key")[0]

# Command the peasant to pick up the gold and silver keys.
hero.command(peasant, "pickUpItem", goldKey)
hero.command(peasant, "pickUpItem", silverKey)
# Now, command the peasant to pick up the last key:


# Command the peasant to drop a key near the first door.
hero.command(peasant, "dropItem", {"x": 40, "y": 34})
# The second key -> the second door.
hero.command(peasant, "dropItem", {"x": 31, "y": 34})
# Drop the first (in the stack) key to the last door:


# Hurry and collect treasures!

