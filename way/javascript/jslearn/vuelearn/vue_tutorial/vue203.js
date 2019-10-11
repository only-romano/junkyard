(function() {
  new Vue({
    el: '#app',
    data: {
      phones: ['iPhone X', 'Galaxy S8', 'Nokia N8', 'Xiaomi Mi6'],
      users: [
        {name: 'Sergey', age: 28},
        {name: 'Katya', age: 20},
        {name: 'Ridj', age: Infinity}
      ]
    }
  })
})();