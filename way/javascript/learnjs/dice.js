let gameRules = {diceNumber: 2, maxAttempts: 3};

let firstCat = {name: 'Рыжик', points: 0};
let secondCat = {name: 'Снежик', points: 0};
let thirdCat = {name: 'Дымок', points: 0};

let cats = [firstCat, secondCat, thirdCat];


const runGame = function (rules, players) {
    for (let currentAttempt = 1; currentAttempt <= rules.maxAttempts; currentAttempt++) {

        for (let i = 0; i < players.length; i++) {
            let throwResult = getRandomArbitrary(1, 7);//(random 1 to 6)

            players[i].points += throwResult;
            console.log(players[i].name + ' выбросил ' + players[i].points);
        }
    }
    return players;
};

function getRandomArbitrary(min, max) {
    return Math.floor(Math.random() * (max - min)) + min;;
}

const getWinners = function (players) {
    let winners = [];
    let max = players[0];

    for (let i = 0; i < players.length; i++) {
        let current = players[i];

        if (current.points > max.points) {
            max = current;
            winners = [max];
        } else if (current.points === max.points) {
            winners.push(current);
        }
    }
    return winners;
};


const printWinners = function (winners) {

    if (winners.length === cats.length) {
        console.log('Все коты как на подбор!');
        return;
    }

    let message = (winners.length === 1) ? 'Победил ' : 'Победили ';

    for (let i = 0; i < winners.length; i++) {
        if (i >= 1) {
            message += ', ';
        }
        message += winners[i].name;
    }

    message += ' с количеством очков: ' + winners[0].points;

    console.log(message);
};

cats = runGame(gameRules, cats);
let winners = getWinners(cats);
printWinners(winners);