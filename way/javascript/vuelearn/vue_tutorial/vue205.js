(function() {
  let app = new Vue({
    el: '#app',
    data: {
      company: '',
      sortParam: '',
      phones: [
        {title:'iPhone 7', company:'Apple', price: 49000},
        {title:'iPhone X', company:'Apple', price: 70000},
        {title:'Galaxy S8', company:'Samsung', price: 45000},
        {title:'Galaxy Note 8', company:'Samsung', price: 50000},
        {title:'Nokia N8', company: 'HMD Global', price: 25000}
      ]
    },
    computed: {
      filteredList: function() {
        let comp = this.company;
        return this.phones.filter(function(elem) {
          if (comp === '') return true;
          else return elem.company.indexOf(comp) > -1;
        })
      },
      sortedList: function() {
        switch(this.sortParam) {
          case 'title': return this.phones.sort(sortByTitle);
          case 'company': return this.phones.sort(sortByCompany);
          case 'price': return this.phones.sort(sortByPrice);
          default: return this.phones;
        }
      }
    }
  });

  let sortByTitle = (d1, d2) => {
    return d1.title.toLowerCase() > d2.title.toLowerCase();
  };
  let sortByCompany = (d1, d2) => {
    return d1.company.toLowerCase() > d2.company.toLowerCase();
  };
  let sortByPrice = (d1, d2) => {
    return d1.price > d2.price;
  };
})();