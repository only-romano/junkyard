function Machine(power) {
  this._power = power;
  this._enabled = false;
  this.enable = function() { self._enabled = true; };
  this.disable = function() { self._enabled = false; };

  var self = this;
}


function CoffeeMachine(power) {
  Machine.apply(this, arguments);

  var parentEnable = this.enable;
  var parentDisable = this.disable;
  var waterAmount = 0;
  var coffeeTimer = null

  this.enable = function() {
    parentEnable();
    this.run();
  }
  this.disable = function() {
    parentDisable();
    clearTimeout(coffeeTimer);
    coffeeTimer = null;
  }
  this.setWaterAmount = function(amount) { waterAmount = amount; };
  this.run = function() { 
    if (this._enabled) {
      if (coffeeTimer) clearTimeout(coffeeTimer);
      coffeeTimer = setTimeout(onReady, 1000);
    } else {
      throw new Error('Coffee machine is disabled');
    } };


  function onReady() { console.log('Coffee is Ready!'); }
}

var coffeeMachine = new CoffeeMachine(10000);
coffeeMachine.enable();
coffeeMachine.run();
console.log(coffeeMachine._enabled);
console.log(coffeeMachine._power);
coffeeMachine.disable();

function Fridge(power) {
  Machine.apply(this, arguments);

  var food = [];

  this.addFood = function(item) {
    if (!this._enabled) {
      console.log( 'Fridge is disabled' );
      return;
    }

    for (var i = 0; i < arguments.length; i++) {
      if ( food.length === parseInt( this._power / 100 ) ) {
        console.log( 'Error: no more space' );
        return;
      }
      food.push(arguments[i]);
    }
  }

  this.getFood = function() {
    return food.slice();
  }

  this.filterFood = function(func) {
    return food.filter(func);
  }

  this.removeFood = function(item) {
    for (var i = 0; i < arguments.length; i++) {
      var index = food.indexOf(arguments[i]);
      if (!~index) {
        console.log(index, ~index, ~22.3);
        console.log( 'There is no ' + arguments[i] + ' in Fridge.');
        continue;
      }
      food.splice(index, 1);
    }
  }

  var parentDisable = this.disable;
  this.disable = function() {
    if (food.length) {
      console.log('Can\'t disable fridge with food');
      return;
    }
    parentDisable();
  }

}

var fridge = new Fridge(500);
fridge.addFood('beef');
fridge.enable();
fridge.addFood( { title: 'cutlet', calories: 200 });
fridge.addFood(
  { title: 'juice', calories: 50 },
  { title: 'vegetables', calories: 25 }
);

fridge.addFood(
  { title: 'pie', calories: 300 },
  { title: 'honey', calories: 350 },
  { title: 'cake', calories: 500 }
);
fridge.addFood('beer');

var fridgeFood = fridge.getFood();
fridgeFood.push('spoon', 'knife');
console.log( fridge.getFood() );


fridge.removeFood('no such food');

console.log( fridge.getFood().length );
var dietItems = fridge.filterFood(function(item) {
  return item.calories <= 50;
});

dietItems.forEach(function(item) {
  console.log(item.title);
  fridge.removeFood(item);
});

console.log( fridge.getFood().length );
fridge.disable();