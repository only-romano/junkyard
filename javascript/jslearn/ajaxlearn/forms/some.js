function submitButton () {
  let xhr = new XMLHttpRequest();
  let params = 'name=' +
    encodeURIComponent(document.getElementsByName('name')[0].value) + '&surname=' +
    encodeURIComponent(document.getElementsByName('surname')[0].value);
  xhr.open("GET", 'submit?' + params, true);
  xhr.setRequestHeader('X-Requested-With', 'XMLHttpRequest');

  xhr.onreadystatechange = function() {
    if (xhr.readyState != 4) return;

      document.getElementsByTagName('button')[0].innerHTML = 'Done!';
    }

  event.preventDefault();
  xhr.send();
}