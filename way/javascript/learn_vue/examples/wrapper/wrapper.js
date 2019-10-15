'use strict';


const store = new Vuex.Store({
  state: {
    selected: 0,
    options: []
  },
  mutations: {
    setOptions: (state, opt) => state.options = opt,
    setSelect: (state, value) => state.selected = value,
  },
  actions: {
    setOptions: ({commit}) => 
      fetch('http://localhost:8000/options.php')
        .then(response => response.json())
          .then(response => commit('setOptions', response)),
    setSelect: ({commit}, value) => commit('setSelect', value),
  }
});


const component = {
  props: ['options', 'value'],
  methods: Vuex.mapActions([
    'setSelect'
  ]),
  mounted: function() {
    let vm = this;
    $(this.$el)
      .select2({ data: this.options })
        .val(this.value)
          .trigger('change')
            .on('change', function() {
              let value = this.value
              vm.$emit('input', value)
              vm.setSelect(value);
            })
  },
  watch: {
    value: function(value) {
      $(this.$el)
        .val(value)
          .trigger('change');
    },
    options: function(options) {
      $(this.$el).empty().select2({ data: options })
    }
  },
  destroyed: function() {
    $(this.$el).off().select2('destroy')
  },
  template: `
    <select @change="setSelect($event.target.value)">
      <slot></slot>
    </select>
  `
};


const wrapper = new Vue({
  el: '#app',
  store,
  components: {
    'selectTwo': component
  },
  computed: Vuex.mapState({
    selected: state => state.selected,
    options: state => state.options
  }),
  methods: Vuex.mapActions([
    'setOptions'
  ]),
  template: `
    <div>
      <p>Selected: {{ selected }}</p>
      <selectTwo :options="options">
        <option disabled value="0">Select one</option>
      </selectTwo>
      <br>
      <button @click="setOptions">Update options</button>
    </div>
  `
});
