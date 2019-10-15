"use strict"

function CoffeeMachine(power) {

  var self = this;
  this.waterAmount = 0;
  this.run = function() {
    runTimer = setTimeout(onReady, getBoilTime());
  };
  this.stop = function() {
    clearTimeout(runTimer);
  }

  var WATER_HEAT_CAPACITY = 4200;
  var runTimer;

  function getBoilTime() {
    return self.waterAmount * WATER_HEAT_CAPACITY * 80 / power;
  }

  function onReady() {
    console.log('Coffee is Ready!');
  }

  console.log('Created coffee-machine with power: ' + power + ' watt.');
}

var coffeeMachine = new CoffeeMachine(50000);
coffeeMachine.waterAmount = 200;

coffeeMachine.run();
coffeeMachine.stop();