'use strict';

(function() {
  window.onscroll = function() {
    let scrolled = window.pageYOffset || document.documentElement.scrollTop;
      document.getElementById('showScroll').innerHTML = scrolled + 'px';
  }

  let avatar = document.getElementById('avatar');
  let avatarBottom = avatar.getBoundingClientRect().bottom + pageYOffset;
  window.addEventListener('scroll', avatarVinnie);

  function avatarVinnie() {
      if (pageYOffset > avatarBottom) {
        avatar.classList.add('fixed');
      } else if (pageYOffset < avatarBottom && avatar.classList.contains('fixed')) {
        avatar.classList.remove('fixed');
      }

  }
})();

(function() {
  let matrix = document.createElement('div');
    for (let i = 0; i < 2000; i++) matrix.innerHTML += `${i} `;
  document.body.appendChild(matrix);

  window.addEventListener('scroll', showNavigateArrow);
  let clientHeight = document.documentElement.clientHeight;
  let navigateArrow = document.createElement('div');
    navigateArrow.className = 'navigate-arrow';
    navigateArrow.style.left = document.documentElement.clientWidth / 2 + 'px';
  document.body.appendChild(navigateArrow);
  let temporalTop;

  function showNavigateArrow() {
    if (pageYOffset > clientHeight) {
      temporalTop = null;
        navigateArrow.style.display = 'block';
        navigateArrow.innerHTML = '▲';
        navigateArrow.onclick = topArrow;
    } else if (pageYOffset < clientHeight && !temporalTop) {
      navigateArrow.style.display = 'none';
    }

    function topArrow() {
      temporalTop = window.pageYOffset;
      scrollTo(0, 0);
        navigateArrow.innerHTML = '▼'
        navigateArrow.onclick = downArrow;
    }

    function downArrow() {
      scrollTo(0, temporalTop);
        navigateArrow.innerHTML = '▲';
        navigateArrow.onclick = topArrow;
    }
  }
})();

(function() {
  window.addEventListener('scroll', uploadImgs)
  let imgs = document.getElementsByTagName('img');
  let targetImgs = [];
    for (let i = 0; i < imgs.length; i++) {
      if (imgs[i].realsrc) {
        imgs[i].addAttribute('data-loaded', '1');
        targetImgs.push(imgs[i]);
      }
    }
  uploadImgs();

  function uploadImgs() {
    for (let i = 0; i < targetImgs.length; i++) {
      if (targetImgs[i] = )
    }
  }
})();