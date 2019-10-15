(function() {
  Vue.component('counter', {
    data: function() {
      return {
        header: 'Counter Program',
        count: 0
      }
    },
    template: `<div><h2>{{header}}</h2>
                <button @click="increase">+</button>
                <span>{{count}}</span></div>`,
    methods: {
      increase: function() {
        this.count++;
      }
    }
  });
  let comp = {
    template: '<div><h2>{{header}}</h2></div>',
    data: function() {
      return { header: 'New Counter Program' }
    }
  };
  new Vue({
    el: '#app',
    components: {
      'counter-new': comp
    }
  });
})();