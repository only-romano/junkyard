var animal = { eats: true };

function Rabbit(name) {
  this.name = name;
}

console.dir( Rabbit.prototype.constructor );

Rabbit.prototype = animal;

console.dir( Rabbit.prototype.constructor );

var rabbit = new Rabbit('Croul');
console.log(rabbit.eats);

var rabbit2 = new rabbit.constructor('Croul girl');

function inherit(proto) {
  function F() {}
  F.prototype = proto;
  var object = new F;
  return object;
}

var girl = {
  sucks: true
}

var alexa = inherit(girl);
console.log(alexa.sucks);
console.log();

if (!Object.create) Object.create = inherit;

function Honey() {}
Honey.prototype = { eats: true };

var sasa = new Honey();
console.log( sasa.eats );

function Honey() {}
Honey.prototype = { eats: true };
var sasa = new Honey();

Honey.prototype = {};
console.log( sasa.eats );

function Honey() {}
Honey.prototype = { eats: true };
var sasa = new Honey();

Honey.prototype.eats = false;
console.log( sasa.eats );

function Honey() {}
Honey.prototype = { eats: true };
var sasa = new Honey();

delete Honey.prototype.eats;
console.log( sasa.eats );

function Rabbit(name) {}
Rabbit.prototype = {
  eats: true
};

var rabbit = new Rabbit();

delete Rabbit.prototype.eats; // (*)

console.log( rabbit.eats );

function Menu(options) {
  options = Object.create(options);
  options.height = 300;

  console.log("width: " + options.width);
  console.log("height: " + options.height);
}

var options = {
  width: 500,
  height: false,
}

var menu = new Menu(options);

  console.log("Original width: " + options.width);
  console.log("Original height: " + options.height);

function Rabbit(name) {
  this.name = name;
}

Rabbit.prototype.sayHi = function() {
  console.dir( this.name );
};

rabbit = new Rabbit("Bonney");

rabbit.sayHi();                         // Bonney
Rabbit.prototype.sayHi();               // Bonney
Object.getPrototypeOf(rabbit).sayHi();  // undefined
rabbit.__proto__.sayHi();               // Bonney


obj = new Rabbit('Pussy');

obj2 = new obj.constructor();

console.log(obj2.