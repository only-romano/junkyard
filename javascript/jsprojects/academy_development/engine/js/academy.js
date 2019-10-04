let app = new Vue({
  el: '#menu',
  data: {
    title: 'Академия'
  },
  template: `
  <div id="menu">
    <p id="menu-title">{{ title }}</p>

    <div id="menu-engine">
      <button id="menu-html" onclick="showMenu('menu-html-view')">HTML/CSS</button>
      <button id="menu-js" onclick="showMenu('menu-js-view')">JavaScript</button>
    </div>

    <div id="menu-html-view">
      <button id="menu-html-back-to-menu" onclick="backToTitle('menu-html-view')">К начальному меню</button>

      <button id="menu-html-base">Основы HTML</button>
      <button id="menu-html-css">Основы CSS</button>

      <button id="menu-html-cascade">Построение сеток</button>
      <button id="menu-html-decor">Декоративные элементы</button>
      <button id="menu-html-text">Оформление текста</button>
      <button id="menu-html-master">Мастерские</button>

      <button id="menu-html-svg">SVG графика</button>
      <button id="menu-html-dynamic">Динамические эффекты</button>
      <button id="menu-html-less">Препроцессор LESS</button>

      <button id="menu-html-keksby">Великий Кексби</button>
    </div>

    <div id="menu-js-view">
      <button id="menu-js-back-to-menu" onclick="backToTitle('menu-js-view')">К начальному меню</button>
      <button id="menu-js-base">Основы JavaScript</button>
      <button id="menu-js-browser">JavaScript в браузере</button>
    </div>
  </div>
  `
})

function menuStart() {
  setTimeout(
    () => {
      document.getElementById('menu-engine').style.opacity = 1;
    }, 250
  );
}

function showMenu(name) {
  let menu = document.getElementById(name);
  menu.style.display = 'block';
  setTimeout(
    () => {
      menu.style.opacity = 1;
      document.getElementById('menu-engine').style.opacity = 0;
    }, 100
  );
}

function backToTitle(name) {
  let menu = document.getElementById(name);
  menu.style.opacity = 0;
  setTimeout(
    () => {
      menu.style.display = 'none';
      menuStart();
    }, 100
  );
}

menuStart();
