var message = "Hello";
var phrase = message;

phrase = "Goodbye";
console.log( message, phrase );

var user = {
    name: "Vasily",
};
var admin = user;

admin.name = "Petro";
console.log( admin.name, user.name);

function deepClone(obj) {
    var clone = {};
    for (var key in obj) {
        if (typeof(obj[key]) === 'object') {
            clone[key] = deepClone(obj[key]);
        } else {
            clone[key] = obj[key];
        }
    }
    return clone;
}

var forClone = {
    'a': 1,
    'b': 2,
    'c': {
        'd': 3,
        'e': 4,
        'f': {
            'g': 5
        }
    },
    'h': 6
}

var clone = deepClone(forClone);

clone.a = 's';
clone.c.f.g = 'so';
console.log( forClone );
console.log( clone );