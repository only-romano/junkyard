(function() {
  Vue.component('userinfo', {
    props: {
      user: {
        type: Object,
        default: function() { return { name: 'Sergey Romanov', age: 28 }; }
      }
    },
    template: '<div><h2>User</h2><p>Name: {{user.name}}</p><p>Age: {{user.age}}</p></div>'
  });
  Vue.component('userlist', {
    props: {
      users: {
        type: Array,
        default: function() { return []; }
      }
    },
    template: '<ul><li v-for="user in users"><p>Name: {{user.name}}</p><p>Age: {{user.age}}</p></li></ul>'
  });

  new Vue({
    el: '#app',
    data: {
      user: {
        name: 'Sergey Romanov',
        age: 28
      },
      users: [{
        name: 'Sergey',
        age: 28
      }, {
        name: 'Ridj',
        age: 17
      }, {
        name: 'Kato',
        age: 2
      }]
    }
  })
})();