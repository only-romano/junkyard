var land = {
  template: `<div id="land"><div @click="">coco</div><button @click="land()">save</button></div>`,
  computed: Vuex.mapState({
  }),
  methods: Vuex.mapActions({
    time: 'timeflow',
    save: 'autosave',
    land: 'setland',
  })
};

var map = {};

var iGame = new Vue({
    el: '#igame',
    store,
    components: {
        land: land,
        map: map,
    },
    computed: Vuex.mapState({
        land: state => state.land,
    }),
    watch: {
        land() {
        },
    },
    template: `
    <div class="app">
        <land v-if></land>
    </div>`,
});

var village;
