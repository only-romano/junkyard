function Animal(name) {
  this.speed = 0;
  this.name = name;

  this.run = function(speed) {
    this.speed += speed;
    console.log(this.name + ' running, speed is ' + this.speed);
  };

  this.stop = function() {
    this.speed = 0;
    console.log(this.name + ' is standing');
  };

  this.sayHi = function() {
    console.log( name );
  }
}

var animal = new Animal('Beast');

animal.sayHi();
console.log(animal.speed);
animal.run(3);
animal.run(10);
animal.stop();

function Beast(name) {
  this.name = name;
  this.speed = 0;
}

Beast.prototype.run = function(speed) {
  this.speed += speed;
  console.log( this.name + ' is running, speed is ' + this.speed );
};

Beast.prototype.stop = function() {
  this.speed = 0;
  console.log( this.name + ' is standing' );
}

Beast.prototype.sayHi = function() {
  console.log( this.name );
}

var beast = new Beast('Animal');

beast.sayHi();
console.log( beast.speed );
beast.run(5);
beast.run(5);
beast.stop();


function CoffeeMachine(power) {
  this._waterAmount = 0;
  this._power = power;
}

CoffeeMachine.prototype.WATER_HEAT_CAPACITY = 4200;

CoffeeMachine.prototype.getTimeToBoil = function() {
  return this._waterAmount * this.WATER_HEAT_CAPACITY * 80 / this._power;
}

CoffeeMachine.prototype.run = function() {
  setTimeout( function() {
    console.log('Coffee is Ready!');
  }, this.getTimeToBoil() );
}

CoffeeMachine.prototype.setWaterAmount = function(amount) {
  this._waterAmount = amount;
}

var coffeeMachine = new CoffeeMachine(10000);
coffeeMachine.setWaterAmount(50);
coffeeMachine.run();

function Hamster() {
  this.food = [];
}

Hamster.prototype.found = function(something) {
  this.food.push(something);
};

var speedy = new Hamster();
var lazy = new Hamster();

speedy.found('apple');
speedy.found('nut');

console.log( speedy.food.length );
console.log( lazy.food.length );