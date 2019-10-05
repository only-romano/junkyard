(function() {
  new Vue({
    el: '#app',
    data: {
      checked: true,
      on: true,
      off: false,
      light: true,
      selectedUsers: [],
      selectedUsers2: [],
      users: [
        {name: 'Sergey', age: 28},
        {name: 'Kato', age: 1},
        {name: 'Ridj', age: 16},
        {name: 'Romanov', age: 28}
      ]
    }
  })
})();