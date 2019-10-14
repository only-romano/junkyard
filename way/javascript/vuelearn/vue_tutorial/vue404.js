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
                 <span>{{count}}</span>
               </div>`,
    methods: {
      increase: function() {
        this.count++;
      }
    }
  });
  new Vue({
    el: '#app'
  })
})();