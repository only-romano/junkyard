(function() {
  var tdMass = document.querySelectorAll('.bogua td');
  for (var i = 0; i < tdMass.length; i++) {
    tdMass[i].style.backgroundColor = tdMass[i].innerHTML.split('<br>')[2];
  }
})();

(function() {
  var selectedTd;
  var oldColor;

  document.querySelector('.bogua').onclick = function(event) {
    var target = event.target;

      while (target != this) {
        if (target.tagName == 'TD') {
          highlight(target);
          return;
        }
        target = target.parentNode;
      }
  };

  function highlight(node) {
      if (selectedTd) { selectedTd.style.backgroundColor = oldColor; }
    selectedTd = node;
    oldColor = selectedTd.style.backgroundColor;
    selectedTd.style.backgroundColor = 'red';
  }
})();

function Menu(elem) {
  this.save = function() {
    alert('Saved');
  };
  this.load = function() {
    alert('Loaded');
  };
  this.search = function() {
    alert('Searching...');
  };
  this.returnDivs = function() {
    Array.prototype.slice.call(document.getElementsByClassName('pane')).
    forEach( function(e) {
      e.style.display = '';
    })
  };

  var self = this;

  elem.onclick = function(e) {
    var target = e.target;
    var action = target.getAttribute('data-action');
    if (action) {
      self[action]();
    }
  };
}

new Menu(menu);

(function() {
  var panes = document.getElementsByClassName('pane');
  for (var i = 0; i < panes.length; i++) {
    createButton(panes[i]);
  }

  function createButton(node) {
    var button = document.createElement('button');
      button.classList.add('remove-button');
      button.innerHTML = '[x]';
      button.style.left = node.getBoundingClientRect().right;
    node.appendChild(button);
  }

  document.querySelector('.exercise1').onclick = function(event) {
    if (event.target.tagName = 'button') {
      event.target.parentNode.style.display = 'none';
    }
  }
})();

(function() {
  document.getElementsByClassName('tree')[0].onclick = function(event) {
    if (event.target.tagName == 'SPAN') {
      var elems = event.target.parentNode.querySelector('ul').classList.
      toggle('hidden-menu');
    }
  }
})();

(function() {
  var grid = document.getElementsByClassName('grid')[0];
  var ths = grid.querySelectorAll('th');

  document.getElementsByClassName('grid')[0].onclick = function(event) {
    if (event.target.tagName == 'TH') {
      var tbody = grid.querySelector('tbody');
      tbody.innerHTML = [].slice.call(tbody.rows).
      sort(function(a,b) { 
        if (event.target.dataset.type === 'number') {
          return +a.children[event.target.cellIndex].innerHTML -
                 +b.children[event.target.cellIndex].innerHTML;
        } else {
          return (a.children[event.target.cellIndex].innerHTML >
                  b.children[event.target.cellIndex].innerHTML) ? 1 : -1;
        }
      }).reduce(function(string, current) { return string +
        current.outerHTML; }, '');
    }
  }
})();