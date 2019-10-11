(function() {
  let app = new Vue({
    el: '#app',
    data: {
      name: 'Sergey',
      age: 28,
      firstname: 'Sergio',
      lastname: 'Romano'
    },
    computed: {
      enabled: function() {
        console.log('computed');
        if (this.age > 17) return 'access allowed';
        else return 'access denied';
      },
      fullname: {
        get: function() {
          return this.firstname + ' ' + this.lastname;
        },
        set: function(newValue) {
          let names = newValue.split(' ');
            this.firstname = names[0];
            this.lastname = names[names.length - 1];
        }
      }
    },
    methods: {
      checkAge: function() {
        console.log("method");
        if (this.age > 17) return 'access allowed';
        else return 'access denied';
      }
    }
  });
})();