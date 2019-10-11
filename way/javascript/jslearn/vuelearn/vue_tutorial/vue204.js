(function() {
  new Vue({
    el: "#app",
    data: {
      newPhone: '',
      start: 0,
      end: 3,
      phones: ['iPhone X', 'Galaxy S8', 'Nokia N8', 'Xiaomi Mi6']
    },
    computed: {
      visibleList: function() {
        return this.phones.slice(this.start, this.end);
      }
    },
    methods: {
      updateList: function() {
        let mass = document.getElementsByTagName('input')[0].value.split(' ');
        Vue.set(this.phones, +mass[mass.length-1], mass.slice(0, mass.length-1).join(' '));
      },
      sliceList: function() {
        let indexes = document.getElementsByTagName('input')[0].value.split(' ');
        if (indexes.length == 2) {
          try {
            this.phones = this.phones.slice(+indexes[0], +indexes[1]);
          } catch {
            return;
          }
        }
      } 
    }
  })
})();