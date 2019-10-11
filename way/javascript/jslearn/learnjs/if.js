var a = +prompt('Введите a:');
var b = +prompt('Введите b:');

if (a > b) {
  console.log( 'a больше b на ', a - b );
} else if (a < b) {
  console.log( 'a меньше b на ', b - a );
} else {
  console.log( 'a равно b' );
}