/*
var user = {
  name: 'Vasily',

  sayHi: function() {
    console.log( 'Hello, ' + user.name + '!' );
  }

};

user.sayHi();

user.sayGoodbye = function() {
  console.log( 'Goodbye, ' + this.name + '!' );
};

user.sayGoodbye();


var admin = user;
user = null;
// admin.sayHi();  свойство name отсутствует у user, ибо объект уже стёрт
admin.sayGoodbye();


user = {
  name: 'Petro',

  sayHi: function() {
    showName(this);  // передать весь объект в функцию showName
  }
};

function showName(namedObj) {
  console.log( namedObj.name );
}

user.sayHi();


function sayHi() {
  console.log( this.firstName );  // функция ещё не знает с каким объектом будет работать, но готова к работе
}

var nurse = {
  firstName: 'Helena',
  console: sayHi
}

nurse.console()

var user = { firstName: 'Vasily' };
var admin = { firstName: 'Admin' };

function func() {
  // 'use strict'  при режиме будет вместо глобального объекта undefined и нельзя будет получить доступ к свойствам
  console.log( this.firstName );
}

user.f = func;
admin.f = func;

user.f();
admin.f();
admin['f']();

console.log()
func();
console.log()


user = {
  name: 'Vasily',
  hi: function() { console.log(this.name); },
  bye: function() { console.log('Goodbye') }
};

user.hi();
// Любая операция над результатом операции получения свойства, кроме вызова, приводит к потере контекста.
(user.name == 'Vasily' ? user.hi : user.bye)();
// Вызов состоит из двух независимых операций: точка . – получение свойства и скобки () – его вызов
// точка возвращает не функцию, а значение специального «ссылочного» типа Reference Type.
// Этот тип представляет собой связку «base-name-strict», где:
// base – как раз объект,
// name – имя свойства,
// strict – вспомогательный флаг для передачи use strict.

// Скобки () получают из base значение свойства name и вызывают в контексте base.
// Другие операторы получают из base значение свойства name и используют, а остальные компоненты игнорируют.
console.log()


var arr = ['a', 'b'];

arr.push( function() {
  console.log( this, this[1] );
})

arr[2]();


var obj = {
  go: function() { console.log(this) }
};

(obj.go)()

'use strict'

var obj, method;

obj = {
  go: function() { console.log(this) }
};

obj.go();

(obj.go)();

(method = obj.go)();   // любые операции, кроме исполнения, превращают Reference Type в функцию

(obj.go || obj.stop)();
console.log();


var user = {
  firstName: 'Vasily',

  export: this  // this вне функции, поэтому он ссылается на глобальное окружение (window Браузерный)
}

console.log( user.export.firstName );
console.log();


var name = '';

user = {
  name: 'Vasily',
  export: function() {
    return this;
  }
};

console.log( user.export().name );  // Vasily, т.к. this определена внутри функции
console.log();


user = {
  name: 'Petro',

  export: function() {
    return {
      value: this
    };
  }

};

console.log( user.export().value.name );  // this определена внутри функции, объект присваивается значением внутреннему объекту.

*/

var calculator = {
  read: function() {
    this.a = +prompt('Input a');
    this.b = +prompt('Input b');
  },
  sum: function() {
    return this.a + this.b;
  },
  mul: function() {
    return this.a * this.b;
  }
}

calculator.read();
console.log( calculator.sum() );
console.log( calculator.mul() );
console.log()


var ladder = {
  step: 0,

  up: function() {
    this.step++;
    return this;
  },

  down: function() {
    this.step--;
    return this;
  },

  showStep: function() {
    console.log( this.step );
    return this;
  }
}

ladder.up();
ladder.up();
ladder.down();
ladder.showStep();

ladder.step = 0;
ladder.up().up().down().up().down().showStep();