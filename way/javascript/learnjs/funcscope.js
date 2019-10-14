'use strict';

function func() {
  console.log('do func');
  const buffer_func = func;
  func = () => {
    buffer_func();
    buffer_func();
  }
}

func();
console.log('___\n');
func();
console.log('___\n');
func();
console.log('___\n');
func();
