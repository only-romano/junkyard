;(function() {

  var message = 'Hello';

  function showMessage() {
    console.log( message );
  }

  showMessage();

})();

/*
ДЛЯ ЧЕГО СКОБОЧКИ:

Дело в том, что «на месте» разрешено вызывать только Function Expression.

1) Если браузер видит function в основном потоке кода – он считает, что это Function Declaration.
2) Если же function идёт в составе более сложного выражения, то он считает, что это Function Expression.

Для этого и нужны скобки – показать, что у нас Function Expression, который по правилам JavaScript
можно вызвать «на месте».
*/

// Можно показать это другим способом, например поставив перед функцией оператор:
+function() {
  console.log('Local alert!');
}();

!function() {
  console.log('It works even like this!');
}();

/*
Зачем точка с запятой в начале?

В начале кода выше находится точка с запятой ; – это не опечатка, а особая «защита от дураков».

Если получится, что несколько JS-файлов объединены в один (и, скорее всего, сжаты минификатором,
но это не важно), и программист забыл поставить точку с запятой, то будет ошибка.
*/

var dudash = (function() {

  var message = 'Goodbye';
  function sayGoodbye() {
    console.log( message );
  }

  return sayGoodbye();

})();
