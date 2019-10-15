'use strict';

const ProductList = {
  template: `
    <ul>
      <li v-for="product in products">
        {{ product.title }} - {{ product.price }}
        <br>
        <button
          :disabled="!product.inventory"
          @click="addProductToCart(product)">
          Add to Cart
        </button>
      </li>
    </ul>
  `,

  computed: Vuex.mapState ({
    products: state => state.Products.all
  }),

  methods: Vuex.mapActions('Cart', [
    'addProductToCart'
  ]),

  created () {
    this.$store.dispatch('Products/getAllProducts');
  }
}
