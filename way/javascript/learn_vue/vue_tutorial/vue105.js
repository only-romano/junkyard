(function() {
  let app = new Vue({
    el: '#app',
    data: {
      counter: 0
    },
    methods: {
      increase: function(range, event) {
        console.log(event);
        this.counter += range;
      },
      decrease: function(range, event) {
        if (this.counter >= range) {
          console.log(event);
          this.counter -= range;
        }
      }
    }
  })
})();