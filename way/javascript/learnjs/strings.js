/*

var str = 'I\'m a JavaScript\u00A9 programmer.';
console.log(str, str.length, str.charAt(6), str[10], str.charAt(31)/* === '' /, str[31] );

var new_str =  str.slice(0, 6) + 'Acma' + str.slice(10);
console.log(new_str, new_str.toUpperCase(), new_str.toLowerCase() );
console.log( new_str.indexOf('Acma'), str.indexOf('m', 3), str.lastIndexOf('a') );

console.log( ~-1, ~0,  ~2);

if (~str.indexOf('Script')) {
    console.log( 'yes' )
}

var pos = 0;
while (true) {
    var foundPos = str.indexOf( 'a', pos);
    if (foundPos == -1) break;

    console.log( foundPos );
    pos = foundPos + 1;
}

console.log( str.substring(6,10), str.substring(25), str.substr(10,6), str.substr(22), str.substring(3,-1), str.slice(18, -8) );

console.log( String.fromCharCode(1072), str.charCodeAt(18) );

var charStr = '';
for (var i = 1034; i <= 1113; i++) {
    charStr += String.fromCharCode(i);
}

console.log( charStr );

*/

var s1 = 'done';
var s2 = 'dope';
console.log( s1 > s2, s1 > 'do', '2' > '14', 2 < '14' );

var s3 = 'Ёлки';
console.log( (s3.localeCompare("Яблони") === -1) ? 's3 is lesser' : '= or greater' );

function ucFirst(str) {
    return (str === '') ? '' : str[0].toUpperCase() + str.slice(1);
}

console.log( ucFirst('vasily'), ucFirst('') );

function checkSpam(str) {
    str = str.toLowerCase();
    return (~str.indexOf('viagra') || ~str.indexOf('xxx')) ? true : false;
}

console.log( checkSpam('buy ViAgrA now'), checkSpam('free xxxxx'), checkSpam('innocent rabbit') );

function truncate(str, maxLength) {
    return str.length <= maxLength ? str : str.slice(0,maxLength-3) + '...';
}

console.log( truncate('Here\'s something I want to tell you about', 20), truncate('Hello!', 20) );

function extractCurrencyValue(str) {
    var currencyValue = ''
    for (var i = 0; i < str.length; i++) {
        var char = +str.charCodeAt(i)
        if (char < 58 && char > 47 ) {
            currencyValue += str[i];
        }
    }
    return currencyValue;
}

console.log( extractCurrencyValue('$120'), extractCurrencyValue('s12ssswf124') );