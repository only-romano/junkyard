
let menu = new Menu({
  title: "Сладости",
  template: _.template(document.getElementById('menu-template').innerHTML.trim()),
  listTemplate: _.template(document.getElementById('menu-list-template').innerHTML.trim()),
  items: {
    cake: "Торт", // cake  <a href="#cake">Торт</a>
    donut: "Пончик", // donut
    chocolate: "Шоколадка" // chocolate
  },
  onselect: showSelected
});

function showSelected(itemName) {
  alert(itemName);
}


let elem = menu.getElem();
document.body.appendChild(elem);
elem.addEventListener('select', function(event) { alert( event.detail ); });


function Menu(options) {
  let elem;

  function getElem() {
    if (!elem) render();
    return elem;
  }

  function render() {
    let html = options.template({
      title: options.title
    });

    elem = document.createElement('div');
    elem.innerHTML = html;
    elem = elem.firstElementChild;

    elem.onmousedown = function() {
      return false;
    }

    elem.onclick = function(event) {
      if (event.target.closest('.title')) {
        toggle();
      }

      if (event.target.closest('a')) {
        event.preventDefault();
        select(event.target.closest('a'));
      }

    }
  }

  function renderItems() {
    if (elem.querySelector('ul')) return;

    let listHtml = options.listTemplate({
      items: options.items
    });
    elem.insertAdjacentHTML("beforeEnd", listHtml);
  }

  function select(link) {
    let widgetEvent = new CustomEvent('select', {
      bubbles: true,
      detail: link.getAttribute('href').slice(1)
    });
    elem.dispatchEvent(widgetEvent)
  }

  function open() {
    renderItems();
    elem.classList.add('open');
  };

  function close() {
    elem.classList.remove('open');
  };

  function toggle() {
    if (elem.classList.contains('open')) close();
    else open();
  };

  this.getElem = getElem;
  this.toggle = toggle;
  this.close = close;
  this.open = open;
}

(function() {


  class Voter {

    constructor(options={}) {
      this.elem = options.elem || this._createVoter();
      this.setVote = function(num) {
        this.elem.children[1].textContent = num;
        this._change(num);
      }
    }
  }

  Voter.prototype._createVoter = function() {
    let mass = [['down', this._downVote, '-'], ['vote', this._empty, 0], ['up', this._upVote, '+']];
    let div = document.createElement('div');
      div.className = 'voter';
      for (let i = 0; i < 3; i++) {
        let span = document.createElement('span');
          span.className = mass[i][0];
          span.onclick = mass[i][1].bind(this);
          span.textContent = mass[i][2];
          div.appendChild(span);
      }
    return div;
  }

  Voter.prototype._downVote = function() {
    event.target.nextElementSibling.textContent -= 1;
  }

  Voter.prototype._upVote = function() {
    event.target.previousElementSibling.textContent -= -1;
  }

  Voter.prototype._empty = function() {}

  Voter.prototype._change = function(num) {
    let widgetEvent = new CustomEvent('change', {
      bubbles: true,
      detail: num
    });
    this.elem.dispatchEvent(widgetEvent)
  }


  class StepVoter extends Voter {
    constructor(options={}) {
      super(options);
      this.step = options.step;
    }
  }

  StepVoter.prototype._downVote = function() {
    event.target.nextElementSibling.textContent -= this.step;
  }

  StepVoter.prototype._upVote = function() {
    event.target.previousElementSibling.textContent -= -this.step;
  }


  let voter = new StepVoter({step: 2});
  document.body.appendChild(voter.elem);
  document.getElementsByClassName('voter')[0]
      .addEventListener('change', function(e) {
          alert( e.detail );
       });

  voter.setVote(5);
  console.dir(voter);


})();


(function() {

  let listSelect = new ListSelect({
    elem: document.getElementById('winnie')
  });
    document.getElementById('winnie')
      .addEventListener('selection', function(e) {
          console.log( e.detail );
       })


  function ListSelect(options) {

    let ul = options.elem;
    let lastClickedLi = null;

      ul.addEventListener('click', clickLi);
      ul.addEventListener('mousedown', function() { return false; });


    function clickLi(event) {
      let target = event.target;
        if (target.tagName != 'LI') return;

        if (event.ctrlKey || event.metaKey) {
          toggleSelect(target);
        } else if (event.shiftKey) {
          selectFromLast(target);
        } else {
          selectSingle(target);
        }

      _select();
      lastClickedLi = target;
    }


    function deselectAll() {
      for (let li of ul.children) {
        li.classList.remove('selected');
      }
    }


    function selectFromLast(target) {
      let startElem = lastClickedLi || ul.children[0];
      let isLastClickedBefore = startElem.compareDocumentPosition(target) & 4;

        if (isLastClickedBefore) {
          for (let elem = startElem; elem != target; elem = elem.nextElementSibling) {
            elem.classList.add('selected');
          }
        } else {
          for (let elem = startElem; elem != target; elem = elem.previousElementSibling) {
            elem.classList.add('selected');
          }
        }

      target.classList.add('selected');
    }


    function _select() {
      let widgetEvent = new CustomEvent('selection', {
        bubbles: true,
        detail: getSelected()
      });
      ul.dispatchEvent(widgetEvent);
    }


    function selectSingle(li) {
      deselectAll();
      li.classList.add('selected');
    }


    function toggleSelect(li) {
      li.classList.toggle('selected');
    }


    const getSelected = () => {
      let values = [];
      [].forEach.call(document.getElementsByClassName('selected'), function(item) {
        values.push(item.textContent)
      });

      return values;
    }

    this.getSelected = getSelected;
  }
})();


(function() {

  class CustomSelect {
    constructor(options={}) {
      this.elem = options.elem || this._createNewSelect();
      this._setEvents(this.elem);
    }
  }

  CustomSelect.prototype._createNewSelect = function() {

    let div = document.createElement('div');
    let button = document.createElement('button');
    let ul = document.createElement('ul');
    let li = document.createElement('li');
      div.className = 'customselect';
      button.className = 'title';
      button.textContent = 'Choose';
      li.setAttribute('data-value', 'some stuff');
      li.textContent = 'Some stuff';

    ul.appendChild(li);
    div.appendChild(button);
    div.appendChild(ul);
    document.body.appendChild(div);

    return div;
  }

  CustomSelect.prototype._setEvents = function(elem) {
    document.addEventListener('click', this._closeSelect.bind(this));
    elem.addEventListener('click', this._toggleShowcase.bind(this));
    elem.addEventListener('selection', this._setSelection.bind(this));
  }

  CustomSelect.prototype._closeSelect = function(div) {
    let target = event.target.tagName;
      if (div.children && target == 'LI') {
        div.classList.remove('open');
        return;
      } else if (!div.children && this.elem.contains(event.target)) {
        return;
      }
    this.elem.classList.remove('open');
  }

  CustomSelect.prototype._toggleShowcase = function() {
    let target = event.target;
      if (event.target.tagName == 'BUTTON') {
        this.elem.classList.toggle('open');
      } else if (event.target.tagName == 'LI') {
        this._selection(event.target, this.elem);
      }
  }

  CustomSelect.prototype._selection = function(li, div) {
    let widgetEvent = new CustomEvent('selection', {
      bubbles: true,
      detail: [li.dataset.value, li.textContent]
    });
    div.dispatchEvent(widgetEvent);
  }

  CustomSelect.prototype._setSelection = function(e) {
    let button = this.elem.querySelector('button');
    let result = document.getElementById('result');
      button.innerHTML = e.detail[1];
      result.textContent = e.detail[0];
    this._closeSelect(this.elem);
  }


  let animalSelect = new CustomSelect({
    elem: document.getElementById('animal-select')
  });

  let foodSelect = new CustomSelect({
    elem: document.getElementById('food-select')
  });

  document.addEventListener('select', function(event) {
    document.getElementById('result').innerHTML = event.detail.value;
  });

})();

(function() {

  class Slider {

    constructor(options={}) {
      this.slider = options.elem || this._createNewSlider();
      this.max = options.max || 100;
      this.value = options.value || 0;
      this._setEvents(this.slider.children[0]);
      document.body.appendChild(this.slider);
    }

  }


  Slider.prototype._createNewSlider = function() {
    let slider = document.createElement('div');
    let thumb = document.createElement('div');
    slider.appendChild(thumb);
      slider.className = 'slider';
      thumb.className = 'thumb';

    return slider;
  }

  Slider.prototype._setEvents = function(thumb) {
    thumb.ondragstart = function() { return false; };
    thumb.onmousedown = this._dragThumb.bind(this);
  }

  Slider.prototype._dragThumb = function(e) {
    let slider = this.slider;
    let thumb = this.slider.children[0];
    let sliderCoords = this._getCoords(slider);
    let thumbCoords = this._getCoords(thumb);
    let shiftX = e.pageX - thumbCoords.left;

      document.onmouseup = (function() {
        document.onmousemove = document.onmouseup = null;
        let onePoint = (slider.offsetWidth - thumb.offsetWidth) / this.max;
        let value = ~~((thumbCoords.left - thumb.offsetWidth/2) / onePoint);
        this.value = value;
        console.log(this.value);
      }).bind(this);

      document.onmousemove = (function(e) {
        let newLeft = e.pageX - shiftX - sliderCoords.left;
        let rightEdge = slider.offsetWidth - thumb.offsetWidth;
          if (newLeft < 0) newLeft = 0;
          if (newLeft > rightEdge) newLeft = rightEdge;

          thumb.style.left = newLeft + 'px';
      }).bind(this);

    return false;
  }
/*
  Slider.prototype._change = function(value) {
    let widgetEvent = new CustomEvent('change', {
      bubbles: true,
      detail: value
    });
    div.dispatchEvent(widgetEvent);
  }

  Slider.prototype._slide = function(value) {
    let widgetEvent = new CustomEvent('slide', {
      bubbles: true,
      detail: value
    });
    div.dispatchEvent(widgetEvent);
  }
*/
  Slider.prototype._getCoords = (elem) => {
    let box = elem.getBoundingClientRect();
    return { top: box.top + pageYOffset, left: box.left + pageXOffset };
  }


  Slider.prototype.setValue = function(value) {
    this.value = value;
  }


  let slider = new Slider();

})();