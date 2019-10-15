// Move to 'Eszter' and get three secret values from her.
hero.moveXY(24, 16);
var secretA = hero.findNearestFriend().getSecretA();
var secretB = hero.findNearestFriend().getSecretB();
var secretC = hero.findNearestFriend().getSecretC();

// Say "TRUE" to 'Tamas' if A AND B are true, OR if C is true. Otherwise, say "FALSE."
// Remember to use parentheses to do your logic in the proper order.
var tam = (secretA && secretB) || secretC;
hero.moveXY(19, 26);
hero.say(tam);

// Say "TRUE" to 'Zsofi' if A OR B is true, AND if C is true. Otherwise, say "FALSE."
hero.moveXY(26, 36);
hero.say((secretA || secretB) && secretC);

// Say "TRUE" to 'Istvan' if A OR C is true, AND if B OR C is true. Otherwise, say "FALSE."
hero.moveXY(37, 34);
hero.say((secretA || secretC) && (secretC || secretB));

// Say "TRUE" to 'Csilla' if A AND B are true, OR if B is true AND C is NOT true. Otherwise, say "FALSE."
hero.moveXY(40, 22);
hero.say((secretA && secretB) || (!secretC && secretB));

