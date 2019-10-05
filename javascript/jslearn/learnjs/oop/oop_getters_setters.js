
function CoffeeMachineV2(power, capacity) {

  this.run = function() {
    runTimer = setTimeout(function() {
        runTimer = null;
        onReady();
      }, getTimeToBoil());
  };

  this.stop = function() {
    clearTimeout(runTimer);
    runTimer = null;
  };

  this.waterAmount = function(amount) {
    if (!arguments.length) return waterAmount;

    if (amount < 0) {
      throw new Error("Water amount value must be a positive number");
    } else if (amount > capacity) {
      throw new Error('You can\'t fill more water then coffee machine capacity = ' + capacity);
    }
    waterAmount = amount;
  };

  this.getPower = function() {
    return power;
  };

  this.addWater = function(amount) {
    self.waterAmount(waterAmount + amount);
  }

  this.setOnReady = function(func) {
    onReady = func;
  }

  this.isRunning = function() {
    return !!runTimer;
  }

  var self = this;
  var waterAmount = 0;
  var WATER_HEAT_CAPACITY = 4200;
  var runTimer = null;

  function getTimeToBoil() {
    return waterAmount * WATER_HEAT_CAPACITY * 80 / power;
  }

  function onReady() {
    console.log('Coffee is Ready!');
  }
}

var coffeeMachine = new CoffeeMachineV2(10000, 500);
coffeeMachine.waterAmount(450);
console.log( coffeeMachine.waterAmount() );


function User() {

  this.setFirstName = function(name) {
    firstName = name;
  };
  this.setSurname = function(name) {
    surname = name;
  };
  this.getFullName = function() {
    if (firstName && surname) {
      return firstName[0].toUpperCase() + firstName.slice(1) +
                   ' ' + surname[0].toUpperCase() + surname.slice(1);
    } else if (!firstName) {
      return 'Please set first name!';
    } else if (!surname) {
      return 'Please set surname!';
    }
  }

  var firstName;
  var surname;
}

var user = new User;
console.log( user.getFullName() );
user.setFirstName('petro');
console.log( user.getFullName() );
user.setSurname('ivancovich');
console.log( user.getFullName() );

var coffeeMacnine2 = new CoffeeMachineV2(10000, 400);
coffeeMacnine2.addWater(200);
coffeeMacnine2.addWater(100);
console.log( coffeeMacnine2.waterAmount() );

coffeeMacnine2.setOnReady( function() {
  console.log('Cofee is ready: ' + coffeeMacnine2.waterAmount() + 'ml');
});


var coffeeMachine3 = new CoffeeMachineV2(20000, 500);
coffeeMachine3.waterAmount(100);

console.log( 'Before: ' + coffeeMachine3.isRunning() );
coffeeMachine3.run();
console.log( 'In process: ' + coffeeMachine3.isRunning() );
coffeeMachine3.setOnReady( function() {
  console.log( 'Coffee is Ready!\nAfter: ' + coffeeMachine3.isRunning() );
});