(function() {
  new Vue({
    el: '#app',
    data: {
      users: [
        {name: 'Sergey Romanov', age: 28},
        {name: 'Ridj', age: 16},
        {name: 'Crazy', age: 10},
        {name: 'Kato', age: 1}
      ],
      selectedUser: null
    }
  })
})();