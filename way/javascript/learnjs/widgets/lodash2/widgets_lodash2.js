'use strict';

let users = [
  {name: 'Вася', age: 10},
  {name: 'Петя', age: 15},
  {name: 'Женя', age: 20},
  {name: 'Маша', age: 25},
  {name: 'Даша', age: 30},
];

let tmpl = "<table> \
             <tr> \
              <% for (var key in mass[0]) { %><th><%-key%></th> <% }; %> \
             </tr> \
             <% mass.forEach(function(user) { %> \
             <tr> \
              <td><%-user.name%></td> \
              <td><%-user.age%></td> \
             </tr> \
            <% }); %></table>";

let table = _.template(tmpl)({mass: users});
let div = document.createElement('div');
  div.innerHTML = table;

document.body.appendChild(div);



function Menu(options) {
  var elem;

  function getElem() {
    if (!elem) render();
    return elem;
  }

  function render() {
    var html = options.template({
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

    var listHtml = options.listTemplate({
      items: options.items
    });
    elem.insertAdjacentHTML("beforeEnd", listHtml);
  }

  function select(link) {
    alert(link.getAttribute('href').slice(1));
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

var menu = new Menu({
  title: "Сладости",
  // передаём также шаблоны
  template: _.template(document.getElementById('menu-template').innerHTML),
  listTemplate: _.template(document.getElementById('menu-list-template').innerHTML),
  items: {
    "donut": "Пончик",
    "cake": "Пирожное",
    "chocolate": "Шоколадка"
  }
});

document.body.appendChild(menu.getElem());