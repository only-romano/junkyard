'use strict';

(function() {
  let html = _.template(document.getElementById('list-template').innerHTML) ({
    title: 'Sweets',
    items: [
      'Cake',
      'Cookie',
      'Pie'
    ]
  });

  let div = document.createElement('div');
    div.innerHTML = html
  document.body.appendChild(div);

  let tmpl = '<ul>\
    <% for (var i=1; i<=count; i++) { %> \
      <li><%=i%></li> \
    <% } %>\
    </ul>';

  div = document.createElement('div');
    div.innerHTML = _.template(tmpl)({count: 5})
  document.body.appendChild(div);

  let compiled = _.template("<h1><%=title%></h1>");
  console.dir(compiled);

  let menu = new Menu({
    title: "Сладости",
    template: _.template(document.getElementById('menu-template').innerHTML),
    listTemplate: _.template(document.getElementById('menu-list-template').innerHTML),
    items: [
      "Торт",
      "Пончик",
      "Пирожное",
      "Шоколадка",
      "Мороженое"
    ]
  });

  document.body.appendChild(menu.getElem());



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

        elem.onmousedown = function() { return false; };

        elem.onclick = function(event) {
          if (event.target.closest('.title')) toggle();
        }
    }


    function renderItems() {
        if (elem.querySelectorAll('ul')[2]) return;

      let listHtml = options.listTemplate({ items: options.items });
        elem.insertAdjacentHTML("beforeEnd", listHtml);
    }


    function open() {
      renderItems();
        elem.classList.add('open');
    };


    function close() { elem.classList.remove('open'); };


    function toggle() {
      if (elem.classList.contains('open')) close();
      else open();
    };

    this.getElem = getElem;
    this.toggle = toggle;
    this.close = close;
    this.open = open;
  }
})();