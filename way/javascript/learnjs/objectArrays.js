person = new Object;
menuSetupAlt = {};

person.name = 'Vasily';
person.age = 25;
console.log( person.name + ':', person.age );

delete person.age;

if ('name' in person) {
    console.log( 'The "name" property exists.' );
}

if ( person.age === undefined ) {
    console.log( 'The "age" property is deleted.');
}

person.sex = undefined;

if ( person.sex !== undefined ) {
    console.log( 'The "sex" property is exist.');
} else if ( 'sex' in person ) {
    console.log( 'The "sex" property is exist, but it\'s value is "undefined".');
}

person['favorite music style'] = 'Jazz';
console.log(person['favorite music style']);

var key = 'name';
console.log( person[key] );

var menuSetup = {
    width: 300,
    height: 200,
    title: "Menu",
    'mother washed windows': true,
    size: {
        top: 90,
        middle: 60,
        bottom: 90
    }
};

menuSetupAlt.width = 300;
menuSetupAlt.height = 200;
menuSetupAlt.title = "Menu";

console.log( menuSetupAlt.title, menuSetup.title, menuSetup.size.top );

var user = {};
user.name = "Vasya";
user.surname = "Petrov";
console.log( user );

user.name = "Sergey";
delete user.surname;
console.log( user );