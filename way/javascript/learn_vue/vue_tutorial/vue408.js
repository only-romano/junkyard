(function() {
  Vue.component('userdetails', {
    props: ['user'],
    template: '<div class="userdetails"><p>Name: {{user.name}}</p><p>Age: {{user.age}}</p></div>'
  });
  Vue.component('userlist', {
    props: ['users'],
    template: '<div><userdetails v-for="user in users" :key="user.name" :user="user"></userdetails></div>'
  });
  new Vue({
    el: '#app',
    data: {
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