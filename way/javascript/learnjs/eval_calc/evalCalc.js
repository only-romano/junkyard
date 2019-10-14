(function() {
  var button = document.createElement('button');
    button.innerHTML = 'Eval Calculator';
    button.style.backgroundColor = 'black';
    button.style.color = 'bisque';
    button.style.padding = '5px';
    button.onclick = evalCalc;
  document.body.appendChild(button);

  function evalCalc() {

    function getResult() {
      var expr, res;

      while (true) {
        expr = prompt('Input expression?', '2-');
          if (expr == null) break;

        try {
          res = eval(expr);
          if (isNaN(res)) {
            throw new Error('Result Undefined');
          }

          break;
        } catch (e) {
          alert( 'Error: ' + e.message + ', repeat input' );
        }
      }
    return res;
    }

    var span = document.createElement('span');
      span.innerHTML = 'Result is: ' + getResult() + '.'
      span.style.border = '1px solid pink';
      span.style.backgroundColor = 'black';
      span.style.color = 'aqua';
      span.style.borderRadius = '25%';
      span.style.padding = '10px';
      span.style.margin = '10px';
    document.body.appendChild(span);

    setTimeout( function(){ document.body.removeChild(span) }, 5000);
  }
})();