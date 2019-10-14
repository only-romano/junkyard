'use strict';

class User {
  constructor(name) {
    this.name = name;
  }

  sayHi() {
    console.log(this.name);
  }
}

let user = new User('Vasily');
user.sayHi();

let User2 = class SiteGuest { sayHi() { console.log('Hello!'); } };
new User2().sayHi();
// new SiteGuest() - error;

let allModels = {};

function createModel(Model, ...args) {
  let model = new Model(...args);

  model._id = Math.random().toString(36).slice(2);
  allModels[model._id] = model;

  return model;
}

let user2 = createModel(class User {
  constructor(name) {
    this.name = name;
  }
  sayHi() {
    console.log('Hi, ' + this.name);
  }
}, 'Vasily');

user2.sayHi();
console.log( allModels[user2._id].name, user2._id );

class User3 {
  constructor(firstName, lastName) {
    this.firstName = firstName;
    this.lastName = lastName;
  }

  get fullName() {
    return `${this.firstName} ${this.lastName}`;
  }

  set fullName(newValue) {
    [this.firstName, this.lastName] = newValue.split(' ');
  }

  ["test".toUpperCase()]() {
    console.log('Passed!');
  }
};

let user3 = new User3('Vasily', 'Pupkov');
console.log(user3.fullName);
user3.fullName = 'Ivan Petrov';
console.log(user3.fullName);
user3.TEST();


class User4 {
  constructor(firstName, lastName) {
    this.firstName = firstName;
    this.lastName = lastName;
  }

  static createGuest() {
    return new User4('Site', 'Guest');
  }
};

let user4 = User4.createGuest();
console.log( user4.lastName );

class Menu {
  static get elemClass() {
    return 'menu';
  }
}

console.log( Menu.elemClass );

class Animal {
  constructor(name) {
    this.name = name;
  }

  walk() {
    console.log('I walk: ' + this.name);
  }
}

class Rabbit extends Animal {
  walk() {
    super.walk();
    console.log('...and jump!');
  }
}


new Rabbit('Vasily').walk();
console.log( Rabbit.prototype.__proto__ == Animal.prototype );

class RabbitCrol extends Animal {
  constructor() {
    try {
      console.log( this )
    } catch (e) {
      console.log( 'This is not defined:', e.message);
    } finally {
      super("Crol");
    }
    console.log(this);
  }
}

new RabbitCrol().walk();

let sym = Symbol('name');
console.log( sym, typeof sym );
console.log( sym == Symbol('name') );
console.log( Symbol.keyFor(sym) );

let name = Symbol.for('test');
console.log( Symbol.for('test') == name );
console.log( Symbol.keyFor(name) );
console.log();

let isAdmin = Symbol.for('isAdmin');

user = {
  name: 'Vasily',
  age: 30,
  [isAdmin]: true
}

console.log(user[isAdmin], user.isAdmin);
console.log( Object.keys(user), user[Symbol.for('isAdmin')] );

let obj = {
  iterator: 1,
  [Symbol.iterator]() {}
}

console.log(obj.iterator, obj[Symbol.iterator],
            Object.getOwnPropertySymbols(obj),
            Object.getOwnPropertyNames(obj) );