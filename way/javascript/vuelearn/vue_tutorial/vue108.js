(function() {
  let app = new Vue({
    el: '#app',
    data: {
      isActive: false,
      isBounded: false,
      color: "",
      size: ""
    },
    computed: {
      classObj: function() {
        return {
          active: this.isActive,
          bounded: this.isBounded
        }
      }
    }
  })
})();