#! Занятие по книге Python Crash Course, chapter 6, "Dictionaries".
# Занятие пятое.

# Nesting - хранение библиотек, листов внутри библиотек или листов.

alien_0 = {
    0: {'color': 'green', 'points': 5, 'speed': 'slow'},
    1: {'color': 'yellow', 'points': 10, 'speed': 'medium'},
    2: {'color': 'red', 'points': 15, 'speed': 'fast'}
}

fleet_of_aliens = []        # Собираем флот инопланетян.

b = 0
while b in range(10):
    n = 0
    while n < 5:
        new_alien = alien_0.get(0)
        fleet_of_aliens.append(new_alien)
        new_alien = ''
        n += 1
    while n < 7:
        new_alien = alien_0.get(1)
        fleet_of_aliens.append(new_alien)
        n += 1
    new_alien = alien_0.get(2)
    fleet_of_aliens.append(new_alien)
    b += 1

for alien in fleet_of_aliens[:8]:
    print(alien)
print("...")
print(fleet_of_aliens)

print("Total number of aliens: " + str(len(fleet_of_aliens)))

aliens = []

# Make 30 green aliens.

for alien_number in range (0,30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

for alien in aliens[0:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10

print(aliens[0:8])

