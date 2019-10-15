try {
  console.log( 'It works' )
  lalala
  console.log( 'This code doesn\'t works' );
} catch(e) {
  console.log( '\nError: ' + e.name + ': ' + e.message + '\n' + e.stack + '\n');
}

console.log( 'This code still works');


try {
  setTimeout(function() {
    throw new Error();
  }, 1000);
} catch (e) {
  console.log( 'Doesn\'t work' );
}


var data1 = '{"name":"Vasily", "age": 30}';
var user1 = JSON.parse(data1);
console.log(user1.name, user1.age);

var data2 = "Has Error";
  try {
    var user2 = JSON.parse(data2);
    console.log(user2.name);
  } catch (e) {
    console.log("Data has an Error, we try to get them another time");
    console.log( e.name );
    console.log( e.message + '\n' );
  }


var data3 = '{ "age": 30 }';

try {
  var user3 = JSON.parse(data3);

  if (!user3.name) {
    throw new SyntaxError('Incorrect data');
  }; console.log( user3.name );
} catch (e) {
  console.log( 'Error: ' + e.message + '\n' );
}

var data4 = '{ "name": "Vasily", "age": 30}';


function readData(data) {
    try {
      var user4 = JSON.parse(data);
        if (!user4.name) {
          throw new SyntaxError('Incorrect data');
        }
      blablabla();
      console.log( user4.name );
    } catch (e) {
        if (e.name == 'SyntaxError') {
          console.log( e.message );
        } else {
          throw e;
        }
    }
}

try {
  readData(data4);
} catch (e) {
  console.log( 'Outer catch error: ' + e.message);
}


function ReadError(message, cause) {
  this.message = message;
  this.cause = cause;
  this.name = 'ReadError';
  this.stack = cause.stack;
}

function readData2() {
  var data = '{ bad data }';

  try {
    var user = JSON.parse(data);
      if (!user.name) {
        throw new SyntaxError('Incorrect data');
      }
      console.log( user4.name );
  } catch (e) {
    if (e.name == 'URIError') {
      throw new ReadError('URI Eroror', e);
    } else if (e.name == 'SyntaxError') {
      throw new ReadError('Syntax Error in data', e);
    } else {
      throw e;
    }
  }
}

try {
  readData2();
} catch (e) {
  if (e.name == 'ReadError') {
    console.log( e.message );
    console.log( e.cause );
  } else {
    throw e;
  }
}