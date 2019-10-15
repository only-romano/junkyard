/*
var menu = {
    width: 300,
    height: 200,
    title: "Menu"
};

var counter = 0;

for (var key in menu) {
    counter++;
    console.log( "Key: " + key, "\tValue: " + menu[key]  );
}

console.log( "Count of properties: " + counter, "(" + Object.keys(menu).length + ")" );

var codes = {
    "7": "Russia",
    "38": "Ukraine",
    "1": "USA"
}

for (var code in codes) console.log( code );

var codes = {
    "+7": "Russia",
    "+38": "Ukraine",
    "+1": "USA"
}

for (var code in codes) {
    var value = codes[code];
    code = +code;
    console.log( code + ": " + value );
}
*/
function isEmpty(obj) {
    var counter = 0;
    for (var key in obj) counter++;
    return !counter;
}

console.log( isEmpty({}), isEmpty({'time': 9}) );


function countSalaries(obj) {
    var sum = 0;
    for (var key in obj) sum += obj[key];
    return sum;
}

console.log( countSalaries({}), countSalaries({"Bill": 100, "Sam": 300, "Jane": 250}) );


function maxSalary(obj) {
    var max = 0;
    var name = 'Where\'s no employes\t';
    for (var key in obj) {
        if (obj[key] > max) {
            name = key;
            max = obj[key];
        }
    }
    return name;
}

console.log( maxSalary({}), maxSalary({"Bill": 100, "Sam": 300, "Jane": 250}) );

function multiplyNumeric(obj) {
    for (var key in obj) {
        var num = obj[key];
        if (+num) {obj[key] = 2 * num};
    }
    return obj;
}

console.log( multiplyNumeric({}), multiplyNumeric({width: 200, height: 300, title: "menu" }) );