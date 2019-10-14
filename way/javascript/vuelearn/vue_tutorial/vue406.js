(function() {
  Vue.component('user', {
    props: {
      name: {
        type: String,
        required: true,
        default: 'Ridj',
        validator: function(value) {
          return value.length > 2 &&  value != 'admin';
        }
      },
      age: {
        type: Number,
        required: true,
        default: 16,
        validator: function(value) {
          return value >= 0 && value < 130;
        }
      }
    },
    template: '<div><h2>User</h2><p>Name: {{name}}</p><p>Age: {{age}}</p></div>'
  });

  new Vue({
    el: '#app',
    data: {
      user: {
        age: 0
      }
    }
  })
})();