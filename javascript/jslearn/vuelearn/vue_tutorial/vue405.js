(function() {
  Vue.component('message-comp', {
    props: ['message'],
    template: '<h2>{{message}}</h2>'
  });
  Vue.component('user', {
    props: ['name', 'age'],
    template: '<div><h2>User</h2><p>Name: {{name}}</p><p>Age: {{age}}</p></div>'
  });
  new Vue({
    el: "#app",
    data: {
      welcome: '',
      user: {
        name: '',
        age: 18
      }
    }
  })
})();