/*
setTimeout(function() {
  console.log( 'Hello' );
}, 1000);

var user = {
  firstName: 'Vasily',
  sayHi: function() {
    console.log( this.firstName );
  }
};

setTimeout(user.sayHi, 1000);  // передано без контекста

var f = user.sayHi;
setTimeout(f, 1000);


// РЕШЕНИЯ ЭТОЙ СИТУАЦИИ

// 1) Обёртка. Нет безопасности, что за тайм-аут не изменятся переменные - admin / user

setTimeout(function() {
  console.log();
  user.sayHi();
}, 1000);


var admin = {
  firstName: 'Admin',
  sayHi: function() {
    console.log( this.firstName + ": Hello, " + arguments[0] );
  }
};

setTimeout(function() {
  admin.sayHi('Petro');
}, 1000);


// 2) bind для привязки контекста

function bind(func, context) {
  return function() {
    return func.apply(context, arguments);
  };
}

function func() {
  console.log( this );
}

var g = bind(func, 'Context');
g();

function def() {
  return func.apply('Context', arguments);
}
def();
console.log();

function bind(func, context) {
  return function() {
    return func.apply(context, arguments);
  };
}

var user = {
  firstName: 'Vasily',
  sayHi: function() {
    console.log( this.firstName + ': Hello, ' + (arguments[0] || 'Anonimous') );
  }
};


setTimeout( bind(user.sayHi, user), 1000);

var sayHi = bind(user.sayHi, user);
sayHi('Petro');
sayHi('Maria');
console.log();


// 3) Встроенный метод bind

function f(a, b){
  console.log( this );
  console.log( a + b );
}

var g = f.bind('Context');  // вместо g = bind(f, 'Context');
g(1, 2);
console.log();

setTimeout(user.sayHi.bind(user), 1000);  // вместо setTimeout( bind(user.sayHi, user), 1000 );

//  методы call/apply вызывают функцию с заданным контекстом и аргументами
//  bind не вызывает функцию, он только возвращает обёртку, которую  можно вызвать позже, которая передаст вызов в
//    исходную  функцию, с привязанным контекстом

// реализация bindAll:

var functions = {
  a: function() {},
  b: function() {},
  c: 'not a func'
}


for (var property in functions) {
  if (typeof functions[property] == 'function') {
    functions[property] = functions[property].bind(functions);
  }
}

console.log( functions );

// КАРРИНГ
// Карринг ( currying ) или каррирование - создание новой функции, путём фиксирования аргументов существующей

function mul(a, b) {
  return a * b * arguments[2] || a * b;
};

var double = mul.bind(null, 2);  // double - является частичной функцией от mul  -  partial function

console.log( double(3) );  // аргументы передаются после фиксированного
console.log( double(4, 3) );
console.log( double(5) );
console.log();


var triple = mul.bind(null, 3);  // контекст не используется в функции, так что фиксируем - null

console.log( triple(3) );
console.log( triple(4) );
console.log( triple(5) );


function bind(func, context /*, args /) {
  var bindArgs = [].slice.call(arguments, 2);

  function wrapper() {
    var args = [].slice.call(arguments);
    var unshiftArgs = bindArgs.concat(args);
    return func.apply(context, unshiftArgs);
  }
  return wrapper;
}

var quatro = bind(mul, null, 4);

console.log();
console.log( quatro(2) );
console.log( quatro(3) );
console.log( quatro(4) );


function f() {
  console.log( this );
}

var user = {
  g: f.bind('Hello')  // [String: 'Hello']
};

user.g();  // изменить однажды привязанный контекст уже нельзя

function f() {
  console.log( this.name );
}

f = f.bind( {name: 'Vasily'} ).bind( {name: 'Petro'} );  // Vasily, так как переназначить заданный контекст нельзя, а следующий
// .bind  установит контекст уже для обёртки, но он не используется

f();
console.log();


function bind(func, context) {
  return function() {
    if (this.name === 'Petro') console.log( 'got it!');
    return func.apply(context, arguments);
  };
}

function g() {
  console.log( this.name );
}

g = bind(g, {name: 'Vasily'} );
g = bind(g, {name: 'Petro'} ); // играло бы роль, если бы функция bind использовала контекст this

g();


function sayHi() {
  console.log( this.name );
}

sayHi.test = 5;
console.log( sayHi.test );

var bound = sayHi.bind( {
  name: 'Kato'
});

console.log( bound.test );  // --- 5

// Результатом работы bind является функция-обёртка над sayHi. Эта функция – самостоятельный объект, у неё уже нет свойства test.
'use strict';

function ask(question, answer, ok, fail) {
  var result = prompt(question, '');
  if (result.toLowerCase() == answer.toLowerCase()) ok();
  else fail();
}

ask("Can we let bird fly?", 'yes', fly, die);

function fly() {
  console.log( 'Bird is flown away :)' );
}

function die() {
  console.log( 'It\'s a pity :(' );
}


var user = {
  login: 'Vasily',
  password: '12345',

  loginOk: function() {
    console.log( this.login + ' enters the site' );
  },

  loginFail: function() {
    console.log( this.login + ': entry error' );
  },

  checkPassword: function () {
    ask('Enter password:', this.password, this.loginOk.bind(this), this.loginFail.bind(this));
  },

  checkPassword2: function() {
    var self = this;
    ask('Enter your password:', this.password,
      function() {
        self.loginOk();
      },
      function() {
        self.loginFail();
      }
    );
  }

};

user.checkPassword();

var vasya = user;
user = null;
vasya.checkPassword();
vasya.checkPassword2();

*/

'use strict';

function ask(question, answer, ok, fail) {
  var result = prompt(question, '');
  if   (result.toLowerCase() == answer.toLowerCase()) ok();
  else fail();
}

var user = {
  login: 'Kato',
  password: '12345',

  loginDone: function(result) {
    console.log( this.login + (result ? ' enters the site.' : ': entry error.') );
  },

  checkPassword: function() {
    ask('Enter password:', this.password,
      (function() {
        this.loginDone(true);
      }).bind(this),
      (function() {
        this.loginDone(false);
      }).bind(this)
    );
  },

  checkPassword2: function() {
    var self = this;
    ask('Enter this password:', self.password,
      function() {
        self.loginDone(true);
      },
      function() {
        self.loginDone(false);
      }
    )
  }

};

var vasya = user;
user = null;
vasya.checkPassword();
vasya.checkPassword2();