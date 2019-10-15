'use strict';

const Shop = {
  getProducts (cb) {
    setTimeout(() => cb(this._products), 100);
  },

  buyProducts (products, cb, errorCb) {
    setTimeout(() => {
      (Math.random() > .5 || navigator.userAgent.indexOf('PhantomJS') > -1)
        ? cb()
        : errorCb();
    }, 100);
  },

  _products: [
    {"id": 1, "title": "iPad 4 Mini", "price": 500.01, "inventory": 2},
    {"id": 2, "title": "H&M T-Shirt White", "price": 19.99, "inventory": 10},
    {"id": 3, "title": "Charli XCX - Sucker CD", "price": 19.99, "inventory": 5}
  ]
}
