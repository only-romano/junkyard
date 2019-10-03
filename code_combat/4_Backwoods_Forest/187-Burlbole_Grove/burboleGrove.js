// Don't attack the burls!
// Functions can return a value.
// When a function is called, it will be equal to the value the function returns.

function shouldAttack(target) {
    // return false if target.type == "burl"
    // return false if no `target`
    if (!target || target.type == "burl") {
        return false;
    }
    
    // Otherwise, return true
    return true;
}

while(true) {
    var enemy = hero.findNearestEnemy();
    // Here we use shouldAttack() to decide if we should attack!
    // heroShouldAttack will be assigned the same value that shouldAttack() returns!
    var heroShouldAttack = shouldAttack(enemy);
    if(heroShouldAttack) {
        hero.attack(enemy);
    }
}
