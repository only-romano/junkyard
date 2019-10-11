(function() {
  new Vue({
    el: '#app',
    data: {
      user: '',
      users: [],
      users2: [
        {name: 'Sergey Romanov', age: 28},
        {name: 'Ridj', age: 16},
        {name: 'Kato', age: 1}
      ],
      selectedUser: ''
    }
  })
})();