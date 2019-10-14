(function() {
  Vue.component('ads', {
    template: '<div><h3>Anouncment</h3><slot>Advertisement space</slot></div>'
  });
  new Vue({
    el: '#app'
  })
})();