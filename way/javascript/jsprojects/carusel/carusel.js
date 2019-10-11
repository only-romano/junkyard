
// creates spans with images
for (var i = 1; i <= 15; i++) {
  var span = document.createElement('span');
  span.classList.add('inner-span');

  var img = document.createElement('img');
  img.classList.add('carusel-img');
  img.setAttribute('src', 'img/carusel' + i + '.jpg');
  span.appendChild(img);

  imgcar.appendChild(span);
}

// sets functions for arrows
var arrows = document.getElementsByClassName('arrow');

arrows[0].addEventListener('click', arrowLeft)
arrows[1].addEventListener('click', arrowRight)

// functions
function arrowRight() {
  var imgs = document.getElementsByClassName('inner-span');

  for (var i = 0; i < imgs.length; i++) {
    var left = parseInt(imgs[i].style.left) || 0;
    var width = parseInt(getComputedStyle(imgs[i].children[0]).width) + parseInt(getComputedStyle(imgs[i]).paddingRight);

    if ( left <  carusel.offsetWidth - imgs.length * width ) { break; }

    imgs[i].style.left = (left - width) + 'px';
  }
}

function arrowLeft() {
  var imgs = document.getElementsByClassName('inner-span');

  for (var i = 0; i < imgs.length; i++) {
    var left = parseInt(imgs[i].style.left) || 0;
    var width = parseInt(getComputedStyle(imgs[i].children[0]).width) + parseInt(getComputedStyle(imgs[i]).paddingRight);

    if ( left >=  0 ) { 
      imgs[i].style.left = '0px';
      break;
    }

    imgs[i].style.left = (left + width) + 'px';
  }
}
