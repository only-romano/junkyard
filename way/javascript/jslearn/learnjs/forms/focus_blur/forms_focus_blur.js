
(function() {
  console.time('Script');


  input.onblur = function() {
    if (isNaN(this.value)) {
      this.classList.add('error');
      error.innerHTML = `You're input some shit but not the number. Correct this. Please, asshole.`;
      input.focus();
    } else {
      this.classList.remove('error');
      error.innerHTML = '';
    }
  };

/*
  input.addEventListener(focus, function() {
    if (this.className == 'error') {
      this.className = '';
      error.innerHTML = '';
    }
  })
*/

  let search = document.getElementsByName('search')[0];
    if (!search.autofocus) search.focus();


    if (form.addEventListener) {
      form.addEventListener('focus', onFormFocus, true);
      form.addEventListener('blur', onFormBlur, true);
    } else {
      form.onfocusin = onFormFocus;
      form.onfocusout = onFormBlur;
    }

  function onFormFocus() { this.className = 'focused'; }
  function onFormBlur() { this.className = '' };

  console.log(document.activeElement);


  console.timeEnd('Script');
})();


(function() {
  let input = document.querySelector('[data-placeholder]');
  showPlaceholder(input);

  function showPlaceholder(input) {
    input.classList.add('placeholder');
    input.value = input.dataset.placeholder;
  }

    if (input.addEventListener) {
      input.addEventListener('focus', onInputFocus, true);
      input.addEventListener('blur', onInputBlur, true);
    } else {
      input.onfocusin = onInputFocus;
      input.onfocusout = onInputBlur;
    }

  function onInputFocus() {
    let placeholder = document.createElement('span');
    let inputBound = input.getBoundingClientRect();
      placeholder.classList.add('placeholder-tooltip');
      placeholder.style.top = inputBound.top - inputBound.height - 1 + 'px';
      placeholder.style.left = inputBound.left + 'px';
      placeholder.innerHTML = input.dataset.placeholder;
    input.value = '';
    document.body.appendChild(placeholder);
  }

  function onInputBlur() {
    let placeholder = document.getElementsByClassName('placeholder-tooltip')[0];
    document.body.removeChild(placeholder);
    if (input.value == '') {
      input.value = input.dataset.placeholder;
    }
  }

})();