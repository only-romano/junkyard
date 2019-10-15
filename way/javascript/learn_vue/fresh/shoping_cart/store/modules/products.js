'use strict';

const Products = {};

(function() {
  const getters = {};
  const state = {
    all: []
  };


  const actions = {
    getAllProducts ({ commit }) {
      Shop.getProducts(products => {
        commit('setProducts', products);
      })
    }
  };


  const mutations = {
    setProducts (state, products) {
      state.all = products;
    },

    decrementProductInventory (state, { id }) {
      const product = state.all.find(product => product.id === id);
      product.inventory--;
    }
  };


  Object.assign(Products, {
    namespaced: true,
    state,
    getters,
    actions,
    mutations
  })
})();
