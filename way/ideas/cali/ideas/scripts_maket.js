(function() {
  new Vue({
    el: '#header_app',
    data: {
      logged: false
    },
    methods: {
      login: function() {
        this.logged = !this.logged;
        document.getElementsByTagName('body')[0].classList.toggle('logged');
      }
    }
  });
})();