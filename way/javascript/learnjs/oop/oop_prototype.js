var animal = {
  eats: true
};

var rabbit = {
  jumps: true
};

rabbit.__proto__ = animal;

console.log( rabbit.jumps, rabbit.eats );

for (var key in rabbit) {
  console.log( key + ' = ' + rabbit[key] + '; is own Property: ' + rabbit.hasOwnProperty(key));
}
console.dir(rabbit.toString);

var data = Object.create(null);
data.text = "Hello";
data.age = 35;

console.dir(data.toString);

console.log( Object.getPrototypeOf(rabbit) );
Object.setPrototypeOf(data, animal);
console.log( data.eats );

var girl = Object.create(animal, {'fucks': {}});
console.log(girl.eats);


var baby = {
  sucks: null
};

var slut = {
  sucks: true
};

slut.__proto__ = baby;
console.log( slut.sucks );

delete slut.sucks;
console.log( slut.sucks );

delete baby.sucks;
console.log( slut.sucks );

var vagina = {
  insert: function() {
    this.full = true;
  }
};

var pussy = {
  __proto__: vagina
}

pussy.insert();
console.log( 'Vagina is empty = ' + vagina.full + ', but pussy is full = ' + pussy.full);


var head = {
  glasses: 1
};

var table = {
  pen: 3,
  __proto__: head
};

var bed = {
  sheet: 1,
  pillow: 2,
  __proto__: table
};

var pockets = {
  money: 2000,
  __proto__: bed
}

console.log( pockets.pen, bed.glasses, table.money );