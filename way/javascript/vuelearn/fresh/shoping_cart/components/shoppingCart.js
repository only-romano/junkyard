'use strict';

const ShoppingCart = {
  template: `
    <div class="cart">
      <h2>Your Cart</h2>
      <p v-show="!products.length"><i>Please add some products to cart.</i></p>
      <ul>
        <li v-for="product in products">
          {{ product.title }} - {{ product.price }} x {{ product.quantity }}
        </li>
      </ul>
      <p>Total: {{ total }}</p>
      <p>
        <button
          :disabled="!products.length"
          @click="checkout(products)">
          Checkout
        </button>
      </p>
      <p v-show="checkoutStatus">Checkout {{ checkoutStatus }}.</p>
    </div>
  `,

  computed: {
    ...Vuex.mapState({
      checkoutStatus: state => state.Cart.checkoutStatus
    }),
    ...Vuex.mapGetters('Cart', {
      products: 'cartProducts',
      total: 'cartTotalPrice'
    })
  },

  methods: {
    checkout (products) {
      this.$store.dispatch('Cart/checkout', products)
    }
  }
}
