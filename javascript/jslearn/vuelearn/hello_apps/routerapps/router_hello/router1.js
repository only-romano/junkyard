const NotFound = { template: '<h2>Page Not Found</h2>' };
const Home = { template: '<h2>Home Page</h2>' };
const Products = { template: '<h2>Products Page</h2>' };
const About = { template: '<h2>About Page</h2>' };

const routes = [
  { path: '/', component: Home },
  { path: '/about', component: About },
  { path: '/products', component: Products },
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