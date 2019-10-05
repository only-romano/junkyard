(function() {
  let app = new Vue({
    el: '#app',
    data: {
      name: "Sergey",
      age: 28,
      number: 1
    },
    methods: {
      factorial: function(num) {
        let result = 1;
          for (let i = 1; i <= num; i++) result *= i;
        return result;
      }
    }
  })
})();