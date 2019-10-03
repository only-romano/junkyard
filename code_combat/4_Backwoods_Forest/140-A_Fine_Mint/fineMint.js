// Peons are trying to steal your coins!
// Write a function to squash them before they can take your coins.

function pickUpCoin() {
    var coin = hero.findNearestItem();
    if(coin) {
        hero.moveXY(coin.pos.x, coin.pos.y);
    }
}

// Write the attackEnemy function below.
// Find the nearest enemy and attack them if they exist!
function attackEnemy() {
    var enemy = hero.findNearestEnemy();
    if (enemy) {
        if (hero.isReady("cleave")) {
            hero.cleave(enemy);
        } else {
            hero.attack(enemy);
        }
    }
}

while(true) {
    attackEnemy(); // ∆ Uncomment this line after you write an attackEnemy function.
    pickUpCoin();
}
