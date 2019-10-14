'use strict';

(function() {
  console.time('Script')


  let form = document.forms.my;
  let elem = form.elements.one;  // form.elements[0];
  console.log( elem.value );

  form = document.forms[1];
  let elems = form.elements.age;
  console.log( `Several elements with save name is Array: ${elems[0].value}, ${elems[1].value}`);

  form = document.forms[2];
  console.log( form.elements.text == form.elements.set.elements.text, form.elements.text );

  form = document.forms.myform;
  console.log( form.elements.text == form.text, form.text );

  form.text.name = 'new-name';
  console.log( 'Bug:', form.elements.text, form.text );

  form = document.forms[4];
  elem = form.elements.surname;
  console.log( elem.form == form, form);
  elem.value = 'Petrov';  // textarea.value = 'new value'

  if (clickme.checked) console.log( 'Checkbox is checked' );

  form = document.forms.formselect;
  let select = form.elements.genre;

  select.appendChild(new Option('Not selected generated select', 'ns value'));
  select.appendChild(new Option('Selected generated select', 's value', true, true));

    for (let option of select.options) if (option.selected) console.log( option.value );

  let option = select.options[1];
  console.log( 'Selected:', option.selected, '\nIndex:', option.index, '\nText:', option.text );


  let forms = document.forms;
    for (form of forms) {
      try {
        option = form.elements[0].options[0];
        if (option.value != "R'n'B") continue;
        select = form.elements[0];
          for (option of select) if (option.selected) console.log( option.value, option.text );
        select.appendChild(new Option('Old-school Classics', 'classics', true, true));
        break;
      } catch (e) {
        continue;
      }
    }



  console.timeEnd('Script');
})();