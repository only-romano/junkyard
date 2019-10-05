'use strict';

const store = new Vuex.Store({
  state: {
    count: 0,
    todos: [
      { id: 1, text: 'Start Girls project', done: true },
      { id: 2, text: 'Finish Girls project', done: false }
    ]
  },
  getters: {
    doneTodos: state => {
      return state.todos.filter(todo => todo.done);
    },
    doneTodosCount: (state, getters) => {
      return getters.doneTodos.length;
    },
    getTodoById: state => id => {
      return state.todos.find(todo => todo.id === id);
    }
  },
  mutations: {
    increment: state => state.count++,
    decrement: state => state.count--,
    incrementBy: (state, payload) => state.count += payload.amount,
  },
  actions: {
    incrementAsync({commit}) {
      setTimeout(() => {
        commit('increment');
      }, 1000)
    }
  }
});

const Counter = {
  template: `
  <div>
    <p>Count is {{ count }}</p>
    <button @click="add">Increase!</button>
    <button @click="min">Decrease.</button>
    <button @click="by5">Increase by 5!.</button>
    <p>{{this.getTodo(2).text}}</p>
  </div>`,
  computed: Object.assign( {},
    Vuex.mapState({
      count: state => state.count,
      todos: state => state.todos,
    }),
    Vuex.mapGetters({
        done: 'doneTodos',
        doneCount: 'doneTodosCount',
        getTodo: 'getTodoById'
    }))
  ,
  methods: Vuex.mapMutations({
    add: 'increment',
    min: 'decrement',
    by5: { type: 'incrementBy', amount: 5 }
  })
}

const counter = new Vue({
  el: '#vuex-app',
  store,
  components: { Counter },
  template: `
  <div>
    <counter></counter>
  </div>
  `
});