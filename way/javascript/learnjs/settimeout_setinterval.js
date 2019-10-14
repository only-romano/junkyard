(function() {
  var phrase = 'Hello';
  var who = 'Vasily';

  function sayHi(phrase, who) {
    console.log( phrase + ', ' + who );
  }

  setTimeout(sayHi, 1000, phrase, who);
  setTimeout(function() {console.log(arguments[0])}, 1000, who);
})();

(function() {
  var timerId = setTimeout(function() { alert(1) }, 1000);
  console.log( timerId );

  clearTimeout(timerId);  // canceled
  console.log( timerId );  // number is still exist
})();

(function() {
  var timerId = setInterval(function() {
    console.log( 'tic' );
  }, 1000);

  setTimeout(function() {
    clearInterval(timerId)
    console.log('Stop!');
  }, 5000);
})();

(function() {
  var i = 30;
  var b = 30;
  var now = new Date();

  function fibbonachi(i) {
    return (i == 0) || (i == 1) ? 1 : fibbonachi(i-1) + fibbonachi(i-2);
  }

  var timeId =  setInterval(function() {
      fibbonachi(i);
      i--;
      console.log('Interval:' + (new Date() - now));
        if (i == 20) {
          clearInterval(timeId);
          console.log('All Intervals:' + (new Date() - now));
        }
      }, 100);

  var timeId2 =  setTimeout(function run() {
      fibbonachi(b);
      b--;
      console.log('Timeout:' + (new Date() - now));
        if (b == 20) {
          console.log('All Timeouts:' + (new Date() - now));
          clearInterval(timeId2);
          return;
        }
      setTimeout(run, 100);
      }, 100);
})();