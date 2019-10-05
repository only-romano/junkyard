/*
function makeCounter() {
    var currentCount = 1;

    return {
        getNext: function() {
        return currentCount++;
        },

        set: function(value) {
            currentCount = value;
        },

        reset: function() {
            currentCount = 1;
        }
    };
}

var counter = makeCounter();

console.log( counter.getNext() );
console.log( counter.getNext() );
counter.set(5);
console.log( counter.getNext() );
counter.reset();
console.log( counter.getNext() );

console.log();


function beautyCounter() {
    var currentCount = 1;

    function counter() {
        return currentCount++;
    }

    counter.set = function(value) {
        currentCount = value;
    };

    counter.reset = function() {
        currentCount = 1;
    };

    return counter;
}

var count = beautyCounter();

console.log( count() );
console.log( count() );
count.set(5);
console.log( count() );
count.reset();
console.log( count() );

function sum(a) {
    return function(b) {
        return a + b;
    };
}

console.log( sum(2)(4) );
console.log( sum(1)(2) );
console.log( sum(5)(-1) );


function makeBuffer() {
    var buffer = '';

    return function() { 
        arguments[0] !== undefined ? buffer += arguments[0].toString() : console.log(buffer)
    };
}

var buffer = makeBuffer();

buffer('Closures');
buffer(' are good');
buffer(' to use.');
buffer();

var buffer2 = makeBuffer();
buffer2(0);
buffer2(1);
buffer2(0);
buffer2();


function newBuffer() {
    var buffer = ''

    function buff() {
        arguments.length === 0 ? console.log(buffer) : buffer += arguments[0];
    }

    buff.clear = function() {
        buffer = '';
    }

    return buff;
}

var newBuf = newBuffer();

newBuf('Test');
newBuf(' is not gonna it you ');
newBuf();

newBuf.clear();
newBuf();

var users = [{
    name: 'Vasily',
    surname: 'Ivanov',
    age: 20
}, {
    name: 'Petro',
    surname: 'Chapaev',
    age: 25,
}, {
    name: 'Maria',
    surname: 'Medvedeva',
    age: 18
}];

users.sort(function(a,b) {
    return a.name > b.name ? 1 : -1;
});

users.sort(function(a,b) {
    return a.age > b.age ? 1 : -1;
});

users.sort(byField('name'));
users.forEach(function(user) {
    console.log( user.name );
});

users.sort(byField('age'));
users.forEach(function(user) {
    console.log( user.name );
});

function byField(field) {
    function sortByField(a, b) {
        switch (field) {
            case 'name':
                return a.name > b.name ? 1 : -1;
            case 'surname':
                return a.surname > b.surname ? 1 : -1;
            case 'age':
                return a.age > b.age ? 1 : -1;
        }
        return a[field] > b[field] ? 1 : -1;  // уже после дописано, с утра что-то не додумался
    }
    return sortByField;
}

*/

function filter(arr, func) {
    var filteredArr = [];
    for (var i = 0; i < arr.length; i++) {
        var x = arr[i];
        if (func(x)) filteredArr.push(x);
    }
    return filteredArr;
}

function inBetween(a, b) {
    return function(c) {
        return c >= a && c <= b;
    }
}

function inArray(arr) {
    return function(c) {
        return arr.indexOf(c) === -1 ? false : true;
    }
}

var arr = [1, 2, 3, 4, 5, 6, 7];

console.log( filter(arr, function(a) {
    return a % 2 == 0;
}));

console.log( filter(arr, inBetween(3, 6)) );
console.log( filter(arr, inArray([1, 2, 10])) );


function makeArmy() {

    var shooters = [];

    for (var i = 0; i < 10; i++) {
        var shooter = function(a) {
            return function() {
                console.log( a )
            };
        };
        shooters.push(shooter(i));
    }

    return shooters;
}

var army = makeArmy();

army[0]();
army[5]();

/* До этого не додумался :(
var shooter = function me() {
    console.log( me.i );
}
shooter.i = i;
*/