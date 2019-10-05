(function printNumbersInterval() {
  var number = 1;
  var numbersInterval = setInterval(function() {
    console.log(number);
    if (number === 20) clearInterval(numbersInterval);
    number++
  }, 100);
});

(function printNumbersTimeout() {
  var number = 1;
  var numbersTimeout = setTimeout(function printNumber() {
    console.log(number);
    if (number === 20) {
      clearTimeout(numbersTimeout);
      return;
    }
    number++;
    setTimeout(printNumber, 100);
  }, 100);
});

(function() {
  setTimeout(function() {
    console.log(i);
  }, 100);

  var i;

  function hardWork() {
    for (i = 0; i < 1e8; i++) var s = i ** 20;
  }

  hardWork();
});

(function() {
  var i;
  var timer = setInterval(function() {
    i++
  }, 10);

  setTimeout(function() {
    clearInterval(timer);
    console.log(i);
  }, 50);

  function f() {
    for (i = 0; i < 1e8; i++) var s = i ** 20;
  }

  f();
});


(function() {
  function Runner() {
    this.steps = 0;

    this.step = function() {
      this.doSomethingHeavy();
      this.steps++;
    };

    function fib(n) {
      return n <= 1 ? n : fib(n - 1) + fib(n - 2);
    }

    this.doSomethingHeavy = function() {
      for (var i = 0; i < 25; i++) {
        this[i] = fib(i);
      }
    };
  }

  var runner1 = new Runner();
  var runner2 = new Runner();

  var t1 = setInterval(function() {
    runner1.step();
  }, 15);

  var t2 = setTimeout(function go() {
    runner2.step();
    t2 = setTimeout(go, 15);
  }, 15);

  setTimeout(function() {
    clearInterval(t1);
    clearTimeout(t2);
    console.log("Interval steps: " + runner1.steps);
    console.log("Timeout steps: " + runner2.steps);
  }, 5000);
});


(function() {
  function delay(f, ms) {
    return function() {
      setTimeout(f, ms, [].slice.call(arguments).join(', '));
    }
  }

  function f(x) {
    console.log( x );
  }

  var f1000 = delay(f, 1000);
  var f1500 = delay(f, 1500);

  f1000('test');
  f1500('test2');
});


(function() {

  function debounce(func, ms) {
    return function() {
      clearTimeout(timer);
      timer = setTimeout(func, ms, [].slice.call(arguments).join(', '));
    }
  }

  function f() {
    console.log( arguments[0] );
  }

  f = debounce(f, 1000);
  var timer;

  f(1);
  f(2);

  setTimeout( function() { f(3) }, 1100);
  setTimeout( function() { f(4) }, 1200);
});

(function() {

  function debounce(f, ms) {

    let timer = null;

    return function(...args) {
      const onComplete = () => {
        f.apply(this, args);
        timer = null;
      }

      if (timer) {
        clearTimeout(timer);
      }

      timer = setTimeout(onComplete, ms);
    };
  }

  function f() {
    console.log( arguments[0] );
  }

  f = debounce(f, 1000);

  f(1);
  f(2);

  setTimeout( function() { f(3) }, 1100);
  setTimeout( function() { f(4) }, 1200);
});


(function() {
  function throttle(f, ms) {
    var timer = null;
    var temp;

    return function(...args) {
      function onComplete() {
        f.apply(this, args);
        clearTimeout(timer);
        timer = setTimeout(none, ms);
        var temp = timer._idleStart;
        clearTimeout(timer);
        var temp = timer._idleStart;
        clearTimeout(timer);
        timer = setTimeout(none, ms);
      }

      function none() {}

      if (!timer) {
        onComplete();
        timer = setTimeout(none, ms);
        temp = timer._idleStart;
        timer = setTimeout(none, ms);
      }

      if(timer) {
        clearTimeout(timer);
        timer = setTimeout(onComplete, ms - timer._idleStart)
        temp = timer._idleStart - temp;
        clearTimeout(timer);
        timer = setTimeout(onComplete, ms - temp)
    };
  }

}

  var f = function(a) {
    console.log(a);
  }

  var f1000 = throttle(f, 500);

  setTimeout(f1000, 50, 1);
  setTimeout(f1000, 300, 2);
  setTimeout(f1000, 400, 3);
  setTimeout(f1000, 500, 4);
  setTimeout(f1000, 600, 5);
  setTimeout(f1000, 700, 6);

});

(function() {
  function throttle(func, ms) {
    var isThrottled = false, savedArgs, savedThis;

    function wrapper() {
      if (isThrottled) {
        savedArgs = arguments;
        savedThis = this;
        return;
      }

      func.apply(this, arguments);

      isThrottled = true;

      setTimeout(function() {
        isThrottled = false;
        if (savedArgs) {
          wrapper.apply(savedThis, savedArgs);
          savedArgs = savedThis = null;
        }
      }, ms);
    }

    return wrapper;
  }

  var f = function(a) {
    console.log(a);
  }

  var f1000 = throttle(f, 500);

  setTimeout(f1000, 50, 1);
  setTimeout(f1000, 300, 2);
  setTimeout(f1000, 400, 3);
  setTimeout(f1000, 500, 4);
  setTimeout(f1000, 600, 5);
  setTimeout(f1000, 700, 6);

})();