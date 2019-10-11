(function() {
  Vue.component('userform', {
    props: ['users'],
    data: function() {
      return { user: { name: '', age: 28 } };
    },
    template: '<div><input type="text" v-model="user.name" /><input type="number" v-model="user.age" /><button @click="userAdd">Add</button></div>',
    methods: {
      userAdd: function(event) {
        this.users.push( { name: this.user.name, age: this.user.age } );
      }
    }
  });
  Vue.component('userform2', {
    props: ['user'],
    template: '<div><input type="text" v-model="user.name" /><input type="number" v-model="user.age" /></div>',
  });
  Vue.component('useritem', {
    props: ['user', 'index'],
    template: '<div><p>Name: {{user.name}}<br>Age: {{user.age}}</p><button @click="userDelete(index)">Delete</button><button @click="userChange(index)">Change</button></div>',
    methods: {
      userDelete: function(index) {
        this.$emit('userdelete', index);
      },
      userChange: function(index) {
        this.$emit('userchange', index);
      }
    }
  });
  new Vue({
    el: '#app',
    data: {
      users: [
        { name: 'Sergey', age: 28 },
        { name: 'Ridj', age: 17 },
        { name: 'Kato', age: 2 }
      ],
      user: {}
    },
    methods: {
      remove: function(index) {
        this.users.splice(index, 1);
      },
      change: function(index) {
        this.user = this.users[index];
      }
    }
  })
})();