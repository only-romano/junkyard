(function() {
  Vue.component('useredit', {
    props: ['name'],
    template: '<div><input v-model="name" /><button @click="save">Save</button></div>',
    methods: {
      save() {
        this.$emit('userchange', this.name);
      }
    }
  });
  Vue.component('userinfo', {
    props: ['name'],
    template: '<div><p>Name: {{name}}</p><button @click="reset">Reset</button></div>',
    methods: {
      reset() {
        this.$emit('userreset');
      }
    }
  })
  new Vue({
    el: '#app',
    data: {
      user: 'Sergey'
    },
    methods: {
      change(name) {
        this.user = name;
      },
      reset() {
        this.user = 'Ridj';
      }
    }
  });
  let eventBus = new Vue();
  Vue.component('useredit2', {
    props: ['user'],
    template: '<div><input v-model="userName" /><button @click="save">Save</button></div>',
    data: function() {
      return { userName: this.user };
    },
    methods: {
      save() {
        eventBus.$emit('userchange', this.userName);
      }
    }
  });
  Vue.component('userinfo2', {
    props: ['user'],
    template: '<div><p>Name: {{userName}}</p></div>',
    data: function() {
      return { userName: this.user };
    },
    created() {
      eventBus.$on('userchange', (name)=>{
        this.userName = name;
      });
    }
  });
  new Vue({
    el: '#app2',
    data: {
      user: 'Sergey'
    }
  })
})();