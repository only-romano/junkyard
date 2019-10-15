console.log( typeof 1, typeof true, typeof 'text' );
console.log( typeof undefined, typeof null, typeof console.log );
console.log( typeof {}, typeof [], typeof new Date );

var toString = {}.toString;
console.log( toString.call([]), toString.call(new Date), toString.call({}) );

function getClass(obj) {
  return {}.toString.call(obj).slice(8, -1);
}

console.log( getClass(new Date), getClass([1,2,3]) );

function User() {}
var user = new User();
console.log( getClass(user) );
console.log( user instanceof User );

console.log( Array.isArray([1,2,3]), Array.isArray('not array') );

if ([1,2,3].splice) {
  console.log( 'It\'s a Duck! Oh, I mean Array!' );
}

if ( (new Date).getTime ) {
  console.log( 'It\'s a Date!', (new Date).getTime() );
}

function sayHi(who) {
  if (Array.isArray(who)) {
    who.forEach(sayHi);
  } else {
    console.log( 'Hi, ' + who + '!');
  }
}

sayHi('Vasily');
sayHi(['Sasha', 'Petya']);
sayHi([['Julia', 'Angelina'], ['Maria', 'Svetlana']]);


function formatDate(date) {
    if ( date.getTime ) {
      return date.toLocaleString("ru", { day: '2-digit', month: '2-digit',
                             year: '2-digit' }).split('-').reverse().join('.');
    } else if (typeof date === 'string') {
      return date.split('-').map(function(name) { return name.slice(-2); }).
                  reverse().join('.');
    } else if (typeof date === 'number') {
      return formatDate(new Date(date * 1000));
    } else if (Array.isArray(date)) {
      return formatDate(new Date(date[0], date[1], date[2]));
    }
}

console.log( formatDate('2011-10-02') );
console.log( formatDate(1234567890) );
console.log( formatDate([2014, 0, 1]) );
console.log( formatDate(new Date(2014, 1, 1)) );
