
function vote() {
  button.innerHTML = ' ... ';
  let xhr = new XMLHttpRequest();
    xhr.open('GET', 'vote', true);
    xhr.onreadystatechange = function() {
      if (xhr.readyState != 4) return;
      if (xhr.status != 200) {
        alert('Ошибка ' + xhr.status + ': ' + xhr.statusText);
        return;
      }

      button.innerHTML = xhr.responseText;
    }

  xhr.send(null);
}