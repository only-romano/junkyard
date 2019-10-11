(function() {
  let app = new Vue({
    el: "#app",
    data: {
      name: 'Sergey',
      age: 28
    },
    methods: {
      welcome: function() {
        return 'Welcome, ' + this.displayName();
      },
      displayName: function() {
        return this.name;
      },
      factorial: function(num) {
        let result = 1;
          for (let i = 1; i <= num; i++) result = result * i;
        return result;
      }
    }
  })
})();