/*
var fruits = ['Apple', 'Orange', 'Peach'];

fruits[2] = 'Pineapple';
fruits[3] = 'Limon';
console.log( fruits, fruits.length );

fruits[4] = {name: 'Petro'};
console.log( fruits[4].name );

var oneFruit = fruits.pop();
var appleFruit = fruits.shift();
fruits.push('Melon', appleFruit);
fruits.unshift(oneFruit, 'Potato');
console.log( fruits );

var pussy = [];
pussy[999] = 'Sasha';
pussy.tips = 88;
console.log( pussy, pussy.tips, pussy[999] );

var arr = ['Apple', 'Orange', 'Peach'];

for (var i = 0; i < arr.length; i++) console.log( arr[i] );
arr.length = 0;
console.log( arr );

function lastElement(arr) {
    return arr[arr.length - 1] || arr.pop();
}

console.log( lastElement(fruits) );

var goods = ['sex', 'drugs', 'rock\'n\'roll'];

function addElement(arr, element) {
    arr[arr.length] = element;
}

addElement(goods, 'code');
console.log( goods );

var styles = ['Jazz', 'Blues'];
styles.push('Rock\'n\'Roll');
styles.length > 1 ? styles[styles.length - 2] = 'Classic' : console.log('Where\'s no such element');
console.log( styles.shift() );
styles.unshift( 'Rap', 'Raggee' );
console.log( styles );

function randomElement(arr) {
    return arr[Math.floor(Math.random() * arr.length)]
}

console.log( randomElement(styles), randomElement(styles), randomElement(styles) );

var arr = [1, 2, 3];
var arr2 = arr;
arr2[0] = 5;
console.log( arr[0], arr2[0] );

function find(arr, value) {
    for (var i = 0; i < arr.length; i++) {
        if (arr[i] === value) return i;
    }
    return -1;
}

arr = ['test', 2, 1.5, false];
console.log( find(arr, 'test'), find(arr, 2), find(arr, 1.5), find(arr, 0) );

function filterRange(arr, a, b) {
    var rangedArr = [];
    for (var i = 0; i < arr.length; i++) {
        if (arr[i] >= a && arr[i] <= b) rangedArr.push(arr[i]);
    }
    return rangedArr;
}

var arr = [5, 4, 3, 8, 0];
var filteredArr = filterRange(arr, 3, 5);
console.log( arr, filteredArr );


function Eratofen(n) {
    var array = [];
    for (var value = 2; value <= n; value++) {
        array.push(value);
    }
    var p = 0;
    while ( array[p]**2 <= n ) {
        for (var i = p+1; i < array.length; i++) {
            if (array[i] % array[p] === 0) {
                array.splice(i, 1);
            };
        }
        p +=1
    }
    return array;
}

var hun = Eratofen(100);
var sum = 0;
for (var i = 0; i < hun.length; i++) {
    sum += hun[i];
}

console.log( sum, hun );

*/

function getMaxSubSum(arr) {
    var maxSum = 0;
    var tempSum = 0;
    for (var i = 0; i < arr.length; i++) {
        if (-arr[i] > tempSum) {
            tempSum = 0;
        } else {
        tempSum += arr[i];
        }
        if (tempSum > maxSum) maxSum = 0 + tempSum;
    };
    return maxSum;
}

console.log( getMaxSubSum([-1, -2, -3]), getMaxSubSum([-1, 2, 3, -9]) ); // 0 , 5
console.log( getMaxSubSum([-1, 2, 3, -9, 11]), getMaxSubSum([-2, -1, 1, 2]) ); // 11, 3
console.log( getMaxSubSum([100, -9, 2, -3, 5]),  getMaxSubSum([1, 2, 3]) ); // 100, 6
/*
 if + > - ? con + tempMax[+,-) : stop + tempMax[+,-);
if temp>- && temp2>- == {+-+} ? max(temp1, temp2);
- [+ +] -   [temp] == maxSum
[+ - + +] - [temp2] == maxSum
- + + - [+] [temp2]
- - [+ +]
[+] - + - +
[+ + +]
*/