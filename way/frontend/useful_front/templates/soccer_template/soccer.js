;'use strict';

(function() {
  let resizePage = () => {
    let headerHeight = document.getElementsByClassName("header")[0].clientHeight;

    let logo = document.getElementsByClassName('header__logo')[0];
    logo.style.width = headerHeight * 0.95 + 'px';
    let title = document.getElementsByClassName('header__title')[0];
    title.style.fontSize = headerHeight * 0.6 + 'px'
    let tm = document.getElementsByClassName('footer__tm')[0];
    tm.style.fontSize = headerHeight * 0.4 + 'px';
  }

  resizePage()
  window.addEventListener("resize", resizePage, false);
})();
