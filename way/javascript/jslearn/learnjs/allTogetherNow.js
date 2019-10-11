'use strict';

console.log('Here will be an stupid ERROR')  /*or not if this cool stuff appears: */  ;  /* yeah, this stuff */

[1, 2, 33].forEach(console.log);

function StringBuilder(str) {
    let stroka = [];
    stroka.push(str);
    return {
        toString: function() {
            return stroka.join('');
        },
        add: function(str) {
            stroka.push(str);
        },
        clear: function() {
            stroka.length = 0;
        },
        addArray: function(arr) {
            stroka.push(arr.join(''));
        },
        addDate:function(date) {
            let d = date || new Date;
            stroka.push(' '+d);
        },
        find: function(str) {
            return stroka.indexOf(str);
        }
    };
}

let str = StringBuilder("Привет");
str.add(", медвед!");
console.log("'"+str+"'");

str.clear();
console.log("'"+str+"'");

let arr = [1,2,3,4,5,6,7];
str.addArray(arr);
console.log("'"+str+"'");

str.clear();
str.addDate(new Date());
str.add(" ");
str.addDate(new Date(2015, 3, 1));
console.log("'"+str+"'");

console.log(str.find("йоу"));
str.add(" йоу йоууу йоууу sadad!!!");
console.log(str.find("йоуу"));