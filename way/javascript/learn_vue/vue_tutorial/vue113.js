(function() {
  let template = function(some) {
    return function() {
      console.log(some + '()');
    }
  };

  new Vue({
    el: '#app',
    data: {
      message: 'Welcome to Vue.js'
    },
    methods: {
      destroy: function() {
        this.$destroy();
      }
    },
    beforeCreate: template('beforeCreate'),
    created: template('created'),
    beforeMount: template('beforeMount'),
    mounted: template('mounted'),
    beforeUpdate: template('beforeUpdate'),
    updated: template('updated'),
    beforeDestroy: template('beforeDestroy'),
    destroyed: template('destroyed')
  })
})();