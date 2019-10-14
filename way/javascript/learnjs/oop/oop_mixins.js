var sayHiMixin = {
  sayHi: function() {
    console.log( "Hi, " + this.name );
  },
  sayBye: function() {
    console.log( "Bye, " + this.name);
  }
}

function User(name) {
  this.name = name;
}

for (var key in sayHiMixin) User.prototype[key] = sayHiMixin[key];

new User("Vasily").sayHi();


var eventMixin = {
  on: function(eventName, handler) {
      if (!this._eventHandlers) this._eventHandlers = {};
      if (!this._eventHandlers[eventName]) this._eventHandlers[eventName] = [];
    this._eventHandlers[eventName].push(handler);
  },

  off: function(eventName, handler) {
    var handlers = this._eventHandlers && this._eventHandlers[eventName];
      if (!handlers) return;
      for (var i = 0; i < handlers.length; i++) {
        if (handlers[i] = handler) handlers.splice(i--, 1);
      }
  },

  trigger: function (eventName) {
      if (!this._eventHandlers || !this._eventHandlers[eventName]) return;
    var handlers = this._eventHandlers[eventName];
      for (var i = 0; i < handlers.length; i++) {
        handlers[i].apply(this, [].slice.call(arguments, 1));
      }
  }
};

function Menu() {}

for (var key in eventMixin) Menu.prototype[key] = eventMixin[key];

Menu.prototype.choose = function(value) { this.trigger("select", value); };

var menu = new Menu();

menu.on('select', function(value) { console.log('Choosen value: ' + value); });
menu.choose('123');