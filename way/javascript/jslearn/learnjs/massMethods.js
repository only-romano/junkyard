/*
var names = 'Maria, Petro, Mary, Vasily';
var arr = names.split(', ');

for (var i = 0; i < arr.length; i++) console.log( "There's a mail for you,", arr[i] );

console.log( "a,b,c,d".split(',', 2), "some text".split('') );
console.log( arr.join('; '), new Array(4).join('la') ); // копирование строки (4-1) раз

delete arr[2];
console.log( arr[2], arr );

var array = ['I', 'am', 'learning', 'JavaScript'];
arr.splice(-2, 1, 'Annet');
console.log( arr, array.splice(2,1), array );
console.log(array.splice(0, 2, 'We', "are", 'learning'), array );
console.log(array.splice(99,0, 'now') , array);

var arrNum1 = [1, 2, 3, 4, 5];
var arrNum2 = arrNum1.slice(1,3);
console.log( arrNum2 );

arr = [1, 2, 15];
arr.sort();
console.log( arr );

function compareNumeric(a, b) {
    if (a > b) return 1;
    if (a < b) return - 1;
}

arr.sort( compareNumeric );
console.log( arr );
[1, -2, 15, 2, 0, 8].sort(function(a, b) {
    console.log( a + " <> " + b );
});

function compareNumericShort(a, b) {
    return a - b;
}

console.log( arr.reverse() );
var arr = [1, 2];
var newArr = arr.concat(3, 4);
console.log( newArr );
newArr = newArr.concat(5, [6, 7, 8], 9, [10]);
console.log( newArr );

arr = [1, 0, false];
console.log( arr.indexOf(false), arr.indexOf(0), arr.indexOf(null) );

arr = [1, 5, 1, 2, 3, 5, 1];
console.log( arr.indexOf(1, 3), arr.lastIndexOf(5) );

var store = {};
var items = ['div', 'a', 'form'];

for (var i = 0; i < items.length; i++) {
    var key = items[i];
    store[key] = true;
};

if (!store['h1']) {
    store['h1'] = true;
};
console.log( store );

var user = {
    name: 'Petro',
    age: 30
}

var keys = Object.keys(user);
console.log( keys );

var obj = {
    className: 'open menu'
}

function addClass(obj, cls) {
    var classes = obj.className ? obj.className.split(' ') : [];
    for (var i = 0; i < classes.length; i++) {
        if (classes[i] === cls) return obj;
    }
    obj.className = classes.concat(cls).join(' ');
}

addClass(obj, 'new');
addClass(obj, 'open');
addClass(obj, 'me');
console.log( obj.className );

function camelize(str) {
    var store = str.split('-');
    for (var i = 1; i < store.length; i++) {
        store[i] = store[i].slice(0,1).toUpperCase() + store[i].slice(1);
    }
    return store.join('');
}

console.log( camelize('background-color'), camelize('list-style-image'), camelize('-webkit-transition') );


var obj = {
    className: 'open my menu menu'
}

function removeClass(obj, cls) {
    var classes = obj.className ? obj.className.split(' ') : [];
    for (var i = classes.length - 1; i >= 0; i--) {
        if (classes[i] === cls) classes.splice(i, 1);
    }
    obj.className = classes.join(' ');
}

removeClass(obj, 'open');
removeClass(obj, 'blabla');
removeClass(obj, 'menu');
console.log( obj.className );


var arr = [5, 3, 8, 1];

function filterRangeInPlace(arr, a, b) {
    for (var i = arr.length - 1; i >= 0; i--) {
        if (arr[i] < a || arr[i] > b) arr.splice(i, 1);
    }
}

filterRangeInPlace(arr, 1, 4);
console.log( arr );


arr = [5, 2, 1, -10, 8];

function sortNumericReverse(a, b) {
    if (a > b) return -1;
    return 1;
}

arr.sort(sortNumericReverse);
console.log( arr );

var arr = ['Python', 'HTML', 'Java', 'CSS', 'JavaScript'];

function sortedClone(arr) {
    return arr.slice().sort();
}

console.log( sortedClone(arr), arr );


arr = [1, 2, 3, 4, 5];

function sortedRandom(a, b) {
    if (Math.round(Math.random())) return -1;
    return 1;
}

arr.sort(sortedRandom);
console.log( arr );


var vasily = { name: 'Vasily', age: 23 };
var masha = { name: 'Maria', age: 18 };
var vovochka = { name: 'Vladimir', age: 63 };
var people = [vovochka, vasily, masha ];

function sortObjAge(a, b) {
    return a.age - b.age;
}

people.sort(sortObjAge);
console.log( people, people[0].age );


var list = { value: 1 };
list.next = { value: 2 };
list.next.next = { value: 3 };
list.next.next.next = { value: 4 };

function printList(list) {
    var way = list;
    while (way.next) {
        console.log( way.value );
        way = way.next;
    }
    console.log( way.value );
}

printList(list);

var list = { value: 1 };
list.next = { value: 2 };
list.next.next = { value: 3 };
list.next.next.next = { value: 4 };

function printListRec(list) {
    console.log( list.value );
    if (list.next) printListRec(list.next);
}

printListRec(list);
console.log('\n');


function printListRecRev(list) {
    if (list.next) printListRecRev(list.next);
    console.log( list.value );
}

printListRecRev(list);
console.log('\n');


function pirntListReverse(list) {
    var way = list;
    var arr = [];
    while (way.next) {
        arr.push(way.value);
        way = way.next;
    }
    arr.push(way.value);
    for (var i = arr.length-1; i >= 0; i--) {
        console.log(arr[i]);
    }
}

pirntListReverse(list);

*/

var arr = ['voz', 'kiborg', 'korset', 'ZOV', 'grobik', 'koster', 'sektor'];
/*
function aclean(arr) {
    var finalArr = arr[0];
    for (var i = 1; i < arr.length; i++) {
        // kiborg
        for (var j = 0; j < finalArr.length; j++) {
            // 'voz'
            if (arr[i].length === finalArr[j].length) {
                for (var k = 0; k < arr[i].length; k++) {
                    if indexOf
                }
            }
        }
    }
}


'voz': 0, 'kiborg': 1, 'korset': 2, 'ZOV': 3, 'grobik': 4, 'koster': 5, 'sektor': 6
*/
function aclean(arr) {
    var dict = {}
    for (var i = 0; i < arr.length; i++) {
        var key = arr[i].toLowerCase().split('').sort().join('');
        dict[key] = arr[i];
    }
    finalArr = [];
    for (var key in dict) {
        finalArr.push(dict[key]);
    };
    return finalArr;
}

console.log( aclean(arr) );


var strings = ['krishna', 'krishna', 'hare', 'hare', 'hare', 'hare', 'krishna', 'krishna', '8-()'];

function unique(arr) {
    var dict = {}
    for (var i = 0; i < arr.length; i++) {
        dict[arr[i]] = true;
    }
    var finalArr = [];
    for (var key in dict) {
        finalArr.push(key);
    }
    return finalArr;
}

console.log( unique(strings) );