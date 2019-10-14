const isPalindrome = (str) => {
    var last = str.length - 1;
    var first = 0;

    while (last > first) {
        while (!str[first].match(/[a-zA-Zа-яА-Я]/)) first++;
        while (!str[last].match(/[a-zA-Zа-яА-Я]/)) last--;
        if (str[first++].toLowerCase() !== str[last--].toLowerCase()) return false;
    }

    return true;
}

console.log(isPalindrome("helL21owolleh"))