showPrimesAndOdds(60);

for (let i = 0; i < 10; i++) {
  if (i % 2 === 0) continue;
  console.log(i);
}

let x = 7;
let n = 8;

if (n < 0) {
  console.log('Степень ' + n +
              'не поддерживается, введите целую степень, большую 0');
} else {
  console.log( pow(x, n) );
}

function pow(x, n) {
  let result = 1;

  for (let i = 0; i < n; i++) {
    result *= x;
  }

  return result;
}

function showPrimesAndOdds(n) {
  for (let i = 2; i < n; i++) {
    if (!isPrimeAndOdd(i)) continue;
    console.log(i);
  }
}

function isPrimeAndOdd(n) {
  for (let i = 2; i < n; i++) {
    if (n % i === 0) return false;
  }
  return isEven(n) ? false : true;
}

function isEven(n) {
  return !(n % 2);
}


// Style contest

function getPow(x, n) {
  let result = 1;

  for (let i = 0; i < n; i++) {
    result *= x;
  }

  return result
}


x = /*prompt("x?", "")*/ 7;
n = /*prompt("n?", "")*/ 8;

if (n < 0) {
  console.log('This is very long text and you\'re better believe what ' + n +
              ' it is wrong to try to put it all into one line.');
} else {
  console.log( pow(x, n) );
}