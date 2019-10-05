function Animal() {}
function Rabbit() {}

Rabbit.prototype = Object.create(Animal.prototype);

var rabbit = new Rabbit();

Rabbit.prototype = {};
console.log( rabbit instanceof Rabbit );
console.log( rabbit instanceof Animal );