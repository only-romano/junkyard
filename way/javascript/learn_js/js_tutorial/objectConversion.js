/*
var obj = {};
var arr = [];

if (obj && []) console.log( 'All objects are - true!' );  // логическое преобразование

var user = {
  firstName: 'Vasily'
};

console.log( user.toString() );  // строковое преобразование
console.log();


user.toString = function() {
  return 'User ' + this.firstName;
};

console.log( user.toString() );
console.log( [1, 2].toString() );

var date = new Date();
console.log( date.toString().slice(0,33) );

var func = function() {};
console.log( func.toString() );
console.log();


var room = {
  number: 777,
  string: 66,  // если бы не числовое - то преобразование привело бы к NaN

  valueOf: function() { return this.number  },

  toString: function() { return this.string }
}

console.log( +room );
delete room.valueOf;
console.log( +room );

console.log( +date );
console.log( +[1, 2] );
console.log();


obj = {
  valueOf: function() {
    return 1;
  }
};

console.log( obj == true );

var obj = {
  valueOf: function() {
    return 1;
  }
};

var a = {
  valueOf: function() {
    return '1';
  }
};

var b = {
  valueOf: function() {
    return '2';
  }
}

console.log( obj + 'test' );
console.log( obj + a );   // преобразуется в строку, достаточно одного строчного значенияя при сложении
console.log( a - b );     // преобразуются обе строки в числа, потому что со строками вычитания не предусмотрено
console.log();

var date = new Date;
console.log( +date );
console.log( date.toString().slice(0,34) + 123 );  // из-за сраной винды с датами проблемы, всегда приходится слайс делать :(
// но тут смысл в том как раз, что не смотря на то, что у даты есть valueOf, при сложении оно не используется, а используется
// toString и ( date + 123 ) выдаст строку.  Это историческое исключение
console.log();


// рубрика ОБЛАВА НА JAVA

var value = new Boolean(false);

if (value) {
  console.log( 'If god doesn\'t exist, why does it works? \nTake this, atheists!' );
}

console.log();
console.log( value );
console.log( 'Bce, Pe6RT, Hac H@E6A^U, PACXODUMCR.' );
console.log();

console.log( Boolean(value) );
console.log( !!value );
console.log( Boolean(value) === !!value );

var a = {}[0];
console.log( a );

var b =  {} + {};
console.log( b );

console.log( ['x'] == 'x' );  // массивы всегда true, как и непустые строки, идёт преобразование к логическому типу


var foo = {

  toString: function() {
    return 'foo';
  },

  valueOf: function() {
    return 2;
  }

};

console.log( foo.toString() );  // 'foo'
console.log( foo + 1 );  // ---'foo1' - 3
console.log( foo + '3' );  // ---'foo3' - 23

// alert( foo );
// alert( foo + 1 );
// alert( foo + '3' );

console.log();
console.log( [] == [] );  // два разных массива, объекты не равны друг другу, даже если содержат одинаковые элементы
console.log( [] == ![] );  // ---всё, кроме этого масива равно ![]
// [] == ![] -> сначала второй массив преобразуется к логическому, любой объект == true, ![] -> false;
// [] == false -> далее численное преобразование объекта без прописанной valueOf преобразует объект в строку [] -> '';
// '' == false -> пустая строка и логический тип преобразуется к числовому типу из-за сравнения разных типов '' -> 0, false -> 0;
// 0 == 0;
console.log();

console.log( new Date(0) - 0 );  // + 0
console.log( new Array(1)[0] + '' );  // + 'undefined'
console.log( ({})[0] );  // + undefined
console.log( [1] + 1 );  // ---'1'  '11'
console.log( [1, 2] + [3, 4] );  // --- '1, 23, 4'  '1,23,4'
console.log( [] + null + 1 );  // + 'null1'
console.log( [[0]][0][0] );  // + 0
console.log( ({} + {}) );  // --- [object][object]  '[object Object][object Object]'


/*
function sum(a) {
  var sum = a;

    function func() {
      console.log( arguments[0] );
      sum += arguments[0];
      console.log( this );
      return func;
    };

  func.valueOf = sum;
  console.log( func.valueOf );

  return func;
}

function sum(a) {
  var sum = +a;
  this.func = function(b) {
    sum += +b;
    return func;
    };
  this.func.valueOf = sum;
  this.func.toString = sum;
  return func;
    this.func = function(b) {
      a = +a + +b;
      this.func.valueOf = a;
      console.log( sum );
      return func;
    };
      this.func.valueOf = a;
}
/

var help = {
  func: function(a) {
    help.func.valueOf += a;
    return help.func;
  },
};

help.func.valueOf = 0;
help.func.toString = function() {
  return help.func.valueOf;
}

help.func(1);
help.func(2);
console.log( help.func == 3 );
console.log();

/*
function sum(a) {

/*
  var obj = {
    sex: function(a) {
      var newObj = {
        sex: this.sex,
      }
      console.log( newObj );

      newObj.sex.valueOf = sex.valueOf + a;
      newObj.sex.toString = function() {
        return newObj.sex.valueOf;
      }
      return newObj.sex;
    }
  }
/
/
function sum(a) {
  help.func.valueOf = a;
  return help.func;
};

console.log( sum(1)(2) == 3 );
console.log( sum(1)(2)(3) == 6 );
console.log( sum(5)(-1)(2) == 6 );
console.log( sum(6)(-1)(-2)(-3) == 0 );
console.log( sum(0)(1)(2)(3)(4)(5) == 15 );

*/

function sum(a) {

  var currentSum = a;

  function f(b) {
    currentSum += b;
    return f;
  }

  f.toString = function() {
    return currentSum;
  };

  return f;
}

console.log( sum(1)(2) == 3 );
console.log( sum(1)(2)(3) == 6 );
console.log( sum(5)(-1)(2) == 6 );
console.log( sum(6)(-1)(-2)(-3) == 0 );
console.log( sum(0)(1)(2)(3)(4)(5) == 15 );