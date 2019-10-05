(function() {
  Vue.component('userdit', {
    props: ['user'],
    data: function() {
      return { userName: this.user };
    },
    template: '<div><input type="text" v-model="userName" @input="onUserChange" /><p>Name: {{userName}}</p></div>',
    methods: {
      onUserChange: function() {
        this.$emit('userchange', this.userName);
      }
    }
  });

  new Vue({
    el: '#app',
    data: {
      name: 'Sergey'
    },
    methods: {
      change: function(value) {
        this.name = value;
      }
    }
  });
})();