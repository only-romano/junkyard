(function() {
  let app = new Vue({
    el: '#app',
    data: {
      name: 'Sergey',
      age: 28,
      text: 'Google',
      link: 'https://google.com',
      message: 'Hello, Vue',
      message2: '<h2>Hello</h2>'
    },
    methods: {
      setMessage: function(event) {
        this.message = event.target.value;
      }
    }
  })
})()