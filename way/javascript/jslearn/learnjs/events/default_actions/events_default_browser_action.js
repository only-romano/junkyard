// choose to be me - sunrise avenue


document.addEventListener('click', function(event) {
  if (event.target.nodeName === 'A') {
    event.preventDefault ? event.preventDefault() : (event.returnValue = false);
  }
})

document.getElementsByClassName('menu')[0].onclick = function(event) {
  if (event.target.nodeName === 'A') {
    alert( event.target.getAttribute('href') );
    return false;
  }
}

function handler() {
  alert('...');
  return false;
}

document.getElementById('contents').onclick = function(event) {
  var target = event.target;
    while (target) {
      if (target.nodeName === 'A') {
        var buttonDiv = document.createElement('div');
          buttonDiv.className = 'question-div';
          buttonDiv.innerHTML = 'Do you want to leave page and go to the link destination?<br>'
        var buttonsSpan = document.createElement('span');
          buttonsSpan.appendChild( buttonYesCreation() );
          buttonsSpan.appendChild( buttonNoCreation() );
        buttonDiv.appendChild(buttonsSpan);
        document.body.appendChild(buttonDiv);
        buttonDiv.style.width = buttonsSpan.getBoundingClientRect().width + 'px';
        buttonDiv.style.top = (window.pageYOffset + (document.body.clientHeight -
             buttonDiv.getBoundingClientRect().height) / 2) + 'px';
        buttonDiv.style.left = (window.pageXOffset + (document.body.clientWidth -
             buttonDiv.getBoundingClientRect().width) / 2) + 'px';
        return false;
      }
      target = target.parentElement;
    }
}

function buttonYesCreation() {
  var buttonYes = document.createElement('button');
    buttonYes.className = 'question-button';
    buttonYes.innerHTML = 'Yes?';
    buttonYes.onclick = function() {
      document.location.href = target.getAttribute('href');
    }

  return buttonYes;
}

function buttonNoCreation() {
  var buttonNo = document.createElement('button');
    buttonNo.className = 'question-button';
    buttonNo.innerHTML = 'No?';
    buttonNo.onclick = function() {
      document.body.removeChild(document.getElementsByClassName('question-div')[0]);
      return false;
    }

  return buttonNo;
}


function preloadImages() {
  for (var i = 0; i < arguments.length; i++) {
    new Image().src = arguments[i];
  }
}

preloadImages(
  "https://js.cx/gallery/img1-lg.jpg",
  "https://js.cx/gallery/img2-lg.jpg",
  "https://js.cx/gallery/img3-lg.jpg",
  "https://js.cx/gallery/img4-lg.jpg",
  "https://js.cx/gallery/img5-lg.jpg",
  "https://js.cx/gallery/img6-lg.jpg",
);

/*
  <p><img id="largeImg" src="https://js.cx/gallery/img1-lg.jpg" alt="Large image"></p>
    <a href="https://js.cx/gallery/img2-lg.jpg" title="Image 2">
                <img src="https://js.cx/gallery/img2-thumb.jpg"></a>
*/

document.getElementById('thumbs').addEventListener('click', function(event) {
  var target = event.target;
  event.preventDefault();
    while (target) {

        if (target.nodeName === 'A') {
          var tempSrc = largeImg.src;
          largeImg.src = target.href;
          target.href = tempSrc;
          target.children[0].src = target.href.slice(0, target.href.indexOf('lg.jpg')) +
              'thumb.jpg';
        }

      target = target.parentNode;
    }
})