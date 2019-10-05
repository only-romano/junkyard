(function() {
  function showPrompt(text, callback) {
    let coverDiv = document.createElement('div');
      coverDiv.className = 'cover-div';
    document.body.appendChild(coverDiv);

    let form = document.createElement('form');
      form.className = 'prompt-form';
      form.innerHTML = `<span>${text}</span><input type="text"><input type="submit" value="Ok"><button>Cancel</button>`;
      form.children[3].onclick = form.onsubmit = escForm;
      document.body.appendChild(form);
      getFormSize();

    function deleteForm(event) {
      event.preventDefault();
      document.body.removeChild(form);
      document.body.removeChild(coverDiv);
      window.removeEventListener('keydown', escForm);
      window.removeEventListener('resize', getFormSize);
    }

    function escForm() {
      if (event.keyCode == 27 || (event.target.tagName == 'BUTTON' && event.type != 'keydown')) {
        callback(null);
        deleteForm(event);
      }
      if (event.type == 'submit') {
        callback(form.children[1].value);
        deleteForm(event);
      }
    }

    function getFormSize() {
      form.style.top = (document.documentElement.clientHeight - form.offsetHeight) / 2 + 'px';
      form.style.left = (document.documentElement.clientWidth - form.offsetWidth) / 2 + 'px';
    }

    window.addEventListener('keydown', escForm);
    window.addEventListener('resize', getFormSize);
    form.children[1].focus();


    let lastElem = form.elements[form.elements.length - 1];
    let firstElem = form.elements[0];

    lastElem.onkeydown = function(e) {
      if (e.keyCode == 9 && !e.shiftKey) {
        firstElem.focus();
          return false;
      }
    };

    firstElem.onkeydown = function(e) {
      if (e.keyCode == 9 && e.shiftKey) {
        lastElem.focus();
        return false;
      }
    };
  }


  let firstForm = document.body.children[0];
    firstForm.onsubmit = promptNote;

  function promptNote() {
    showPrompt(firstForm.children[0].value, function(value) { alert(value) });
    return false;
  }
})();


function validate(form) {
  let elems = form.getElementsByTagName('*');
    for (elem of elems) {
      if (elem.value === '' && elem.tagName != 'OPTION') {
        console.log(elem);
        createSpan(elem, 'Please fill this field');
      }
    }

  let passwords = form.querySelectorAll('input[type="password"]');
    if (passwords[0].value != passwords[1].value) {
      createSpan(passwords[0], 'Passwords doesn\'t match!');
      return false;
    }

  function createSpan(elem, note) {
    let elemRect = elem.getBoundingClientRect();
    let message = document.createElement('span');
      message.className = 'correct-message';
      message.innerHTML = note;
      message.style.top = elemRect.top + window.pageYOffset + 'px';
      message.style.left = elemRect.right + window.pageXOffset + 3 + 'px';

      elem.style.border = '1px solid red';
      form.addEventListener('input', removeStuff)
    document.body.appendChild(message);

    function removeStuff() {
      document.body.removeChild(message);
      form.removeEventListener('input', removeStuff);
      elem.style.border = '';
    }
  }
}