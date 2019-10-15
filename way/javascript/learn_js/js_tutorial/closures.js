/* function sayHi(name) {
    // LexicalEnvironment = { name: 'Vasily', phrase: undefined }
    var phrase = "Hello, " + name;

    // LexicalEnvironment = { name: 'Vasily', phrase: 'Hello, Vasily' }
    console.log( phrase );
}

sayHi('Vasily');  // LexicalEnvironment = undefined;


var userName = 'Kato';

function sayHiKato() {
    // sayHi.[[Scope]] = window;
    console.log( userName );
}

sayHiKato();

/*
При создании функции:
1) функция получает ссылку [[Scope]] на объект с переменными, в контексте которого была создана;
2) при запуске функции создаётся новый объект с переменными LexicalEnvironment со ссылкой на внешний объект
   из переменных из [[Scope]];
3) при поиске переменных он осуществляется сначала в текущем объекте переменных, а потом - по этой ссылке;
/

var phrase = 'Hello';

function sayTo(name) {
    console.log( phrase + ', ' + name );
}

sayTo('Vasily');

phrase = 'Bye, bye'
sayTo('Vasily');


function sayHiBye(firstName, lastName) {

    console.log( "Hello, " + getFullName() );
    console.log( "Bye, bye, " + getFullName() );

    function getFullName() {
        return firstName + " " + lastName;
    }

}

sayHiBye("Katenka", "Felix");

/*
В подфункции getFullName() функции sayHiBye():
1) переменные firstName / lastName сначала ищутся во внутреннем пространстве имён LexicalEnvironment;
2) не находя там, ищет в своём getFullName.[[Scope]], которая содержит переменные пространства вызова, т.е. функции sayHiBye();
3) если бы не нашёл там, то отпраувился бы дальше в getFullName.[[Scope{sayHiBye.[[Scope]]}]], то есть уже в глобальное
   пространство имён и там бы нашёл переменную, если она есть там.
/

var phrase = 'Hello';

function say() {

    function go() {
        console.log( phrase );
    }

    go();
}

say();


function makeCounter() {
    var currentCount = 1;

    return function() {
        return currentCount++;
    };
}

var counter = makeCounter();
console.log( counter() );
console.log( counter() );
console.log( counter() );

var counter2 = makeCounter();
console.log( counter2() );

/*
Way of environment:
1) 86 -> 78(86): counter.LexicalEnvironment = { currentCount: undefined };
2) 79(86): counter.LexicalEnvironment = { currentCount: 1 };
3) 81(86): function.LexicalEnvironment.[[Scope: counter.LexicalEnvironment]]
4) counter = function() { return currentCOunt++; }; counter.LexicalEnvironment.[[Scope{currentCount: 1}]]
5) 87: currentCount++; counter.LexicalEnvironment.[[Scope{currentCount: 1}]];
6) 88: currentCount++; counter.LexicalEnvironment.[[Scope{currentCount: 2}]];
7) 89: currentCount++; counter.LexicalEnvironment.[[Scope{currentCount: 3}]];

8) 91: аналогичные шаги 1-4; counter2.LexicalEnvironment.[[Scope{currentCount: 1}]];
9) 92: currentCount++; counter.LexicalEnvironment.[[Scope{currentCount: 1}]];
/

function f() {}

// Свойства функции доступны отовсюду и всегда, это использование функции "как объекта".
f.test = 5;
console.log( f.test );

function makeCounter() {
    function counter() {
        return counter.currentCount++;
    };
    counter.currentCount = 1;

    return counter;
}

var counter = makeCounter();
console.log( counter(), counter() );

counter.currentCount = 5;
console.log( counter() );

// Замыкание – это функция вместе со всеми внешними переменными, которые ей доступны.


say('Vasily');  // на момент вызова функции, сама функция уже работоспособна, но переменная phrase инициирована, но не определена

var phrase = 'Hello';

function say(name) {
    console.log( name + ', ' + phrase );
}


var value = 0;

function f() {
    if (1) {
        value = true;  // в локальном скопе объявлена (147) value, так что будет присвоено именно ей true
    } else {
        var value = false;
    }

    console.log( value );
}

f();
console.log(value);  // глобальная value не изменилась


function test() {

    console.log( window );  // undefined, т.к. переменная инициирована, но не определена, иначе был бы отсыл к объекту window(браузер)
    var window = 5;

    console.log( window );  // переменной wundow определено значение 5
}

test();

*/

var a = 5;

(function() {
    console.log(a);
}) ()


function makeCounter() {
    var currentCount = 1;
    console.log(currentCount);

    return function() {
        var currentCount = 3;
        return currentCount;
    }
}

var counter = makeCounter()
console.log( counter() );


var currentCounter = 1;

function makeCount() {

    return function() {
        return currentCounter++;
    };
}

var counter = makeCount();
var counter2 = makeCount();

console.log( counter() );  // 1
console.log( counter() );  // 2

console.log( counter2() );  // 3
console.log( counter2() );  // 4