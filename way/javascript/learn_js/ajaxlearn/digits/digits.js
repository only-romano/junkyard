function run() {
  let xhr = new XMLHttpRequest();
  write(xhr.readyState);
    xhr.open('GET', 'digits', true);
    write(xhr.readyState);
    xhr.onreadystatechange = function() {
      write(xhr.readyState + "; Symbols: " + xhr.responseText.length);
    }

    xhr.send();
}


function write(text) {
  let li = log.appendChild(document.createElement('li'));
    li.innerHTML = text;
}