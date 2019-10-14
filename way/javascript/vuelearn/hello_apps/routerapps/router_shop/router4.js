const NotFound = {
  template: '<h2>Page Not Found</h2>'
};

const HomeLink = {
  template: '<router-link to="/" exact>Home Page</router-link>'
};

const Products = {
  template: `<div><h2>Products</h2><ul>
    <li><router-link to="/phones">Smartphones</router-link></li>
    <li><router-link to="/tablets">Tablets</router-link></li></ul></div>`
};

const PhonesAds = {
  template: '<div><h3>Smartphones Ad</h3><p>Apple Smartphones Sale</p></div>'
};

const TabletsAds = {
  template: '<div><h3>Tablets Ad</h3><p>Buy Samsung Tablets!</p></div>'
};

const Phones = {
  template: '<h2>All about smartphones</h2>'
};

const Tablets = {
  template: '<h2>All about tablets</h2>'
};

const routes = [
  {
    path: '/',
    components: {
      default: HomeLink,
      content: Products
    }
  }, {
    path: '/phones',
    components: {
      default: HomeLink,
      ads: PhonesAds,
      content: Phones
    }
  }, {
    path: '/tablets',
    components: {
      default: HomeLink,
      ads: TabletsAds,
      content: Tablets
    }
  }, {
    path: '/404',
    component: NotFound
  }, {
    path: '*',
    redirect: '/404'
  }
];

const router = new VueRouter({
  mode: 'history',
  routes: routes
});

new Vue({
  el: '#app',
  router: router
});
