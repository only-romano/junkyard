var app = new Vue( {
  el: "#app",
  data: {
    message: "Hello, Vue!"
  },
  methods: {
    setMessage: function(event) {
      this.message = event.target.value;
    }
  }
})

var app2 = new Vue({
  el: '.someclass',
  data: {
    name: 'Sergey',
    age: 27,
    text: 'Awesome Blog',
    link: 'https://this-is-awesome.herokuapp.com/',
    message: 'Hello :(',
    htmlmessage: '<h2>I just wanna feel real love</h2>'
  },
  methods: {
    welcome: function() {
      return "Welcome!";
    },
    displayName: function() {
      return this.name;
    },
    factorial: function(n) {
      let result = 1;
      for (let i = 1; i <= n; i++) {
        result = result * i;
      }
      return result;
    },
    setMessage: function(event) {
      this.message = event.target.value;
    }
  }
})