(function() {
  let app = new Vue({
    el: '#app',
    data: {
      current: ''
    },
    methods: {
      change: function() {
        let temp = this.$refs.header.innerText;
          if (!this.current) this.$refs.header.innerText = 'Welcome to Vue.js!';
          else this.$refs.header.innerText = this.current;
        this.current = temp;
      }
    }
  })
})();