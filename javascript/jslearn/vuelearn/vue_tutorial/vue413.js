(function() {
  Vue.component('userform', {
    props: ["addfn"],
    data: function() {
      return {
        user: { name: '', age: 18 }
      }
    },
    template: '<div><input type="text" v-model="user.name" /><input type="number" v-model="user.age" /><button @click="addfn({name:user.name, age:user.age})">Add</button></div>'
  });
  Vue.component('useritem', {
    props: ['user', 'index', 'removefn'],
    template: '<div><p>Name: {{user.name}}<br>Age: {{user.age}}</p><button @click="removefn(index)">Delete</button></div>'
  });
  new Vue({
    el: '#app',
    data: {
      users: [
        {name: 'Sergey', age: 28},
        {name: 'Ridj', age: 17},
        {name: 'Kato', age: 2}
      ]
    },
    methods: {
      remove: function(index) {
        this.users.splice(index, 1);
      },
      add: function(user) {
        this.users.push(user);
      }
    }
  })
})();