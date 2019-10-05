'use strict';

const App = {
  template:`
    <div id="app">
      <h1>Shopping Cart Example</h1>
      <hr>
      <h2>Products:</h2>
      <ProductList />
      <hr>
      <ShoppingCart />
    </div>
  `,
  components: { ProductList, ShoppingCart }
}
