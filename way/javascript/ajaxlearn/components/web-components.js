let MyTimerProto = Object.create(HTMLButtonElement.prototype);
let intbut;

MyTimerProto.tick = function() {
  this.timer++;
  this.innerHTML = this.timer;
}

MyTimerProto.createdCallback = function() {
  this.timer = 0;
}

MyTimerProto.attachedCallback = function() {
  intbut = setInterval(this.tick.bind(this), 1000);
}

MyTimerProto.detachedCallback = function() {
  removeInterval(intbut);
}

document.registerElement('my-timer', {
  prototype: MyTimerProto,
  extends: 'button'
});

let timer = document.createElement('button', 'my-timer');
  timer.id = "time";
  timer.innerHTML = 0;
  timer.setAttribute('is', "my-timer");
  timer.onclick = function() {
    alert("Current value is: " + this.innerHTML);
  };

  document.body.appendChild(timer);


setTimeout(function() {
  document.registerElement("hello-world", {
    prototype: {
      __proto__: HTMLElement.prototype,
      sayHi: function() { alert('Hello!') }
    }
  });

  hello.sayHi();
}, 2000);


let pseudo = pselem.createShadowRoot();
  pseudo.innerHTML = '<h3><content select="h3"></content></h3>\
                      <p>Привет из подполья!</p><h4>\
                      <content select="h4"></content></h4>'

pseudo = pssection.createShadowRoot();
  pseudo.innerHTML = "<content select='h1'></content>\
                      <content select='.author'>Ты автор сраный.</content>\
                      <content></content>"