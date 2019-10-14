const NotFound = { template: '<h2>Page Not Found</h2>' };
const Home = { template: '<h2>Home Page</h2>' };
const Products = { template: '<div><h1>Products</h1><router-view></router-view></div>' };

const Phones = { template: '<div><h2>Category One: Phones</h2><h3 v-if="$route.params.id">Id: {{$route.params.id}}</h3></div>' };
const Tablets = { template: '<div><h2>Category Two: Tablets</h2><h3 v-if="$route.params.id">Id: {{$route.params.id}}</h3></div>' };

const routes = [
  { path: '/', component: Home },
  {
    path: '/products',
    component: Products,
    children: [
      {
        path: 'phones/:id?',
        component: Phones
      }, {
        path: 'tablets/:id?',
        component: Tablets
      }
    ]
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