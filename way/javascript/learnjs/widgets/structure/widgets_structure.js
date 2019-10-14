'use strict';

let pageClock;
let listSelect;

(function() {
  function Menu(options) {
    let elem = options.elem;

    elem.onmousedown = function() { return false; };
    elem.onclick = function(event) {
      let close = event.target.closest('.title');
      if (close && elem.contains(close)) toggleOpen();
    };

    function toggleOpen() {
      elem.classList.toggle('open');
    }

    this.toggleOpen = toggleOpen;
  }

  let menu = new Menu({elem: document.getElementById('sweets-menu')});

  let objToMenu = {
    title: 'Animals',
    items: [
      'Kitty',
      'Doggy',
      'Ducky',
      'Mouse',
      'Birdy'
    ]
  };

  let newMenu = new MenuCreate(objToMenu);
  let elemNewMenu = newMenu.getElem();
  document.body.appendChild(elemNewMenu);

  function MenuCreate(options) {
    let elem;

    function getElem() {
      if (!elem) render();
      return elem;
    }

    function render() {
      elem = document.createElement('div');
        elem.className = 'menu';

      let titleElem = document.createElement('span');
        elem.appendChild(titleElem);
        titleElem.className = 'title';
        titleElem.textContent = options.title;

      elem.onmousedown = function() { return false; };

      elem.onclick = function(event) {
        if (event.target.closest('.title')) toggle();
      }
    }

    function renderItems() {
      let items = options.items || [];
      let list = document.createElement('ul');
        items.forEach(function(item) {
          let li = document.createElement('li');
            li.textContent = item;
            list.appendChild(li);
        });

      elem.appendChild(list);
    }

    function open() {
      if (!elem.querySelector('ul')) renderItems();

      elem.classList.add('open');
    }

    function close() {
      elem.classList.remove('open');
    }

    function toggle() {
      if (elem.classList.contains('open')) close();
      else open();
    }

    this.getElem = getElem;
    this.toggle = toggle;
    this.close = close;
    this.open = open;

  }

})();

(function() {

  pageClock = new Clock({
    elem: document.getElementById('clock')
  })

  function Clock(options) {
    let elem = options.elem;
    let timeInterval;

    function start() {
      setTime();
      timeInterval = setInterval(setTime, 1000);
    }

    function stop() {
      clearInterval(timeInterval);
    }

    function setTime() {
      let time = new Date();
      let [hour, min, sec] = [time.getHours(),
                                    time.getMinutes(), time.getSeconds()]
      elem.children[0].innerHTML = hour < 10 == 1 ? '0' + hour : hour;
      elem.children[1].innerHTML = min < 10 == 1 ? '0' + min : min;
      elem.children[2].innerHTML = sec < 10 == 1 ? '0' + sec : sec;
    }

    this.start = start;
    this.stop = stop;
  }
})();

(function() {

  function Slider() {

    let slider = document.createElement('div');
    let thumb = document.createElement('div');
    slider.appendChild(thumb);
      slider.className = 'slider';
      thumb.className = 'thumb';

      thumb.ondragstart = function() { return false; };

      thumb.onmousedown = function(e) {

        let sliderCoords = getCoords(slider);
        let thumbCoords = getCoords(thumb);
        let shiftX = e.pageX - thumbCoords.left;

          document.onmouseup = function() {
            document.onmousemove = document.onmouseup = null;
          }

          document.onmousemove = function(e) {

            let newLeft = e.pageX - shiftX - sliderCoords.left;
            let rightEdge = slider.offsetWidth - thumb.offsetWidth;

              if (newLeft < 0) newLeft = 0;
              if (newLeft > rightEdge) newLeft = rightEdge;

            thumb.style.left = newLeft +'px';
          }

        return false;
      }

    const getCoords = (elem) => {
      let box = elem.getBoundingClientRect();
      return { top: box.top + pageYOffset, left: box.left + pageXOffset };
    }

    return slider;
  }

  let slider = new Slider();
  document.body.appendChild(slider);
})();

(function() {

  listSelect = new ListSelect({
    elem: document.getElementById('winnie')
  });


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

/*
  <div id="voter" class="voter">
    <span class="down">-</span>
    <span class="vote">0</span>
    <span class="vote">+</span>
  </div>
*/

(function() {


  class Voter {

    constructor(options={}) {
      this.elem = options.elem || this._createVoter();
      this.setVote = function(num) {
        this.elem.children[1].textContent = num;
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
  voter.setVote(5);
  console.dir(voter);

})();