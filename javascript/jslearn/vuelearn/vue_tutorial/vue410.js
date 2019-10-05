(function() {
  Vue.component('userdit', {
    props: ['user'],
    template: '<div><input type="text" v-model="user" /><p>Name: {{user}}</p></div>'
  });
  Vue.component('userdit2', {
    props: ['user'],
    data: function() {
      return { userName: this.user };
    },
    template: '<div><input type="text" v-model="userName" /><p>Name: {{userName}}</p></div>'
  });
  new Vue({
    el: '#app',
    data: {
      name: 'Sergey'
    },
    methods: {
      resetName: function() {
        this.name = 'Ridj';
      }
    }
  });
  new Vue({
    el: '#app2',
    data: {
      name: 'Sergey'
    },
    methods: {
      resetName: function() {
        this.name = 'Ridj';
      }
    }
  })
})();