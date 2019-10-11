(function() {
  Vue.component('user', {
    template: '<div class="user"><slot username="Sergey" userage="28"></slot></div>'
  });
  new Vue({
    el: '#app'
  })
  Vue.component('userlist', {
    props: ['users'],
    template: '<ul><slot v-for="user in users" :username="user"></slot></ul>'
  });
  new Vue({
    el: '#app2',
    data: {
      users: ['Sergey', 'Ridj', 'Kato']
    }
  })
})();