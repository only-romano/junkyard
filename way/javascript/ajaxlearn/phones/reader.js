function loadPhones() {
  let xhr = new XMLHttpRequest();
    xhr.open('GET', 'phones.json', true);
    xhr.send();
    xhr.onreadystatechange = function() {
      if (xhr.readyState != 4) return;

      button.innerHTML = 'Done!';
      button.disabled = false;

      if (xhr.status != 200)
        alert('Ошибка ' + xhr.status + ': ' + xhr.statusText);
      else {
        try {
          let phones = JSON.parse(xhr.responseText);
          showPhones(phones);
        } catch (e) {
          alert('Error: ' + e.message);
        }
      }
    }

    button.innerHTML = 'Loading...';
    button.disabled = true;
}

function showPhones(phones) {
  phones.forEach(function(phone) {
    let li = phoneslist.appendChild(document.createElement('li'));
      li.innerHTML = phone.name;
  });
}