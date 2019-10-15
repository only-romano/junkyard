(function() {
  let app = new Vue({
    el: '#app',
    data: {
      color: '',
      width: 100,
      height: 100
    },
    computed: {
      styleObj: function() {
        return {
          'background-color': this.color,
          width: this.width + 'px',
          height: this.height + 'px'
        }
      },
      colorStyle: function() {
        return {
          backgroundColor: this.color,
        }
      },
      sizeStyle: function() {
        return {
          width: this.width + 'px',
          height: this.width + 'px'
        }
      }
    }
  })
})();