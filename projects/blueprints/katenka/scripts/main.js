'use strict';

const title = ['Фан Катёнки', 'Fan of Katenka'];

const store = new Vuex.Store({
  state: {
    lang: true
  },

  mutations: {
    toggleLang: state => state.lang = !state.lang,
  },

  actions: {
    changeLang: ({commit}) => commit('toggleLang'),
  }
});


const app = new Vue({
  el: '#app',
  store,

  computed: Vuex.mapState({
    lang: state => state.lang
  }),

  methods: Vuex.mapActions([
    'changeLang'
  ]),

  watch: {
    lang () {
      document.querySelector('head title').textContent = title[this.lang ? 0 : 1];
    }
  },

  template: pageTemplate
});
