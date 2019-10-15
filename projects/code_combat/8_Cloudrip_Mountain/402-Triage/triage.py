doctor = hero.findByType("paladin")[0]
mage = hero.findByType("pixie")[0]
helper = hero.findByType("peasant")[0]
soldiers = hero.findByType("soldier")

doctorPatients = []
magePatients = []
helperPatients = []

for soldier in soldiers:
    if soldier.maxSpeed < 6:
        magePatients.append(soldier)
    elif soldier.health < soldier.maxHealth / 2:
        doctorPatients.append(soldier)
    else:
        helperPatients.append(soldier)

mage.patients = magePatients
doctor.patients = doctorPatients
helper.patients = helperPatients
