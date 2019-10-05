'use strict';


const App = Object.freeze({
  name: 'My Version App',
  version: '2.1.4',
  helpers: {
    reverseText: function(text) {
      return text.split('').reverse().join('');
    }
  }
})


const store = new Vuex.Store({
  state: {
    users: [],
    age: null,
    name: null,
    movie: null,
    email: null,
    errors: [],

    Cosmic: {
      budgetErrors: [],
      weapons: 0,
      shields: 0,
      coffee: 0,
      ac: 0,
      droids: 0,
      total: 0,
    },

    Server: {
      errors: [],
      name: '',
      api: '/server.php?product='
    },

    helpers: {
      validEmail: email => /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/.test(email),
    }
  },

  mutations: {

    // Form app
    setUsers: (state, users) => state.users = users,
    setName: (state, name) => state.name = name,
    setAge: (state, age) => state.age = age,
    setMovie: (state, movie) => state.movie = movie,
    setEmail: (state, email) => state.email = email,

    checkForm: (state, event) => {
      state.errors = [];
        if (!state.name) state.errors.push('You must specify the name.');
        if (!state.age) state.errors.push('You must specify the age.');
        if (!state.email) state.errors.push('Email is required.');
        else if (!state.helpers.validEmail(state.email)) state.errors.push('Email is incorrect');

      if (!state.errors.length) return true;
      event.preventDefault();
    },

    // Cosmic app
    setWeapons: (state, weapons) => {
      state.Cosmic.total += weapons - state.Cosmic.weapons;
      state.Cosmic.weapons = +weapons;
    },
    setShields: (state, shields) => {
      state.Cosmic.total += shields - state.Cosmic.shields;
      state.Cosmic.shields = +shields;
    },
    setCoffee: (state, coffee) => {
      state.Cosmic.total += coffee - state.Cosmic.coffee;
      state.Cosmic.coffee = +coffee;
    },
    setAc: (state, ac) => {
      state.Cosmic.total += ac - state.Cosmic.ac;
      state.Cosmic.ac = +ac;
    },
    setDroids: (state, droids) => {
      state.Cosmic.total += droids - state.Cosmic.droids;
      state.Cosmic.droids = +droids;
    },

    checkBudget: (state, event) => state.Cosmic.total == 100 ? true :
      (state.Cosmic.budgetErrors = ['Total sum must be 100$!']) &&
      event.preventDefault(),

    // Server app
    setServerName: (state, name) => state.Server.name = name.toLowerCase(),

    checkProduct: (state, event) => {
      event.preventDefault();
      state.Server.errors = [];;
        if (state.Server.name === '') state.Server.errors.push('Provide name of the product.');
        else fetch(state.Server.api + encodeURIComponent(state.Server.name))
              .then(resolve => resolve.json())
                .then(resolve => resolve.error ? state.Server.errors.push(resolve.error) : alert('Done!'));
    }
  },

  actions: {
    // Form app
    setUsers: ({commit}, users) => commit('setUsers', users),
    setName: ({commit}, name) => commit('setName', name),
    setAge: ({commit}, age) => commit('setAge', age),
    setMovie: ({commit}, movie) => commit('setMovie', movie),
    setEmail: ({commit}, email) => commit('setEmail', email),
    checkForm: ({commit}, event) => commit('checkForm', event),

    // Cosmic app
    setWeapons: ({commit}, weapons) => commit('setWeapons', weapons),
    setShields: ({commit}, shields) => commit('setShields', shields),
    setCoffee: ({commit}, coffee) => commit('setCoffee', coffee),
    setAc: ({commit}, ac) => commit('setAc', ac),
    setDroids: ({commit}, droids) => commit('setDroids', droids),
    checkBudget: ({commit}, event) => commit('checkBudget', event),

    // Server app
    setServerName: ({commit}, name) => commit('setServerName', name),
    checkProduct: ({commit}, event) => commit('checkProduct', event),
  }
});


Vue.prototype.$myCoolApp = 'My sexy cool App';
Vue.prototype.$http = axios;
Vue.prototype.$reverseText = function(propertyName) {
  this[propertyName] = this[propertyName].split('').reverse().join('');
}


const app1 = new Vue({
  el: '#app1',
  store,

  data: {
    message: 'Hello Vue Cookbook!',
    appVersion: App.version,
  },

  computed: Vuex.mapState({
    users: state => state.users,
  }),

  methods: {
    getUsersList: function() {
      this.$http.get('https://jsonplaceholder.typicode.com/users')
        .then(response => this.$store.dispatch('setUsers', response.data))
    },
    reverseText: App.helpers.reverseText
  },

  beforeCreate: function() {
    console.log(this.$myCoolApp);
  },
  created: function() {
    this.getUsersList();
    this.$reverseText('$myCoolApp') || console.log(this.$myCoolApp);
  },

  template: `
    <div id="app1">
      <h2>{{ reverseText(message) }}</h2>
      <ul>
        <li v-for="user in users">{{ user.name }}</li>
      </ul>
    </div>
  `
});


const app2 = new Vue({
  el: '#app2',
  store,

  computed: Vuex.mapState({
    name: state => state.name,
    age: state => state.age,
    movie: state => state.movie,
    email: state => state.email,
    errors: state => state.errors
  }),

  methods: Vuex.mapActions([
    'setName', 'setAge', 'setMovie', 'setEmail', 'checkForm'
  ]),

  template: `
    <form
        id="app2"
        @submit="checkForm($event)"
        action="something"
        method="post"
        novalidate="true" >

      <p v-if="errors.length">
        <b>Please correct specified errors:</b>
        <ul>
          <li v-for="error in errors">{{ error }}</li>
        </ul>
      </p>

      <p>
        <label for="name">Name</label>
        <input
            id="name"
            type="text"
            name="name"
            :value="name"
            @input="setName($event.target.value)" />
      </p>

      <p>
        <label for="age">Age</label>
        <input
            id="age"
            type="number"
            name="age"
            min="0"
            :value="age"
            @input="setAge($event.target.value)" />
      </p>

      <p>
        <label for="email">Email</label>
        <input
            id="email"
            type="email"
            name="email"
            :value="email"
            @input="setEmail($event.target.value)" />
      </p>

      <p>
        <label for="movie">Favorite movie</label>
        <select
            id="movie"
            name="movie"
            :value="movie"
            @change="setMovie($event.target.value)" >

          <option>Star Wars</option>
          <option>Vanilla Sky</option>
          <option>Atomic Blonde</option>
        </select>
      </p>

      <p>
        <input type="submit" value="Send" />
      </p>
    </form>
  `
});


const app3 = new Vue({
  el: '#app3',
  store,

  computed: Vuex.mapState({
    errors: state => state.Cosmic.budgetErrors,
    weapons: state => state.Cosmic.weapons,
    shields: state => state.Cosmic.shields,
    coffee: state => state.Cosmic.coffee,
    ac: state => state.Cosmic.ac,
    droids: state => state.Cosmic.droids,
    total: state => state.Cosmic.total
  }),

  methods: Vuex.mapActions([
    'checkBudget', 'setWeapons', 'setShields', 'setCoffee',
    'setAc', 'setDroids'
  ]),

  template: `
    <form
        id="app3"
        @submit="checkBudget"
        action="something"
        method="POST"
        novalidate="true">

      <p v-if="errors.length">
        <b>Please correct following errors:</b>
        <ul>
          <li v-for="error in errors">{{ error }}</li>
        </ul>
      </p>

      <p>
        Imagine that you have a update budget as 100$, please set
        how many of it you want to spend for following features of
        new generation <strong><i>"Star Destroyer"</i></strong>.
        Please, don't forget - you can not spend more then 100$.
      </p>

      <p>
        <input
            type="number"
            name="weapons"
            :value="weapons"
            @input="setWeapons($event.target.value)" />
          Weapons<br/>

        <input
            type="number"
            name="shields"
            :value="shields"
            @input="setShields($event.target.value)" />
          Shields<br/>

        <input
            type="number"
            name="coffee"
            :value="coffee"
            @input="setCoffee($event.target.value)" />
          Coffee</br/>

        <input
            type="number"
            name="ac"
            :value="ac"
            @input="setAc($event.target.value)" />
          Condition<br/>

        <input
            type="number"
            name="droids"
            :value="droids"
            @input="setDroids($event.target.value)" />
          Mouse droids<br/>
      </p>

      <p :class="{ gotcha: total == 100, overdose: total > 100 }">
        Total: {{ total }}
      </p>

      <p>
        <input type="submit" value="Send" />
      </p>
    </form>
  `
});


const app4 = new Vue({
  el: '#app4',
  store,

  computed: Vuex.mapState({
    errors: state => state.Server.errors,
    name: state => state.Server.name,
  }),

  methods: Vuex.mapActions({
    checkForm: 'checkProduct',
    setName: 'setServerName'
  }),

  template: `
    <form
        id="app4"
        @submit="checkForm"
        method="POST">
      <p v-if="errors.length">
        <b>Please correct provided errors:</b>
        <ul>
          <li v-for="error in errors">{{ error }}</li>
        </ul>
      </p>

      <p>
        <label for="name-p">Name of the product: </label>
        <input
            id="name-p"
            type="text"
            name="name"
            :value="name"
            @input="setName($event.target.value)" />
      </p>

      <p>
        <input type="submit" value="Send" />
      </p>
    </form>
  `
});
