'use strict';

const app = new Vue({
  el: '#app',
  data: {
    num: '1',
    swit: false
  },/*
  computed: {
    x: this.func
  },*/
  methods: {
    void: function (i) {
      if (document.getElementById('void')) document.getElementById('void').innerText = +i*2;
    },
    ret: function (i) {
      if (document.getElementById('void')) document.getElementById('void').innerText = +i*2;
      return i*2;
    }
  },
  template: `
  <div>
    <label>Input: <input v-model="num" /></label><br><br>
    <button @click="swit = !swit">{{ swit ? "Void" : "Return"}}</button><br><br>
    <div> Actions: <span id="void"></span></div><br><br><br>
    <div> x = function() * 2 = {{swit ? +void(num)*2 : +ret(num)*2}}</div>
  </div>
  `
})