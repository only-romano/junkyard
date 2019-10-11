(function() {
  let app = new Vue({
    el: '#app',
    data: {
      name: 'Sergey',
      age: 28
    },
    template: '<h2>Name: {{name}} - Age: {{age}}</h2>'
  })
})()