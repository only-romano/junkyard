(function() {
  let toggleMixin = {
    data: function() {
      return { state: true, on: "ON", off: "OFF"};
    },
    methods: {
      toggle: function() {
        this.state = !this.state;
      }
    },
    created () {
      this.$options.template = '<div>' + this.$options.template +
        '<button @click="toggle" v-show="state">{{on}}</button>' +
        '<button @click="toggle" v-show="!state">{{off}}</button></div>';
    }
  };
  Vue.component('light', {
    template: '<h3>{{header}}</h3>',
    mixins: [toggleMixin],
    computed: {
      header() {
        return this.state == true ? "Light is turned on" : "Light is turned off";
      }
    }
  });
  Vue.component('enabled', {
    template: 'Turn {{state === false ? "on" : "off"}} Function',
    mixins: [toggleMixin]
  });
  new Vue({
    el: '#app'
  });
  Vue.mixin({
    created: function() {
      console.log('global mixin');
    }
  });
  Vue.component('message', {
    template: '<h2>Hello</h2>'
  });
  new Vue({
    el: '#app2'
  })
})();