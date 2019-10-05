(function() {
  Vue.component('container', {
    template: '<div><header><slot name="header">Default header</slot></header><article><slot></slot></article><footer><slot name="footer"></slot></footer></div>'
  });
  new Vue({
    el: '#app'
  })
})();