const NotFound = { template: '<h2>Page Not Found</h2>' };
const Home = { template: `<div><h2>Home Page</h2><ul>
  <li><router-link :to="{ name: 'products', params: { id: 1 }}">Product One</router-link></li>
  <li><router-link :to="{ name: 'products', params: { id: 2 }}">Product Two</router-link></li>
  <li><router-link :to="{ name: 'products', params: { id: 3 }}">Product Three</router-link></li>
  <li><router-link :to="{ name: 'products', params: { id: 4 }}">Product Four</router-link></li>
  </ul></div>` };
const Products = { template: '<h2>List of Market {{$route.params.id}}</h2>' };

const routes = [
  { path: '/', component: Home },
  {
    path: '/products/:id',
    component: Products,
    name: 'products'
  },
  { path: '*', component: NotFound }
];

const router = new VueRouter({
  mode: 'history',
  routes: routes
});

new Vue({
  el: '#app',
  router: router
})