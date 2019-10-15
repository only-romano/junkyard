(function() {
  var field = document.createElement('div');
  var ball = document.createElement('div');
    field.className = 'field';
    field.style.height = document.documentElement.clientHeight * 0.3 + 'px';
    ball.className = 'ball';
    field.appendChild(ball);
  document.body.appendChild(field);
})();


(function() {
  var ball = document.getElementsByClassName('ball')[0];

  ball.onmousedown = function(event) {
    var coords = getCoords(ball);
    var shiftX = event.pageX - coords.left;
    var shiftY = event.pageY - coords.top;

      ball.style.position = 'absolute';
    document.body.appendChild(ball);
    moveAt(event);
      ball.style.zIndex = 4;

    function moveAt(event) {
      ball.style.left = event.pageX - shiftX + 'px';
      ball.style.top = event.pageY - shiftY + 'px';
    }

    document.addEventListener('mousemove', moveDoc);

    function moveDoc(event) {
      moveAt(event);
    }

    ball.addEventListener('mouseup', function upBall() {
      document.removeEventListener('mousemove', moveDoc);
      ball.removeEventListener('mouseup', upBall);
    });
  }

  ball.ondragstart = function() {
    return false;
  }

  function getCoords(elem) {
    var box = elem.getBoundingClientRect();
    return {
      top: box.top + pageYOffset,
      left: box.left + pageXOffset
    };
  }
})();


(function() {
  var slider = document.getElementsByClassName('slider')[0];
  var thumb = document.getElementsByClassName('thumb')[0];

  slider.addEventListener('click', moveThumbOnClick);

  function moveThumbOnClick(event) {
    var width = slider.offsetWidth;
    var side = thumb.offsetWidth / 2;
    var left = event.pageX - slider.getBoundingClientRect().left - side;
      if (left < width / 30) left = width / 30 - side;
      if (left > width / 30 * 29) left = width / 30 * 29 - side;
    thumb.style.left = left + 'px';
  }

  thumb.ondragstart = function() { return false };

  thumb.onmousedown = function(event) {
    var shiftX = event.pageX - getLeft(thumb);
    moveThumb(event);

    function moveThumb(event) {
      var width = slider.offsetWidth;
      var side = thumb.offsetWidth / 2;
      var left = event.pageX - slider.getBoundingClientRect().left - shiftX;
        if (left < width / 30) left = width / 30 - side;
        if (left > width / 30 * 29) left = width / 30 * 29 - side;
      thumb.style.left = left + 'px';
    }

    document.addEventListener('mousemove', moveDocThumb);

    function moveDocThumb(event) {
      moveThumb(event);
    }

    document.addEventListener('mouseup', function upThumb() {
      document.removeEventListener('mousemove', moveDocThumb);
      document.removeEventListener('mouseup', upThumb);
    });
  }

  function getLeft(elem) {
    return elem.getBoundingClientRect().left + pageXOffset;
  }
})();


(function() {
  var field = document.getElementsByClassName('field2')[0];

  document.ondragstart = function() { return false; };

  function getCoords(elem) {
    var box = elem.getBoundingClientRect();
    return {
      top: box.top + pageYOffset,
      left: box.left + pageXOffset,
      width: box.width,
      height: box.height
    };
  }

  document.addEventListener('mousedown', moveHeroes);

  function moveHeroes(event) {

    if ( event.target.classList.contains('draggable') ) {
      var width = Math.max(
        document.body.scrollWidth, document.documentElement.scrollWidth,
        document.body.offsetWidth, document.documentElement.offsetWidth,
        document.body.clientWidth, document.documentElement.clientWidth
      );
      var height = Math.max(
        document.body.scrollHeight, document.documentElement.scrollHeight,
        document.body.offsetHeight, document.documentElement.offsetHeight,
        document.body.clientHeight, document.documentElement.clientHeight
      );
      var hero = event.target;
      var coords = getCoords(hero);
      var shiftX = event.pageX - coords.left;
      var shiftY = event.pageY - coords.top;

        hero.style.position = 'absolute';
        hero.style.zIndex = 8;
      document.body.appendChild(hero);
      moveHero(event);

      function moveHero(event) {
        var left = event.pageX - shiftX;
        var top = event.pageY - shiftY;

          if (left < 0) {
            left = 0;
          } else if (left > width - coords.width) {
            left = width - coords.width;
          }

          if (top < 0) {
            top = 0;
          } else if (top > height - coords.height) {
            top = height - coords.height;
          }

          hero.style.left = left + 'px';
          hero.style.top = top + 'px';
      }

      document.addEventListener('mousemove', moveHeroListener);

      function moveHeroListener(event) {
        moveHero(event);
      }

     document.addEventListener('mouseup', function downHero() {
      document.removeEventListener('mousemove', moveHeroListener);
      document.removeEventListener('mouseup', downHero);
    });
    }
    return false;
  }
})();