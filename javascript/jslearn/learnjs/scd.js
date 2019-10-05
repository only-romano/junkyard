function smallestCommons(arr) {
  function findDivs(n) {
    var divs = [];
    var sq = n**0.5;
    for (var i = 2; i <= sq; i++) {
      if (n % i === 0) {
        if (isPrimal(i)) {
          divs.push(i);
        } else {
          divs = divs.concat(findDivs(i));
        }
        var n2 = n/i;
        if (isPrimal(n2)) {
          divs.push(n2);
        } else {
          divs = divs.concat(findDivs(n2));
        }
      break;
      }
    }
    return divs.length ? divs : [n];
  }

  function isPrimal(n) {
    var sq = n**0.5;
    for (var i = 2; i <= sq; i++) {
      if (n % i === 0) return false;
    }
    return true;
  }

  function getCollection(arr) {
    var collection = {};
    for (var i = 0; i < arr.length; i++) {
      var key = arr[i].toString();
      if (collection[key]) {
        collection[key]++;
      } else {
        collection[key] = 1;
      }
    }
    return collection;
  }

  function updateGlobalCollection(obj) {
    for (key in obj) {
      if (globalCollection[key]) {
        globalCollection[key] = globalCollection[key] < obj[key] ? obj[key] : globalCollection[key];
      } else {
        globalCollection[key] = obj[key];
      }
    }
  }


  arr.sort((a,b)=>a>b?1:-1);
  var globalCollection = {};
  for (var i = arr[0]; i <= arr[1]; i++) {
    updateGlobalCollection(getCollection(findDivs(i)));
  }

  var num = 1;
  for (var key in globalCollection) {
    for (var i = 1; i <= globalCollection[key]; i++) {
        num *= +key;
    }
  }

  return num;
}


smallestCommons([23, 18]);