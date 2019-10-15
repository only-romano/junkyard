(function() {
  Vue.component('userdetails', {
    props: ['user'],
    template: '<div><h2>User Info</h2><div v-if="visible"><p>Name: {{user.name}}</p><p>Age: {{user.age}}</p></div></div>',
    data: function() { return { visible: false }; }
  });
  new Vue({
    el: '#app',
    data: {
      user: {
        name: 'Sergey',
        age: 28
      }
    },
    methods: {
      toggle: function() {
        this.$refs.details.visible = !this.$refs.details.visible;
      }
    }
  })
})();