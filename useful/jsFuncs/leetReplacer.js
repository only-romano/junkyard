'use strict';
// 1337 replacer

const leetIt = (text) => text
    .replace(/O|o/g, 0)
        .replace(/L|l/g, 1)
            .replace(/E|e/g, 3)
                .replace(/A|a/g, 4)
                    .replace(/S|s/g, 5)
                        .replace(/T|t/g, 7)
                            .replace(/G|g/g, 9);


// console.log(leetIt("hello, my darling friend!"))
