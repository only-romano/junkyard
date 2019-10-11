(function() {
  Vue.filter('capitalize', function(value) {
    return value.charAt(0).toUpperCase() + value.slice(1, value.length);
  });
  new Vue({
    el: '#app',
    data: {
      message: 'hello world!'
    }
  });
  Vue.component('message', {
    template: '<h2>{{text | uppercase}}</h2>',
    data: function() {
      return {
        text: 'vue filters'
      };
    },
    filters: {
      uppercase(value) {
        return value.toUpperCase();
      }
    }
  });
  new Vue({
    el: '#app2',
    data: {
      header: 'hello world!'
    }
  })
})();