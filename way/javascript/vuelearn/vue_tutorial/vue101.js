(function() {
  let app = new Vue({
    el: "#app",
    data: {
      message: 'Hello, Vue!'
    },
    methods: {
      setMessage: function(event) {
        this.message = event.target.value;
      }
    }
  })
})();