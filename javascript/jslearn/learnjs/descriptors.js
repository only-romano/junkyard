/*
'use strict';  вызовет ошибку при изменении неизменяемого свойства

var user = {};
var descUser = {};

user.name = 'Vasily';

Object.defineProperty(descUser, 'name', { value: 'Petro', configurable: true, writable: true, enumerable: true });

console.log( user );
console.log( descUser );
console.log();


user = {};

// writable: false  запрещает присвоение 'user.name == ...' ;  configurable: false  запрещает удаление свойства 'delete user.name' ;
Object.defineProperty(user, 'name', { value: 'Vaslly', writable: false, configurable: false });

user.name = 'Ivan';
console.log( user.name );


user = { name: 'Vasily' };

user.toString = function() { return this.name };
for (var key in user) console.log( key + ': ' + user[key] );
console.log();

Object.defineProperty(user, 'toString', { enumerable: false });
for (var key in user) console.log( key + ': ' + user[key] );


user = {
  firstName: 'Vasily',
  surname: 'Petrov'
}

Object.defineProperty(user, 'fullName', { get: function() { return this.firstName + ' ' + this.surname; } });
console.log( user.fullName );
console.log();


user = {};

Object.defineProperty(user, 'fullName', {
  get: function() { return this.firstName + ' ' + this.surname },
  set: function(value) {
  var split = value.split(' ');
  this.firstName = split[0];
  this.surname = split[1];
  }
});

user.fullName = 'Maria Magdalena';
console.log( user.fullName );

user = {
  firstName: 'Vasily',
  surname: 'Petrov',

  get fullName() {
    return this.firstName + ' ' + this.surname;
  },

  set fullName(value) {
    var split = value.split(' ');
    this.firstName = split[0];
    this.surname = split[1];
  }
};

console.log( user.fullName );
console.log();

user.fullName = 'Ridj Forever';
console.log( user.firstName );
console.log( user.surname );
console.log( user.fullName );
console.log();

function User(name, age) {
  this.name = name;
  this.age = age;
}

var kato = new User('Kato', 19);
console.log( kato.age );


function UserMod(name, birthday) {
  this.name = name;
  this.birthday = birthday;

  Object.defineProperty(this, 'age', {
    get: function() {
      var today = new Date();
      var todayYear = new Date(today - this.birthday);
      return todayYear.getFullYear() - 1970;
    }
  });
}

var sergio2 = new UserMod('Sergio', new Date(1990, 2, 18));
var sergio = new UserMod('Sergio', new Date(1990, 6, 18));

console.log( sergio.birthday );
console.log( sergio.age );
console.log( sergio2.age );

var user = {};

// объявление несколько свойств сразу через  Object.defineProperties( obj, descroptors )
Object.defineProperties(user, {
  firstName: {
    value: 'Katenka'
  },

  surname: {
    value: 'Felix'
  },

  fullName: {
    get: function() {
      return this.firstName + ' ' + this.surname;
    }
  }
});

console.log( user.fullName );
console.log();


var obj = {
  a: 1,
  b: 2,
  internal: 3
};

Object.defineProperty(obj, 'internal', {
  enumerable: false
});

console.log( Object.keys(obj) );  // возвращает только перечеслимые свойства enumerable
console.log( Object.getOwnPropertyNames(obj) );  // возвращает все свойства объекта, даже скрытые и неперечислимые enumerable: false
console.log();


var newObj = {
  test: 5
};
var descriptor = Object.getOwnPropertyDescriptor(newObj, 'test');
console.log( newObj.test );

delete descriptor.value;
delete descriptor.writable;
descriptor.get = function() {
  console.log( 'Pervert ^^' );
};

delete newObj.test;  // если не удалить, то новый дескриптор поставится рядом со старым test

Object.defineProperty(newObj, 'test', descriptor);

newObj.test;

*/

var closed = {
  only: 'zero'
}

Object.preventExtensions(closed);  // запрещает добавление свойств в объект

console.log( closed );

closed.new = 'no';
closed.only = 'one';
console.log( closed );
console.log();


Object.seal(closed);  // запрещает добавление, удаление и изменение properties текущих свойств

closed.only = 'two';
delete closed.only;
console.log( closed );


Object.freeze(closed);  // запрещает добавление, удаление, изменение свойств, все свойства configurable: false, writable: false;

closed.only = 'no way';
console.log( closed );
console.log();


console.log( Object.isExtensible(closed) );  // проверка на отсутствие  Object.preventExtensions  - true если оно отсутствует
console.log( Object.isSealed(closed) );  // проверка на  Object.seal  - true если оно есть
console.log( Object.isFrozen(closed) );  // проверка на  Object.freeze  -  true если оно есть
console.log();


function User(fullName) {
  this.fullName = fullName;
}

var vlad = new User('Vladimir Putin');

Object.defineProperty(vlad, 'firstName', {
  get: function() {
    return this.fullName.split(' ')[0];
  },
  set: function(value) {
    var temp = this.fullName.split(' ');
    temp[0] = value;
    this.fullName = temp.join(' ');
  }
})

Object.defineProperty(vlad, 'lastName', {
  get: function() {
    return this.fullName.split(' ')[1];
  },
  set: function(value) {
    var temp = this.fullName.split(' ');
    temp[1] = value;
    this.fullName = temp.join(' ');
  }
})

console.log( vlad.firstName );
console.log( vlad.lastName );

vlad.lastName = 'Navalniy';
console.log( vlad.fullName );