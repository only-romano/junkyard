(function() {
  let vm1 = new Vue({
    el: '#app1',
    data: {
      name: 'Sergey',
      age: 27
    },
    methods: {
      setName: function(value) {
        this.name = value;
      }
    }
  });

  vm1.setAge = function(value) {
    vm1.age = value;
  }
  vm1.setAge(28);
  vm1.setName('Sergio');
  vm1.position = 'moderator';
  setTimeout(() => {
    vm1.position = 'admin'
  }, 2000);

  let vm2 = new Vue({
    el: '#app2',
    data: {
      title: ''
    },
    methods: {
      onClick: function() {
        vm1.setName(this.title);

      }
    }
  })
})();