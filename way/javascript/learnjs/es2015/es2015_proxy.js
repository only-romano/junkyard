'use strict';

let user = {};

let proxy = new Proxy(user, {
  get(target, prop) {
    console.log(`Reading ${prop}`);
    return target[prop];
  },
  set(target, prop, value) {
    console.log(`Writing ${prop} ${value}`);
    target[prop] = value;
    return true;
  }
});

proxy.firstName = 'Kato';
proxy.firstName;

console.log(user.firstName);


let dictionary = {
  'Hello': 'Privet',
  'Bye': 'Poka'
};


dictionary = new Proxy(dictionary, {
  get(target, phrase) {
    if (phrase in target) {
      return target[phrase];
    } else {
      console.log(`No phrase: ${phrase}`);
      return phrase;
    }
  },

  deleteProperty(target, phrase) {
    return true;
  },

  has(target, phrase) {
    return true;
  }
})

delete dictionary['Hello'];
console.log( dictionary['Hello'], 'Hello' in dictionary );
console.log( dictionary['Welcome'], 'Welcome' in dictionary );

let user2 = {
  name: 'Sergio',
  surname: 'Romano',
  _version: 1,
  _secret: 123456
};

let proxy2 = new Proxy(user2, {
  enumerate(target) {
    let props = Object.keys(target).filter(function(prop) {
      return prop[0] != '_';
    });

    return props[Symbol.iterator]();
  }
});

for (let prop in proxy2) {
  console.log(prop);
}

function sum(a, b) {
  return a + b;
}

let proxy3 = new Proxy(sum, {
  apply: function(target, thisArg, argumentsList) {
    console.log(`Will be count sum of: ${argumentsList}`);
    return target.apply(thisArg, argumentsList);
  }
});

console.log( proxy3(1, 2) );


function User(name, surname) {
  this.name = name;
  this.surname = surname;

  this.fullName = function() {
    return `${this.name} ${this.surname}`;
  }
}

let UserProxy = new Proxy(User, {
  construct: function(target, argumentsList) {
    console.log(`Run new UserProxy with arguments: ${argumentsList}`);
    return new target(...argumentsList);
  }
});

let user3 = new UserProxy('Sergio', 'Romanov');
console.log( user3.fullName() );