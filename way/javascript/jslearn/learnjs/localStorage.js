
if (window.localStorage) {
  let elements = document.querySelectorAll('[name]');
    for (let i = 0, length = elements.length; i < length; i++) {
      (function(element) {
        let name = element.getAttribute('name');
          element.value = localStorage.getItem(name) || '';
          element.onkeyup = function() {
            localStorage.setItem(name, element.value);
          };
      })(elements[i]);
    }
}