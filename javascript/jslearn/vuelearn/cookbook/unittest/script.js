'use strict';


const store = new Vuex.Store({
  state: {
    run: true,
    username: ''
  },

  mutations: {
    setName: (state, name) => state.username = name,
  },

  getters: {
    checkError: (state) => state.username.trim().length < 7 
      ? 'Please enter a longer username'
      : '',
  },

  actions: {
    setName: ({commit}, name) => commit('setName', name),
  }
});


const app = new Vue({
  el: '#app',
  store,

  data: {
    testName: ''
  },

  watch: {
    testName() {
      this.setName(this.testName);
    }
  },

  computed: {
    ...Vuex.mapState({
      username: state => state.username
    }),
    ...Vuex.mapGetters({
      error: 'checkError'
    })
  },

  methods: Vuex.mapActions([
    'setName'
  ]),

  template: 
  `
    <div id="app">
      <input 
        :value="username"
        @input="setName($event.target.value)" 
        />

      <div
        v-if="error"
        class="error"
        >
        {{ error }}
      </div>
    </div>
  `
});


test('Foo', () => {

  const wrapper = testUtils.shallowMount(app);

  wrapper.setData({
    testName: ' '.repeat(7)
  });

  expect(wrapper.find('.error').exists()).toBe(true);

  wrapper.setData({
    testName: 'Lachlan'
  });

  expect(wrapper.find('.error').exists()).toBe(false);

})
