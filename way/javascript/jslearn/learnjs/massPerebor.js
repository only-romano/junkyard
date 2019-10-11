/*

var arr = ['Apple', 'Orange', 'Pine'];

arr.forEach( function(item, i, arr) {
    console.log( i + ': ' + item + " (massive:" + arr + ")" );
});     // forEach передаёт в функцию callback три аргуумента = элемент массива, его индекс, сам массив


console.log( arr.filter( function(string) {
    return string > 'B';
}) );   // filter возвращает массив из элементов, которые, переданные аргуметном в функцию, возвращают true

var numbers = [1, -1, 2, -2, 3];
var positiveArr = numbers.filter(function(number) {
    return number > 0;
});

console.log( positiveArr, numbers );


var names = ['Python', 'HTML', 'CSS', 'Java', 'JavaScript', 'PostgreSQL'];
var nameLengths = names.map( function(name) {
    return name.length;
});     // map возвращает массив возрвратов функции, которой передаются по очереди элементы изначального массива

console.log( nameLengths)


numbers = [1, -1, 2, -3, 3, 5, 7, -12];
// every возвращает true, если все элементы массива возвращают true в проверочной функции
// some возвращает true, если хотя бы один элемент массива возвращает true в проверочной функции
function isPositive(number) {
    return number > 0;
}

console.log( numbers.every(isPositive), numbers.some(isPositive) );


var arrayReduce = [1, 2, 3, 4, 5];

var result = arrayReduce.reduce( function(sum, current) {
    return sum ** current;
});

var resultToRight = arrayReduce.reduceRight( function(sum, current) {
    return sum ** current;
})
console.log( result, resultToRight );

*/

var arr = ['There', 'is', 'a', 'life', 'on', 'Mars'];

var arrLength = [];
for (var i = 0; i < arr.length; i++) {
    arrLength[i] = arr[i].length;
};

var arrLengthMap = arr.map( function(a) { return a.length; });
console.log( arrLength, arrLengthMap );


var nums1 = [1, 2, 3, 4, 5, 6];
var nums2 = [-2, -1, 0, 1];

function getSums(arr) {
    var newArr = []
    var finalSum = arr.reduce( function(sum, current) {
        newArr.push(sum);
        return sum + current;
    });
    newArr.push(finalSum);
    return newArr;
}

console.log( getSums(nums1), getSums(nums2) );