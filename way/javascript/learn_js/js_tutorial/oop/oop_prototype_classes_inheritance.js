
function Animal(name) {
  this.name = name;
  this.speed = 0;
}

Animal.prototype.run = function(speed) {
  this.speed += speed;
  console.log( this.name + ' is running, speed is ' + this.speed );
};

Animal.prototype.stop = function() {
  this.speed = 0;
  console.log( this.name + 'is standing' );
};


function Rabbit(name) {
  Animal.apply(this, arguments);
}

Rabbit.prototype = Object.create(Animal.prototype);
Rabbit.prototype.constructor = Rabbit;

Rabbit.prototype.jump = function() {
  this.speed++;
  console.log( this.name + ' is jumping');
};

Rabbit.prototype.run = function(speed) {
  Rabbit.prototype.__proto__.run.apply(this, arguments);
  this.jump();
}

var rabbit = new Rabbit('Rabo');
rabbit.run(5);


function Animal2(name) {
  this.name = name;
}

Animal2.prototype.walk = function() {
  console.log( this.name + ' walks');
};

function Rabbit2(name) {
  Animal2.apply(this, arguments);
}

Rabbit2.prototype = Object.create(Animal2.prototype);
Rabbit2.prototype.constructor = Rabbit2;

Rabbit2.prototype.walk = function() {
  console.log( this.name + ' walks & jumps!' );
};

var rabbit2 = new Rabbit2('crol');
rabbit2.walk();

var animal2 = new Animal2('any');
animal2.walk();


function Clock(options) {
  this._template = options.template;
}

Clock.prototype._render = function() {
  var date = new Date();
  var hours = date.getHours();
    if (hours < 10) hours = '0' + hours;
  var minutes = date.getMinutes();
    if (minutes < 10) minutes = '0' + minutes;
  var seconds = date.getSeconds();
    if (seconds < 10) seconds = '0' + seconds;

  var output = this._template.replace('h', hours).replace('m', minutes).replace('s', seconds);

  console.log(output);
}

Clock.prototype.stop = function() {
  clearInterval(this._timer);
};

Clock.prototype.start = function() {
  this._render();
  var self = this;
  this._timer = setInterval(function() {self._render();}, 1000);
};


function ExtendedClocks(options) {
  Clock.apply(this, arguments);
  this.precision = +options.precision || 1000;
}

ExtendedClocks.prototype = Object.create(Clock.prototype);
ExtendedClocks.prototype.constructor = ExtendedClocks;

ExtendedClocks.prototype.start = function() {
  this._render();
  var self = this;
  this._timer = setInterval(function() {self._render();}, this.precision);
}


var clock = new ExtendedClocks({template: 'h:m:s', precision: 2000});
clock.start();


function Menu(state) {
  this._state = state || Menu.STATE_CLOSED;
};

Menu.prototype.STATE_OPEN = 1;
Menu.prototype.STATE_CLOSED = 0;

Menu.prototype.open = function() {
  this._state = Menu.STATE_OPEN;
};

Menu.prototype.close = function() {
  this._state = Menu.STATE_CLOSED;
};

Menu.prototype._stateAsString = function() {
  switch (this._state) {
    case Menu.STATE_OPEN:
      return 'open';

    case Menu.STATE_CLOSED:
      return 'close';
  }
};

Menu.prototype.showState = function() {
  console.log(this._stateAsString());
};


function AnimatingMenu() {
  Menu.apply(this, arguments);
}

AnimatingMenu.prototype = Object.create(Menu.prototype);
AnimatingMenu.prototype.constructor = AnimatingMenu;

AnimatingMenu.prototype.STATE_ANIMATED = 2;

AnimatingMenu.prototype.open = function() {
  var self = this;
  this._state = this.STATE_ANIMATED;
  this._timer = setTimeout(function() {
    Menu.prototype.open.call(self);
  }, 1000);
};

AnimatingMenu.prototype.close = function() {
  clearTimeout(this._timer);
  Menu.prototype.close.apply(this);
};

AnimatingMenu.prototype._stateAsString = function() {
  switch (this._state) {
    case this.STATE_ANIMATED:
      return 'animated';

    default:
      return Menu.prototype._stateAsString.call(this);
  }
};

    // использование..

var menu = new AnimatingMenu();
menu.showState(); // закрыто
menu.open();
menu.showState(); // анимация
setTimeout(function() {
  menu.showState();
  menu.close();
  menu.showState(); // закрыто (закрытие без анимации)
}, 1000);