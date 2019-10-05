/*
function bind(func, context) {
  return function() {
    console.log( context );
    return func.apply(context, arguments);
  };
}


function f(x) {
  var fact = 1;
  for (var i = 2; i <= x; i++) {
    fact *= i;
  }
  return fact;
}

var timers = {};

f = timingDecorator(f, 'myFunc');

console.log( f(20) );
console.log( f(50) );
console.log( f(70) );

function timingDecorator(f, timer) {
  return function() {
    var start = performance.now();

    var result = f.apply(this, arguments);  // форвардинг вызова (forwarding), изнутри f всё выглядит так, как была вызвана напрямую

    if (!timers[timer]) timers[timer] = 0;
    timers[timer] += performance.now() - start;

    return result;
  };
}

var fibonacci = function f(n) {
  return (n > 2) ? f(n - 1) + f(n - 2) : 1;
}

fibonacci = timingDecorator(fibonacci, 'fibo');


console.log( fibonacci(10) );
console.log( fibonacci(20) );

console.log( 'Fibonacci: ' + timers.fibo + 'ms' );
console.log( 'Factorials: ' + timers.myFunc + 'ms' );

function sum(a, b) {
  return a + b;
}

console.log( sum(true, { name: 'Vasily', age: 35 }) );


function checkNumber(value) {
  return typeof value == 'number';
}

function typeCheck(f, checks) {
  return function() {
    for (var i = 0; i < arguments.length; i++) {
      if (!checks[i](arguments[i])) {
        console.log( 'Not supported entry: ' + i + ' (' + arguments[i] + ')' );
        return;
      }
    }
    return f.apply(this, arguments);
  }
}


sum = typeCheck(sum, [checkNumber, checkNumber]);

console.log( sum(1, 2) );

sum(true, null);
sum(1, ['array', 'in', 'sum?!']);


var users = {
  'vasily': 'user',
  'petro': 'user',
  'kato': 'admin'
};

function isAdmin(name) {
  if (users[name] === 'admin') return true;
  return false;
}

function checkPermissionDecorator(f) {
  return function() {
    if (isAdmin(arguments[0])) {
      return f.apply(this, arguments);
    }
    console.log( 'You don\'t have rights! Uahahahah!' );
  }
}

function save() {
  console.log( 'saved' );
}

save = checkPermissionDecorator(save);
save('vasily');
save('kato');

function makeLogging(f, log) {
  return function() {
    log.push(arguments[0]);
    f(arguments[0]);
  }
}

function fakeFriends(a) {
  console.log( 'Another fake friend: ' + a );
}


var log = [];
fakeFriends = makeLogging(fakeFriends, log);

fakeFriends('Kolya');
fakeFriends('Kuzma');
console.log();


for (var i = 0; i < log.length; i++) {
  console.log( 'Log ' + (i+1) + ': ' + log[i] + '.');
}
console.log();


function makeLoggingLearn(f, log) {

  function wrapper(a) {
    log.push(a);
    return f.call(this, a);
  };

  return wrapper;
}

log = [];
fakeFriends = makeLoggingLearn(fakeFriends, log);

fakeFriends('Iosif');
fakeFriends('Eugene');
fakeFriends('Nicolay');
fakeFriends('Kuzma');
fakeFriends('They all');
console.log();

for (var i = 0; i < log.length; i++) {
  console.log( 'Learn Log ' + (i+1) + ': ' + log[i] + '!');
}

function makeLogging(func, log) {
  return function() {
    var temp = [];
    for (var i = 0; i < arguments.length; i++) {
      temp.push(arguments[i]);
    }
    log.push(temp);
    func.apply(this, arguments);
  }
}


function work(a, b) {
  console.log( a + b );
}

var log = [];
work = makeLogging(work, log);

work(1, 2);
work(4, 5);

for (var i = 0; i < log.length; i++) {
  var args = log[i];
  console.log( 'Log ' + (i+1) + ': ' + args.join() + ';' );
}
console.log();


function makeLoggingLearn(f, log) {

  function wrapper() {
    log.push([].slice.call(arguments));
    return f.apply(this, arguments);
  }

  return wrapper;
}

log = [];
work = makeLoggingLearn(work, log);

work(7, 10);
work(11, 22);

for (var i = 0; i < log.length; i++) {
  var args = log[i];
  console.log( 'Learning log ' + (i+1) + ': ' + log[i] + '!');
}

*/

function makeCaching(f) {
  var cache = {};

  return function() {

    var arg = arguments[0];
    if (arg in cache) {
      console.log( 'Cached ' + arg + ' result: ' + cache[arg] );
      return cache[arg];
    } else {
      var result = f(arg);
      cache[arg] = result;
      console.log( 'New ' + arg + ': ' + result );
      return result;
    }
  };
}


function f(x) {
  return Math.random() * x;
}

f = makeCaching(f);

var a, b;

a = f(1);
b = f(1);
console.log( a == b );

b = f(2);
console.log( a != b );


function shortCache(f) {
  var cache = {};

  return function(x) {
    if (x in cache) return cache[x];
    cache[x] = f.call(this, x);
  };

}