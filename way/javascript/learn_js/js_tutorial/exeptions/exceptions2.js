function sum(n) {
  return n ? (n + sum(n - 1)) : 0;
}

var n = +prompt('Inptut n?', 100);
var start = new Date();

try {
  var result = sum(n);
} catch (e) {
  result = 0;
} finally {
  var diff = new Date() - start;
}

alert( result ? result : 'Error was occured');
alert( 'Runtime is: ' + diff);


function func() {
  try {
    return 1;
  } finally {
    alert( 'Call is over' );
  }
}

alert( func() );


var data = '{ "name": "Vasily"}';

try {
  var jsonData = JSON.parse(data);
  if (!jsonData.age) {
    throw new Error('Incorrect data');
  }
  console.log( jsonData.age );
} catch (e) {
  console.log( e.message );
}


window.onerror = function(message, url, lineNumber) {
  alert('Catched global error!\n' + 'Message: ' + message +
        '\n(' + url + ':' + lineNumber + ')');
};

function readData() {
  error();
}

readData();