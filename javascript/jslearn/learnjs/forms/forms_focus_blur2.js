(function Mouse() {
  mouse.setAttribute('tabindex', '1');
  mouse.addEventListener('focus', addListeners);
  mouse.addEventListener('blur', removeListeners);

  function addListeners() {
    mouse.addEventListener('keydown', moveMouse);
  }

  function removeListeners() {
    mouse.removeEventListener('keydown', moveMouse);
  }

  function moveMouse() {
    let mouseRect = mouse.getBoundingClientRect();
      mouse.style.position = 'absolute';
      if (event.keyCode == 37) {
        mouse.style.left = mouseRect.left - mouseRect.width + 'px';
      } else if (event.keyCode == 38) {
        mouse.style.top = mouseRect.top - mouseRect.height + 'px';
      } else if (event.keyCode == 39) {
        mouse.style.left = mouseRect.left + mouseRect.width + 'px';
      } else if (event.keyCode == 40) {
        mouse.style.top = mouseRect.top + mouseRect.height + 'px';
      }
  }

})();

(function divToArea() {
  document.documentElement.addEventListener('keydown', editDiv);
  document.documentElement.addEventListener('keyup', pressedKeyClear);
  let pressedKeys = [];
  let areaDisplay = false;

  function editDiv() {
    pressedKeys.push(event.keyCode);
    if (~pressedKeys.indexOf(17) && ~pressedKeys.indexOf(69)) {
      areaDisplay = true;
      pressedKeys = [];
        view.style.display = 'none';
        area.style.display = 'block';
        area.value = view.innerHTML;
        area.focus();
        event.preventDefault();
    } else if (~pressedKeys.indexOf(17) && ~pressedKeys.indexOf(83) && areaDisplay) {
      areaDisplay = false;
      pressedKeys = [];
        view.style.display = 'block';
        area.style.display = 'none';
        view.innerHTML = area.value;
        event.preventDefault();
    } else if (~pressedKeys.indexOf(27) && areaDisplay) {
      areaDisplay = false;
      pressedKeys = [];
        view.style.display = 'block';
        area.style.display = 'none';
        area.value = view.innerHTML;
        event.preventDefault();
    }
  }

  function pressedKeyClear() {
    pressedKeys.splice(pressedKeys.indexOf(event.keyCode), 1);
  }
})();