(function() {
  let app = new Vue({
    el: '#app',
    data: {
      number: '',
      result: ''
    },
    methods: {
      factorial: function(newNumber) {
        this.result = 'Factorial calculating in process...';;
        setTimeout(() => {
          let res = 1;
            for (let i = 1; i <= newNumber; i++) res *= i;
          this.result = 'Factorial of ' + newNumber + ' is equal to ' + res;
        }, 2000);
      }
    },
    template: '<div><p>Input number: <input v-model="number"></p>' +
      '<p>{{result}}</p></div>',
    watch: {
      number: function(newNumber) {
        if (newNumber > 0) this.factorial(newNumber);
      }
    }
  })
})();